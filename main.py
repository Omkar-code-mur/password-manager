from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_gen():
    import random

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password = password_symbols + password_numbers + password_letters

    shuffle(password)
    password = "".join(password)
    pass_input.delete(0, END)
    pass_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_input.get()
    Email = email_input.get()
    Password = pass_input.get()

    if len(website) == 0 or len(Password) == 0:
        messagebox.showerror(title="Opps", message="Please don't keep any entry empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the entered"
                                                          f" details: \n Email : {Email}\n Password :"
                                                          f" {Password}. \nIs it Okay to save?")
        if is_ok:
            with open("data.txt", "a") as datafile:
                datafile.write(f"{website} | {Email} | {Password}\n")
            web_input.delete(0, END)
            web_input.focus()
        pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pass_Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1, columnspan=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

web_input = Entry(width=55)
web_input.focus()
web_input.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=55)
email_input.insert(0, "omkarkodmur2031@gmail.com")

email_input.grid(row=2, column=1, columnspan=2)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=36)
pass_input.grid(row=3, column=1)


generate_button = Button(text="Generate Password", command=password_gen)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=46, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()
