class Train:
    railways = "IndianRails"

    def __init__(self, name, seats, fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    
    def getStatus(self):
        print("*******")
        print(f"The train {self.name} is having {self.seats} seats are available for you !")
        L1 = []
        for i in range(1, self.seats+1):
            L1.append(f"TR00{i}")
        print(L1)
        print("*******")
    
    def cancelTicket(self,seats, b):
        self.seats=seats
        self.b=f"TR00{b}"
        print(f'Your ticket number :{self.b} is successfully cancelled')
        L1 = []
        for i in range(1, self.seats+1):
            L1.append(f"TR00{i}")
        L1.remove(self.b)
    
    def bookMyTrip(self, seat):
        self.seat=seat
        for i in range(self.seat+1):
            if (self.seat!=0):
                print(f"Your seat successfully booked!!\nYour seat number is  TR00{self.seats}")
                self.seat=self.seat-1
                self.seats=self.seats-1
            elif self.seat>self.seats:
                print("Sorry this train is full! Kindly try in tatkal")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")



intracity = Train("Raajdhani Express", 5, 1500)
# intracity.getStatus()
intracity.fareInfo
intracity.bookMyTrip(6)
intracity.cancelTicket(5, 3)
intracity.getStatus()
 
    