from tkinter import *
def key_press(event):
    print(f"{event.char}")

def mouse_press(event):
    print({event.x},{event})

def next_widget(event):
    event.widget.tk_focusNext().focus()

window = Tk()
window.geometry("400x400")
Entry(window).pack()
Entry(window).pack()

window.bind("<Key>", key_press) #<Return>
window.bind("<Button-1>", mouse_press) #мышь
window.bind("<Motion>", mouse_press) #<Button-3> 
window.bind("<Tab>", next_widget)

window.mainloop()
