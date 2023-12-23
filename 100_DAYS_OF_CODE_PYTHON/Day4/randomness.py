# import tkinter as tk
# import random
# interface = tk.Tk()
# interface.title("Random Number Generator")
# def genrandnum():
#     minval = int(minentry.get())
#     maxval = int(maxentry.get())
#     randnum = random.randint(minval, maxval)
#     res.config(text=f"Random Number: {randnum}")
# minlabel = tk.Label(interface, text="Minimum Value:")
# minlabel.pack()
# minentry = tk.Entry(interface)
# minentry.pack()
# maxlabel = tk.Label(interface, text="Maximum Value:")
# maxlabel.pack()
# maxentry = tk.Entry(interface)
# maxentry.pack()
# res = tk.Label(interface, text="", pady=10)
# res.pack()
# genbutton = tk.Button(interface, text="Generate Random Number", command=genrandnum)
# genbutton.pack()
# interface.mainloop()

import random
random_int= random.randint(5 , 50)
print(random_int)

random_float = random.random()
print(random_float)