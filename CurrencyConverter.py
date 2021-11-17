
from tkinter import *   # tkinter is the standard Python GUI
from PIL import ImageTk, Image
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

root = Tk()
root.title("Live Currency Converter")
root.geometry("400x200")

options = ["USD", "EUR", "GBP", "JPY", "BRL", "AUD", "CAD",
           "CHF", "CNY", "MXN", "INR","RUB"]

start_clicked = StringVar()
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
    elif from_country == options[11]:
        my_pic = Image.open("russia_flag.png")

    resized = my_pic.resize((200, 100), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resized)   # save the resized image
    flag_label.config(image=new_pic)
    flag_label.photo = new_pic # save a reference of the image


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
    elif to_country == options[11]:
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

start_num = StringVar()
start_num = Entry(root)

end_clicked = StringVar()
end_clicked.set("Select a country to end")
dropdown2 = OptionMenu(root, end_clicked, *options, command=second_country)#, command=end_selected)

dropdown.config(font = (36))
dropdown2.config(font = (36))
start_num.config(font=36)

dropdown.grid(row=0,column=0)
dropdown2.grid(row=0,column=1)
start_num.grid(row=1, column=0)

# need to allow for decimals
conversion = CurrencyRates(force_decimal=True)
sign = CurrencyCodes()
# activate the conversion
def activate_clicked():
    start = start_clicked.get()
    end = end_clicked.get()
    new_sign = sign.get_symbol(end)
    try:
        value = float(start_num.get())
        finalValue = conversion.convert(start, end, Decimal(value))
        finalAnswer = new_sign + str(finalValue)
    except ValueError:  # if non-integer is entered
        finalAnswer = "Please enter a number."

    result = Label(root)
    result.config(text=finalAnswer)
    result.grid(row=1, column=1)
    result.config(font=36)
    finalValue = 0
    new_sign = ""
    finalAnswer = ""

activate = Button(root, text="Activate", command=activate_clicked)
activate.grid(row=2,column=1)
root.mainloop()     # stay open until you close it

