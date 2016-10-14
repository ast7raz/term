# -*- coding: utf-8 -*-

import urllib2
import urllib
import cookielib,re
import lxml.html as html
import json
import logging
#logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO, filename = u'Z:\\home\\test.key\\www\\mysite\\Agree_base_django.log')

def Admin_Authorization(user="", password=""):
    url=""
    slov={"signin[username]":user, "back":"", "signin[password]":password}
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie),urllib2.ProxyHandler({'https','195.26.17.110:3081'}))
    urllib2.install_opener(opener)
    data_to_request = slov
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36",
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
    params_auth = urllib.urlencode(data_to_request)
    request_auth = urllib2.Request(url, params_auth, headers)
    page=opener.open(request_auth).read()
    #print(page)
    reg="window.localStorage.+"
    p=re.compile(reg)
    tok=p.findall(page)
    dkt=tok[0].split(" = '")[1].replace("';","")
    token={"token":dkt}
    return opener, token

def get_partlist(opener):
    posturl="%s/ajax-lists-filters/backend/autocomplete/partners" %opener.host
    data={"search":"*","related_fields":{"type_action":"1"}, "token":opener.token["token"]}
    dat=urllib.urlencode(data)
    PartList=json.loads(opener.open(posturl, dat).read())
    return PartList
def get_cash_in_club(opener, club_id, ):
    posturl="%s/backend.php/club/%s/edit" %(opener.host, club_id)
    #data={"club_id":club_id}
    #dat=urllib.urlencode(data)
    page=opener.open(posturl).read()
    #print(page)
    pag=html.document_fromstring(page)
    li=pag.xpath("//*[@id='club_cashdesks_of_club_list']/option")
    list_cash_id=[]
    for i in li:
        try:
            if i.attrib["selected"]=="selected":
                list_cash_id.append(i.attrib["value"])
        except KeyError:
            pass
    if len(list_cash_id)>0:
        return True, list_cash_id
    else:
        return False, list_cash_id
    #list_cash_id=[]
    #for key in CashList:
    #    cash_base_id=((CashList[key]["name"]).split(" ")[2].split("/")[-2])
    #    list_cash_id.append(cash_base_id)
    #if len(CashList)>0:
    #    return True, list_cash_id
    #else:
    #    return False, list_cash_id

def get_clubs_url(opener):
    clubsurl="%s/backend.php/club" %opener.host
    page=opener.open(clubsurl).read()
    htmlpage=html.document_fromstring(page)
    range_pages=htmlpage.xpath('//*[@id="footer"]/div[1]/b')[0].text.split(" ")[3]
    #print(range_pages)
    url_list=[]
    for p in range(int(range_pages)):
        p=p+1
        url_list.append("%s?page=%s" %(clubsurl, p))
    return url_list

def get_clubs_on_page(opener, cluburl):
    page=opener.open(cluburl).read()
    htmlpage=html.document_fromstring(page)
    tbody=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr')
    slov={}
    for tr in range(len(tbody)):
        tr=tr+1
        base_id=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]' %tr)[0].attrib["rel"]
        cashInClub, ListCashId=get_cash_in_club(opener,base_id)
        if cashInClub==True:
            part_name=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[1]' %tr)[0].text.replace("\n","").strip()
            club_name=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[2]' %tr)[0].text.replace("\n","").strip()

            slov[base_id]={"club_name":club_name, "part_name":part_name, "base_id":base_id, "list_cash":ListCashId}
            #print(slov[base_id])
    return slov

def agr_club_in_cash(clubs_dictions, cashs_dictions):
    for key in clubs_dictions:
        #print(key+"  in clubs")
        cash_list=clubs_dictions[key]["list_cash"]
        for id in cash_list:
            #print(id+"  in cashs")
            try:
                cashs_dictions[id].update({"club_base_id":key})
            except KeyError:
                pass
    return cashs_dictions



def get_all_clubs(opener):
    all_clubs={}
    clubsurl=get_clubs_url(opener)
    for i in clubsurl:
        all_clubs.update(get_clubs_on_page(opener,i))
        logging.info(str(i))
        print(i)
    return all_clubs
