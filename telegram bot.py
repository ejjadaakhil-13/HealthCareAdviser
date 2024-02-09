# Importing Telebot Package
from telebot import *

# Token For Accessing the Bot
bot = TeleBot('6797260133:AAG9bD_medAIWk7b6wEKJkeZxCZSoQ58AWA')

# Defines the size of the Buttons
keyboard = types.ReplyKeyboardMarkup(row_width=1)

# Creating Main Buttons for the bot
Mainbtn1 = types.KeyboardButton('Health Tips')
Mainbtn2 = types.KeyboardButton("Health Care Products")

#Buttons for the Tips
btn1 = types.KeyboardButton('Workouts 🦾')
btn2 = types.KeyboardButton('Food Guide 🥣')
btn3 = types.KeyboardButton('Yoga Guide 🙋‍♂️')
btn4 = types.KeyboardButton('Health Tips Guide 🧑‍⚕️')
btn5 = types.KeyboardButton('Lower Back Pain issues 🤕')
btn6 = types.KeyboardButton('Remove Toxic Waste in our body ☣️')
btn7 = types.KeyboardButton('Reduce body heat in the body 🔥')
btn8 = types.KeyboardButton('Remedies for dry Skin during winter❄️')
btn9 = types.KeyboardButton('Skin care Routine for Men🚹')

#Creating Buttons for Products
btn10 = types.KeyboardButton('Glucometer For sugar Test')
btn11 = types.KeyboardButton('Blood Pressure Monitoring Machine')
btn12 = types.KeyboardButton('Shampoo for Dandruff')
btn13 = types.KeyboardButton('Facewash for Acne')
btn14 = types.KeyboardButton('Facewash for Tan Removal')
btn15 = types.KeyboardButton('Oximeter')
#Return Buttons
returnbtn1=types.KeyboardButton('Return 🔙')


# Adding Buttons for the Bot
keyboard.add(Mainbtn1, Mainbtn2)

# Product Buttons
product_keyboard = types.ReplyKeyboardMarkup(row_width=1)
product_keyboard.add(btn10, btn11, btn15, btn12, btn13, btn14, returnbtn1 )

# Health Tips Buttons
health_tips_keyboard = types.ReplyKeyboardMarkup(row_width=1)
health_tips_keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, returnbtn1)

# Start Button
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! This is your health adviser", reply_markup=keyboard)

# Help Button
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 'Enter "/start" to go back.\nUse the buttons below to navigate through our bot.', reply_markup=keyboard)

# Button Controls
@bot.message_handler(func=lambda message: True)
def content(message):

    # Main Button controlls
    if message.text == 'Health Tips':
        bot.reply_to(message, "Choose a category:", reply_markup=health_tips_keyboard)
    elif message.text == 'Health Care Products':
        bot.reply_to(message, "Choose a product:", reply_markup=product_keyboard)

    # Button Controls for the Tips
    elif message.text == 'Workouts 🦾':
        bot.reply_to(message, "Here is the Workouts Guide: \n https://youtu.be/cbKkB3POqaY?si=_docH5TuQWk529op ")
    elif message.text == 'Food Guide 🥣':
        bot.reply_to(message, "Here is the Food Guide: \n https://youtu.be/mJ1iIiVV0mM?si=Gj3SolajwpkiuOgy \n https://youtu.be/rWAQpgTdQmc?si=0TxdxFbQAjjg83Yk")
    elif message.text == 'Yoga Guide 🙋‍♂️':
        bot.reply_to(message, "Here is the Yoga Guide: \n https://youtu.be/sTANio_2E0Q?si=k_1gh2dkqsZTpCJK ")
    elif message.text == 'Health Tips Guide 🧑‍⚕️':
        bot.reply_to(message, "Here is the Health Tips Guide: \n https://youtu.be/OYpXKocfWlU?si=Xe11nYiiEDzIHb3a \n https://youtu.be/rWAQpgTdQmc?si=0TxdxFbQAjjg83Yk")
    elif message.text == 'Lower Back Pain issues 🤕':
        bot.reply_to(message, "Here is the way to get rid of Lower Back Pain issues: \n https://youtube.com/shorts/2wZSaZypDwI?si=ygdJPbJzM-dkzych ")
    elif message.text == 'Remove Toxic Waste in our body ☣️':
        bot.reply_to(message, "Here is the tip to get rid of Toxic Waste in our body: \n https://youtu.be/3IYM8K9ZtWw?si=-NTp6C6gHoEigo6j")
    elif message.text == 'Reduce body heat in the body 🔥':
        bot.reply_to(message, "Here is the tip to Reduce body heat in the body : \n https://youtu.be/pCaz06psb0s?si=IxEjuylfU3dbDMPH")
    elif message.text == 'Remedies for dry Skin during winter❄️':
        bot.reply_to(message, "Remedies for dry Skin during winter : \n https://youtu.be/qmQ8LYx_ky8?si=jE0M-kAh7JtQBzlA")
    elif message.text == 'Skin care Routine for Men🚹':
        bot.reply_to(message, "Skin care Routine for Men : \n https://youtu.be/6l-4iC18H68?si=UYSsPTEWaCwwnKh0")

    # Return Button
    elif message.text == 'Return 🔙':
        bot.reply_to(message, "Returning to main menu" , reply_markup=keyboard)

    # Button controls for Products
    elif message.text == 'Glucometer For sugar Test':
        bot.reply_to(message, "Glucometer For sugar Test : \n https://amzn.eu/d/fXN3VMF")
    elif message.text == 'Blood Pressure Monitoring Machine':
        bot.reply_to(message, "BP Machine : \n https://amzn.eu/d/arzE1NZ")
    elif message.text == 'Shampoo for Dandruff':
        bot.reply_to(message, "Shampoo for Dandruff : \n https://amzn.eu/d/8nTLc1K")
    elif message.text == 'Facewash for Acne':
        bot.reply_to(message, "Facewash for Acne: \n https://amzn.eu/d/13Ik2it")
    elif message.text == 'Facewash for Tan Removal':
        bot.reply_to(message, "Facewash for Tan Removal: \n https://amzn.eu/d/dYs7y4a")
    elif message.text == 'Oximeter':
        bot.reply_to(message, "Oximeter: \n https://amzn.eu/d/cQEQhQe")


    else:
        bot.send_message(message.chat.id, "Sorry, I didn't understand what you were telling. Here are the things I can help you with", reply_markup=keyboard)

bot.polling()
