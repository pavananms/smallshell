
import os

def instdecomp(cmd):    

    args=cmd.split(cmd)
    os.execvp(args[0],args)

def exect(cmd):        
    newpid=os.fork()
    if newpid==0:
        instdecomp(cmd)
    else:
        os.wait()  

def shell():
    #print "----------MSP Shell---------\n\n\n"

    while(1):
        cmd=raw_input("MSPshell:")
        
        if cmd[:1]=='cd':
            print cmd
            path=cmd.split()[1]
            os.chdir(path)
        
        exect(cmd)

        
       
shell()

