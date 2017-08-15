
import tweepy
import telebot
import re
from telebot import types

CONSUMER_KEY ="TaOBuLQzlqzbPvwRhFABrNmcK"
CONSUMER_SECRET = "fmTeJQce4K4J84SRjDnZHhadu7rpzj8qIraLbmGWWtdMn4UP8H"   
ACCESS_KEY = "956931200-0NigVK2HyUZUUmEVRHte3j7nYL1oQqzQmVg3E3vr"    
ACCESS_SECRET = "Jjb2QhYNp6SpBe7k3k0HTSl5DQCgoVstETn9eja634pZS"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
f = open('text.txt')
a = f.read()
f.close()
blacklist = re.findall("[^= ]+" , a)
print blacklist
api = tweepy.API(auth)
token = "434040230:AAH1N0wEjOtQxbcQIQzP6mgC_gLaKujDnH4"
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if not message.text.lower().strip().encode('utf8') in blacklist and message.text != "/start":
        api.update_status(message.text)
        bot.send_message(message.chat.id,"Готово")
        print "send"
    elif message.text.lower().strip().encode('utf8') in blacklist:
        bot.send_message(message.chat.id,"Плохое слово")
    if message.text == "/start":
        bot.send_message(message.chat.id,"Все сообщение будут будут твититься на аккаунт твиттер g_danil_d")
        bot.send_message(message.chat.id,"https://twitter.com/g_danil_d")
        
if __name__ == '__main__':
    bot.polling(none_stop=True)
