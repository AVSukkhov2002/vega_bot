import telebot
import json
import requests

# Замените токен на ваш токен бота
TOKEN = "7711006069:AAHEkBhsVmTuHNFn4hldupjtrVb0eJt5nE0"
bot = telebot.TeleBot(TOKEN)

url = "http://vega.mirea.ru/aiapi/api/generate"
headers = {
    'Content-Type': 'application/json'
}

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Waiting...")
    
    payload = json.dumps({
        "model": "gemma2:27b",
        "prompt": message.text  
    })
    
    response = requests.post(url, headers=headers, data=payload)
    
    if response.status_code == 200:
        
        responseText = response.text
        json_objects = responseText.splitlines()

        responseStr = ""
        for res in json_objects:
            data = json.loads(res)
            response_value = data["response"]
            responseStr += response_value
    
        bot.reply_to(message, responseStr)
    else:
        bot.reply_to(message, f"Ошибка API: {response.status_code}")


bot.polling()
