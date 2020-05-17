import telebot


def run_bot(idx):
    bot = telebot.TeleBot('AAGpkI_n3Ngm_9O625rsyTepaHXcp6-Jzuo')
    bot.send_message(0, f'{idx}ALARM')
    bot.polling()

