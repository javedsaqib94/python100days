import random



# def getName (name):
#     newname = name
#     length = len(newname)
#     print(f"name is {newname} and the length of the name is {length}" )


# getName(input("what is your name? "))


# city_name = input("What's the name of the city you grew up in? \n")
# pet_name = input ("what is you name? \n")

# print("Your band name could be " + city_name + " " + pet_name + "\n")

# mystery = 734_529.678
# print(type(mystery))
# print(mystery)

# print(len("12345"))


# #### TIP CALCULATOR EXCERCISE ####
# print("\n Welcome to the  \btip calculator! \n")

# total_bill =  float(input ("What was the total bill?  $"))
# tip_paid =  int(input ("How much % tip would you like to give? 10, 12 or 15? "))
# total_people =  int(input ("How many people to split the bill? "))



# print(type(total_bill))
# print(type(tip_paid))
# print(type(total_people))

# tip_in_percent = ( total_bill / 100 ) * tip_paid 

# print(f"Calculated tip on your bill is: $ {tip_in_percent}")

# calculation_in_total = round (((total_bill + tip_in_percent) / total_people) , 2)


# print(f"Each person should pay: {calculation_in_total}")

# input_number = int(input ("Enter you number here: "))

# if input_number % 2 == 0:
#     print(input_number)
#     print("You have typed an even number")
# else:
#     print(input_number)
#     print("You have typed an odd number")

##### Generate random numbers ## import random  ##  to user

# random_num = random.randint(1,23)
# print(random.randint(1,23))   ## generate random integers
# print(random.random())   ## no arguments to add (from 0 but not included 1 in it) (cannot include upper bound)
# print(random.uniform(0,3))   ## from 0 to 3 (can include upper bound)

##### Heads and tails program with random numbers:

# random_input  =  random.randint(1,10)

# if random_input % 2 == 0:
#     print('Heads')
# else:
#     print('Tails')


###########LISTS#########
######### Generate a random name out of all 6 friends #############

# friends = ["John", "Matt", "Malik", "Ali", "Nadir", "Arsalan"]
# random_choice = random.randint(0,5)


# print(friends[random_choice])

# print(random.choice(friends)) #### build-in function for random list item reterival 


############ FIND OUT MAX number from the list ###########

# numbers = [1,2,33,4,25,6,57,43,98,0]
# print(type(numbers))

# sum = 0
# max = 0
# for x in numbers:
#     sum += x
#     if x > max:
#         max = x
#         print(numbers)  ## list printing
#         print(f" Max number is : {max}")
    
# print(sum)
# print(max)


############ ADD all numbers with range function #############
# total = 0
# for x in range (1, 101):
#     total += x
# print(f"total equals to : {total}")



########### Checking list by copying into new list -> It will only copy the reference not values #######


# final_password = ['a', 'c', '8', '6', '#', '!']
# temp_final_pass = [""]
# temp_final_pass = final_password

# print(final_password.index)
# print(temp_final_pass.index)


# print(f"final temp password is here :{temp_final_pass}")
# print(f"final password is here :{final_password}")

# del temp_final_pass[1:-1]

# print(final_password.index)
# print(temp_final_pass.index)


# print(f"final temp password is here :{temp_final_pass}")
# print(f"final password is here :{final_password}")


############### WHILE LOOP ###############



number_of_anything  =  10
while number_of_anything > 0 :
    print(f"HURRAY IT RAN at number: {number_of_anything}")
    number_of_anything -= 1