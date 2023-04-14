

    #!/usr/bin/env python3
     
    """Backup docker containers and compose files."""
     
    import getpass
    import logging
    from pathlib import Path
    import subprocess
    import sys
    import time
     
     
    class Container:
        """Container class."""
        def __init__(self, name, container_with_db=False):
            """Init container object."""
            self.name = name
            if container_with_db:
                # If the only data we need to backup is database, then
                # it's located in /opt
                self.container_path = Path(f'/opt/docker/persistent/{self.name}-db')
                self.internal_backup_path = Path(f'/mnt/common/docker/containers/{self.name}-db')
            else:
                # Else set container path to /mnt/media/docker/containers
                self.container_path = Path(f'/mnt/media/docker/containers/{self.name}')
                self.internal_backup_path = Path(f'/mnt/common/docker/containers/{self.name}')
            self.compose_file = Path(f'/mnt/media/docker/compose/active/{self.name}/docker-compose.yml')
     
            # Create backup dir if not exists
            self.internal_backup_path.mkdir(exist_ok=True, parents=True)
     
        def down(self):
            """Put container down."""
            subprocess.run([
                'docker-compose',
                '-f',
                self.compose_file,
                'down'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     
        def up(self):
            """Put container up."""
            subprocess.run([
                'docker-compose',
                '-f',
                self.compose_file,
                'up',
                '-d'
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     
     
    class ExternalDrive:
        """Class to manager external drive."""
        def __init__(self):
            """Init external drive object."""
            self.uuid = 'dbb6dfac-a22c-4ec8-a9c6-97d5d82d887e'
            self.name = 'External HDD'
            self.mount_point = Path('/mnt/mirror')
            self.decrypt_name = 'mirror_crypt'
            self.key_path = Path('/luks-media-ext.key')
     
            if not self.mount_point.is_dir():
                self.mount_point.mkdir(mode=0o755)
     
        def decrypt(self):
            """Decrypt drive."""
            subprocess.run([
                'cryptsetup',
                'open',
                f'/dev/disk/by-uuid/{self.uuid}',
                self.decrypt_name,
                '--key-file',
                self.key_path
            ])
     
        def mount(self):
            """Mount drive."""
            dev_path = Path(f'/dev/mapper/{self.decrypt_name}')
            subprocess.run([
                'mount',
                '-v',
                dev_path,
                self.mount_point
            ])
     
        def umount(self):
            """Umount drive."""
            subprocess.run([
                'umount',
                '-R',
                self.mount_point
            ])
     
        def encrypt(self):
            """Close decrypted drive."""
            subprocess.run([
                'cryptsetup',
                'close',
                self.decrypt_name
            ])
     
     
    def backup_compose_dir():
        """Backup compose dir to internal drive."""
        compose_dir = Path('/mnt/media/docker/compose')
        internal_backup_path = Path('/mnt/common/docker/compose')
        subprocess.run([
            'rsync',
            '-ahc',
            '--delete',
            f'{compose_dir}/',
            f'{internal_backup_path}/'
        ])
     
     
    def backup_to_internal_drive(container_obj):
        """Backup docker files from original drive to internal backup drive."""
        subprocess.run([
            'rsync',
            '-ahc',
            '--delete',
            '--',
            f'{container_obj.container_path}/',
            f'{container_obj.internal_backup_path}/'
        ])
     
     
    def backup_to_external_drive():
        """Backup files from internal to external drive."""
        internal_backup_root = '/mnt/common/docker'
        external_backup_root = '/mnt/mirror/docker'
        subprocess.run([
            'rsync',
            '-ahc',
            '--delete',
            f'{internal_backup_root}/',
            f'{external_backup_root}/'
        ])
     
     
    def backup_to_remote_drive():
        """Backup files from internal to remote drive."""
        internal_backup_root = '/mnt/common/docker'
        remote_backup_root = 'nas-mirror:/mnt/media/docker'
        subprocess.run([
            'rsync',
            '-ahc',
            '--delete',
            f'{internal_backup_root}/',
            f'{remote_backup_root}/'
        ])
     
     
    def set_up_logging(script_name):
        """Set up logging for script."""
        log_path = Path('/var/log').joinpath(f'{script_name}.log')
        logging.basicConfig(
            encoding='utf-8',
            level=logging.DEBUG,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler(sys.stdout)
            ]
        )
     
     
    def is_nas_reachable():
        """Check if NAS is reachable over network to be able to backup
        data."""
        ping_proc = subprocess.run([
            'ping',
            '-c',
            '1',
            '-W',
            '2',
            '192.168.77.30'
        ], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        if ping_proc.returncode:
            return False
        return True
     
     
    def multisync():
        """Sync triple time to write cache to disk."""
        subprocess.run(['sync'])
        subprocess.run(['sync'])
        subprocess.run(['sync'])
     
     
    def format_seconds_to_hms(total_seconds):
        """Convert seconds to HH MM SS format."""
        hours = total_seconds // 3600
        minutes = (total_seconds - hours*3600) // 60
        seconds = total_seconds - (hours*3600 + minutes*60)
        hours = str(hours).zfill(2)
        minutes = str(minutes).zfill(2)
        seconds = str(seconds).zfill(2)
        hms = f'{hours}h {minutes}m {seconds}s'
        return hms
     
     
    def are_permissions_ok():
        """Check if user who run script has root permissions."""
        if getpass.getuser() == 'root':
            return True
        return False
     
     
    def main():
        # Check permissions.
        if not are_permissions_ok():
            logging.error('Not enough permissions')
            sys.exit(1)
     
        # Get start time.
        start_time = time.time()
     
        # Get script name.
        script_name = Path(__file__).name.strip('.py')
     
        # Set up logging.
        set_up_logging(script_name)
        logging.info(f'Script {script_name} started')
     
        # Dictionary with container names and booleans. If value is true
        # then container has database that is located separately
        # (/opt/docker/persistent).
        containers = {
            'nginx-proxy-manager': False,
            'vaultwarden': False,
            'gitea': False,
            'nextcloud': True,
            'joplin': True,
            'miniflux': True,
            'adguard': False
        }
     
        # Put each container down, backup data, start container.
        for container_name, with_db in containers.items():
            container = Container(container_name, with_db)
            container.down()
            backup_to_internal_drive(container)
            container.up()
     
        # Backup compose files.
        backup_compose_dir()
     
        # Sync.
        multisync()
     
        # Backup from internal drive to external drive.
        drive = ExternalDrive()
        drive.decrypt()
        drive.mount()
        if drive.mount_point.is_mount():
            backup_to_external_drive()
            multisync()
            drive.umount()
        else:
            logging.error(f'{drive.name} was not mounted. Backup skipped.')
        drive.encrypt()
     
        # Backup from internal drive to remote drive.
        if is_nas_reachable():
            backup_to_remote_drive()
        else:
            logging.error('NAS is not reachable. Backup skipped.')
     
        # Show time.
        finish_time = time.time()
        seconds = int(finish_time - start_time)
        formatted_time = format_seconds_to_hms(seconds)
        logging.info(f'Finished in {formatted_time}')
     
     
    if __name__ == '__main__':
        main()


