import os
import pickle
import json
import sys

def dir(path):
    for list in os.listdir(path):
        p = os.path.join(path, list)
        if os.path.isdir(p):
            dir(p)
        else:
            read(p)

def read(p):
    'print (p)'
    if p.find('.swf') > -1:
        directory = 'D:/Desktop/export/ver3/' + os.path.basename(p).replace('.swf', '.fla')

        cmd = 'java -jar D:/ffdes-4.0.5/ffdec.jar -format fla:cs6.0 -export fla "' + directory + '" ' + p
        print(cmd)
        os.system(cmd)

pre = os.getcwd()
if len(sys.argv) > 1:
    dir(sys.argv[1])
else:
    dir(pre)