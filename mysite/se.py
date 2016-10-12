# -*- coding: cp866 -*-
import subprocess
import sys
import datetime

if __name__ == "__main__":
    if len(sys.argv)>1:
        cmd=sys.argv[1]
    else:
        cmd="py.py"
    PIPE = subprocess.PIPE
    p=subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        stderr=subprocess.STDOUT)
    while True:
        s = p.stdout.readline()
        if not s: break
        f=open("log.txt","a")
        ti=datetime.datetime.now()
        f.write(str(ti)+":="+s)
        print(str(ti)+":="+s)
        f.close()
        
    #print("Программа "+cmd+" запущена!")
    
