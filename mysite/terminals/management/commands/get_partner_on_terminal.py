# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from terminals.models import Keys
from phonebook.models import Partner
from terminals.Lib import get_part_on_version_term
import logging, os, shutil
class Command(BaseCommand):
    args=""
    help="Geting partners of version"
    option_list = BaseCommand.option_list + (
        make_option("-V",
                    '--ver',
                    dest='version',
                    default="",
                    help='Geting partners of version terminal' ),


    )

    def handle(self, *args, **options):
        print("partner")
        print(options["version"])
        #keys=Keys.objects.filter(version__icontains=options["version"])
        #print(len(keys))
        partners=get_part_on_version_term(options["version"])
        for i in partners:
            #print(i.part_name)
            if u"\xab" in i.part_name:
                i.part_name=i.part_name.replace(u"\xab",u"<<")
            if u"\xbb" in i.part_name:
                i.part_name = i.part_name.replace(u"\xbb", u">>")

            keys=Keys.objects.filter(part=i)
            keys_new=keys.filter(version__icontains="~")
            keys_old = keys.filter(version__icontains=".")
            #print(len(keys))
            print(u"%s - всего ключей:%s; новых терминалов:%s; старых терминалов:%s;" %(i.part_name, len(keys), len(keys_new), len(keys_old)))