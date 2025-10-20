import tkinter as tk
from tkinter import filedialog

def open_subwindow():
    root.withdraw()  # Hide the main window

    sub = tk.Toplevel()
    sub.title("Subwindow")
    sub.geometry("400x300")
    label_sub = tk.Label(sub, text='This is a subwindow.')
    label_sub.pack(pady=20)
    sub_entry = tk.Entry(sub, width=40)
    sub_entry.pack(pady=10)

    def select_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            sub_entry.delete(0, tk.END)
            sub_entry.insert(0, folder_path)

    select_sub_button = tk.Button(sub, text="choose correct folder", command = select_folder)
    select_sub_button.pack(pady=10)

    def submit():
        folder_name = label_entry.get()
        folder_pass = sub_entry.get()
        print("Folder Name:", folder_name)
        print("Folder Path:", folder_pass)
        sub.destroy()
        root.destroy()  # Show the main window again

    tk.Button(sub, text="Submit", command=submit).pack(pady=20)    


root = tk.Tk()
root.title("tkinter Exercises")
root.geometry("800x700")

label_root = tk.Label(root, text='Tkinter Exercises is fun.')
label_root.pack(pady=(10,20))

label_entry = tk.Entry(root, width=50)
label_entry.pack(pady=(10,0))

create_button = tk.Button(root, text="Studying is Continued...", command = open_subwindow)
create_button.pack(pady=(10,20))

root.mainloop()