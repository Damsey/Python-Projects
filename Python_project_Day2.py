import random
import string
import tkinter as tk

def password_generator(length):
  character = string.ascii_letters + string.digits + string.punctuation
  password = "".join(random.choice(character) for _ in range(length))
  return password

def password_generator_interface():
  password_length = int(entry_length.get())
  if password_length < 6:
    label_result.config(text="The length of the password must be at least 6 characters.")
  else:
    generated_password = password_generator(password_length)
    label_result.config(text="Password Generated: " + generated_password)


root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Enter the desired password length: ")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

generator_button = tk.Button(root, text = "Generate Password", command=password_generator_interface)
generator_button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()