# Isra Tariq 
# Task:2 
# Creating a contact book for my intership task i.e codesoft intership 
import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBookGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        
        self.contact_book = ContactBook()

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Name:").grid(row=0, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.name_var).grid(row=0, column=1)

        tk.Label(self.master, text="Phone:").grid(row=1, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.phone_var).grid(row=1, column=1)

        tk.Label(self.master, text="Email:").grid(row=2, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.email_var).grid(row=2, column=1)

        tk.Label(self.master, text="Address:").grid(row=3, column=0, sticky="e")
        tk.Entry(self.master, textvariable=self.address_var).grid(row=3, column=1)

        tk.Button(self.master, text="Add Contact", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="View Contact List", command=self.view_contact_list).grid(row=5, column=0, columnspan=2, pady=10)
# conditions to add  contact in conatct book 
    def add_contact(self):
        name = self.name_var.get()
        phone_number = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        if name and phone_number:
            new_contact = Contact(name, phone_number, email, address)
            self.contact_book.add_contact(new_contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Name and phone number are required.")

    def view_contact_list(self):
        contacts = self.contact_book.get_contacts()
        if contacts:
            contact_list_window = tk.Toplevel(self.master)
            tk.Label(contact_list_window, text="Contact List").pack()

            for contact in contacts:
                tk.Label(contact_list_window, text=f"Name: {contact.name}, Phone: {contact.phone_number}").pack()
        else:
            messagebox.showinfo("Info", "Contact list is empty.")

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set()

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts

# Create the main application window
root = tk.Tk()
app = ContactBookGUI(root)
root.mainloop()
