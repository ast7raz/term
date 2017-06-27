from subprocess import Popen, PIPE
def st():
        p=Popen(["/usr/local/bin/python", "/var/www-support/mysite/manage.py", "start_proc"],
                shell=True,
                #stdout=open("/var/www-support/mysite/duble_event/test.log", "w+"),
                #stderr=PIPE,
                )
        return True
#p.wait()
#res, err= p.communicate()
#print(res)
if __name__=="__main__":
    print(st())