from tkinter import *
from tkinter import messagebox  #  Module, not a class
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    window.clipboard_append(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # read old data
            data = json.load(data_file)
            print(data)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Unknown", message=f"No {website} exist in file.")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def save():
    website = website_entry.get()
    email_username = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please make sure there are no fields empty.")
    else:  # json.dump() to write/create[serialized], json.load()[unserialized] to read data, json.update() to update/add, indent for readability
        try:
            with open("data.json", "r") as data_file:
                # read old data
                data = json.load(data_file)    
        except FileNotFoundError:  # Create file if it does not exist
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data       
            data.update(new_data)
            
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            clear_entries()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=55)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "soulbolt@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", width=16, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=16, command=search)
search_button.grid(row=1, column=2)



window.mainloop()
