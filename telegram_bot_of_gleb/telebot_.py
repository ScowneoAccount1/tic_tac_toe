import telebot
from utils import *
from extensions import keys, TOKEN

# EXECUTION ==== ==== ==== ==== ==== ==== ==== ====
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help', 'start'])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, '''Добро пожаловать. Этот бот нужен для переводов валют. Формат комманд.
/curs <сколько> <из какой валюты переводить> <в какую валюту переводить>
например: /curs 1500 рубль евро
(также работают kurs, и курс)

вы можете посмотреть список названия валют в /values''')


@bot.message_handler(commands=['curs', 'kurs', 'курс'])
def convert_(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        
        if len(values) != 4:
            raise ConvertionException('неправильное кол-во параметров')
            
        _, amount, base, quote = values
        data = CursConverter.convert(quote, base, amount)
    
    except ConvertionException as err:
        bot.reply_to(message, f'Ошибка пользывателя\n{err}')
    
    except Exception as err:
        bot.reply_to(message, f'Ну удалось обработать комманду\n{err}')
    
    else:
        ans = f'~{float(amount) * data} {quote}\n(1 {base} ≈ {data} {quote})'
        bot.send_message(message.chat.id, ans)


@bot.message_handler(commands=['values'])
def repeat(message: telebot.types.Message):
    text = ''
    
    for i, v in enumerate(keys):
        text += '\n' + v
        
    bot.send_message(message.chat.id, text)

bot.polling(non_stop=True)


