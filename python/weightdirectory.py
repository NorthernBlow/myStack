import os

basedir = "/home/northerblow/prog/"

subnames = os.listdir(basedir)
for subname in subnames:
    sub_size = 0
    subpath = "%s/%s" % (os.path.dirname(basedir), subname)
    for path, subdirs, file in os.walk(subpath):
         for files in file:
              filename = os.path.join(path, files)
              sub_size += os.path.getsize(filename) /1024 /1024
    print ("%s - %.1f Mb" % (basedir[len[basedir]: ], sub_size))