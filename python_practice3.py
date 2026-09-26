import pandas as pd
import numpy as  np
import math as mt

# l1=[10,20,30,40,50]
# l1.sort()

# middle= mt.floor(l1.index(l1[-1])/2)
# # print(middle)m
# print(l1[middle])
nums = (10, 30, 20)
# nums.append(40)
# print(nums)
# nums.extend([50,60])
# print(nums)
# print(nums.remove(20))
# print(nums)
# print(nums.index(30))

# nums.sort()
# nums.reverse()


# a=[10,20,30,20,40,50]
# b=(40,32,45,30,50)
# a=set(a)
# print(a.intersection(b))
# print(a.union(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# numbers=set(numbers)
# print(numbers)
# employees = ["Amit", "Rahul", "Amit", "Gurpreet", "Rahul", "Simran"]
# employee=set(employees)
# print(employee)
# list1 = [1, 2, 3, 4]
# list1=set(list1)
# list2 = [3, 4, 5, 6]
# list2=set(list2)
# lm=list1.union(list2)

# print(lm)
# numbers = [10, 20, 30, 40, 50]
# tp=set(numbers[0:3])
# print(tp)
# a = [1, 2, 3]
# x=a.pop()
# # c=a.copy()
# # c[0]=100
# print(x)
# a=[1, 2, 3, 4, 5]
# d=list(map(lambda x: x*2,a))
# print(d)
# a=["10", "20", "30", "40"]
# a=pd.Series(a)
# i=list(map(lambda x: x,a))
# i=pd.Series(i)
# i=i.astype(int)
# print(i.dtypes)

# x=[10, 15, 20, 25, 30, 35]
# x=list(filter(lambda x:x%2==0,x))
# print(x)

# x=[10, 60, 30, 80, 90, 20]
# x=list(filter(lambda x: x>50,x))
# print(x)

# x=[2, 4, 6, 8]
# x=list(map(lambda x: x**2,x))
# print(x)

# x=["Amit", "Rahul", "Gurpreet", "Simran", "Raj"]
# x=list(filter(lambda x: len(x)>5,x))
# print(x)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num=list(map(lambda x: x**2,filter(lambda x:x%2==0,numbers)))
# print(num)
# num=list(map(lambda x: x**3,filter(lambda x:x%2==0,numbers)))
# print(num)