"""class ClubThread(threading.Thread):
    def __init__(self, opener, cluburl):
        threading.Thread.__init__(self)
        self.daemon=False
        self.opener=opener
        self.cluburl=cluburl
    def run(self):
        all_clubs.update(get_clubs_on_page(self.opener, self.cluburl))

"""
def get_cashs_url(opener):
    cashsurl="%s/backend.php/cashdesk" %opener.host
    page=opener.open(cashsurl).read()
    htmlpage=html.document_fromstring(page)
    range_pages=htmlpage.xpath('//*[@id="footer"]/div[1]/b')[0].text.split(" ")[3]
    #print(range_pages)
    url_list=[]
    for p in range(int(range_pages)):
        p=p+1
        url_list.append("%s?page=%s" %(cashsurl, p))
    return url_list
def get_cashs_on_page(opener, cluburl):
    page=opener.open(cluburl).read()
    htmlpage=html.document_fromstring(page)
    tbody=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr')
    slov={}
    for tr in range(len(tbody)):
        tr=tr+1
        activ=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[2]' %tr)[0].text.replace("\n","").strip()

        if activ!=u'\u0417\u0430\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u043d':
            club_name=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[8]' %tr)[0].text.replace("\n","").strip()
            if club_name!="":
                part_name=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[9]' %tr)[0].text.replace("\n","").strip()
                base_id=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[1]/a' %tr)[0].attrib["href"].split("/")[-2]
                cash_name=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[1]/a' %tr)[0].text.replace(u"Касса ","")
                #print(club_name)
                slov[base_id]={"club_name":club_name, "part_name":part_name, "base_id":base_id, "cash_name":cash_name}
                #print(cash_name)
                #print(slov[base_id])
    return slov
def get_all_cash(opener):
    all_cashs={}
    clubsurl=get_cashs_url(opener)
    for i in clubsurl:
        all_cashs.update(get_cashs_on_page(opener,i))
        logging.info(unicode(i))
        #print(unicode(i))
    return all_cashs
def get_terminal_url(opener):
    terminalurl="%s/backend.php/terminal" %opener.host
    page=opener.open(terminalurl).read()
    htmlpage=html.document_fromstring(page)
    range_pages=htmlpage.xpath('//*[@id="footer"]/div[1]/b')[0].text.split(" ")[3]
    #print(range_pages)
    url_list=[]
    for p in range(int(range_pages)):
        p=p+1
        url_list.append("%s?page=%s" %(terminalurl, p))
    return url_list
def get_key(opener,id):
    url="%s/backend.php/terminal/%s/edit" %(opener.host, str(id))
    page2 = opener.open(url).read()
    text2=html.document_fromstring(page2)
    key=text2.xpath("//*[@id='terminal']/fieldset/div[1]/div[5]/text()")[1].replace('\n\t\t\t\t\t', '').replace("\t\t\t\t", "")
    return key

def get_terminals_on_page(opener, termurl):
    page=opener.open(termurl).read()
    htmlpage=html.document_fromstring(page)
    tbody=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr')
    slov={}
    #print()

    for tr in range(len(tbody)):

        tr=tr+1
        activ_base=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[5]/img' %tr)[0].attrib["title"]
        if activ_base=="Checked":
            activ=True
        else:
            activ=False
        blocked_base=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[6]/img' %tr)[0].attrib["title"]
        if blocked_base=="Checked":
            blocked=True
        else:
            blocked=False
        name=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[1]' %tr)[0].text.replace("\n","").strip()
        part=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[2]' %tr)[0].text.replace("\n","").strip()
        club=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[3]' %tr)[0].text.replace("\n","").strip()
        base_id=htmlpage.xpath('//*[@id="sf_admin_content"]/div/table/tbody/tr[%s]/td[7]/ul/li/a' %tr)[0].attrib["href"].split("/")[-2]
        key=get_key(opener, base_id)
        #print([key, name, part, club, activ, blocked, base_id])
        slov[base_id]={"key":key, "name":name, "part_name":part, "club_name":club, "activ":activ, "blocked":blocked, "base_id":base_id}
    return slov

def get_all_terminals(opener):
    all_terminals={}
    clubsurl=get_terminal_url(opener)
    for i in clubsurl:
        all_terminals.update(get_terminals_on_page(opener,i))
        logging.info(unicode(i))
        #print(i)
    return all_terminals

def get_cashs_and_clubs(opener):
    #logging.info(u"")
    clubs=get_all_clubs(opener)
    cashs=get_all_cash(opener)
    cashs_new=agr_club_in_cash(clubs,cashs)
    return clubs, cashs_new


if __name__=="__main__":
    pass
