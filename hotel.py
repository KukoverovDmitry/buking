import os
os.system("cls")    
from tkinter import *
from tkinter import messagebox as mb


def book_seats(event=None):
    s = seat_entry.get() #input("Введите место для бронирования (от Б1 до Б9)")
    try:
        if seats[s] == "свободно":
            seats[s] = "забронировано"
            update_canvas()
            mb.showinfo(title="Успешно", message=   f"Место {s} успешно забронировано")
               
        else:
            mb.showinfo(title=f"Место", message=f"  {s} уже забронировано или не существует")
                        
    except KeyError:
        print(f" Место {s} не существует")
        return book_seats(seats)

def cancel_seats(event=None):
    s = cancel_entry.get() #input("Введите место для бронирования (от Б1 до Б9)")
    try:
        if seats[s] == "забронировано":
            seats[s] = "свободно"
            update_canvas()
            mb.showinfo(title="Успешно", message=   f"Место {s} успешно отмененана бронь")
               
        else:
            mb.showinfo(title=f"Место", message=f"  {s} уже забронировано или не существует")
                        
    except KeyError:
        print(f" Место {s} не существует")
        return book_seats(seats)
    
seats = {f"Б{i}": "свободно" for i in range (1,10)}

def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x,y,x +30, y + 30, fill=color)
        canvas.create_text(x+15, y+10 , font="Arial 10", text=seat)    






window = Tk()
window.title("Бронирование мест")
window.geometry("500x400")


canvas = Canvas(window, width=400, height=80   )
canvas.pack()
canvas.create_rectangle(20,20,50,50, fill="green")
canvas.create_text(100, 10, text="Свободно")

canvas2 = Canvas(window, width=400, height=80   )
canvas2.pack()
canvas2.create_rectangle(20,20,50,50, fill="red")
canvas2.create_rectangle(200,20,230,50, fill="green")
canvas2.create_text(100, 35, text="Свободно", font="Arial 15")
canvas2.create_text(320, 35, text="Забронировано", font="Arial 15")


seats = {f"Б{i}": "свободно" for i in range (1,10)} #создание словаря - места и их статуса

update_canvas()

seat_entry = Entry(window, width=10)
seat_entry.pack(pady=10)
seat_entry.focus()
seat_entry.bind("<Return>", book_seats)
Button(window, text="Забронировать место", command=lambda: book_seats(seats)).pack(pady=10)

cancel_entry = Entry(window, width=10)
cancel_entry.pack(pady=10)
cancel_entry.bind("<Return>", cancel_entry)

Button(window, text="Отменить бронь", command=lambda: cancel_seats(seats)).pack(pady=10)


window.mainloop()


