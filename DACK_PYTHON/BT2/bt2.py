import sqlite3
from tkinter import *
from tkinter import messagebox

conn = sqlite3.connect("database3.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
)
""")

conn.commit()

def add_user():
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()
    if not name or not age or not address:
        messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    try:
        cursor.execute("INSERT INTO users (name, age, address) VALUES (?, ?, ?)", (name, int(age), address))
        conn.commit()
        messagebox.showinfo("Thành công", "Đã thêm người dùng!")
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        address_entry.delete(0, END)
        display_users()
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


def display_users():
    listbox.delete(0, END)
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        listbox.insert(END, f"ID: {row[0]}, Tên: {row[1]}, Tuổi: {row[2]}, Địa chỉ: {row[3]}")

def delete_user():
    try:
        selected_item = listbox.get(listbox.curselection())
        user_id = int(selected_item.split(",")[0].split(":")[1].strip())
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        messagebox.showinfo("Thành công", "Người dùng đã được xóa!")
        display_users()
    except IndexError:
        messagebox.showwarning("Lỗi", "Vui lòng chọn một người dùng để xóa!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))
def update_user():
    try:
        selected_item = listbox.get(listbox.curselection())
        user_id = int(selected_item.split(",")[0].split(":")[1].strip())
        new_name = name_entry.get()
        new_age = age_entry.get()
        new_address = address_entry.get()
        if not new_name or not new_age or not new_address:
            messagebox.showwarning("Lỗi", "Vui lòng nhập đầy đủ thông tin để cập nhật!")
            return
        cursor.execute("UPDATE users SET name = ?, age = ?, address = ? WHERE id = ?", (new_name, int(new_age), new_address, user_id))
        conn.commit()
        messagebox.showinfo("Thành công", "Cập nhật thông tin thành công!")
        name_entry.delete(0, END)
        age_entry.delete(0, END)
        address_entry.delete(0, END)
        display_users()
    except IndexError:
        messagebox.showwarning("Lỗi", "Vui lòng chọn một người dùng để sửa!")
    except Exception as e:
        messagebox.showerror("Lỗi", str(e))




root = Tk()
root.title("Quản lý người dùng")

Label(root, text="Tên:").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Tuổi:").grid(row=1, column=0, padx=5, pady=5)
age_entry = Entry(root)
age_entry.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Địa chỉ:").grid(row=2, column=0, padx=5, pady=5)
address_entry = Entry(root)
address_entry.grid(row=2, column=1, padx=5, pady=5)


add_button = Button(root, text="Thêm", command=add_user)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

delete_button = Button(root, text="Xóa", command=lambda: delete_user())
delete_button.grid(row=5, column=0, columnspan=2, pady=10)

update_button = Button(root, text="Sửa", command=lambda: update_user())
update_button.grid(row=5, column=1, columnspan=2, pady=10)



listbox = Listbox(root, width=50)
listbox.grid(row=4, column=0, columnspan=2, pady=10)

display_users()

root.mainloop()

conn.close()
