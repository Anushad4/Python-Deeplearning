import random

class Flight:
    def __init__(self, airline_name, flight_number):                                        #Default constructor for flight class
        self.airline_name = airline_name
        self.flight_number = flight_number

    def flight_display(self):                                                               #Displaying flight details
        print('Airlines : ', self.airline_name)
        print('Flight number : ', self.flight_number)


class employee:                                                                             #eloyee class
    def __init__(self, e_id, e_name, e_age, e_gender):                              #eloyee class constructor
        self.e_name = e_name
        self.e_age = e_age
        self.__e_id = e_id
        self.e_gender =  e_gender
    def e_display(self):                                                            #Displaying eloyee details
        print("Name of employee: ",self.e_name)
        print('employee id: ', self.__e_id)
        print('employee age: ',self.e_age)
        print('employee gender: ', self.e_gender)

class Passenger:                                                                            #Passenger class
    def __init__(self):
        Passenger.__passport_number = input("Enter the passport number of the passenger: ") #Passport number is declared as private data member
        Passenger.name = input('Enter name of the passenger: ')
        Passenger.age = input('Enter age of passenger : ')
        Passenger.gender = input('Enter the gender: ')
        Passenger.class_type = input('Select business or economy class: ')

class Baggage():                                                                            #Baggage class
    cabin_bag = 1
    bag_fare = 0
    def __init__(self, checked_bags):
        self.checked_bags = checked_bags
        if checked_bags > 2 :                                                               #Calculating the cost if there are more than two cabin bags
            for i in checked_bags:
                self.bag_fare += 100
        print("Number of checked bags allowed: ",checked_bags,"bag fare: ",self.bag_fare)


class Fare(Baggage):                                                                        #Fare class which is subclass of Baggage
    counter = 150                                                                           #Cost is fixed for purchasing at counter
    online = random.randint(110, 200)                                                       #Cost varies with ticket is purchased through online and fair is generated through random function
    total_fare=0
    def __init__(self):
        super().__init__(2)                                                                 #Super call
        x = input('Buy ticket through online or counter: ')
        if x == 'online':
            Fare.total_fare = self.online + self.bag_fare
        elif x == 'counter':
            Fare.total_fare = self.counter + self.bag_fare
        else:
            x=input('Enter correct transaction type:')
        print("Total Fare before class type: ",Fare.total_fare)


class Ticket(Passenger, Fare):                                                             #Multiple inheritence
    def __init__(self):
        print("Passenger name:",Passenger.name)                                            #Acccessing parent class variable
        if Passenger.class_type == "business":
            Fare.total_fare+=100
        else:
            pass
        print("Passenger class type:",Passenger.class_type)
        print("Total fare:",Fare.total_fare)                                              #Displaying total fair for itenary


f1=Flight('American Airlines',6789)
f1.flight_display()

e0 = employee('e1', 'e_Anu', 21, 'F')
e0.e_display()

p1 = Passenger()

fare1=Fare()

t= Ticket()