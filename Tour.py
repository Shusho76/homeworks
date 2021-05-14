import random
class Hotel:
    def __init__(self, hotel_name, place, mid_rooms, mid_price, lux_room, lux_price):
        
        self.hotel_name = hotel_name 
        self.place = place
        self.dict_mid = {}
        for key in mid_rooms:
            self.dict_mid[key] = random.choice("AB") # A is for "Available" , "B" is for "Bisy"
        self.mid_price = mid_price
        self.lux_room = lux_room
        self.dict_lux = {}
        for key in lux_room:
           self.dict_lux[key] = "A"
        self.lux_price = lux_price
       
               
    def presentation_hotel(self):
        return F"Our hotel's name is {self.hotel_name}, it is in {self.place}. It has 5 mid_rooms {self.dict_mid} and 3 lux_room {self.dict_lux}, prices for mid-rooms {self.mid_price} and for lux {self.lux_price}"
    
    def booking_room (self, booking, booking_number):
        self.booking = booking
        self.booking_number = booking_number
        if self.booking == "mid_rooms":

            for x in self.dict_mid[booking_number]:

                if x == "A": 
                    print("Yes,this room is free, you can book: Welcome to our hotel")
                    self.dict_mid[booking_number] = "B"
                    print(self.dict_mid)
                else:
                    print("Choose another one, this room is bisy")   
                    print(present_hotel.booking_room(input("Choose room type\n"),input("Choose room\n")))

        elif self.booking == "lux_room":

            for x in self.dict_lux[booking_number]:
                
                if x == "A":
                    print("Yes,this room is free, you can book: Welcome to our hotel")
                    self.dict_lux[booking_number] = "B"
                    # print(self.dict_lux)
                else:
                    print("Choose another one, this room is bisy")   
                    print(present_hotel.booking_room(input("Choose room type\n"),input("Choose room\n")))            
        else:
            print("We have no such kinde of room. Choose another one")
            print(present_ho1tel.booking_room(input("Choose room type\n"),input("Choose room\n"))) 


    def available_rooms_chek(self):
        D = self.dict_mid
        B = self.dict_lux
        A = (list(D.values()).count("A"))
        C = (list(B.values()).count("A"))
        if  A!=0:
            print("We have ", A , "available mid_rooms ")
        if  C!=0:
            print("We have ", C , "available lux_room ")
        else:
            print("No, we have no any available rooms")

    def discount_hotel(self): 
        return F"We have discount - 20 percent for mid_rooms and 30 persent for lux_room for just merried couple.You can book mid_rooms for {self.mid_price - (self.mid_price*20/100)} and lux_room for {self.lux_price - (self.lux_price*30/100)}"       
  
class Taxi:
    def __init__(self,taxi_name, car_type, price_for_tour):
        self.taxi_name = taxi_name
        self.car_type = car_type
        self.price_for_tour = price_for_tour

    def presentation_taxi(self):
        return F"Our taxi service called {self.taxi_name}. Our cars very comfortabl {self.car_type}. Tours cost {self.price_for_tour}drams for one km."    
    def discount_taxi(self):
        return F"Taxi {self.taxi_name} have discount for tours from 50 km."
class Tour(Hotel,Taxi):
    def __init__(self, tour_name, distination , hotel_name, place, mid_rooms, mid_price, lux_room, lux_price, taxi_name, car_type, price_for_tour):
        self.tour_name = tour_name
        self.distination = distination
        Hotel.__init__(self,hotel_name, place, mid_rooms, mid_price, lux_room, lux_price)
        Taxi.__init__(self,taxi_name, car_type, price_for_tour)
    
    def presentation_tour(self):
        return F"Welcomе to our {self.tour_name} tour company. We offer very interesting tour to {self.place}.Our tour have two kind of prices for one person - wich include transport and hotel mid_price {self.mid_price + self.distination*self.price_for_tour}  and lux_price {self.lux_price + self.distination*self.price_for_tour}. We travel in comfortable cars {self.car_type} of {self.taxi_name} taxi service: In {self.place}\
we stay in {self.hotel_name} hotel wich have two types of rooms mid_rooms {self.mid_price} and lux_room {self.lux_price}." 
present_hotel = Hotel("Liliana", "Dilijan", ("room01", "room02","room03", "room04","room05"), 10000, ("room01", "room02", "room03"), 30000)  
print(present_hotel.presentation_hotel())     
print(present_hotel.booking_room(input("Choose room type\n"),input("Choose room\n")))
print(present_hotel.available_rooms_chek())
print(present_hotel.discount_hotel())
print("\n\n")
present_taxi = Taxi("Luna",("BMW", "Opel","Mersedes"), 100)
print(present_taxi.presentation_taxi())
print(present_taxi.discount_taxi())
print("\n\n")
present_tour = Tour("Enjoy", 30 , "Liliana", "Dilijan", ("room01", "room02","room03", "room04","room05"), 10000, ("room01", "room02", "room03"), 30000, "Luna", ("BMW" , "Opel" , "Mersedes"),100)
print(present_tour.presentation_tour())