# num=sum(filter(lambda x:x%5==0,numbers))
# y=0
# for i in range(0,len(num)):
#     y+=num[i]
# print(num)    
# employees = [
#     {"name": "Amit", "salary": 40000},
#     {"name": "Rahul", "salary": 60000},
#     {"name": "Gurpreet", "salary": 70000},
#     {"name": "Simran", "salary": 45000}
# ]
# y=list(filter(lambda x:x["salary"]>50000,employees))
# names=list(map(lambda x:x["name"],y))
# # print(employees)
# # y=[{"name":"Gurp","salary":40000}]
# print(names)
# y=list(filter(lambda x:x["salary"]>50000,employees))
# z=sum(map(lambda x:x["salary"],y))
# print(z)     
# sales = [
#     {"product": "Laptop", "amount": 50000},
#     {"product": "Mouse", "amount": 2000},
#     {"product": "Keyboard", "amount": 3000},
#     {"product": "Monitor", "amount": 15000}
# ]
# y=list(filter(lambda x:x["amount"]>5000,sales))  
# z=sum(map(lambda x:x["amount"],y)) 
# print(z)
# orders = [
#     {"customer": "Amit", "amount": 500},
#     {"customer": "Rahul", "amount": 1500},
#     {"customer": "Gurpreet", "amount": 2500},
#     {"customer": "Simran", "amount": 700}
# ]
# y=list(filter(lambda x:x["amount"]>1000,orders))
# z=list(map(lambda x:x["customer"].upper(),y))
# print(z)     In this particular series we are going now let's see how to create this many people regarding the selection of the team Go up only let's understand how internally how it is working whenever you will upload any files these files will be saved into stages that will under see in the next video but as of now you can understand stage is nothing but a it is kind of the storage location where your files will be checked so this is the file system right these files will be saved into the stages only now after that you are selecting the database where you want to create the table so let's select this let me give the table name where I want to load the data so this database table I have selected now you have loaded a file now what is happening that file is saved into the stages that one of the location you can understand where your file is saved now how internally it is happening we are using a copy into command so we are doing a copy into this table and from where we are reading a data we are reading a data from my status from these stages it is reading where the stuff they want to load the data so this database table I have selected now you have loaded a five now what is happening that file is saved into the stages that one of the location you can understand where your file is shipped now how internally it is happening we are using a copy into command so we are doing a copy into this table and from where we are reading a data we are reading a data from stages from these stages it is reading a data and it is saving the data into the particular table so this is how internally the whole things are working before moving to the next step it's very important to understand the how overall internal things are working right and next video we'll understand about the stage concept there you will get more clarity where we will discuss how the files are being saved and from there how we are doing a copying to the multiple tables and all I hope you got high level idea how internal internally the things are working in a UI when you are using a loaded command so my usage stage how many type of stage we have everything we will write on the same in this video let's start what is the stage file storage location which is used by snow climp store or access the file it was automated location this is a file storage location when I'm saying the file storage location where we store our files where we store our files before loading the data into a snowlet table before loading the data into snublet table just try to understand with one example suppose I have a employee dot CSV file and these files are available to my local this is available in my local I have to do proper conversion of data format integer still have access about your local machine right and how Snowflake will read the data from your local machine so this kind of the challenges for that what I will do first I have to read this file I have to read this pass this file I have to do proper conversion proper date format if a file is located how snow click will know and how Snowflake will file is nothing but the decision file storage location so what we do we first load the date to these stages we first load of these stages we read the data we read the data snow delete the data the data and finally load the data into so stage is nothing but the it is a temporary storage you can say where your files will be stored I will be finally loading the data that your file is located or snow table loading the data snowflake data so for that part I will first I have to read this file I have to read this file how Snowflake will know about your local machine where your file is located how Snowflake will and how Snowflake will have access about your local machine like and how Snowflake will read the data from your local machine so this location so what we do we first load the data we first load the file into this cases we first load the file into stages now from these stages we can finally load the data into so this stages is nothing but it is a file study location where we store the file on a temporary basis welcome to every new support inside the subject files are stored inside the subject only and this store is will be managed by a slope like itself when it is external files are stored container slope but files are stored outside of the slope like cloud is stored in SO ADLS which is below the files will be stored outside of the slot ten and that will be managed by us not by slot so that is the state is nothing but a between the file location that we have a total that we stand up is the files are stored inside the slope and which is managed by the sub itself external means files are stored outside of the snow tip like AWS as a location and that will be managed others discuss one by one internal storage files are storing side manage storage snow type manage is everything we do not have to manage bucket directly now for the internal also we have a three type internal also we have a three type we have the third one is internal stitch but it is a user stage each user automatically get I say user stage you automatically is nothing but five should be able you will create a user right one stage you will alter it you will get one location file install location you will already the file you can store the file so such this user automatically gets one stage we do not have to create the stage for them and how easily you can access this at the rate you will get the stage one stage there you can put the sign and from that stage you can put the data into it so that is the user stage second is the table stage so like the table is table automatically get suit so every table will get one stage every table will have one stage and from that stage it will open file here and from there and how it stage you can see at the repository this is the simple we load you there we'll understand what stage there you can put your files and finally from that file you can reload and put the data input similarly for the table and the table you get one stage that stage actually you can utilize the files there from there you can utilize the data and finally you can put the data now coming to the here we create a magnet here we create a mango stage and this is the material use and the size and finally we will open it data so when you have a multiple files multiple users as it is we understand we have got two type stages only the internal in internal in internal stage storage will inside the same thing and that will be managed by itself we have a file one is user still we use aget one is not able to create that stage actually you can use or store the file and from that stage will that stage will and they will pass the location

# names = ["Amit", "Rahul", "Gurpreet", "Raj", "Simran"]
# A=[ i for i in names if len(i)>4 ]
# print(A)

