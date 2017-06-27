import runer_lib
import urllib
import logging, time, json
from datetime import datetime
from duble_event.models import Exceptions, Found_duplicates, Logging_duplicates, Parser_duble_event
def get_exceptions():
    ids=[]
    sports=[]
    teams=[]
    except_objects=Exceptions.objects.all()
    for except_object in except_objects:
        if except_object.Symptom=="id":
            ids.append(int(except_object.text))
        elif except_object.Symptom=="sport":
            sports.append(except_object.text)
        elif except_object.Symptom == "team":
            teams.append(except_object.text)
        else:
            pass
        #print(ids)
    return {"ids":ids, "sports":sports, "teams":teams}
def connect(url="https://rub90.com/contentdata/prematch/ru"):
    try:
        parser_config=Parser_duble_event.objects.get(site_name="rub901")
        pars_url=parser_config.pars_url
    except Parser_duble_event.DoesNotExist:
        pars_url=url
    try:
        page= urllib.urlopen(pars_url)
        response=json.load(page)
    except:

        logging.error("Connection problem")
        time.sleep(10)
        response=connect()
    return response

def pars(event_json):
    event_list={}
    event_json=event_json["delta"]["bm"]
    #print(event_json)
    for event_proh in event_json:
        #print(event_proh)
        event_json[event_proh]["desc"]["state"]=event_json[event_proh]["PP-0"]["state"]

        event_list[event_json[event_proh]["desc"]["id"]]=event_json[event_proh]["desc"]
    return event_list

def search_duble(event_list):
    find_dubles=[]
    exceptions=get_exceptions()
    #event_list_2=event_list
    for key in event_list.keys():
        event=event_list.pop(key)
        #exceptions
        #print(event)
        if event["id"] not in exceptions["ids"] and\
            event["sport"]["ru"]not in exceptions["sports"] and\
            event["teams"]["1"]["ru"]not in exceptions["teams"] and \
            event["teams"]["2"]["ru"] not in exceptions["teams"]:
            if u"blocked" not in event["state"].keys():
                #print((key, event["state"]))
                for key2 in event_list.keys():
                    event2=event_list[key2]
                    if u"blocked" not in event2["state"].keys():
                        #print(("                ",key2, event2["state"]))
                        if ((event["teams"]["1"]["ru"]==event2["teams"]["1"]["ru"])or\
                            (event["teams"]["1"]["ru"]==event2["teams"]["2"]["ru"]))and \
                            ((event["teams"]["2"]["ru"] == event2["teams"]["2"]["ru"]) or \
                            (event["teams"]["2"]["ru"] == event2["teams"]["1"]["ru"])) and \
                            (event["sport"]["ru"]==event2["sport"]["ru"]):

                            diff_date=abs(event["date"]-event2["date"])
                            if diff_date<7200:
                                find_dubles.append({"event1":event, "event2":event2})
    return find_dubles
def base_writer(find_dubles):
    if len(find_dubles)>0:
        for duble in find_dubles:
            #print(duble["event1"]["teams"])
            #print(duble["event2"]["teams"])
            try:
                Found_duplicates.objects.get(event1_id=duble["event1"]["id"],
                                             event2_id=duble["event2"]["id"],
                                             #event1_date=duble["event1"]["date"],
                                             #event2_date=duble["event2"]["date"],
                                             )
            except Found_duplicates.DoesNotExist:
                duble_event=Found_duplicates()
                duble_event.event1_id=duble["event1"]["id"]
                duble_event.event2_id=duble["event2"]["id"]
                duble_event.event1_date=datetime.utcfromtimestamp(duble["event1"]["date"])
                duble_event.event2_date=datetime.utcfromtimestamp(duble["event2"]["date"])
                duble_event.event1_team1=duble["event1"]["teams"]["1"]["ru"]
                duble_event.event1_team2 =duble["event1"]["teams"]["2"]["ru"]
                duble_event.event2_team1 =duble["event2"]["teams"]["1"]["ru"]
                duble_event.event2_team2 = duble["event2"]["teams"]["2"]["ru"]
                duble_event.event1_sport = duble["event1"]["sport"]["ru"]
                duble_event.event2_sport =duble["event2"]["sport"]["ru"]
                duble_event.event1_provider =duble["event1"]["state"]["provider_id"]
                duble_event.event2_provider =duble["event2"]["state"]["provider_id"]
                duble_event.save()
        list_added_dubles = Found_duplicates.objects.all()
        for duble in find_dubles:
            list_added_dubles=list_added_dubles.exclude(event1_id=duble["event1"]["id"],
                                             event2_id=duble["event2"]["id"],
                                                            )
        for added_dubles in list_added_dubles:
            added_dubles.delete()
    else:
        list_added_dubles=Found_duplicates.objects.all()
        for added_dubles in list_added_dubles:
            added_dubles.delete()
if __name__ == "__main__":

    #event_json=connect()["delta"]["bm"]
    #event_list=pars(event_json)
    #find_dubles=search_duble(event_list)
    find_dubles=[{'event2': {u'category': {u'ordering': 0, u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435', u'id': 2000000081}, u'tournament': {u'ordering': 0, u'country': {u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0439', u'alpha_2': u'WORLD', u'id': None, u'alpha_3': u'WORLD'}, u'id': 2000001383, u'ru': u'\u0422\u043e\u0432\u0430\u0440\u0438\u0449\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0447\u0438 \u0414\u043e 21 \u0433\u043e\u0434\u0430', u'rating': 1}, u'teams': {u'1': {u'ru': u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430 (\u0434\u043e21)', u'id': 2000041263}, u'2': {u'ru': u'\u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0438\u044f (\u0434\u043e21)', u'id': 2000048738}}, 'state': {u'active': True, u'provider_id': 1, u'short_id': 6001}, u'anons': False, u'filters': u'', u'date': 1496934000, u'sport': {u'ordering': 15, u'ru': u'\u0424\u0443\u0442\u0431\u043e\u043b', u'id': 1}, u'id': 2000958819}, 'event1': {u'category': {u'ordering': 0, u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0435', u'id': 2000000081}, u'tournament': {u'ordering': 0, u'country': {u'ru': u'\u041c\u0435\u0436\u0434\u0443\u043d\u0430\u0440\u043e\u0434\u043d\u044b\u0439', u'alpha_2': u'WORLD', u'id': None, u'alpha_3': u'WORLD'}, u'id': 2000001383, u'ru': u'\u0422\u043e\u0432\u0430\u0440\u0438\u0449\u0435\u0441\u043a\u0438\u0435 \u043c\u0430\u0442\u0447\u0438 \u0414\u043e 21 \u0433\u043e\u0434\u0430', u'rating': 1}, u'teams': {u'1': {u'ru': u'\u0423\u043a\u0440\u0430\u0438\u043d\u0430 (\u0434\u043e21)', u'id': 2000041263}, u'2': {u'ru': u'\u0424\u0438\u043d\u043b\u044f\u043d\u0434\u0438\u044f (\u0434\u043e21)', u'id': 2000219561}}, 'state': {u'active': True, u'provider_id': 2, u'anons': True, u'short_id': 4962}, u'anons': True, u'filters': u'', u'date': 1496934000, u'sport': {u'ordering': 15, u'ru': u'\u0424\u0443\u0442\u0431\u043e\u043b', u'id': 1}, u'id': 2000958582}}]
    base_writer(find_dubles)