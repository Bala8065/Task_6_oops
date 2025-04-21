#1. Problem 1 : Bank account 
#Create a base class bank account with attributes like account number, balance, and methods like deposit()a and withdraw(). Inherit from this class to create subclasses saving account and current account. The saving account should have an interest rate and a method to calculate interest. The current account should have a minimum balance requirement. Implement encapsulation to protect the account balance and ensure that withdrawals cannot exceed the balance or minimum balance requirements. 

class BankAccount:
    def __init__(self, account_number, initial_balance=0.0):
        self.account_number = account_number
        self.__balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


class SavingAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0.0, interest_rate=0.02):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest earned: {interest}")
        return interest


class CurrentAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0.0, minimum_balance=500.0):
        super().__init__(account_number, initial_balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount > 0 and self.get_balance() - amount >= self.minimum_balance:
            # Use base class withdraw
            super().withdraw(amount)
        else:
            print(f"Withdrawal denied. Balance must not fall below minimum balance of {self.minimum_balance}.")


# Example usage:
print("=== Saving Account ===")
savings = SavingAccount("SA123", 1000.0, 0.05)
savings.deposit(500)
savings.withdraw(200)
savings.calculate_interest()

print("\n=== Current Account ===")
current = CurrentAccount("CA456", 1000.0, 300.0)
current.deposit(200)
current.withdraw(950)  # Should be denied
current.withdraw(700)  # Should be allowed

#2. Problem 2: Employee management 
#Create a base class employee with attributes like name salary and a method calculate salary(). Inherit from this class to create subclasses regular employee,Contract employee and manager.Each subclass should have specific attributes and calculations for salary Implement inheritance and polymorphism to calculate the salary of different employee types based on their specific attributes and rules

class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        # Base method to be overridden
        return self.base_salary


class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)  # No base salary for contract employees
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Manager(Employee):
    def __init__(self, name, base_salary, allowance, bonus_percent):
        super().__init__(name, base_salary)
        self.allowance = allowance
        self.bonus_percent = bonus_percent  # percentage of base salary

    def calculate_salary(self):
        bonus = self.base_salary * self.bonus_percent
        return self.base_salary + self.allowance + bonus


# Polymorphic salary calculation
def print_employee_salary(employee):
    print(f"{employee.name}'s total salary: {employee.calculate_salary()}")


# Example usage:
regular = RegularEmployee("Alice", 50000, 5000)
contract = ContractEmployee("Bob", 100, 160)  # hourly rate * hours
manager = Manager("Charlie", 80000, 10000, 0.1)

print_employee_salary(regular)
print_employee_salary(contract)
print_employee_salary(manager)

#3. Problem 3: Vehicle rental 
#Create a base class vehicle with attributes like model,rental_rate and a method calculate_rental(). Inherit from this class to create subclasses car,Bike and Truck. Each subclass should have specific attributes and calculations for rental rates.implement polymorphism to calculate The rental cost of different vehicles based on their type and rental duration   

class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate  # base rate per day

    def calculate_rental(self, days):
        return self.rental_rate * days


class Car(Vehicle):
    def __init__(self, model, rental_rate, luxury_tax=0.10):
        super().__init__(model, rental_rate)
        self.luxury_tax = luxury_tax  # 10% extra for luxury cars

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        tax = base_cost * self.luxury_tax
        return base_cost + tax


class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_fee=20):
        super().__init__(model, rental_rate)
        self.helmet_fee = helmet_fee  # flat fee

    def calculate_rental(self, days):
        return super().calculate_rental(days) + self.helmet_fee


class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_fee_per_ton=50, load_tons=1):
        super().__init__(model, rental_rate)
        self.load_fee_per_ton = load_fee_per_ton
        self.load_tons = load_tons

    def calculate_rental(self, days):
        base_cost = super().calculate_rental(days)
        load_fee = self.load_fee_per_ton * self.load_tons
        return base_cost + load_fee


# Polymorphic function to print rental cost
def print_rental(vehicle, days):
    print(f"{vehicle.model} rental for {days} days: {vehicle.calculate_rental(days)}")


# Example usage
car = Car("BMW 5 Series", 100, luxury_tax=0.15)
bike = Bike("Yamaha R15", 30)
truck = Truck("Volvo Truck", 200, load_fee_per_ton=75, load_tons=3)

print_rental(car, 5)    # Car rental with luxury tax
print_rental(bike, 3)   # Bike rental with helmet fee
print_rental(truck, 2)  # Truck rental with load fee
