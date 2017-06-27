import psutil, sys, os, time
from mysite.settings import DUBLE_EVENT_DIR

def proccess_started(file_name="server"):
    filename=os.path.join(DUBLE_EVENT_DIR, file_name+".pid")
    try:
        f=open(filename)
        pid=int(f.read())
        f.close()
    except:
        pid = os.getpid()
        f = open(filename, "w")
        f.write(str(pid))
        f.close()
    else:
        if psutil.pid_exists(pid)==True:
            #print("Exist process with id: "+str(pid))
            sys.exit()
        else:
            pid=os.getpid()
            f = open(filename, "w")
            f.write(str(pid))
            f.close()
def proccess_status(proc_name="server"):
    filename = os.path.join(DUBLE_EVENT_DIR, proc_name + ".pid")
    try:
        f = open(filename)
        pid = int(f.read())
        f.close()
    except:
        return False
    else:
        if psutil.pid_exists(pid) == True:
            return True
        else:
            return False
def proccess_kill(proc_name="server"):
    filename = os.path.join(DUBLE_EVENT_DIR, proc_name + ".pid")
    try:
        f = open(filename)
        pid = int(f.read())
        f.close()
    except:
        return False
    else:
        if psutil.pid_exists(pid) == True:
            p=psutil.Process(pid)
            #print(p.cmdline()[1])
            p.terminate()
            return True
        else:
            return False
def st():
    proccess_started()
    while True:

        #print(proccess_status())
        time.sleep(10)
if __name__=="__main__":
    proccess_started()
    while True:

        #print(proccess_status())
        time.sleep(10)
        #proccess_kill()



#print (sys.exit())
