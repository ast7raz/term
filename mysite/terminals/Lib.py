import psutil
from phonebook.models import Partner

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

def get_pid_of_log(log="D:\\gitterm\\mysite\\Logs_site\\Agree.log"):
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
#print(get_pid_of_log())

def kill_proc(pid):
    try:
        p = psutil.Process(int(pid))
        # print(p)
    except psutil.NoSuchProcess:
        #print ("What?")
        return False
    p.kill()
    return True
def get_part_on_version_term(version=""):
    partners = Partner.objects.all()
    if version != "":
        partners = partners.filter(keys__version__icontains=version)
    partners = partners.distinct()
    partners = partners.order_by("part_name")
    return partners
