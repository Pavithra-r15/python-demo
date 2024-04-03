# # string1 ="With!"
# # string2 = "Barefoot on the grass"
# # print(string1.capitalize())
# # print(string1.lower())
# # print(string1.count('e'))
# # print(string2.find('grass'))
# # print('-'.join(string2))
# # print(string1.upper())
# # print(string1.index('i'))
# # #rfind will print end of the letter  from where it has to start searching for a character
# # print(string1.rfind('e'))
# # #strip is for removing backspace and whitespace
# # print(string1.strip())
# # #lstrip is removing left side whitespace
# # print(string1.lstrip())
# # #lstrip is removing right side whitespace
# # print(string1.rstrip())
# # print(len(string1))
# # print(string1.replace("With!", "Baby"))

# # #Calculate the average of number

# # num =[10,20,30,40,50,100,120,790]
# # total = sum(num)
# # average = total/len(num)
# # print(average)

# # country = {
# #     "id" : 1,
# #     "country_name" : "India",
# #     "code" : "+91",
# #     "State" : ["Kerala", "Tamil nadu", "karnataka", "Andhra Pradesh", "Delhi"],
# #      "City" : [{
# #          "id": 1,
# #          "name" : "chennai"
# #      },
# #      {
# #          "id": 2,
# #          "name": "Trivandrum"
# #      },
# #      {
# #          "id": 3,
# #          "name" : "Bangalore"
# #      },{
# #          "id": 4,
# #          "name" : "Chittod"
# #      },{
# #          "id": 5,
# #          "name" : "Delhi"
# #      }]
     
# # }
# # Name="abcd"
# # number=str(1234567890)
# # print(f"My name is {Name} and I'm from {country['City'][0]['name']}, {country['State'][1]}, {country['country_name']} and my mobile number is {country['code']} {number}" )
# # print("My name is",Name, "and I'm from",country['City'][0]['name'],country['State'][1],country['country_name'], "and my mobile number is",country['code'] ,number)
# # print("my name is " +Name+" "+"and I'm from "+country['City'][0]['name']+" "+country["State"][1]+" "+country["country_name"]+" "+"and my mobile number is"+" "+country["code"]+" "+number)

# # a=str(10)  
# # b="20"
# # c=a+" "+b
# # print(c)


# #Calculator application 
# # menus

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# #operation="sub"
# operation=input("Enter operation: ")
# if operation=="add":
#     c=a+b
#     print(c)
# elif operation=="sub":
#     c=a-b
#     print(c)
# elif operation=="mul":
#     c=a*b
#     print(c)
# elif operation=="div":
#     c=a/b
#     print(c)
# elif operation=="mod":
#     c=a%b
#     print(c)
# elif operation=="floor":
#     c=a//b
#     print(c)
# else:
#     print("Invalid Choice")


# Loop and Conditions Task - Python

shopping_cart = {
    "mobile_phone" : "1",
    "ear_phone" : "3",
    "case_cover" : "1",
    "accessories" : "6"
}

price = {
    "mobile_phone" : "19000",
    "ear_phone" : "3500",
    "case_cover" : "350",
    "accessories" : "220"
}


total=0

for item, quantz in shopping_cart.items():
    if item in price:
        total = total +  int(quantz) * int(price[item]) 
        print("Total amount to be paid is Rs.",total,"for the selected items.")


# print total amount of cart items.