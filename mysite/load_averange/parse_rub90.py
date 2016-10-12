__author__ = 'user'
import urllib2,os
import lxml.html as html
"""from PIL import Image"""
from StringIO import StringIO
'''try:
    from load_averange.img_control import LA, LA1
except:
    print("Not import PIL")'''
username="admin"
password="CeeBip3x"



class LoadAverange_p():
    links=["http://p1.rub90.com:9920/monit-per-process/",
           "http://p2.rub90.com:9920/monit-per-process/",
           "http://p3.rub90.com:9920/monit-per-process/",
           "http://p2lxc1.rub90.com:9920/monit-per-process/",]
    address="/var/www-support/static/la"
    ad="/lapng/"
    def __init__(self,name_dir):
        #print(name_dir)
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None, "http://p1.rub90.com:9920/monit-per-process/", username, password)
        handler = urllib2.HTTPDigestAuthHandler(password_mgr)
        self.opener = urllib2.build_opener(handler)
        #print(name_dir)
        self.path=os.path.join(self.address, name_dir)
        if os.path.exists(self.path)!=True:
            os.mkdir(self.path)
        for i in self.links[1:]:

            password_mgr.add_password(None, i, username, password)
            handler = urllib2.HTTPDigestAuthHandler(password_mgr)
            self.opener.add_handler(handler)

        urllib2.install_opener(self.opener)
        #setupd opener
        self.links_img=[]
        for url in self.links:
            r=urllib2.urlopen(url).read()
            #print(r)
            page=html.document_fromstring(r)
            li=page.xpath("/html/body/center/center")
            #print(li)
            for i in range(len(li)+1):
                if i==1 and len(li)==1:
                    retr=''
                else:
                    retr="["+str(i)+"]"
                ul=page.xpath("/html/body/center/center%s/img/@src" % retr)
                if len(ul)>0:
                    link_img=ul[0].replace("./",url)
                    serv_name=link_img.split("/")[2].split(".")[0]
                    name=serv_name+"_"+link_img.split("/")[-1]
                    name2=serv_name+"_"+str(i)+"png"
                    adress=os.path.join(self.path, name2)
                    new_link=self.ad+name_dir+"/"+name2
                    #print(new_link)
                    slov_img={"name":name, "serv_name":serv_name, "link_img":link_img, "address":adress, "new_link":new_link,'LA':0}
                    self.links_img.append(slov_img)
    def get_all_images(self):
        for i in range(len(self.links_img)):
            resource = urllib2.urlopen(self.links_img[i]["link_img"])
            out=open(self.links_img[i]["address"], "wb")
            out.write(resource.read())
            out.close()
            '''try:
                self.links_img[i]["LA"]=LA(self.links_img[i]["address"])["LA"]
            except:
                print("Not LA of not import Pil")'''

    def get_img_by_name(self, name):
        for i in range(len(self.links_img)):
            if self.links_img[i]["name"]==name:
                resource = urllib2.urlopen(self.links_img[i]["link_img"])
                out=open(self.links_img[i]["address"], "wb")
                out.write(resource.read())
                out.close()
                '''try:
                    self.links_img[i]["LA"]=LA(self.links_img[i]["address"])["LA"]
                except:
                    print("Not LA of not import Pil")'''
                #print(self.links_img[i]["LA"])
                return self.links_img[i]
'''    def get_new_img_by_name(self, name):

        for i in range(len(self.links_img)):

            if self.links_img[i]["name"]==name:
                try:
                    resource = urllib2.urlopen(self.links_img[i]["link_img"])
                    #print(resource.read())
                    img1=Image.open(StringIO(resource.read()))
                    #img1.show()
                    self.links_img[i]["LA"]=LA1(img1)["LA"]
                    #print(self.links_img[i]["LA"])
                    return self.links_img[i]
                except:
                    return self.links_img[i]
'''


if __name__=="__main__":
    r=LoadAverange_p("ats")
    #print(r.links_img)
    name="p1_apache2.png"
    print("start")
    r.get_all_images()
    print("stop")
    for i in r.links_img:
        print(i["new_link"])