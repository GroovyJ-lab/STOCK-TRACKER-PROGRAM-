# -*- coding: utf-8 -*

count = 0
sum = 0

full_name = input("Please enter your full name: ")
min_price = float(input("Please enter the minimum price: "))
price_list = [69, 71, 84, 91, 11, 22, 60, 50, 10, 20]

for i in price_list:
    sum =i + sum  
    if i >min_price: 
        count += 1  
        
print("Hello ", full_name, "the minimum price is ", min_price) 
print("There are", count, "prices greater than the minimum price")
print("The total price is", sum)
 