from tkinter import *

ws = Tk()
ws.geometry('500x180')
ws.title('°C to °F')

f = ("Times bold", 14)


def main():
    ws.destroy()
    import main


def C_to_F():
    ws.destroy()
    import C_to_F


Label(
    ws,
    text="Convertion from Celsius to Fahrenheit: ",
    font=f,
    padx=20,
    pady=20,
).pack()
input = Entry()
input.pack()


def convertCF():
    temp = float(input.get())
    temp_F = temp*9/5+32
    ans['text'] = 'Temperature in Fahrenheit is: '+str(int(temp_F))+'°F'


button = Button(text='Convert', command=convertCF)
button.pack()

ans = Label(text=' ', font=('Courrier', 15, 'bold'))
ans.pack()

Button(
    ws,
    text="Main page",
    font=f,
    command=main
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="°F to °C",
    font=f,
    command=C_to_F
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
