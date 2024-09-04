
import random
#########################################
##                                      ##
##         Generate password            ##
##                                      ##
##########################################

alphabets = ['a', 'b', 'c', 'd', 'e']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$']

print("Welcome to your own Password generater! ")
alphabets_input = int(input("How many Alphabets you want in your password? Please specify here: "))
numbers_input = int(input("How many Numbers you want in your password? Please specify here: "))
symbols_input = int(input("How many Symbols you want in your password? Please specify here: "))

final_password = []

if alphabets_input > 0:
    for a in range(alphabets_input):
        final_password.append(random.choice(alphabets))

if numbers_input > 0:
    for a in range(numbers_input):
        final_password.append(random.choice(numbers))

if symbols_input > 0:
    for a in range(symbols_input):
        final_password.append(random.choice(symbols))


#final_password = ['a', 'c', 8, 6, '#', '!']

##### print(type(final_password))
##### print(final_password)

####### 1st method to shuffle #########

random.shuffle(final_password)
print(f"List after the Build-in shuffle function : {final_password}\n" )

##### OPTION 1 printing in a string format ##########
password = ""      
for char in final_password:
    password += char
print(f"password is  with shuffle: {password} \n")
#### print(final_password)

####### 2nd and build-in function to shuffle #########
temp_final_pass = []
temp_final_pass= final_password       
fnf = []
for i in range(len(temp_final_pass)): ### run it thru whole length -> get a length -> int value
    index = random.randrange(len(temp_final_pass))     ### get a random range number  with randomrange() -> int values
    ### print(final_password[index])       ### printing it out.  ## Testing
    fnf.append(temp_final_pass[index])
    ### print(fnf)                      #### Testing
    del temp_final_pass[index]         #### delete coz of not getting a duplicated values. 

#### print(f"final password is here :{temp_final_pass}")
#### print(f"final password is here :{final_password}")
print(f"list of complex mixing funtion {fnf} \n")

##### OPTION # 2 printing in a string format ##########
no_commas = ''
for i in fnf:
    no_commas += i
print(f"Your password is with rangerand: {no_commas}")

