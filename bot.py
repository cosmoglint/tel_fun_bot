import sys
import time
import telepot
import re
import os
import random
import requests
import json

ram = 558581271
mini = -367351399
soor = -339475858
ayyan = 962370773
kiddo = 575182560
uthanda = 947821180
ram1 = 765106731
chatd = [ram,mini,uthanda,ram1,kiddo,ayyan,soor]
botd = '903555004:AAEMh0BWCVbIjh2pv-yPWDC7sjo3vFZdpRI'
#input chat id here because i dont want you stealin it

def handle(msg):
    chat_id = msg['chat']['id']
    #print(chat_id)
    #bot.sendMessage(chat_id,"hi dude! type \"random image\" for fun or type \"limit\" for motivation. play around with other commands")

    command = msg['text']
    cmd = command
    if command == "/start":
        bot.sendMessage(chat_id,"Hey!, I am the bot to go to for fun and instant gratification. Type /help for list of available commands")
        #! type \"random image\" for fun and \"fun\" for actual fun or type \"limit\" for motivation. play around with other commands, good for applause and some instant gratification

    if '@Therambot' in command:
        command = re.sub('@Therambot', '', command)
        command = command.strip()
        #bot.sendMessage(chat_id,"hi")


    if chat_id :
        #command = msg['text'] in chatd
        print('Got command: %s' % command)

        if command == 'hi' or command == 'Hi' or command == 'hey' or command == 'Hey' or command == 'hlo' or command == 'Hlo' or command == '/hi':
            bot.sendMessage(chat_id,"hi dude")
        elif command == '/help':
            bot.sendMessage(chat_id, "This is an interactive bot.\n Type /quote for a life changing quote\n /joke for some fun \n /limit to test \n /lucky for numbers(if you think  numbers are cool) \n /iss to launch a nuke to iss \n /num <a_number> for randum facts \n /lol to rofl \n /image for a random image \n /good to appreciate \n /leave to get data \n /bye")

        elif command == 'unakku leave ah' or command == 'leave' or command == 'are you free' or command == 'free' or command == '/free' or command == '/leave':
            bot.sendMessage(chat_id,"enakku all day leavu only")

        elif command == 'Quote' or command == "quote" or command == 'quotes' or command == 'Quotes' or command == '/quote':
            url = 'https://random-math-quote-api.herokuapp.com/'
            response = requests.get(url)

            bot.sendMessage(chat_id, response.json()["author"] + " says " + response.json()["quote"])

        elif command == '/bye':
            bot.sendMessage(chat_id, "Strange world out there, have fun. C ya")

        elif command == 'Joke' or command == 'joke' or command == 'tell me a joke' or command == 'random joke' or command == '/joke':

            joke = 'http://api.icndb.com/jokes/random'
            response = requests.get(joke)
            bot.sendMessage(chat_id, response.json()['value']['joke'])

        elif command == '/boyorgirl':
            a = ['Boys rule bruh', 'Girls rock']
            c = random.choice(a)
            bot.sendMessage(chat_id,c)

        elif command == '/lucky':
            nu = random.randint(0, 1000)
            bot.sendMessage(chat_id, "you rolled " + str(nu))
            url =  "http://numbersapi.com/" + str(nu) +  "/trivia"
            response = requests.get(url)
            bot.sendMessage(chat_id, response.content)

        elif command == '/iss':
            iss = 'http://api.open-notify.org/iss-now'
            response = requests.get(iss)
            msg = "the ISS is at " + response.json()['iss_position']['latitude'] + " latitude and " + response.json()['iss_position']['longitude'] + " longitude"
            bot.sendMessage(chat_id, msg)

        elif command == '/god' or command == 'who is god':
            bot.sendMessage(chat_id, "nithyanandha is god of all")

            #bot.sendMessage(chat_id,"A ghost cannot harm you, it can only be seen by you. at the most, it can ask you for help")
            url=r"C:\Users\vinu\Pictures\Nithyananda_16ecff2e858_original-ratio.jpg"
            files = {
                      'chat_id': (None, chat_id),
                      'photo': (url, open(url, 'rb')),
                  }

            response = requests.post('https://api.telegram.org/bot903555004:AAEMh0BWCVbIjh2pv-yPWDC7sjo3vFZdpRI/sendphoto', files=files)
            bot.sendMessage(chat_id, 'so the ME resides in this as ME, is residing in all of that as ME, so that ME through this ME, TALKING to ME')

        elif '/happybirthday' in command:
            namee = re.sub("/happybirthday", "", command)
            bot.sendMessage(chat_id, "Happy birthday to you " )
            bot.sendMessage(chat_id, "Happy birthday to you " )
            bot.sendSticker(chat_id, 'CAACAgIAAxkBAAEBNbBfOTkug3wiBN_bhu8X1xdajDieWwACGwADwDZPE329ioPLRE1qGgQ')
            bot.sendMessage(chat_id,", Happy birthday dear "+ namee + "happy birthday to youuu")
        elif "/num" in command:
            cm = re.sub("/num " , '', command)
            if cm.isalnum():
                url =  "http://numbersapi.com/" + cm +  "/trivia"
                response = requests.get(url)
                bot.sendMessage(chat_id, response.content)
            else:
                bot.sendM
                essage(chat_id, "please enter a valid number")

        elif command == 'lol' or command == 'LOL' or command == 'laugh' or command == 'Laugh' or command == 'fun' or command == 'Lol' or command == 'Laugh' or command == 'Fun' or command == 'haha' or command == 'hahaha' or command == '/fun' or command == '/lol':
            funny = ['omg','OMG','OH MY GOD', 'HAHAAAA', 'HAAAAHAAA', 'funny', 'fun', 'AMAZING', 'whaaaaaa', 'what a comedy', 'i like it']
            d = random.choice(funny)
            bot.sendMessage(chat_id, d)
            ls = ['CAACAgIAAxkBAAIkhl5AOxru1mCR8yb1jhIvMkEpDaI4AAKwAgACxKtoCwSf0XHzvMWIGAQ','CAACAgIAAxkBAAIkiF5AOyD4qYKlOJxWmWKWTOgX53T4AAI8AwACzFRJCTegElDEcMYQGAQ','CAACAgIAAxkBAAIkil5AOyT7tWjukLMtAhEhnOQq6uU-AAKiAAMQIQIQxrVTm75UvzgYBA','CAACAgIAAxkBAAIkjF5AOyhnAZ5WhXKu6WRiTu3gXtpWAALDCAACbjLYAAGR-qRB36oyyBgE','CAACAgIAAxkBAAIkjl5AOypFPpY7ChSja1JWk8V1ec1lAAJsAgACP5XMCu9l9HdcT1gzGAQ','CAACAgIAAxkBAAIkj15AOyz7Elzrizm0qpwFkJn_v25vAAItAQACNnYgDr98iJTa8UGLGAQ','CAACAgIAAxkBAAIkkV5AOy0XrKNk6iWWwW-GXl8lTAvKAAIYDQACqAgvCHMCg7wqLID9GAQ','CAACAgIAAxkBAAIklF5AOy9HzTqCj717FbqrpvhSjp0AAz0FAALO2OgLLb6L8EKsBTwYBA','CAACAgIAAxkBAAIklV5AOzCv1lHc58czlznvJlPZ-u_BAAJSAAMnFEkLSho84LdXrUYYBA','CAACAgIAAxkBAAIkl15AOzLJmBzX9a_8J--aBhsR6WTPAAIQCAACCLcZAv1hDJP-QGlDGAQ','CAACAgIAAxkBAAIkmV5AOzT_SW2x0GxgwVDMC-ON_v3AAAJyCAACeVziCQxup4NcDPzxGAQ','CAACAgIAAxkBAAIkm15AOzV6ZpiMLf5HJsxUggvV-maKAAKrAwACxKtoCzYlBUbq0Lu3GAQ','CAACAgIAAxkBAAIknV5AOzZEK6s2KgT0DM3B6ys3g-pzAAJNAQACihKqDqYrjuhTZfB7GAQ','CAACAgIAAxkBAAIkn15AOzhG5WWmvii5mKPTpxDuWINxAAKlBwACYyviCalHOTk5PcUcGAQ','CAACAgIAAxkBAAIkol5AO0TfvKrslXWxvhkdt1DTeB9gAALnAgACz1-LB0hSLoWZ0Ll3GAQ','CAACAgIAAxkBAAIko15AO0a1FTm3J_xyB2O10R8kO04SAAJ-CAACeVziCWn3Vn6MWgfLGAQ','CAACAgIAAxkBAAIkpV5AO0ch8u_leGnQp06x0zLXWwLaAAIdBQACRvusBORUZvwZtqBPGAQ','CAACAgIAAxkBAAIkp15AO0kN0hGRcG9InMrTlGlmGz9jAAKqCAACCLcZAhA7hg6QqIIJGAQ','CAACAgIAAxkBAAIkqV5AO0tI4uhMsYMgoXyS7UD4mZHIAAIEAAOhjEELy73UzzfsYz8YBA','CAACAgIAAxkBAAIkq15AO0xqPT-KikGtCTl305YG30YYAAJ4AAMfAUwV-QhNK9uACHUYBA','CAACAgIAAxkBAAIkrV5AO04lgZKMqVvCNhHXNg4fQI97AAKOBQACztjoC2dmbSmMv8ekGAQ','CAACAgIAAxkBAAIkr15AO09WejAwDEV7hp2--3NKzNjAAAKfBQACztjoC9aaeEx9l4qBGAQ','CAACAgIAAxkBAAIksl5AO1EDZxraghVL9B5Fx50W_1_YAAJuBgACRvusBJmLas5zNJdnGAQ','CAACAgIAAxkBAAIks15AO1J8D-9A3JDwosCR3x_d1pHxAALtAwACRvusBKmEs35zzy1TGAQ','CAACAgIAAxkBAAIktV5AO1NUOE2WW70bXHuvv8tn1gMgAAJyBwACCLcZAnteK5cgBgUfGAQ','CAACAgEAAxkBAAIkt15AO1Ui4N_RRLni9emJ0f5INPwcAAJVCAACv4yQBNFAPbhRk_BtGAQ','CAACAgIAAxkBAAIkuV5AO1YU8DJqJtviWGYLjsS5HfXuAAKbBgAC0lqIAeop_r-qmmS2GAQ','CAACAgIAAxkBAAIku15AO1cf2GXhCRHMTkwU6em2hAABGgACGQQAAsSraAtobQ1OQPASkRgE','CAACAgIAAxkBAAIkvV5AO1isIrTQFM6kmr6_sPYC5ex6AAKgBgACRvusBCYeaMrGJ7TQGAQ','CAACAgIAAxkBAAIkwF5AO1zsJcMEJRrPjJKCKOiKXYEyAAIyAANVLHgLj1dXp-fz39UYBA','CAACAgIAAxkBAAIkwV5AO10VPKywZHdfs_arJBRaaHKfAAIBAgACIIEVAAG8K0AjA7atGhgE','CAACAgIAAxkBAAIkw15AO14uzou8BQABEv7iX8qWj4yXdQACNAMAAs-71A4F54AEKJAeWBgE','CAACAgIAAxkBAAIkxV5AO2BtlmswZy8oslHw6xYAAYdgRQACAQADwDZPExguczCrPy1RGAQ','CAACAgIAAxkBAAIkx15AO2HVFMkguLP8rI-nOvEwXS2QAAL4AwACzFRJCUUDpdt-9K5FGAQ','CAACAgIAAxkBAAIkyV5AO2LGYgW7k0dUf4y6lRoXF1boAALbAAMnFEkLprMkgsv-mg4YBA','CAACAgIAAxkBAAIky15AO2RoPpgAAbrRy8rLWAl1pqv9VAACkAMAApzW5wqo4xBcsPhBxRgE','CAACAgIAAxkBAAIkzl5AO2Zvxyhdcl7zhJkyb2WpP_FYAAKfAgAC3PKrB_RS-uAmCt9tGAQ','CAACAgIAAxkBAAIk0F5AO2h68FMyvS9x7iNXMmNBcL1lAALFAwACztjoCxo5Tzbdh5d1GAQ','CAACAgIAAxkBAAIk0V5AO2ros9v4q0_wf4fTya6iAg8dAALWAANWnb0KCXXJDOIvIQoYBA','CAACAgIAAxkBAAIk1F5AO28HTtTd9A2q1pA5dbpXvOsvAAIYAAP3AsgP5xNcQ1GQgDQYBA','CAACAgIAAxkBAAIk1V5AO3AAAXqAsol2EhOrA4EvPMYkkgACGQADFkJrCiW-o11UT9X6GAQ','CAACAgIAAxkBAAIk115AO3GLr4pz14GBN1535_EBti4wAAIEBgACztjoC58JKMTEWA-JGAQ','CAACAgIAAxkBAAIk2V5AO3IjPwABXbQgIcxul2fSbNMVHwACIwEAAphsyAqdGmdA4qCy5xgE','CAACAgIAAxkBAAIk215AO3QQGdXtwIaoDVdHDy2-2ueRAALdAAMfAUwVhFo8E__yyy4YBA','CAACAgIAAxkBAAIk3l5AO3ZEjIEAAe4dFL91-vMrUETG0wACpwADMNSdEd5jQjYYM_sQGAQ','CAACAgIAAxkBAAIk4F5AO3nFIbe8kUgU0Henz5VtvE2IAAIyBgAC0lqIAfNrlmbIUeEZGAQ','CAACAgIAAxkBAAIk4V5AO3qAhA1kdCis4AGA9NiDVDSCAAL2BgACRvusBBgjD1OORk_rGAQ','CAACAgIAAxkBAAIk5V5AO31nxEzgmqrdcbV47HrvYt5hAAIQAAMNttIZ0fWfOOcTY8UYBA','CAACAgEAAxkBAAIk6F5AO4DIBT0rRUxt_QmILi5Dvp67AALdCQACv4yQBNIi5Cn8DNEPGAQ','CAACAgIAAxkBAAIk6V5AO4H2qppT8Oxj5tDENMHF3XKEAAIoAQACVp29CvWtctHoQoegGAQ','CAACAgIAAxkBAAIk615AO4MWfNUzwpOphtDkQ3joSkPMAAKqAgACNnYgDlhzg812_BCTGAQ','CAACAgIAAxkBAAIk7V5AO4QN4ff98TEjjugUGUwT-F6yAALGAAMw1J0R6FaFQZPw53IYBA','CAACAgIAAxkBAAIk8F5AO4YL9wx2bF13PakVFPXb10coAAKjAAP3AsgP3vsoD3HpiaUYBA','CAACAgIAAxkBAAIk8l5AO4ltD7j-B_GAsElcSF46jY0PAAJxAQACzFRJCWHFyuEbWTscGAQ','CAACAgIAAxkBAAIk9F5AO4v44dvKUZKMEX-vz_0hEriOAAIwAAPPu9QOf5nr9xN9eWoYBA','CAACAgIAAxkBAAIk9V5AO4253wywxZ1LhWUgGqipFuURAAIhAAPBnGAMqTQSSpKIefwYBA']
            x = random.choice(ls)
            bot.sendSticker(chat_id, x)

        elif command == 'do you have limits' or command == 'limits' or command == 'Limits' or command == 'limit' or command == 'Limit' or command == '/limit':
            bot.sendMessage(chat_id,"sky is the limit")
            lst = ['CAACAgIAAxkBAAIkgl5AGIl0YRbS1laQqDy3NhWIpUKQAALfAAM2diAO7Y5WtrX4gfoYBA','CAACAgIAAxkBAAIkgF5AGIc3fm819HUVg5vrtF_adDcKAALzAAM2diAOPcupn1zTAzAYBA','CAACAgIAAxkBAAIkfV5AGIDKRCDHs_tMy1w_Yq8LND1cAAI7BQACztjoC7NEWclhCLopGAQ','CAACAgIAAxkBAAIke15AGH7-pRtUY0xOdbJOX0r2Xji4AAI0BQACztjoC92Sd1j7LIyrGAQ','CAACAgIAAxkBAAIkel5AGHwqoj4WnOO6fzmHGqoaqt26AAIMDQACqAgvCDr1tW5-TfIRGAQ','CAACAgIAAxkBAAIkYF5AFk07bAcy3gROG5S4B8a9NEutAAJLAQACihKqDgABOI6wzx8G0hgE','CAACAgIAAxkBAAIkYl5AFlBbOHKr3Yv3hqZ0wAABUQ0a1gACwAMAAsSraAuVMpYVqIpeHhgE','CAACAgIAAxkBAAIkZF5AFlXs2kJfX57ZAk7zjueW-bjIAAJwCAACeVziCWnUeUcX8MduGAQ','CAACAgIAAxkBAAIkaF5AFt03juT_p98UY47j_-pid-XsAAIqAAPBnGAMI8aLpMDqqgwYBA','CAACAgIAAxkBAAIkal5AFuN_rdPlmTe9i-fTwlk9RzazAAKbAQACzFRJCVrVfZ8u9XqUGAQ','CAACAgIAAxkBAAIkbF5AFurznrJDV7lZt1j0xCm8wIyDAAKYAAP3AsgPbpoKbEX2mzsYBA','CAACAgIAAxkBAAIkbl5AFvDgZduepOnlBSCribBIDH2WAAK6AAMw1J0RhNfEiMRQZ1YYBA','CAACAgIAAxkBAAIkcF5AFvyn4tGVCHrZx_KEkKl6EG1aAAK5AgACNnYgDu106wVn0luFGAQ','CAACAgIAAxkBAAIkcl5AFv9lvWEtItJeUulsAAHUjg2IkwACQAEAAladvQps6VtALEnWJRgE','CAACAgIAAxkBAAIkdF5AFwZDiIeyo2i34CZ78Lg-ikBoAAIlAAMNttIZhH34MWbLGT8YBA','CAACAgIAAxkBAAIkdV5AFwYPOQu-yx2s4p3POe-xxFZYAAI0AAMNttIZfKboYDN5zqIYBA','CAACAgIAAxkBAAIkdl5AFwehhcl_M7ihODLrMtvxK-7uAAIVAAMNttIZXGSsuYDVQEYYBA','CAACAgIAAxkBAAIkXl5AFeaYxXVb8Hg_yLfPkNzAoUJ_AAK9UwACns4LAAFZYnRjkWRr2RgE']
            f = random.choice(lst)
            bot.sendSticker(chat_id, f)
            #on(11)
        elif command == 'what are you doing' or command == 'inna panra' or command == 'Wat r u doing':
            bot.sendMessage(chat_id,"unna mariye vetti than")
            bot.sendSticker(chat_id, 'CAACAgIAAxkBAAIkU14_8Fu9zTnngsfO9R6qqthD4bnFAALKAAMw1J0RFiKclLUaiGYYBA')
            bot.sendMessage(chat_id,"chatting")
            #GPIO.output(18,GPIO.LOW)
            #off(11)
        elif command == 'fuck' or command == 'Fuck' :
            bot.sendMessage(chat_id,"su moodu")
            bot.sendSticker(chat_id, 'CAACAgIAAxkBAAIls15CSzB0aOVFxgxaBT6S8Hkt08TfAAJKBwACRvusBCNCmw1f3sTgGAQ')

        elif command == 'appreciate' or command == 'Appreciate' or command == 'good'or command == 'Good' or command == '/good':
            bot.sendMessage(chat_id,"good job!")
            bot.sendSticker(chat_id, 'CAACAgIAAxkBAAIkV14_9CYqLKrIgV0fFHEvOzGZWeAmAAIxBAACzFRJCcMhGChhVx22GAQ')

        elif command == 'random image' or command == 'Random image' or command == 'random pic' or command == 'image' or command == 'Image' or command == '/image':
            bot.sendMessage(chat_id,"sending")
            #a = random.choice(os.listdir(r"C:\Users\vinu\Pictures\bot"))
            ch = str(chat_id)
            #url=r"C:\Users\vinu\Pictures\bot"+"\\"+a
            url = "https://picsum.photos/200/300"
            pic = requests.get(url)
            files = {
                      'chat_id': (None, ch),
                      'photo': (pic.content),
                  }

            response = requests.post('https://api.telegram.org/bot903555004:AAEMh0BWCVbIjh2pv-yPWDC7sjo3vFZdpRI/sendphoto', files=files)
            #'https://picsum.photos/536/354', open('https://picsum.photos/536/354', 'rb')
            #a = random.choice(os.listdir(r"C:\Users\vinu\Pictures\renders"))
            bot.sendMessage(chat_id,"Bye!")
            #bot.sendPhoto(msg['chat']['id'], (os.path.basename(r'C:\Users\vinu\Desktop\Bot\Screen_Shot_2019-06-07_at_3.40.52_PM.png'), open(r'C:\Users\vinu\Desktop\Bot\Screen_Shot_2019-06-07_at_3.40.52_PM.png')))
            #bot.sendPhoto(chatd, open('https://picsum.photos/536/354'))

        elif command == 'random audio' or command == 'random music' or command == 'music':
            bot.sendMessage(chat_id,"sending")
            a = random.choice(os.listdir(r"C:\Users\vinu\Music\collecteds"))
            url=r"C:\Users\vinu\Music\collecteds"+"\\"+a
            bot.sendAudio(chat_id, url)

        elif '@Therambot' in cmd or ('/' in cmd and cmd != '/start'):
            bot.sendMessage(chat_id,"sorry I don't understand")
            bot.sendSticker(chat_id, 'CAACAgIAAxkBAAIkVV4_81dWZRUwGoWvMk0x8S5-8y8QAAISAAPANk8TM7yeAS6VBzcYBA')
    else:
        print("unauthorized!")

bot = telepot.Bot(botd)
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')
