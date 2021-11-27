
from tkinter import *   # tkinter is the standard Python GUI
from PIL import ImageTk, Image
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *


root = Tk()
root.title("Live Currency Converter")
root.geometry("400x200")
result = Label(root)  # will display converted value, needs to be global variable

options = ["USD", "EUR", "GBP", "JPY", "BRL", "AUD", "CAD",
           "CHF", "CNY", "MXN", "INR","RUB"]

start_clicked = StringVar()
start_clicked.set("Select a country")


# function opens up picture based off the country to begin conversion
def first_country(from_country):
    if from_country == options[0]:
        my_pic = Image.open("usa_flag.png")
    elif from_country == options[1]:
        my_pic = Image.open("eu_flag.png")
    elif from_country == options[2]:
        my_pic = Image.open("uk_flag.png")
    elif from_country == options[3]:
        my_pic = Image.open("japan_flag.png")
    elif from_country == options[4]:
        my_pic = Image.open("brazil_flag.png")
    elif from_country == options[5]:
        my_pic = Image.open("australia_flag.png")
    elif from_country == options[6]:
        my_pic = Image.open("canada_flag.png")
    elif from_country == options[7]:
        my_pic = Image.open("switzerland_flag.png")
    elif from_country == options[8]:
        my_pic = Image.open("china_flag.png")
    elif from_country == options[9]:
        my_pic = Image.open("mexico_flag.png")
    elif from_country == options[10]:
        my_pic = Image.open("india_flag.png")
    else:
        my_pic = Image.open("russia_flag.png")

    resized = my_pic.resize((200, 100), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)   # save the resized image
    flag_label.config(image=new_pic)
    flag_label.photo = new_pic  # save a reference of the image


# function opens up picture based off the country to end conversion
def second_country(to_country):
    if to_country == options[0]:
        my_pic = Image.open("usa_flag.png")
    elif to_country == options[1]:
        my_pic = Image.open("eu_flag.png")
    elif to_country == options[2]:
        my_pic = Image.open("uk_flag.png")
    elif to_country == options[3]:
        my_pic = Image.open("japan_flag.png")
    elif to_country == options[4]:
        my_pic = Image.open("brazil_flag.png")
    elif to_country == options[5]:
        my_pic = Image.open("australia_flag.png")
    elif to_country == options[6]:
        my_pic = Image.open("canada_flag.png")
    elif to_country == options[7]:
        my_pic = Image.open("switzerland_flag.png")
    elif to_country == options[8]:
        my_pic = Image.open("china_flag.png")
    elif to_country == options[9]:
        my_pic = Image.open("mexico_flag.png")
    elif to_country == options[10]:
        my_pic = Image.open("india_flag.png")
    else:
        my_pic = Image.open("russia_flag.png")

    resized = my_pic.resize((200, 100), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)
    flag_label2.config(image=new_pic)
    flag_label2.photo = new_pic


# display list to allow user selection
dropdown = OptionMenu(root, start_clicked, *options, command=first_country)

flag_label = Label(root)
flag_label.grid(row=3, column=0)
flag_label2 = Label(root)
flag_label2.grid(row=3, column=1)

start_num = Entry(root)
end_clicked = StringVar()
end_clicked.set("Select a country to end")
dropdown2 = OptionMenu(root, end_clicked, *options, command=second_country)#, command=end_selected)

dropdown.config(font=36)
dropdown2.config(font=36)
start_num.config(font=36)

dropdown.grid(row=0, column=0)
dropdown2.grid(row=0, column=1)
start_num.grid(row=1, column=0)

# need to allow for decimals
conversion = CurrencyRates(force_decimal=True)
sign = CurrencyCodes()


# activate the conversion
def activate_clicked():
    start = start_clicked.get()
    end = end_clicked.get()
    new_sign = sign.get_symbol(end)

    global result
    result.destroy()  # destroy the old labels so it doesn't get overwritten
    try:
        value = float(start_num.get())
        final_value = conversion.convert(start, end, Decimal(value))
        final_answer = new_sign + str(final_value)
    except ValueError:  # if non-integer is entered
        final_answer = "Please enter a number."
    result = Label(root)

    result.config(text=final_answer)
    result.grid(row=1, column=1)
    result.config(font=36)


activate = Button(root, text="Convert", command=activate_clicked)

activate.grid(row=2, column=1)

'''
crypto_options = ['BTC', 'ETH', 'DOGE', 'CRO', 'SHIB']


def first_crypto(from_crypto):
    if from_crypto == options[0]:
        my_pic = Image.open('bitcoin.png')
    elif from_crypto == options[1]:
        my_pic = Image.open('ethereum.png')
    elif from_crypto == options[2]:
        my_pic = Image.open('doge.png')
    elif from_crypto == options[3]:
        my_pic = Image.open('crypto.com.png')
    else:
        my_pic = Image.open('shiba.png')
    resized = my_pic.resize((200, 100), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)  # save the resized image
    flag_label.config(image=new_pic)
    flag_label.photo = new_pic  # save a reference of the image


def crypto_clicked():
    start_crypto = StringVar()
    start_crypto.set('Select a crypto')
    dropdown = OptionMenu(root, start_crypto, *crypto_options, command=first_crypto)
    dropdown.grid(row=0, column=0)

crypto_button = Button(root, text="Switch to crypto?", command=crypto_clicked)
crypto_button.grid(row=3, column=1)
'''
root.mainloop()     # stay open until you close it

