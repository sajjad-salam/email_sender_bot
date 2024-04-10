import telebot
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from threading import Thread



Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
C = '\x1b[2;35m'
BB = '\x1b[2;36m'
Y = '\x1b[1;34m'
all = '_._._._._.'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
Bl = '\x1b[1;34m'
P = '\x1b[1;35m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
E = '\x1b[0;90m'
print(('\033[92m—'*25)+'\n• DEV BY @S_J_O_D •\n'+('—'*25))
print(f'''{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-

    𓆩‹ 𝐾𝐼𝑁𝐺 𝑂𝐹 𝐸𝑁𝐺𓆪

                              ███████╗  █████╗       ██╗      ██╗  █████╗  ██████╗  
                              ██╔════╝ ██╔══██╗      ██║      ██║ ██╔══██╗ ██╔══██╗ 
                              ███████╗ ███████║      ██║      ██║ ███████║ ██║  ██║ 
                              ╚════██║ ██╔══██║ ██   ██║ ██   ██║ ██╔══██║ ██║  ██║ 
                              ███████║ ██║  ██║ ╚█████╔╝ ╚█████╔╝ ██║  ██║ ██████╔╝ 
                              ╚══════╝ ╚═╝  ╚═╝  ╚════╝   ╚════╝  ╚═╝  ╚═╝ ╚═════╝  
                  『ᴍᴀᴅᴇ ʙʏ : ENG.DEV SAJJAD ™ 
                         ᴛᴇʟᴇɢʀᴀᴍ: https://t.me/S_J_O_D 
                            DEV-INFO : https://t.me/KING_OF_ENG  』
                            
                            
{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-
  {Y}[{P}*{Y}]{C}Code By :{W} 𓆩𝑬𝑵𝑮-𝑺𝑨𝑱𝑱𝑨𝑫𓆪
  {Y}[{P}*{Y}]{C}DEV-INFO : {W}@KING_OF_ENG
{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-{G}-{R}-''')
dead = (C+"""▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬~𓆩𝑬𝑵𝑮-𝑺𝑨𝑱𝑱𝑨𝑫𓆪~▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬▭▬""")
print(dead)

# تكوين المتغيرات العامة
bot_token = 'توكنك'
bot = telebot.TeleBot(bot_token)
email_senders = []
email_passwords = []
set_sender_email = False
email_subject = ''
email_message = ''

# تعريف الأزرار
keyboard = telebot.types.InlineKeyboardMarkup()
btn_add_recipient = telebot.types.InlineKeyboardButton('اضف حساب', callback_data='add_recipient')
btn_add_sender = telebot.types.InlineKeyboardButton('اضف مرسل', callback_data='add_sender')
btn_change_recipient = telebot.types.InlineKeyboardButton('اختيار حساب', callback_data='change_recipient')
btn_set_subject = telebot.types.InlineKeyboardButton('تعيين موضوع', callback_data='set_subject')
btn_set_message = telebot.types.InlineKeyboardButton('تعيين كليشه', callback_data='set_message')
btn_set_interval = telebot.types.InlineKeyboardButton('السليب', callback_data='set_interval')
btn_set_message_count = telebot.types.InlineKeyboardButton('عدد الارسال', callback_data='set_message_count')
btn_start_sending = telebot.types.InlineKeyboardButton('بدء الارسال', callback_data='start_sending')
btn_show_accounts = telebot.types.InlineKeyboardButton('حساباتي', callback_data='show_accounts')
keyboard.row(btn_add_recipient, btn_add_sender)
keyboard.row(btn_change_recipient, btn_set_subject, btn_set_message)
keyboard.row(btn_set_interval, btn_set_message_count)
keyboard.row(btn_start_sending, btn_show_accounts)

# قائمة المستخدمين المسموح لهم باستخدام البوت
allowed_users = ['ايديك']

# قائمة المستلمين
recipients = []

# متغيرات الفاصل الزمني وعدد الرسائل
interval_seconds = 0
message_count = 0

# استقبال الرسائل من المستخدمين
@bot.message_handler(commands=['start'])
def start(message):
    if str(message.from_user.id) in allowed_users:
        bot.reply_to(message, 'اهلا بك في بوت الرفع الخارجي المطورين!', reply_markup=keyboard)
    else:
        bot.reply_to(message, 'انت غير مشترك في البوت.')

