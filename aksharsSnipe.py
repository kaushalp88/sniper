import urllib2
import simplejson
import requests

import urllib2
import json
from twilio.rest import TwilioRestClient
from time import sleep

def sendMessage(count):
    acount_sid = "AC27ee1c3ad33b5a65196df1be692516ac"
    auth_token = "e597e20b27bdc19f0348ddfa46351caf"
    client = TwilioRestClient(acount_sid, auth_token)

    req = urllib2.Request("https://sis.rutgers.edu/soc/courses.json?subject=920&semester=12013&campus=NB&level=U")
    opener = urllib2.build_opener()
    f = opener.open(req)
    dict = json.loads(f.read())
    print dict[0]['sections'][1]['openStatus']
    print dict[0]['sections'][1]['index']
    if dict[0]['sections'][1]['openStatus']:
        client.sms.messages.create(body="Course just opened up!", to="+17324856402", from_="+17324973029")
        return count + 1
    elif count > 36000000:
        client.sms.messages.create(body="Course is still closed...", to="+17324856402", from_="+17324973029")
        return 0
    return count + 1
count = 40000000000000
while True:
    count = sendMessage(count)
    print count
    sleep(10)    

