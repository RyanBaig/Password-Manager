import os
import pickle
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style

def populate_dropdown():
    try:
        with open("info.pkl", "rb") as file:
            data = pickle.load(file)
            password_locations = [item["Password Location"] for item in data]
            dropdown['values'] = tuple(password_locations)
    except (FileNotFoundError, EOFError):
        pass

def delete_info():
    selected_password_location = dropdown.get()
    if selected_password_location in password_locations:
        data = []
        with open("info.pkl", "rb") as f:
            data = pickle.load(f)

        # Filter out the selected password location
        filtered_data = [item for item in data if item["Password Location"] != selected_password_location]

        with open("info.pkl", "wb") as f:
            pickle.dump(filtered_data, f)

        password_locations.remove(selected_password_location)
        dropdown['values'] = tuple(password_locations)

        messagebox.showinfo("Info Deleted", "Info Deleted Successfully.")
    else:
        messagebox.showerror("Error", "Selected password location not found.")


def retrieve_info():
    selected_password_location = dropdown.get()
    if selected_password_location in password_locations:
        with open("info.pkl", "rb") as f:
            data = pickle.load(f)
            for item in data:
                if item["Password Location"] == selected_password_location:
                    messagebox.showinfo("Info", f"Email: {item['Email']}\nPassword: {item['Password']}")
                    break
    else:
        messagebox.showerror("Error", "Selected password location not found.")


win = tk.Tk()
win.title("Password Manager By Ryan")
win.geometry("500x500")
title_font = ("Arial", 20, "bold")
title = tk.Label(win, text="Password Manager", font=title_font)
title.pack(padx=10)
win.style = Style(theme="darkly")

notebook = ttk.Notebook(win, width=500, height=500)
notebook.pack()

add = ttk.Frame(notebook)
view = ttk.Frame(notebook)
notebook.add(add, text="Add Passwords")
notebook.add(view, text="View Passwords")

dropdown = ttk.Combobox(view, width=30)
dropdown.pack(padx=10)

populate_dropdown()

retrieve_button = tk.Button(view, text="Retrieve", command=retrieve_info)
retrieve_button.pack(padx=10)

delete_button = tk.Button(view, text="Delete", command=delete_info)
delete_button.pack(padx=10)

password_location_label = tk.Label(add, text="Password Location (google.com, gmail.com, etc.)")
password_location_label.pack(padx=10)
password_location = tk.Entry(add, width=30)
password_location.pack(padx=10)


def save_info():
    if not password_location.get() or not email.get() or not password.get():
        messagebox.showerror("Error", "Please fill out all fields.")
    else:
        new_info = {
            "Password Location": password_location.get(),
            "Email": email.get(),
            "Password": password.get()
        }
        try:
            with open("info.pkl", "rb") as f:
                data = pickle.load(f)
        except EOFError:
            data = []
        except FileNotFoundError:
            data = []
        data.append(new_info)

        with open("info.pkl", "wb") as f:
            pickle.dump(data, f)

        password_locations.append(password_location.get())
        dropdown['values'] = tuple(password_locations)

        messagebox.showinfo("Info Submitted", "Info Submitted Successfully!")
        password_location.delete(0, tk.END)
        email.delete(0, tk.END)
        password.delete(0, tk.END)


password_locations = []


def retrieve_password_locations():
    try:
        if hasattr(sys, '_MEIPASS'):  # Check if running as an executable
            file_dir = sys._MEIPASS
        else:
            file_dir = os.path.dirname(__file__)

        with open(os.path.join(file_dir, "info.pkl"), "rb") as f:
            data = pickle.load(f)
            for item in data:
                password_locations.append(item["Password Location"])
    except (FileNotFoundError, EOFError):
        pass


retrieve_password_locations()

email_label = tk.Label(add, text="Email")
email_label.pack(padx=10)
email = tk.Entry(add, width=30)
email.pack(padx=10)

password_label = tk.Label(add, text="Password")
password_label.pack(padx=10)
password = tk.Entry(add, width=30, show="*")
password.pack(padx=10)

submit_button = tk.Button(add, text="Submit", command=save_info)
submit_button.pack(padx=10)



win.mainloop()
