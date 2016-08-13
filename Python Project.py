from twilio.rest import TwilioRestClient 
from random import choice

#-------------Jordane's Code Block Start----------------------------------------------------------------------------------------------------------------

####### The Statments For Use ########################################################################################################################## 
level1 = [
	"It's a beautiful day, and you live in a great neighborhood. You should totally go take a walk",
	"Some times we all just need to take a walk around town and enjoy the people and places we live in.",
	"go for a walk"
		]

level2 = [
	"You should check out http://www.xgenstudios.com/games/, stickRPG is the ish",
    "Armor games has a lot of really great games you should check http://armorgames.com/"
    	]

level3 = [
	"Hey there a pokemon at {}.", "Hey go Check out this pokeStop at {}. Use your Balls wisely.",
    "MoewTwo has be spoted you can find him here: {}"
    	]

distractions = [level1, level2, level3]
#########################################################################################################################################################

###### Example crimes ###################################################################################################################################
# Hispanic man forcfully touchs woman
crime_One = [[True,False],"Riverside Park, Manhattan"]
#  Woman dies in Queens
crime_two = [[True,True],"Queens"]
# man climbs trump tower
crime_three = [[False,False],"Trump Tower"]

crimes = [crime_One,crime_two,crime_three]
#########################################################################################################################################################

###### Response handler #################################################################################################################################
def gettingCrimeData(CrimeInformation):
	global distractions
	violence = CrimeInformation[0][0]
	fatality = CrimeInformation[0][1]
	if violence != fatality:
		return choice(distractions[1])
	elif violence == fatality:
		if violence == True:
			return choice(distractions[2]).format(CrimeInformation[1])
		if violence == False:
			return choice(distractions[0])
#########################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def sendText(list_of_crimes):
	body = []
	for crime in list_of_crimes:
		body.append(gettingCrimeData(crime))
	
	ACCOUNT_SID = "AC20cc5b1f042adc1f0f5b0618fb0ab609" 
	AUTH_TOKEN = "27982e849cf56c7f370ee764e93f248f" 

	client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
	for item in body:
		client.messages.create(
			to = "+19176519839", 
    		from_="+15017250604",
    		body= item,
    		media_url="http://farm2.static.flickr.com/1075/1404618563_3ed9a44a3a.jpg"

			)
sendText(crime)