names = [
    "  gurpreet SINGH  ",
    "AMIT kumar",
    "  rahul SHARMA",
    "Neha   Verma ",
    "PRIYA   singh"
]
# name=tuple(names)
# a,b,c,d,e=name
# a=a.strip()
# a=a.title()
# b=b.strip()
# b=b.title()
# c=c.strip()
# c=c.title()
# d=d.strip()
# d=d.title()
# print(a,b,c,d ,sep=",")
# s=" ".join(names.strip())
# s=s.split(" ")
# # s=s.remove(' ')
# print(s)
# names = [
#     "  gurpreet   singh ",
#     "RAHUL sharma",
#     "  amit   KUMAR",
#     "priya   singh  "
# ]
# n=[]
# for i in names:
#     i=" ".join(i.strip().split())
#     print(i)
#     i=i.title()
#     n.append(i)
# print(n)
# names = [
#     "Gurpreet Singh",
#     "Rahul Sharma",
#     "Amit Kumar"
# ]


# for i in names:
#     i=i.lower().split()
#     i=".".join(i)
#     print(i)

# text = "Py@th#on $is %very &powerful!"
# arr=[]
# for i in text:
#     if i=="@"or i=="#" or i=="%" or i=="&" or i=="!"or i=="$":
#         i=i.replace("%","").replace("@","").replace("#","").replace("&","").replace("!","").replace("$","")
#         arr.append(i)

#     else:
#         arr.append(i)

# txt="".join(arr)  
# print(txt)     





# for i in names:
#     i=i.lower().split()
#     i=".".join(i)
#     print(i)

# numbers = [10, 20, 30]
# for i in numbers:
#     print(i)

# numbers = [10, 20, 30, 40, 50]
# it=iter(numbers)
# # for i in numbers:
    
# print(next(it))
# print(next(it))
# print(next(it))

# class student:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course


# stu1=student("Harpreet",'B.C.A')
# print(stu1.course)

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display_details(self):
#         print("brand: ",self.brand)
#         print("model: ",self.model)

# Audi=car("Q8","2025")

# Audi.display_details()

# class employee:
#     def __init__(self,bonus,salary):
#         self.salary=salary
#         self.bonus=bonus
#     def update_salary(self,amount):
#         self.salary=self.salary+amount
#     def calculate_bonus(self):
#         return self.bonus
#     def display_details(self):
#         print('Salary:',self.salary)
#         print('bonus: ',self.calculate_bonus())


# emp1=employee(3700,37000)
# emp1.display_details()
# emp1.update_salary(1000)
# emp1.display_details()

# class employee:
#     Company="ABC Technology"
#     def __init__(self,bonus,salary):
#         self.bonus=bonus
#         self.salary=salary
#     @classmethod
#     def company_update(cls,company):
#         cls.Company=company
#     @staticmethod
#     def is_valid_comp(salary):
#         return salary>0

# emp1=employee(30000,3000)
# employee.company_update("xyz technology")

# print(employee.Company)
# print(employee.is_valid_comp(-40000))


# class Employee:

#     company = "ABC"

#     def __init__(self, name):
#         self.name = name


# emp1 = Employee("Amit")
# emp2 = Employee("Ravi")

# Employee.company = "XYZ"

# print(emp1.company)
# print(emp2.company)

# class car:
#     wheel=4
#     def __init__(self,brand):
#         self.brand=brand

# Audi=car("Q8")
# print(Audi.wheel)
# print(Audi.brand) 

# class Employee:
#     Company="ABC"
#     def __init__(self,salary):
#         self.salary=salary
#     @classmethod
#     def change_company(cls,company):
#         cls.Company=company
#     @staticmethod
#     def is_even_salary(salary):
#         return salary%2==0
    

# emp1=Employee(50000)
# Employee.change_company("XYZ")
# print(Employee.Company)
# print(emp1.is_even_salary(5000))

# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary


# emp=Employee(5000)
# print(emp.__salary)

# class Employee:
#     def __init__(self,salary):
#         self.salary=salary

#     def deposit(self,amount):
#         self.salary+=amount
#         return self.salary

#     def withdraw(self):
#         if self.salary<0:
#             print("It must be Positive")


# don=Employee(2000)
# print(don.deposit(200))
# print(don.withdraw())

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     @balance.setter
#     def deposit(self,amount):
#         # if amount<0:
#         #     print("amount must be positive:")
#         #     return
#         self.__balance+=amount
#         # print("Balance is deposied")
#         return "Balance is deposied"

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self,amount):
#         self.__balance+=amount


