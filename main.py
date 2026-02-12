class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.free = True

    def book(self):
        if self.free:
            self.free = False
            return True
        return False

    def release(self):
        self.free = True


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        print("\nBo'sh xonalar:")
        for r in self.rooms:
            if r.free:
                print(f"Xona {r.number} | Narx: {r.price}")

    def book_room(self, number):
        for r in self.rooms:
            if r.number == number and r.free:
                r.book()
                print("Xona bron qilindi!")
                return
        print("Xona band yoki mavjud emas!")


hotel = Hotel("Grand Tashkent")

for i in range(1, 11):
    hotel.add_room(Room(i, 150000 + i * 10000))

while True:
    print("\n1. Xonalar")
    print("2. Bron qilish")
    print("3. Chiqish")
    c = input(">>> ")

    if c == "1":
        hotel.show_rooms()
    elif c == "2":
        num = int(input("Xona raqami: "))
        hotel.book_room(num)
    elif c == "3":
        break
