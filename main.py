from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)

    password = "".join(password_list)

    # for char in password_list:
    #   password += char

    pwd_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pwd_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showwarning(title="Attention",message="Some fields empty, please try again!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                      f"\nEmail: {email}"
                                                      f"\nPassword: {password}"
                                                      f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")

            website_entry.delete(0, END)
            email_entry.delete(0, END)
            pwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Create Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create Labels and Entries
# Website Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# Email Label
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# Password Label
pwd_label = Label(text="Password:")
pwd_label.grid(column=0, row=3)

# Website Entry
website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)

# Email Entry
email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "filipeaugusto2299@gmail.com")

# Password Entry
pwd_entry = Entry(width=21)
pwd_entry.grid(column=1, row=3)

# Create Buttons
# Generate Password Button
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
