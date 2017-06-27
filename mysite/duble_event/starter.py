from subprocess import Popen, PIPE
def st():
        p=Popen(["C:\Python27\python.exe", "D:/gitterm/mysite/manage.py", "start_proc"],
                shell=True,
                stdout=open("D:/gitterm/mysite/duble_event/test.log", "w+"),
                #stderr=PIPE,
                )
        return True
#p.wait()
#res, err= p.communicate()
#print(res)