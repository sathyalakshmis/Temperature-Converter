from tkinter import *

ws = Tk()
ws.geometry('500x180')
ws.title('°F to °C')

f = ("Times bold", 14)

def main():
    ws.destroy()
    import main

def C_to_F():
    ws.destroy()
    import C_to_F

Label(
    ws,
    text="Convertion from Fahrenheit to Celsius: ",
    font=f,
    padx=20,
    pady=20,
).pack()
input = Entry()
input.pack()

def convertFC():
    temp = float(input.get())
    temp_C = (temp-32)*5/9
    ans['text'] = 'Temperature in Celsius is: '+str(int(temp_C))+'°C'

button = Button(text='Convert', command=convertFC)
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
    text="°C to °F",
    font=f,
    command=C_to_F
).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
