import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize the main application window
window = tk.Tk()
window.title("Contact Book")
window.configure(bg="sea green")

# Dictionary to store contacts
contacts = {}

def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    if name:
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")
        if phone:
            contacts[name] = {'phone': phone, 'email': email, 'address': address}
            view_contacts()
        else:
            messagebox.showwarning("Error", "Phone number is required!")
    else:
        messagebox.showwarning("Error", "Name is required!")

def view_contacts():
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        contact_listbox.insert(tk.END, name)

def show_selected_contact(event):  # Accept event parameter directly
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected)
        details = contacts[name]
        info = f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}"
        messagebox.showinfo("Contact Info", info)
    else:
        messagebox.showwarning("Error", "Select a contact to view.")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected)
        del contacts[name]
        view_contacts()
    else:
        messagebox.showwarning("Error", "Select a contact to delete.")

def search_contact():
    search_name = simpledialog.askstring("Search", "Enter the name to search:")
    if search_name:
        if search_name in contacts:
            messagebox.showinfo("Contact Found", f"Contact: {search_name}\nPhone: {contacts[search_name]['phone']}\nEmail: {contacts[search_name]['email']}\nAddress: {contacts[search_name]['address']}")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")
    else:
        messagebox.showwarning("Error", "Please enter a name to search.")

# UI Setup
window.geometry("400x400")  # Set window size

heading = tk.Label(window, text="Contact Book", font=("Times New Roman", 20), bg="#2E8B57", fg="white")  # Complementary background
heading.pack(pady=10)

contact_listbox = tk.Listbox(window, width=50)
contact_listbox.pack(pady=10)
contact_listbox.bind('<<ListboxSelect>>', show_selected_contact)  # Directly reference the function

add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

search_button = tk.Button(window, text="Search Contact", command=search_contact)
search_button.pack(pady=5)

exit_button = tk.Button(window, text="Exit", command=window.quit)
exit_button.pack(pady=5)

# Run the application
window.mainloop()
