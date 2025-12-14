import tkinter as tk

form = tk.Tk()
form.title("Tkinter Pack")
form.geometry("400x300")
form.minsize(300, 200)

#  左側（固定）
left = tk.Frame(form, bg="lightgreen", width=40)
left.pack(side="left", fill="y")

#  右側（固定）
right = tk.Frame(form, bg="lightblue", width=40)
right.pack(side="right", fill="y")

#  中間（自動撐開）
content = tk.Frame(form, bg="white")
content.pack(side="left", expand=True, fill="both")

# 上層（紅色）
top = tk.Frame(content, bg="red", height=60)
top.pack(side="top", fill="x")
top.pack_propagate(False)


left_box = tk.Frame(top, bg="red")
left_box.pack(side="left", expand=True, fill="both")

center_box = tk.Frame(top, bg="red")
center_box.pack(side="left", expand=True, fill="both")

right_box = tk.Frame(top, bg="red")
right_box.pack(side="left", expand=True, fill="both")

tk.Label(left_box, text="left", bg="white").pack(anchor="n")
tk.Label(center_box, text="center", bg="white").pack(anchor="n")
tk.Label(right_box, text="Right", bg="white").pack(anchor="n")

# 中層（黃色）
middle = tk.Frame(content, bg="yellow")
middle.pack(expand=True, fill="both")

# 下層（藍色）
bottom = tk.Frame(content, bg="blue", height=30)
bottom.pack(side="bottom", fill="x")
bottom.pack_propagate(False)

form.mainloop()
