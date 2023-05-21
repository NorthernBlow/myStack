import os


#print("Локальные директории:", os.listdir(path='/mnt/Seagate/music/'))


def local_dirs():
    path = '/mnt/Seagate/music/'

    return [dir for dir in os.listdir(path) if os.path.join(path, dir) and not dir.endswith('.mp3') and not dir.endswith('.pdf')]

list_harddisk_music = local_dirs()

print(list_harddisk_music)




