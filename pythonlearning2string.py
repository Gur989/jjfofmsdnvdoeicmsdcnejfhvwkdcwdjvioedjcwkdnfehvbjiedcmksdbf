# firstname="Bavandeep"
# lastname="kaur"
# fullname= firstname +" "+  lastname
# print(firstname+" "+lastname)

# #string indexing
# print(firstname[0])
# print(firstname[-1])

# #slicing
# print(firstname[0:5])
# print(firstname[::-1])


# ### string functions
# print(firstname.upper())
# print(firstname.lower())
# print(firstname.rstrip())
# print(firstname.replace("Bavandeep","nannu"))
# print(len(firstname))  
# print(fullname.split())
# print("kaur" in fullname.lower())

# fullname="bavandeep"
# print(fullname[0].upper()+fullname[1:])
# print("hii")

# sentence="   Data analytics is fun   "
# print(sentence.strip())
# print(len(sentence))


# if else condition
# num=input("please enter the number")
# num=int(num)
# if num>5 and num<50:
#     print("The number goes viral")
# elif num>50:
#     print("The number is out of range")
# else:
#     print("normal number")

# #Ternary
# num1=4
# tname="even" if num1%2==0 else "odd"
# print(tname)

#falsy false,(),{},[],range(0),0,0.0,none,""
#for loops
# for i in range(6):
#     print(i)

# for i in enumerate(range(10,15)):
#     print(i)

# for i,item in enumerate(["a","b","c"]):
#     print(i,item)

# while loop
# num=5
# while num>0:
#     print(num)
#     num-=1

# for i in range(7):
#     if i==5:
#         break
#     print(i)


# for i in range(7):
#     if i==5:
#         continue
#     print(i)

#list comprehension
#[new_value if condition else other_value
 #for variable in iterable]
# redf=["even" if i%2==0 else "odd" for i in range(10)]
# print(redf)

# #list comprehension practice
# numlist=[i for i in range(1,21)]
# print(numlist)

# #list of squares from 1 to 15
# numlist=[i**2 for i in range(1,16)]
# print(numlist)

# from 1 to 30 even number
# even_number=[i for i in range (1,31)  if i%2==0 ]
# print(even_number)

# # from 1 to 30 odd number
# odd_number=[i for i in range (1,30) if i%2!=0]
# print(odd_number)

# divisible_5= [i for i in range(1,100) if i%5==0 ]
# print(divisible_5)

# divisible_3_7=[i for i in range (10) if i %3==0 or i%7==0]
# print(divisible_3_7)

# words = ["python","java","sql","excel"]
# cap=[i.upper() for i in words]
# print(cap)

# fruit=["Apple","Banana","Kiwi","Orange"]
# fruit_list=[len(i) for i in fruit]
# print(fruit_list)

# numbers=[-5,-2,3,8,-1,10]
# numbering=[i for i in numbers if i >0]
# print(numbering)

# Words=["Python","SQL","Machine","AI","Analytics"]
# wording=[i for i  in Words if len(i)>5 ]
# print(wording)

#Remove empty string
# coding=["Python","","SQL","","Excel"]
# code_lang=[ i for i in coding if i!=""]
# print(code_lang)

# letters = list("programming")
# vowel=[en for i in letters for en in i if en in ["a","e","i","o","u"]]
# print(vowel)

#check number
# text="A1B2C3D4"
# dig=[ i for i in text if i.isdigit()]
# print(dig)

# text="P123ython45"
# alph=[i for i in text if i.isalpha()]
# print(alph)


# files=["sales.csv","data.xlsx","employee.csv","ppt.pptx"]
# fi=[ i for i in files if i.find(".csv")>0]
# print(fi)

# lst=[1,2,2,3,4,4,5]
# lst1=[i for i in lst if lst.count(i)==1]
# #print(lst1)
# even=["even" if i%2==0 else "odd" for i in range(10) ]
# print(even)

# lst=[10,20]
# lst.append(30)
# lst.extend([40])
# lst.insert(2,55)
# #lst.remove(30)
# #lst.pop(2)
# lst.sort()
# print(lst)

# lst=[20,40,324,23,44,8]
# max=lst[0]
# for i,val in enumerate(lst):
    
#     if val>max:
#         max=val
# print(max)

lst=[20,40,60,10]
max=lst[0]
#second_largest
for x in lst:
    if max<x:
       sec_max=max
       max=x

print(sec_max)
