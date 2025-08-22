#print(seats)

# while True:
#     book_seats(seats)
#     booking = input("Хотите еще одно место забронировать? (да/нет)")
#     if booking.lower() != "да":
#         break

# print("Итоговое состояние бронирования мест")
# for  i , (seat, status) in enumerate(seats.items()):
#     print(f"{i+1}.  {seat}: {status}")


from tkinter import *

window = Tk()
window.geometry("400x400")
# def update_canvas():
#     canvas.delete("all")
#     for i, (seat, status) in enumerate(seats.items()):
#         x = i * 40 + 20
#         y = 20
#         color = "green" if status == "свободно" else "red"
#         canvas.create_rectangle(x,y,x +30, y + 30, fill=color)
#         canvas.create_text(x+15, y+10 , font="Arial 10", text=seat)  





canvas2 = Canvas(window, width=400, height=80   )
canvas2.pack()
canvas2.create_rectangle(20,20,50,50, fill="red")
canvas2.create_rectangle(200,20,230,50, fill="green")
canvas2.create_text(100, 35, text="ЗАНЯТО", font="Arial 15")
canvas2.create_text(280, 35, text="ЗАНЯТО", font="Arial 15")






window.mainloop()

