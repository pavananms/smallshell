import os
import sys
old=os.dup(1)
os.close(1)
os.open("out.txt",os.O_WRONLY)
x=os.fork()
if x==0:
    os.execvp('ls',['ls','-a'])
else:
    os.wait()

os.close(1)
os.dup(old)
os.close(old)
