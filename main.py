from tkinter import *
ws = Tk()
ws.geometry('400x200')
ws.title('Temperature Converter')

f = ("Times bold", 14)


def C_to_F():
    ws.destroy()
    import C_to_F


def F_to_C():
    ws.destroy()
    import F_to_C


Label(
    ws,
    text="Temperature Converter(°C and °F)",
    padx=20,
    pady=20,
    font=f
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="°C to °F",
    font=f,
    command=C_to_F
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="°F to °C",
    font=f,
    command=F_to_C
).pack(fill=X, expand=TRUE, side=LEFT)
ws.mainloop()
