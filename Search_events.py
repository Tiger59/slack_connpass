import requests
import json
import slackweb
def events_handler(event, context):
    slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
    url = 'https://connpass.com/api/v1/event/?keyword=神戸'
    events="*近々開催されるイベントです*\n"
    obj = json.loads(requests.get(url).text)
    for i in obj["events"]:
        time=i['started_at'].split("T")
        time[1]=time[1].split(":")
        events=events+"*"+i["title"]+"*"+"\n>"+time[0]+" "+time[1][0]+":"+time[1][1]+"~\n> "+i["event_url"]+"\n"
    slack.notify(text=events)
    return
