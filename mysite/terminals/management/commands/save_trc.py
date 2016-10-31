from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from terminals import rts_save_ip
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
        rts_save_ip.saver_go()