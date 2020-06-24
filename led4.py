
# -*- coding: utf-8 -*-
import telebot
import datetime
from time import sleep
#bot = telebot.TeleBot('1023899509:AAEX4KXDYer8DW8ZGxOxFQ4fStWwgTJrAeA')


bot = telebot.TeleBot('1023899509:AAHSDEZaop4490O84oFiOuvMHdprM8uVs-g')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'РўС‹ РЅР°РїРёСЃР°Р» _  /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    slovar_privet={
        u'РїСЂРёРІРµС‚':'РґР°СЂРѕС„',
        u'С…Р°Р№':'Р№РѕСѓ',
        u'РґРµРЅСЊ РґРѕР±СЂС‹Р№':'Р—РґСЂР°РІСЃС‚РІСѓР№С‚Рµ',
        u'Р·РґСЂР°РІСЃС‚РІСѓР№С‚Рµ':'РџСЂРёРІРµС‚СЃС‚РІСѓСЋ',
        u'С…РµР»РѕСѓ': 'Р‘РѕСЂРµРІ Р±СЂР°С‚',
        u'СЂР°С…РјРµС‚': 'РҐР°Р№',
        u'С…РѕР№': 'Р”РѕР±СЂРѕРіРѕ',
        u'abc': 'yyyaaa',
        u'С…Р°Р№ РїРёРїР»': 'РЎР°Р»Р°Рј Р”РѕСЂРѕРіРѕР№'
    }
    slovar_poka={
        u'РїРѕРєР°':'СЃС‡Р°СЃС‚Р»РёРІРѕ',
        u'РїРѕРєРµРґ':'Р‘СѓРґСЊ!',
        u'РґРѕСЃРІРёРґР°РЅРёСЏ':'РђРґРёРѕСЃ!',
        u'Р±Р°Р№':'Р‘Р°Р№ Р±Р°Р№',
        u'РїСЂРѕС‰Р°Р№':'Р”РѕСЃРІРёРґР°РЅРёСЊСЏ',
        u'СЃС‡Р°СЃС‚Р»РёРІРѕ':'РџРѕРєР°',
        u'Р°РґРёРѕСЃ':'РїРѕРєР° РїРѕРєР°'
    }
    slovar_stopprogram={
        u'СЃС‚РѕРї':'Р’С‹РєР»СЋС‡Р°СЋСЃСЊ',
        u'stop':'РѕС‚РєР»СЋС‡РµРЅРёРµ',
        u'РІС‹РєР»СЋС‡РёСЃСЊ':'РѕСЃС‚Р°РЅРѕРІРєР°_РїРёС‚Р°РЅРёСЏ',
        u'power_off':'РѕС‚РєР»СЋС‡РµРЅ'        
    }
    key =message.text.lower()
    if key in slovar_privet:
        bot.send_message(message.chat.id,slovar_privet[key] )
    else:
        if key in slovar_poka:
            bot.send_message(message.chat.id,slovar_poka[key])    
        else:
            if key in slovar_stopprogram:
                bot.send_message(message.chat.id,slovar_stopprogramm[key])
                sleep(5)
                exit(0)
            else:    
                bot.send_message(message.chat.id, 'РЎРёРµ РІС‹СЂР°Р¶РµРЅРёРµ РјРЅРµ РЅРµ РІРµРґРѕРјРѕ СЃРёСЂ!')
                bot.send_message(message.chat.id, '... РЅРѕ СЏ Р±С‹СЃС‚СЂРѕ СѓС‡СѓСЃСЊ...')
    


bot.polling()
