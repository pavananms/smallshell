
import os

arg=raw_input("enter redirection command:")

def redirectfrom(arg):

    args= arg.split()
    x=args.index('<')
    fname=args[x+1]
    #open(fname,'w')
    print fname
    xargs = args[:x]
    print str(args[0])
    old=os.dup(1)
    os.close(1)
    os.open(fname,os.O_RDONLY)
    x=os.fork()
    if x==0:
        os.execvp(args[0],xargs)
    else:
        os.wait()

    os.close(1)
    os.dup(old)
    os.close(old)

redirectfrom(arg)
