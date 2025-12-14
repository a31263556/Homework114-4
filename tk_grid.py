import tkinter as tk

form = tk.Tk()
form.title("Tkinter Grid")
form.geometry("400x300")

#  第一層：左右中
form.columnconfigure(0, weight=0)   # 左（固定）
form.columnconfigure(1, weight=1)   # 中（伸縮）
form.columnconfigure(2, weight=0)   # 右（固定）
form.rowconfigure(0, weight=1)

# 左側
left = tk.Frame(form, bg="lightgreen", width=40)
left.grid(row=0, column=0, sticky="ns")

# 右側
right = tk.Frame(form, bg="lightblue", width=40)
right.grid(row=0, column=2, sticky="ns")

# 中間
content = tk.Frame(form, bg="white")
content.grid(row=0, column=1, sticky="nsew")

# 第二層：上中下
content.rowconfigure(0, weight=0)   # 上
content.rowconfigure(1, weight=1)   # 中
content.rowconfigure(2, weight=0)   # 下
content.columnconfigure(0, weight=1)

# 上層（紅色）
top = tk.Frame(content, bg="red", height=60)
top.grid(row=0, column=0, sticky="ew")
top.grid_propagate(False)

top.columnconfigure(0, weight=1)
top.columnconfigure(1, weight=1)
top.columnconfigure(2, weight=1)

tk.Label(top, text="left", bg="white").grid(row=0, column=0, sticky="n")
tk.Label(top, text="center", bg="white").grid(row=0, column=1, sticky="n")
tk.Label(top, text="Right", bg="white").grid(row=0, column=2, sticky="n")

# 中層（黃色）
middle = tk.Frame(content, bg="yellow")
middle.grid(row=1, column=0, sticky="nsew")

# 下層（藍色）
bottom = tk.Frame(content, bg="blue", height=30)
bottom.grid(row=2, column=0, sticky="ew")
bottom.grid_propagate(False)

form.mainloop()