import time

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'add_recipient':
        bot.reply_to(call.message, 'الرجاء ارسال الايميل المراد الارسال اليه')
        bot.register_next_step_handler(call.message, add_recipient)
    elif call.data == 'add_sender':
        bot.reply_to(call.message, 'الرجاء ارسال الايميل الخاص بك')
        bot.register_next_step_handler(call.message, add_sender)
    elif call.data == 'change_recipient':
        bot.reply_to(call.message, 'الرجاء ارسال الايميل المراد الشد او الرفع عليه')
        bot.register_next_step_handler(call.message, change_recipient)
    elif call.data == 'set_subject':
        bot.reply_to(call.message, 'الرجاء ارسال الموضوع الخاص بكليشتك')
        bot.register_next_step_handler(call.message, set_subject)
    elif call.data == 'set_message':
        bot.reply_to(call.message, 'الرجاء ارسال الكلمة الخاصة بكليشتك')
        bot.register_next_step_handler(call.message, set_message)
    elif call.data == 'set_interval':
        bot.reply_to(call.message, 'الرجاء ارسال الفاصل الزمني بين الرسائل (بالثواني)')
        bot.register_next_step_handler(call.message, set_interval)
    elif call.data == 'set_message_count':
        bot.reply_to(call.message, 'الرجاء ارسال عدد الرسائل المطلوب إرسالها')
        bot.register_next_step_handler(call.message, set_message_count)
    elif call.data == 'start_sending':
        bot.reply_to(call.message, 'جارٍ بدء إرسال الرسائل...')
        start_sending(call.message)
    elif call.data == 'show_accounts':
        show_accounts(call.message)


def add_recipient(message):
    recipient = message.text
    if recipient:
        recipients.append(recipient)
        bot.reply_to(message, 'تمت إضافة الحساب المستلم بنجاح!')
    else:
        bot.reply_to(message, 'خطأ في إضافة الحساب المستلم. الرجاء المحاولة مرة أخرى.')


def add_sender(message):
    sender_email = message.text
    if sender_email:
        email_senders.append(sender_email)
        bot.reply_to(message, 'الرجاء إرسال كلمة المرور الخاصة بالحساب المرسل.')
        bot.register_next_step_handler(message, add_sender_password)
    else:
        bot.reply_to(message, 'خطأ في إضافة الحساب المرسل. الرجاء المحاولة مرة أخرى.')


def add_sender_password(message):
    sender_password = message.text
    if sender_password:
        email_passwords.append(sender_password)
        bot.reply_to(message, 'تمت إضافة الحساب المرسل بنجاح!')
    else:
        bot.reply_to(message, 'خطأ في إضافة كلمة المرور. الرجاء المحاولة مرة أخرى.')


def change_recipient(message):
    recipient = message.text
    if recipient:
        recipients.clear()
        recipients.append(recipient)
        bot.reply_to(message, 'تم تغيير الحساب المستلم بنجاح!')
    else:
        bot.reply_to(message, 'خطأ في تغيير الحساب المستلم. الرجاء المحاولة مرة أخرى.')


def set_subject(message):
    global email_subject
    email_subject = message.text
    bot.reply_to(message, 'تم تعيين الموضوع بنجاح!')


def set_message(message):
    global email_message
    email_message = message.text
    bot.reply_to(message, 'تم تعيين الكلمة الخاصة بالرسالة بنجاح!')


def set_interval(message):
    global interval_seconds
    interval_seconds = int(message.text)
    bot.reply_to(message, 'تم تعيين الفاصل الزمني بنجاح!')


def set_message_count(message):
    global message_count
    message_count = int(message.text)
    bot.reply_to(message, 'تم تعيين عدد الرسائل بنجاح!')



def start_sending(message):
    global email_senders, email_passwords, recipients, email_subject, email_message, interval_seconds, message_count
    if len(email_senders) == 0 or len(email_passwords) == 0:
        bot.reply_to(message, 'الرجاء إضافة مرسل وكلمة مرور المرسل قبل بدء عملية الإرسال')
        return

    for i in range(message_count):
        sender_index = i % len(email_senders)
        recipient_index = i % len(recipients)

        sender_email = email_senders[sender_index]
        sender_password = email_passwords[sender_index]
        recipient_email = recipients[recipient_index]

        send_email(sender_email, sender_password, recipient_email, email_subject, email_message,message)

        time.sleep(interval_seconds)

    bot.reply_to(message, 'تمت عملية الارسال بنجاح.')



def send_email(sender_email, sender_password, recipient_emails, subject, message,msag):

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = subject


    msg.attach(MIMEText(message, 'plain'))


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_emails, text)
        server.quit()
        print("تم إرسال البريد الإلكتروني بنجاح")
        bot.reply_to(msag, 'تم ارسال رسالة .')
    except Exception as e:
        bot.reply_to(msag, 'حدث خطأ في ارسال رسالة .')
        print("حدث خطأ أثناء إرسال البريد الإلكتروني:", str(e))
    
 

def show_accounts(message):
    if len(email_senders) == 0:
        bot.reply_to(message, 'لم يتم إضافة أي حسابات مرسلة حتى الآن.')
    else:
        accounts = []
        for i in range(len(email_senders)):
            accounts.append(f'حساب رقم {i+1}: {email_senders[i]}')

        bot.reply_to(message, '\n'.join(accounts))
        
        
bot.polling()