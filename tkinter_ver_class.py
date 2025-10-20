import tkinter as tk
from tkinter import filedialog

class FolderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("フォルダ名入力")
        self.master.geometry("400x150")

        # フォルダ名入力欄
        tk.Label(master, text="フォルダ名を入力:").pack(pady=5)
        self.name_entry = tk.Entry(master, width=40)
        self.name_entry.pack(pady=5)

        # ボタンでサブウィンドウを開く
        tk.Button(master, text="次へ", command=self.open_subwindow).pack(pady=10)

    def open_subwindow(self):
        self.master.withdraw()  # メインウィンドウを非表示

        self.sub = tk.Toplevel()
        self.sub.title("フォルダパス選択")
        self.sub.geometry("400x200")

        tk.Label(self.sub, text="フォルダパスを選択:").pack(pady=5)
        self.path_entry = tk.Entry(self.sub, width=40)
        self.path_entry.pack(pady=5)

        tk.Button(self.sub, text="フォルダを選ぶ", command=self.select_folder).pack(pady=5)
        tk.Button(self.sub, text="送信", command=self.submit).pack(pady=10)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder_path)

    def submit(self):
        folder_name = self.name_entry.get()
        folder_path = self.path_entry.get()
        print("フォルダ名:", folder_name)
        print("フォルダパス:", folder_path)
        self.sub.destroy()
        self.master.destroy()  # メインウィンドウを再表示

# 実行部分
if __name__ == "__main__":
    root = tk.Tk()
    app = FolderApp(root)
    root.mainloop()
