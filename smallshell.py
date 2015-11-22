import os 
def to(arg):
    args= arg.split()
    x=args.index('>')
    fname=args[x+1]
    open(fname,'w')
    xargs = args[:x]
    #print str(args[0])
    old=os.dup(1)
    os.close(1)
    os.open(fname,os.O_WRONLY|os.O_CREAT)
    x=os.fork()
    if x==0:
        os.execvp(args[0],xargs)
    else:
        os.wait()

    os.close(1)
    os.dup(old)
    os.close(old)

def froms(arg):

    args=arg.split()
    x=args.index('<')
    fname=args[x+1]
    xargs=args[:x]
    old=os.dup(0)
    os.close(0)
    os.open(fname,os.O_RDONLY)
    x=os.fork()
    if x==0:
        os.execvp(args[0],xargs)
    else:
        os.wait()
    os.close(0)
    os.dup(old)
    os.close(old)

def pipeline(cmd):
    std_in=os.dup(0)
    std_out=os.dup(1)
    count = cmd.count('|')
    commands=cmd.split('|')
    for i in commands:
        commands[commands.index(i)]=commands[i].split()
    pipes=[]
    for i in range(count):
        pipes.append(tuple(os.pipe()))
    if os.fork()==0:
        os.dup2(pipes[0][1],1)
        for k in range(count):
            for j in range(2):
                os.close(pipes[k][j])
        os.execvp(commands[0][0],commands[0])
    else:
        for i in range(1,count):
            if os.fork()==0:
                os.dup2(pipes[i-1][0],0)
                os.dup2(pipes[i][1],1)
                for k in range(count):
                    for j in range(2):
                        os.close(pipes[k][j])
                os.execvp(commands[i][0],commands[i])
        if os.fork()==0:
            os.dup2(pipes[-1][0],0)
            for k in range(count):
                for j in range(2): 
                    os.close(pipes[k][j])
            os.execvp(commands[-1][0],commands[-1])
        else:
            for k in range(count):
               for j in range(2):
                   os.close(pipes[k][j])
            for i in range(count):
                os.wait()
            os.wait()
            os.dup2(std_out,1)
            os.dup2(std_in,0)
            return
            
        


def instdecomp(cmd):
    args=cmd.split()
    os.execvp(args[0],args)
    


def shell():
    print "----------MSP Shell---------\n\n\n"
    while(1):
        cmd=raw_input("MSPshell:")
        if '<' in cmd:
        	froms(cmd)
    
        if '>' in cmd:
        	to(cmd)
        	
        if cmd=='exit':
            exit(0)
        
        newpid=os.fork()
        if newpid==0:
            instdecomp(cmd)
        else:
            os.wait()  
        
shell()



  

    
