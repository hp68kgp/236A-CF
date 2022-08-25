from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    final_password = "".join(password_list)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_name = website_entry.get()
    email = username_entry.get()
    password_created = password_entry.get()
    new_data = {
        website_name: {
            "email": email,
            "password": password_created
        }
    }
    # else:
    #     is_ok = messagebox.askokcancel(title=website_name,
    #                                    message=f"These are the details entered: \nEmail: {email} \nPassword: {password_created} \nIs it okay to save?")

    # if is_ok:
    if len(password_created) == 0 or len(website_name) == 0:
        messagebox.showinfo(title="oops", message="Please do not leave any of the fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                # reads the old data after opening json file
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updates old data with new_data
            data.update(new_data)
            # open the file to write mode from read mode so that we can dump new_data
            with open("data.json", "w") as file:
                # puts/dumps the new_data in the json file
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# label
website = Label(text="Website:")
website.grid(row=1, column=0)

username = Label(text="Email/Username:")
username.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2, sticky=N + S + W + E)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(row=2, column=1, columnspan=2, sticky=N + S + W + E)
username_entry.insert(0, "harshilpt68@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky=N + S + W + E)

# Button
generate_password = Button(text="Generate Password", command=create_password)
generate_password.grid(row=3, column=2)

add = Button(text="Add", width=35)
add.grid(row=4, column=1, columnspan=2, sticky=N + S + W + E)
add.config(command=save)

window.mainloop()
