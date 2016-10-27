import psutil

def test_procces(pid, serch_string):
    try:
        p = psutil.Process(int(pid))
        #print(p)
    except psutil.NoSuchProcess:
        return False
    cmd=p.cmdline()
    #print("test_proccess")
    #print(cmd)
    if serch_string in cmd:
        return True
    else:
        return False

def get_pid_of_log(log):
    f=open(log, "r")
    text=f.read()
    f.close()
    list_of_text=text.split("\n")
    string_pid=""
    for i in list_of_text:
        if "This proccess pid" in i:
            string_pid=i
    #print(string_pid)
    pid=string_pid.split(" ")[-1]
    return pid
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
#print(get_pid_of_log())
>>>>>>> 2742650... added mass effect in key online.
=======
#print(get_pid_of_log())
>>>>>>> 2742650... added mass effect in key online.
=======
#print(get_pid_of_log())
>>>>>>> 2742650... added mass effect in key online.
=======
#print(get_pid_of_log())
>>>>>>> 2742650... added mass effect in key online.

def kill_proc(pid):
    try:
        p = psutil.Process(int(pid))
        # print(p)
    except psutil.NoSuchProcess:
        #print ("What?")
        return False
    p.kill()
    return True