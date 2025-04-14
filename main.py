#﻿Name: Balakumar
#Email: bala8065@gmail.com
#Phno: 9790816791
#Batch code: PAT-C-WE-E-B7


#Oops Task


#1. Problem 1 : Bank account 
#Create a base class bank account with attributes like account number, balance, and methods like deposit()a and withdraw(). Inherit from this class to create subclasses saving account and current account. The saving account should have an interest rate and a method to calculate interest. The current account should have a minimum balance requirement. Implement encapsulation to protect the account balance and ensure that withdrawals cannot exceed the balance or minimum balance requirements. 


# Python program to create Bankaccount class


# with both a deposit() and a withdraw() function


class Bank_Account:
def __init__(self):
                                self.balance=0
                                print("Hello!!! Welcome to the Deposit & Withdrawal Machine")


                        def deposit(self):
                                amount=float(input("Enter amount to be Deposited: "))
                                self.balance += amount
                                print("\n Amount Deposited:",amount)


                        def withdraw(self):
                                amount = float(input("Enter amount to be Withdrawn: "))
                                if self.balance>=amount:
                                        self.balance-=amount
                                        print("\n You Withdrew:", amount)
                                else:
                                        print("\n Insufficient balance ")


                        def display(self):
                                print("\n Net Available Balance=",self.balance)


# Driver code


# creating an object of class
s = Bank_Account()


# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()






#2. Problem 2: Employee management 
#Create a base class employee with attributes like name salary and a method calculate salary(). Inherit from this class to create subclasses regular employee,Contract employee and manager.Each subclass should have specific attributes and calculations for salary Implement inheritance and polymorphism to calculate the salary of different employee types based on their specific attributes and rules
class Employee:
   def __init__(self, name, base_salary):
       self.name = name
       self.base_salary = base_salary


   def calculate_salary(self):
       return self.base_salary


   def __str__(self):
       return f"{self.name}: ${self.calculate_salary():.2f}"


class RegularEmployee(Employee):
   def __init__(self, name, base_salary, benefits=0.1):
       super().__init__(name, base_salary)
       self.benefits = benefits  # e.g., 10% of base salary


   def calculate_salary(self):
       return self.base_salary + (self.base_salary * self.benefits)


class ContractEmployee(Employee):
   def __init__(self, name, hourly_rate, hours_worked):
       super().__init__(name, base_salary=0)  # No base salary
       self.hourly_rate = hourly_rate
       self.hours_worked = hours_worked


   def calculate_salary(self):
       return self.hourly_rate * self.hours_worked


class Manager(Employee):
   def __init__(self, name, base_salary, bonus=0):
       super().__init__(name, base_salary)
       self.bonus = bonus


   def calculate_salary(self):
       return self.base_salary + self.bonus


employees = [
   RegularEmployee("Alice", 5000),
   ContractEmployee("Bob", 50, 160),
   Manager("Charlie", 8000, 2000)
]


for emp in employees:
   print(emp)

#3. Problem 3: Vehicle rental 
#Create a base class vehicle with attributes like model,rental_rate and a method calculate_rental(). Inherit from this class to create subclasses car,Bike and Truck. Each subclass should have specific attributes and calculations for rental rates.implement polymorphism to calculate The rental cost of different vehicles based on their type and rental duration   


class Vehicle:
   def __init__(self, model, rental_rate):
       self.model = model
       self.rental_rate = rental_rate  # Rate per day


   def calculate_rental(self, days):
       return self.rental_rate * days  # Default calculation


   def __str__(self):
       return f"{self.model} Rental Cost: ${self.calculate_rental(1):.2f} per day"


class Car(Vehicle):
   def __init__(self, model, rental_rate, insurance_fee=20):
       super().__init__(model, rental_rate)
       self.insurance_fee = insurance_fee  # Extra charge for cars


   def calculate_rental(self, days):
       return (self.rental_rate * days) + (self.insurance_fee * days)


class Bike(Vehicle):
   def __init__(self, model, rental_rate, discount=0.1):
       super().__init__(model, rental_rate)
       self.discount = discount  # Discount for long rentals


   def calculate_rental(self, days):
       total_cost = self.rental_rate * days
       if days > 5:  # Discount applies if rented for more than 5 days
           total_cost *= (1 - self.discount)
       return total_cost


class Truck(Vehicle):
   def __init__(self, model, rental_rate, load_fee=50):
       super().__init__(model, rental_rate)
       self.load_fee = load_fee  # Additional fee for truck rentals


   def calculate_rental(self, days):
       return (self.rental_rate * days) + self.load_fee


# --- Example Usage ---
vehicles = [
   Car("Toyota Camry", 50),
   Bike("Yamaha R15", 15),
   Truck("Ford F-150", 100)
]


rental_days = 7  # Example duration


for vehicle in vehicles:
   print(f"{vehicle.model} Rental Cost for {rental_days} days: ${vehicle.calculate_rental(rental_days):.2f}")
