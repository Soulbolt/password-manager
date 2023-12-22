from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=1)

website_label = Label(text="Website:")
website_label.grid(column=0, row=2)
website_input = Entry(width=60)
website_input.grid(column=1, row=2)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=3)
email_entry = Entry(width=60)
email_entry.grid(column=1, row=3)
password_label = Label(text="Password")
password_label.grid(column=0, row=4)
password_entry = Entry(width=32)
password_entry.grid(column=1, row=4)
generate_password_button = Button(text="Generate Password",)
generate_password_button.grid(column=1.5, row=4)
add_button = Button(text="Add", width=60)
add_button.grid(column=1, row=5)



window.mainloop()
