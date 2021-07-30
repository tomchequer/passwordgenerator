#This is a simples RANDOM password generator
#im buildint it as practice
#this might help you prevent hackers from accesing your data
#so enjoy!
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to my password generator!')
print("""
  .--------.
    / .------. 
   / /        \ 
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |     |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
""")


howmanyletters = int((input("How many letters do you want in your password?\n")))
howmanysymbols = int(input("How many symbols do you want in your password?\n"))
howmanynumbers = int(input("How many numbers do you want in your password?\n"))



#password = ""
#simplifiedpassowrd 
#here i created a little algoritim in order to create a simple password.
#It works building a random password like (randomletters + randomnumbers + randomsymbols)
#but it's not 100% random, 'cause the order of those characters is not randomized.
#but anyway is better than your regular 1234 password.

#for i in range(1, howmanyletters + 1):
  #randomletters = random.choice(letters)
  #password += str(randomletters)

#for i in range (1, (howmanynumbers + 1)):
  #randomnumbers = random.choice(numbers)
  #password += str(randomnumbers)
  
#for i in range (1, howmanysymbols + 1):
  #randomsymbols = random.choice(symbols)
  #password += (randomsymbols)

#print(f'Your simplified password is {password}')



#hardtocrackpassword
#now i created a harder to crack password
#which all characters and them order is completly randomized
#making it almost impossible to crack

password_list = []
for i in range(1, howmanyletters + 1):
  password_list.append(str(random.choice(letters)))

for i in range (1, (howmanynumbers + 1)):
  password_list.append(str(random.choice(numbers)))
  
for i in range (1, howmanysymbols + 1):
  password_list.append((random.choice(symbols)))

random.shuffle(password_list)


#password = ''.join(password_list)
#i could use this method, but im using another one for practicing.

password = ''
for i in password_list:
  password = password + str(i)

print(f'Your hard to crack password is {password}')
