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
    
       
        



seats = {f"Б{i}": "свободно" for i in range (1,10)}
#print(seats)

# while True:
#     book_seats(seats)
#     booking = input("Хотите еще одно место забронировать? (да/нет)")
#     if booking.lower() != "да":
#         break

# print("Итоговое состояние бронирования мест")
# for  i , (seat, status) in enumerate(seats.items()):
#     print(f"{i+1}.  {seat}: {status}")

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
window.geometry("400x200")

canvas = Canvas(window, width=400, height=80   )
canvas.pack()
seats = {f"Б{i}": "свободно" for i in range (1,10)}

update_canvas()

seat_entry = Entry(window, width=10)
seat_entry.pack(pady=10)

Button(window, text="Забронировать", command=lambda: book_seats(seats)).pack(pady=10)

window.mainloop()


