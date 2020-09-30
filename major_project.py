'''
import telebot
​
#Shivani_first_bot
my_bot = telebot.TeleBot("1284511559:AAHYbzcDpqiP7PYzxeJHhZJIgFiVasspOi8")
​
@my_bot.message_handler(commands=['start'])
def send_welcome(message):
        my_bot.reply_to(message, "This is mine first bot, you are welcome!!!")
        print(dir(message))
​
my_bot.polling()
'''
​
import telebot
​
#Shivani_first_bot
my_bot = telebot.TeleBot("1284511559:AAHYbzcDpqiP7PYzxeJHhZJIgFiVasspOi8")
​
@my_bot.message_handler(commands=['start', "say_again"])
def send_welcome(message):
        my_bot.reply_to(message, "This is mine first bot. " + str(message.from_user.first_name) + "is welcome...")
        print("Message from : " + message.from_user.first_name)
​
@my_bot.message_handler(func=lambda m:True)
def send_echo_as_reply(msg):
​
        print(msg.from_user.first_name + "said : " + msg.text)
        my_bot.reply_to(msg, msg.text)
​
my_bot.polling()


'''
import requests as req
import json
print(1)
city = "jaipur"
response = req.get("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=f1b8ef0889ec10bd4e2003dad5b093e1" % city)

response_text = response.text
response_dict = json.loads(response_text)

temprature = int(response_dict["main"]["temp"]) - 273
humidity = int(response_dict["main"]["humidity"])

print("Temprature is : ", temprature)
print("Humidity is : ", humidity)
'''


'''
import requests as req
import json

response = req.get("https://api.covid19india.org/v3/data-all.json")

if response.status_code == 200:

	dict_data = json.loads(response.text)
	dict_data_today = dict_data['2020-06-11']


	for state, values in dict_data_today.items():

		print(state, " : ", end="")

		try:
			total_confirmed = int( values["total"]["confirmed"] )
			total_tested    = int( values["total"]["tested"] )
			total_death     = int( values["total"]["deceased"])

			ratio_confirmed_vs_tested = (total_confirmed / total_tested ) * 100
			ratio_death_vs_confirmed = (total_death / total_confirmed ) * 100

			print("test_ratio : ", ratio_confirmed_vs_tested, "death_ratio : ", ratio_death_vs_confirmed)
		
		except:
			print("no data available")

else:

	print("some error")
'''
