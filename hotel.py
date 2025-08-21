import os
os.system("cls")    

def book_seats(seats):
    s = input("Введите место для бронирования (от Б1 до Б9)").lower()
    if seats[s] == "свободно":
        seats[s] = "забронировано"
        print(f"Место {s} успешно забронировано")
    else:
        print(f"Место {s} уже забронировано или не существует")
        



seats = {f"Б{i}": "свободно" for i in range (1,10)}
print(seats)
while True:
    book_seats(seats)
    booking = input("Хотите забронировать? (да/нет)")
    if booking.lower() != "да":
        break

print("Итоговое состояние бронирования мест")
for  i , (seat, status) in enumerate(seats.items()):
    print(f"{i}.  {seat}: {status}")
    
print("Программа завершена" )

