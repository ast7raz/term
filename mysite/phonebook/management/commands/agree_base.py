from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from phonebook import save_Base
import logging, os, shutil
class Command(BaseCommand):
    args=""
    help="Agreegator db for rub90 admin"
    option_list = BaseCommand.option_list + (
        make_option("-p",
                    '--partners',
                    action='store_false',
                    dest='partners',
                    default=True,
                    help='If this chapter is True agreegator is read admin on partner' ),
        make_option("-c",
                    '--cashs_clubs',
                    action='store_false',
                    dest='clubs',
                    default=True,
                    help='If this chapter is True agreegator is read admin on club'),
        make_option("-t",
                    '--terminals',
                    action='store_false',
                    dest='terminals',
                    default=True,
                    help='If this chapter is True agreegator is read admin on Terminals'),
    )

    def handle(self, *args, **options):
        try:
            f = open(save_Base.filename, "w")
        except Exception, e:
            logging.info(e.args[1].decode("cp1251"))
        logging.info(u'This proccess pid %s' % str(os.getpid()))
        save_Base.agree_all_data(partner=options["partners"], clubs_cashs=options["clubs"], terminals=options["terminals"])
        strdel = save_Base.remoove_facke_bd()
        logging.info(strdel)
        newfilename = save_Base.getNewFileName(save_Base.filename)
        shutil.copy2(save_Base.filename, newfilename)