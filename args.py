# Difference between parameter and arguments
# function is a set code which makes the code easier. we can use that similar code by passing different
# arguments at multiple times.

def making_pizza(flavour):
    print(flavour,"pizza")

making_pizza("cheese") 

#Parameter functions
def making_food(item="Paneer"):
    print("Kadai",item)
    # default arguments
making_food("mashroom")

# Multiple arguments
# It stores arguments as tuples

def number(*args):
    print(args)
number(2,3,45,9)



#Lambda function
max=lambda a,b: "a is maximum" if(a>b) else "b is maximum"
print(max)

#Area of circle
area=lambda r: 3.14*r**2
print(area(2))

# map(function,var)
freinds=["Arun","Garur","Karan"]
rmn=map(lambda x: x.upper(),freinds)
print(list(rmn))

#filter(function,number)
num=[20,34,99,341,33,56]
numb=filter(lambda x: x%2==0,num)
print(list(numb))

#odd number
num=[32,33,89,67,5476,789]
numodd=filter(lambda x: x%2!=0,num)
print(list(numodd))

#number >50
num=[32,324,23442,23,343]
numgreater50=filter(lambda x: x>50,num)
print(list(numgreater50))

#string greater than 5 charaters
vvvar=["dfko","dnsjin","dkff","dskds"]
strgrt50=filter(lambda x: len(x)>5 ,vvvar)
print(list(strgrt50))


#args
def jinks(*nums):
    return sum(nums)
print(jinks(6,7,8,9))

#kwars
def nms(**ui):
    return ui
print(nms(name="dsjfhsi",Rollno=23,short_name="sddf"))