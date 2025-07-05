#25 questions based on def function

#ans1
def numb(a):
    if a % 2 == 0 :
        print('yes it is even ')
    else:
        print('it is odd')
numb(2) 

#ans2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(0))


#ans3
def reverse_string(s):
    return s[::-1]
print(reverse_string("dev"))  

#ans4
def check(strin):
    if (strin==strin[::1]):
        print(f'yes it is palindrome!')
    else:

        print('not a palindrome')
check('madam')    

#ans5
def maxim(a,b,c):
    if(a>b and a>c):
        print(f'yes (a) is maximum number')
    elif (b>a and b>c):
        print(f'yes (b) is maximum number')  
    else:
         print(f'yes (c) is maximum number')     
maxim(5,7,9)         


#ans6
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    return count
stra=input("enter the string:")
vow=count_vowels(stra)
print ("number of vowels :",vow)


#ans7
def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))

#ans8
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci_recursive(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
terms = int(input("Enter number of terms: "))
result = fibonacci_recursive(terms)
print("Fibonacci series:", result)



#ans9
import math

def find_gcd(a, b):
    return math.gcd(a, b)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD is:", find_gcd(x, y))


#ans10
def is_prime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#ans11
def square(a):
    return a ** 2

def cube(a):
    return a ** 3

num = int(input("Enter a number: "))
print("Square:", square(num))
print("Cube:", cube(num))

#ans12
def leap_year(a):
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print("The year is a leap year.")
    else:
        print("The year is not a leap year.")
year = int(input("Enter a year: "))
leap_year(year)

#ans13
def find_largest(lst):
    if not lst:
        return None  
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
numbers = [10, 45, 23, 89, 3]
print("Largest element:", find_largest(numbers))

 
#ans14
def char(s):
    count = 0
    for i in s:
        count += 1
    return count

stra = input("Enter the string: ")
view = char(stra)
print("Number of characters:", view)


# ans15
def merge_lists(list1, list2):
    return list1 + list2
a = [1, 2, 3]
b = [4, 5, 6]
merged = merge_lists(a, b)
print("Merged list:", merged)

#ans16
def custom_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
numbers = [5, 2, 9, 1, 3]
sorted_list = custom_sort(numbers)
print("Sorted list:", sorted_list)


#ans17
def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
print("Duplicates:", find_duplicates(numbers))

#ans18
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
text = input("Enter a string: ")
result = char_frequency(text)
print("Character frequencies:", result)

#ans19
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

result = simple_interest(p, r, t)
print("Simple Interest is:", result)


#ans21
def get_even_numbers(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = get_even_numbers(numbers)
print("Even numbers:", evens)




#ans22
def to_binary(n):
    return bin(n)[2:]  
num = int(input("Enter a number: "))
binary = to_binary(num)
print("Binary equivalent:", binary)

#ans23
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5 is:", factorial(5))


#ans24
def second_largest(lst):
    unique_list = list(set(lst))  # remove duplicates
    if len(unique_list) < 2:
        return None
    unique_list.sort()
    return unique_list[-2]
print("Second largest:", second_largest([10, 20, 4, 45, 99, 99]))


#ans25
def is_sorted(lst):
    return lst == sorted(lst)
print("Is the list sorted?", is_sorted([1, 2, 3, 4]))  
print("Is the list sorted?", is_sorted([1, 3, 2]))    







# oops 15 questions 
#ans1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
p1 = Person("Alice", 25)
p1.display()


#ans2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
r1 = Rectangle(4, 5)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())


#ans3  
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_grade(self):
        print(f"{self.name}'s Grade: {self.grade}")
s1 = Student("Bob", "A+")
s1.display_grade()

#ans4
class PrivateExample:
    def __init__(self):
        self.__secret = "This is private"

    def show_secret(self):
        print("Secret:", self.__secret)
p = PrivateExample()
p.show_secret()

#ans5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.show_balance()

#ans6
class Person:
    def __init__(self, name, age, city):
        # Initializing attributes
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
p1 = Person("Alice", 24, "Delhi")
p1.display_info()


#ans7
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")
d = Dog()
d.sound()
d.bark()

#ans8
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")
obj = C()
obj.showA()
obj.showB()
obj.showC()


#ans9
class Demo:
    count = 0

    @staticmethod
    def greet():
        print("Hello from static method")

    @classmethod
    def show_count(cls):
        print("Count:", cls.count)
Demo.greet()
Demo.show_count()

#ans10
class Point:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Point(self.value + other.value)

    def __str__(self):
        return f"Point: {self.value}"
p1 = Point(5)
p2 = Point(10)
p3 = p1 + p2
print(p3)


#ans11
class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    def speak(self):
        print("Child speaking (overridden)")
c = Child()
c.speak()


#ans12
class ParentSuper:
    def __init__(self):
        print("Parent constructor")

class ChildSuper(ParentSuper):
    def __init__(self):
        super().__init__()
        print("Child constructor")
cs = ChildSuper()



#ans13
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        print("Object count:", cls.count)
a = Counter()
b = Counter()
c = Counter()
Counter.get_count()



#ans14
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"
book = Book("Python 101")
print(book)


#ans15
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus
m = Manager("Dev", 50000, 10000)
print("Manager Salary:", m.get_salary())
