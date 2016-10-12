__author__ = 'user'
import PIL.Image as Image

def LA(adr):
    img_len=400
    img1=Image.open(adr)

    img2=img1.crop((471,30,472,130))
    im={"fon":0,"ave":0,"la":0,"ost":0}
    for i in img2.getcolors():
        if i[1]==(255,255,255):
            im["fon"]=i[0]
        elif i[1]==(255,0,0):
            im["ave"]=i[0]
        elif i[1]==(243,191,191):
            im["la"]=i[0]
        else:
            im["ost"]=i[0]
    aver=im["ave"]+im["ost"]
    return {"LA":aver}
def LA1(img1):
    #img_len=400
    #img1=Image.open(adr)

    img2=img1.crop((471,30,472,130))
    im={"fon":0,"ave":0,"la":0,"ost":0}
    for i in img2.getcolors():
        if i[1]==(255,255,255):
            im["fon"]=i[0]
        elif i[1]==(255,0,0):
            im["ave"]=i[0]
        elif i[1]==(243,191,191):
            im["la"]=i[0]
        else:
            im["ost"]=i[0]
    aver=im["ave"]+im["ost"]
    return {"LA":aver}
def LoAv(adr):
    sl={}
    img_len=399
    img1=Image.open(adr)
    for il in range(img_len):
        img2=img1.crop((471-il,30,472-il,130))
        im={"fon":0,"ave":0,"la":0,"ost":0}
        for i in img2.getcolors():
            if i[1]==(255,255,255):
                im["fon"]=i[0]
            elif i[1]==(255,0,0):
                im["ave"]=i[0]
            elif i[1]==(243,191,191):
                im["la"]=i[0]
            else:
                im["ost"]=i[0]
        aver=im["ave"]+im["ost"]
        sl["LA"+str(il)]=aver
    return sl

if __name__=="__main__":
    print(LoAv("Z:\\home\\test.key\\www\\static\\la\\p1_1")["LA0"])