# bacc=BankAccount(2000) 
# print(bacc.deposit(400))
# bacc.set_balance(500)
# print(bacc.get_balance())
# # print(bacc._balance)

# class bankAccount:
#     def __init__(self,balance):
#         self.__balance=balance
#     @property
#     def deposit(self):
#         return self.__balance

#     @deposit.setter
#     def deposit(self,amount):
#         if self.__balance>0:
#             self.__balance+=amount
#             return self.__balance

# asl=bankAccount(3500)
# print(asl.deposit)
# asl.deposit=400
# print(asl.deposit)


# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary

#     @property
#     def fet(self):
#         return self.__salary

#     @fet.setter
#     def ret(self, amount):
#         if amount>0:
#             self.__salary+=amount
       

# dft=Employee(5000)
# dft.ret=400
# print(dft.fet)

# class Employee:
#     def __init__(self,salary):
#         self.__salary=salary

#     def get_salary(self):
#         return self.__salary

#     def set_salary(self,amount):
#         self.__salary+=amount
      

# emp=Employee(3000)
# emp.set_salary(400)
# print(emp.get_salary())

    
# class Person:
#     country='India'
#     def __init__(self,age):
#         if age in range(0,121):
#             self.age=age
#         else:
#             return "Please Enter the valid age"

#     @classmethod
#     def change_country(self,country):
#         self.country=country

# Per=Person(25) 
# print(Per.age)
# Per.change_country("Canada")
# print(Per.country)

#Password Protection

# password=[]
# pa=input("please enter the password in it")
# class user:
#       def __init__(self,pa):
#             hasit=False
#             if pa.isalpha()==True and len(pa)>8:
#                  hasit==True
#                  self.pa=pa
#             else:
#                   return "Please enter the valid password"

# ass=user(pa)
# print(ass.pa)
         

# class product:
#     def __init__(self,price,quantity):
#             self.__price=price
#             self.__quantity=quantity

#     @property
#     def current_inventory(self):
#           return self.__quantity
    
#     @current_inventory.setter
#     def add_stock(self,new_quantity):
#           self.__quantity+=new_quantity

#     @current_inventory.setter
#     def del_quantity(self,new_quantity):
#           self.__quantity-=new_quantity
          
# prosdf=product(2300,6)  
# prosdf.add_stock=2
# prosdf.del_quantity=1   
# print(prosdf.current_inventory)


# class employee:
#     # def __init__(self,name):
#     #     self.name=name
#     def work_wing(self):
#         print("This is not decided yet")
#         pass

#     def work(self):
#         print("Employee work")

# class data_analyst(employee):
#     # def __init__(self,salary):
#     #     self.salary=salary

#     def tools():
#         print("Tools are needed in this")

#     def work(self):
#         super().work()
#         print("data analyst work")

# emp=data_analyst()
# emp.work()

        
# class Employee:
#     def __init__(self,name):
#         self.name=name

#     def sue(self):
#         print("This is the Employee class")

# class Data_analyst(Employee):
#     def __init__(self,name,tools):
#         super().__init__(name)
#         self.tools=tools

#     def sue(self):
#         print("This is the Data analyst")

# class data_enginner(Data_analyst):
#     def __init__(self,name,tools,rmty):
#         super().__init__(name,tools)
#         self.rmty=rmty
# Da=data_enginner("nvjk","Python","ML")
# print(Da.name,Da.tools)
# print(Da.rmty)


# class Employee:
#     def __init__(self,name):
#         self.name=name

# class Data_analyst(Employee):
#     def __init__(self,name,tools):
#         super().__init__(name) 
#         self.tools=tools
           

# rop=Data_analyst("Excel","abc")
# print(rop.name, rop.tools)

# class employee:
#     def __init__(self,name):
#         self.name=name

#     def work(self):
#         print("This is the Employee")


# class f():
#     def work(self):
#         print("This is the f")


# class d(f,employee):
#     pass

# dfo=d("r")
# print(d.mro())



class animal:
    def sound(self):
        print("This is animal sound")

class  dog(animal):
    def sound(self):
        # super().sound()
        print("Dog is Barking")

fp=dog()
print(fp.sound())
