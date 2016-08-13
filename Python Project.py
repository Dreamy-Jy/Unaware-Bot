from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC20cc5b1f042adc1f0f5b0618fb0ab609" 
AUTH_TOKEN = "27982e849cf56c7f370ee764e93f248f" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create(
    to="+19176519839", 
    from_="+15017250604", 
    body="Hey Jenny! Good luck on the bar exam!", 
    media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg", 
)
