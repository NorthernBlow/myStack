import os
import subprocess
 
def execfile(path, globals=None, locals=None):
    if globals is None:
        globals = {}
    globals.update({"__file__": path, "__name__": "__main__"})
    with open(path, "rb") as f:
        exec(compile(f.read(), path, "exec"), globals, locals)
 
def collect_commands(root_dir):
    commands = []
 
    for root, dirs, files in os.walk(root_dir):
        # print(root)
        for name in files:
            ext = os.path.splitext(name)[-1]
            if ext != ".py":
                pass
 
            path = os.path.join(root, name)
 
            table = {}
            execfile(path, locals=table)
 
            if "CMDS" in table:
                commands = commands + (table["CMDS"])
                
    return commands
 
def execute_unique_commands(commands):
    executed = []
    
    for cmd in commands:
        if cmd in executed:
            print("duplicate: " + cmd)
        else:
            subprocess.run(cmd)
            executed.append(cmd)
 
def main():
    execute_unique_commands(collect_commands("testdata"))
 
if __name__ == "__main__":
    main()
