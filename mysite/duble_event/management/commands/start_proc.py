from django.core.management.base import BaseCommand, CommandError
from duble_event.runer_lib import proccess_started, st
from duble_event.Parser_event import connect, pars, search_duble,base_writer
from duble_event.models import Logging_duplicates
from datetime import datetime
class Command(BaseCommand):
    args=""
    help="Agreegator db for rub90 admin"
    def handle(self, *args, **options):
        proccess_started()
        try:

            while True:

                Page=connect()
                #print(Page)
                Event_list=pars(Page)
                Find_dubles=search_duble(Event_list)
                base_writer(Find_dubles)
        except:
            loging_event = Logging_duplicates()
            loging_event.event1_id = 0
            loging_event.event2_id = 0
            loging_event.event1_date = datetime.utcnow()
            loging_event.event2_date = datetime.utcnow()
            loging_event.event1_team1 = "Parser"
            loging_event.event1_team2 = "Stop"
            loging_event.event2_team1 = "User"
            loging_event.event2_team2 = "Error"
            loging_event.event1_sport = "Error"
            loging_event.event2_sport = "Error"
            # print(loging_event)
            loging_event.save()








        """find_dubles = [{'event2':{u'category':{u'ordering': 0,
                                                 u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435',
                                                 u'id': 2000000081},
                                  u'tournament': {u'ordering': 0,
                                                  u'country': {
                                                                u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0439',
                                                                u'alpha_2': u'WORLD',
                                                                u'id': None,
                                                                u'alpha_3': u'WORLD'},
                                                  u'id': 2000001383,
                                                    u'ru': u'\u0422\u043e\u0432\u0430\u0440\u0438\u0449\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0447\u0438 \u0414\u043e 21 \u0433\u043e\u0434\u0430',
                                                    u'rating': 1},
                                  u'teams': {
                                                u'1': {u'ru': u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430 (\u0434\u043e21)',
                                                       u'id': 2000041263},
                                                u'2': {u'ru': u'\u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0438\u044f (\u0434\u043e21)',
                                                        u'id': 2000048738}},
                                  'state': {u'active': True,
                                            u'provider_id': 1,
                                            u'short_id': 6001},
                                   u'anons': False,
                                  u'filters': u'',
                                  u'date': 1496934000,
                                    u'sport': {u'ordering': 15,
                                               u'ru': u'\u0424\u0443\u0442\u0431\u043e\u043b',
                                              u'id': 1},
                                  u'id': 2000958819},
                        'event1': {u'category': {u'ordering': 0,
                                                                                                      u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435',
                                                                                                      u'id': 2000000081},
                                                                                        u'tournament': {u'ordering': 0,
                                                                                                        u'country': {
                                                                                                            u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0439',
                                                                                                            u'alpha_2': u'WORLD',
                                                                                                            u'id': None,
                                                                                                            u'alpha_3': u'WORLD'},
                                                                                                        u'id': 2000001383,
                                                                                                        u'ru': u'\u0422\u043e\u0432\u0430\u0440\u0438\u0449\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0447\u0438 \u0414\u043e 21 \u0433\u043e\u0434\u0430',
                                                                                                        u'rating': 1},
                                                                                        u'teams': {u'1': {
                                                                                            u'ru': u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430 (\u0434\u043e21)',
                                                                                            u'id': 2000041263}, u'2': {
                                                                                            u'ru': u'\u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0438\u044f (\u0434\u043e21)',
                                                                                            u'id': 2000219561}},
                                                                                        'state': {u'active': True,
                                                                                                  u'provider_id': 2,
                                                                                                  u'anons': True,
                                                                                                  u'short_id': 4962},
                                                                                        u'anons': True, u'filters': u'',
                                                                                        u'date': 1496934000,
                                                                                        u'sport': {u'ordering': 15,
                                                                                                   u'ru': u'\u0424\u0443\u0442\u0431\u043e\u043b',
                                                                                                   u'id': 1},
                                                                                        u'id': 2000958582}},










                       ]
        base_writer(find_dubles)"""