# -*- coding: utf-8 -*-
__author__ = 'user'
import os, sys, argparse,time, shutil

import rubParse
import logging
from autorizback import Opener
#import setuper

from mysite import settings
logdir=settings.LOG_DIR
filename=os.path.join(logdir,'Agree.log')

logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO, filename = filename)
#print(filename)
#print(logdir)
from phonebook.models import Cash,Club,Partner
from terminals.models import Keys, Parser_users

def cash_agree(cash_diction):
    """print(cash_diction)
    for key in cash_diction:
        print("%s:%s" %(key,cash_diction[key]))"""
    try:
        part=Partner.objects.get(part_name=cash_diction["part_name"])
        club=Club.objects.get(base_id=cash_diction["club_base_id"], partner=part)
        """try:
            club=Club.objects.get(club_name=cash_diction["club_name"], partner=part)
        except Club.MultipleObjectsReturned:
            club=Club.objects.filter(club_name=cash_diction["club_name"], partner=part)[-1]"""
        try:
            cash=Cash.objects.get(base_id=cash_diction["base_id"])
        except Cash.DoesNotExist:
            cash=Cash()
        cash.base_id=cash_diction["base_id"]
        cash.cash_name=cash_diction["cash_name"]
        cash.partner=part
        cash.club=club
        cash.save()
    except Club.DoesNotExist:
        logging.info(u"Club DoesNot Exist: %s for cash base_id - %s" %(unicode(cash_diction["club_name"]), unicode(cash_diction["base_id"])))
    except KeyError:
        pass
    except Partner.DoesNotExist:
        logging.info(u"Partner DoesNot Exist: %s for cash base_id - %s" %(unicode(cash_diction["part_name"]), unicode(cash_diction["base_id"])))


def club_agree(club_diction):
    try:
	try:
    	    part=Partner.objects.get(part_name=club_diction["part_name"])
    	except Partner.MultipleObjectsReturned:
    	    partobj= Partner.objects.filter(part_name=club_diction["part_name"])
    	    for part in partobj:
    		print(part)
        #print(club_diction)
        try:
            club=Club.objects.get(base_id=club_diction["base_id"])
        except Club.DoesNotExist:
            club=Club()
        #print(club_diction["part_name"])
        club.partner=Partner.objects.get(part_name=club_diction["part_name"])
        club.base_id=club_diction["base_id"]
        club.club_name=club_diction["club_name"]
        #print(club)
        club.save()
    except Partner.DoesNotExist:
        logging.info(u"Partner DoesNot Exist: %s for club base_id - %s" %(unicode(club_diction["part_name"]), unicode(club_diction["base_id"])))
def partner_agree(part_diction):
    name=part_diction[1]
    base_id=part_diction[0]
    try:
        part=Partner.objects.get(base_id=base_id)
    except Partner.DoesNotExist:
        part=Partner()
    part.part_name=name
    part.base_id=base_id
    part.save()
def terminal_agree(term_diction):
    if term_diction["club_name"]!="":
        #print(term_diction)
        try:
            part=Partner.objects.get(part_name=term_diction["part_name"])
            try:
        	club=Club.objects.get(club_name=term_diction["club_name"], partner=part)
    	    except Club.MultipleObjectsReturned:
    		club=Club.objects.filter(club_name=term_diction["club_name"],partner=part)
    		for i in club:
    		    print(i)
    		    print(part)
    		    bad=i
    		club=bad
            #print(club)
            """try:
                club=Club.objects.get(club_name=cash_diction["club_name"], partner=part)
                except Club.MultipleObjectsReturned:
                club=Club.objects.filter(club_name=cash_diction["club_name"], partner=part)[-1]"""
            try:
                term=Keys.objects.get(base_id=term_diction["base_id"])
            except Keys.DoesNotExist:
                term=Keys()
            term.base_id=term_diction["base_id"]
            term.key=term_diction["key"]
            term.name=term_diction["name"]
            term.active=term_diction["activ"]
            term.blocked=term_diction["blocked"]
            term.part=part
            term.club=club
            term.save()
            #print(term.part)
        except Club.DoesNotExist:
            logging.info(u"Club DoesNotExist %s for key %s"%(term_diction["club_name"], term_diction["key"]))
        except Partner.DoesNotExist:
            logging.info(u"Partner DoesNotExist %s for key %s" %(term_diction["part_name"], term_diction["key"]))

def agree_partners(parts_dictions):
    for i in parts_dictions:
        partner_agree(i)
