from  tkinter import *
import time
def calculate(event):
    text = event.widget.cget("text")
    if text == "=":
        if calVal.get().isdigit():
            value = int(calVal.get())
        else:
            try:
               value = eval(calValen.get())
            except Exception as err:
                value  = "Error"
                calVal.set(value)
                calValen.update()
                time.sleep(1)
                value = ""
        calVal.set(value)
        calValen.update()
    elif text == "C":
        calVal.set("")
        calValen.update()
    elif text == "←":
        val = calVal.get()
        setVal = val[: len(val)-1]
        calVal.set(setVal)
        calValen.update()
    else:
        calVal.set(calVal.get()+text)


root = Tk()
root.title("Calculator")
root.geometry("600x600")
root.minsize(400,400)
root.maxsize(500,500)

inputFrame = Frame(root)
inputFrame.grid(pady=10, padx=7)

calVal = StringVar()

calValen = Entry(inputFrame, fg= "white", bg= "black", font="Helvetica 18 bold", width=37, textvariable= calVal)

calValen.grid(row =1 , column=1, ipady =10)

keyboardFrame = Frame(root, bg = "black")
keyboardFrame.grid(row= 2, column=0)

symbolBtns = ["C","=", "/", "*","-" ,"+", ".", "0", "←"]
btnCount = len(symbolBtns)-1
print(btnCount)
btn = 9
for row in range(6):
    for col in range(3):
        if btn not in symbolBtns and btn > 0:
             Btn = Button(keyboardFrame, padx= 27, text =f"{btn}", font = "Helvetica", width= 4, height = 1, fg ="dark green", bg="white")
             Btn.grid(row=row, column=col, padx= 19, pady=19)
             Btn.bind("<Button-1>", calculate)
             btn = btn-1
        else:
             Btn = Button(keyboardFrame, padx=27, text=f"{symbolBtns[btnCount]}", font="Helvetica", width=4, height=1, fg="dark green", bg=
             "white")
             Btn.grid(row=row, column=col, padx=19, pady=19)
             Btn.bind("<Button-1>", calculate)
             btnCount = btnCount - 1

root.mainloop()