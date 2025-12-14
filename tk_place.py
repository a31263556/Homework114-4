import tkinter as tk

form = tk.Tk()
form.title("Tkinter Place")
form.geometry("400x300")

#  左側 10%
left = tk.Frame(form, bg="lightgreen")
left.place(relx=0, rely=0, relwidth=0.1, relheight=1)

#  右側 10%
right = tk.Frame(form, bg="lightblue")
right.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)

#  中間 80%
content = tk.Frame(form, bg="white")
content.place(relx=0.1, rely=0, relwidth=0.8, relheight=1)

#  上層 20%（紅色）
top = tk.Frame(content, bg="red")
top.place(relx=0, rely=0, relwidth=1, relheight=0.2)

# 紅色內分三等份
tk.Label(top, text="left", bg="white").place(relx=0.02, rely=0.05)
tk.Label(top, text="center", bg="white").place(relx=0.5, rely=0.05, anchor="n")
tk.Label(top, text="Right", bg="white").place(relx=0.98, rely=0.05, anchor="ne")

#  中層 70%（黃色）
middle = tk.Frame(content, bg="yellow")
middle.place(relx=0, rely=0.2, relwidth=1, relheight=0.7)

#  下層 10%（藍色）
bottom = tk.Frame(content, bg="blue")
bottom.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

form.mainloop()