def agree_clubs(clubs_dictions):
    for key in clubs_dictions:
        club_agree(clubs_dictions[key])
def agree_cashs(cashs_dictions):
    for key in cashs_dictions:
        cash_agree(cashs_dictions[key])
def agree_terminals(terms_dictions):
    for key in terms_dictions:
        terminal_agree(terms_dictions[key])

def agree_all_data(partner=True,clubs_cashs=True, terminals=True):
    logging.info(u"Start Agreegate")
    logging.info(u"Agregate param: Partner=%s; Club and Cash=%s; Terminals=%s;" %(unicode(partner), unicode(clubs_cashs), unicode(terminals)))
    PU=Parser_users.objects.get(parser="adminka")
    opener=Opener(object_user=PU)
    if partner==True:
        logging.info(u"Partner")
        #print("Partner")
        partlist=rubParse.get_partlist(opener)
        agree_partners(partlist)
    if clubs_cashs==True:
        logging.info(u"Clubs and Cashs")
        #print("Clubs and Cashs")
        clubs, cashs=rubParse.get_cashs_and_clubs(opener)
        agree_clubs(clubs)
        agree_cashs(cashs)
    if terminals==True:
        logging.info(u"Terminals")
        #print("Terminals")
        term=rubParse.get_all_terminals(opener)
        agree_terminals(term)
    logging.info(u"Agreegate Done")
def boolifT(string):
    if string=="True" or string=="true" or string=="t" or string=="T":
        return True
    else:
        return False
def boolifF(string):
    if string=="False" or string=="false" or string=="f" or string=="F":
        return False
    else:
        return True
def createParser():
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--partner", type=boolifF, default=True, help='Keep "f" or "F" or "false" or "False" to disable agreegate Partners')
    parser.add_argument("-c","--clubs_cashs", type=boolifF, default=True, help='Keep "f" or "F" or "false" or "False" to disable agreegate Cashs and Clubs')
    parser.add_argument("-t","--terminals", default=True, type=boolifF, help='Keep "f" or "F" or "false" or "False" to disable agreegate Terminals')
    return parser
def getNewFileName(filename):
    strtime=time.strftime("%d.%m_%H.%M.%S")
    #print(strtime)
    #strtime="1"
    filename=os.path.split(filename)[-1]
    listfilnaem=filename.split(u".")
    filname=listfilnaem[-2]+strtime
    listfilnaem[-2]=filname
    newfilename=".".join(listfilnaem)
    #print(newfilename)
    newfilename=newfilename.split(u"\\")[-1]
    #print(newfilename)
    newfilename=os.path.join(logdir, newfilename)
    #print(newfilename)
    return newfilename
def main():

    try:
        f=open(filename, "w")
    except Exception, e:
        logging.info(e.args[1].decode("cp1251"))
    logging.info( u'This proccess pid %s' %str(os.getpid()))
    parser=createParser()
    namespase=parser.parse_args(sys.argv[1:])
    #print(namespase)
    #try:
    agree_all_data(partner=namespase.partner, clubs_cashs=namespase.clubs_cashs, terminals=namespase.terminals)
    strdel=remoove_facke_bd()
    logging.info(strdel)
    #except:
    #    logging.info("Process stoped with Error")
    #finally:
    newfilename=getNewFileName(filename)
    shutil.copy2(filename, newfilename)
def remoove_facke_bd():
    parts=Partner.objects.filter(cash__isnull=True, keys__isnull=True)
    lenparts=u"Delete %s partners" %len(parts)
    parts.delete()
    clubs=Club.objects.filter(cash__isnull=True, keys__isnull=True)
    lenclubs=u"Delete %s clubs" %len(clubs)
    clubs.delete()
    return " and ".join([lenparts, lenclubs])
def Get_prtners_receive_terminals():
    parts=Partner.objects.all()
    print("Number of all partners: %s" %str(len(parts)))
    parts=parts.exclude(keys__isnull=True)
    print("Number of partners with terminals: %s" %str(len(parts)))
    return parts
def Get_clubs_receive_terminals():
    clubs=Club.objects.all()
    print("Number of all clubs: %s" %str(len(clubs)))
    clubs=clubs.exclude(keys__isnull=True)
    print("Number of clubs with terminals: %s" %str(len(clubs)))
    return clubs



"""if __name__=="__main__":
    print(Get_project_path())
    main()"""
if __name__=="__main__":

    main()