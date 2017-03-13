from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from terminals.pars_trcv2 import TRC_Parser
from terminals.models import Parser_users
import logging, os, shutil
class Command(BaseCommand):
    args=""
    help="Scaning trc of key online"
    option_list = BaseCommand.option_list + (
        make_option("-p",
                    '--partners',
                    action='store_false',
                    dest='partners',
                    default=True,
                    help='If this chapter is True agreegator is read admin on partner' ),


    )

    def handle(self, *args, **options):
        PU = Parser_users.objects.get(parser="trcv2")
        parser=TRC_Parser(username=PU.username, password=PU.userpass, url=PU.parsurl)
        for key in parser.get_list_keys():
            key.save_in_db()