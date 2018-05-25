import random
import sys
import os

print("Hello world")

#Comment

'''Multi line comment'''

name = "Sheen"
print(name)

'''Numbers String List Tuples Dictionaries/Maps'''


'''+ - * / // **'''
'''** exponential calculations'''
'''// perform division and discard the remainder'''


print("5+2 = ",5+2)
print("5-2 = ",5-2)
print("5*2 = ",5*2)
print("5/2 = ",5/2)
print("5**2 = ",5**2)
print("5//2 = ",5//2)


print("1+2-3*2 = " , 1+2-3*2)
print("(1+2-3)*2 = " , (1+2-3)*2)


#To insert a quote to a String

quote = "\"Always Remember You Are Unique\""

multi_line_quote = '''just
like everyone else'''

new_string = quote+multi_line_quote

print("%s %s %s" %('I like the quote', quote,multi_line_quote))

#To not get a new line every time
print("I dont like this ", end="")
print("new lines")
#to add many new lines at once
print('\n' *5);

#List
print("**************Lists**************")
grocery_list = ['Juice','Tomatoes','Potatoes','Bannanas']
print('First Item ', grocery_list[0])
grocery_list[0]= 'Green Juice'
print('First Item ', grocery_list[0])

#To print a subset
print(grocery_list[1:3])

other_events = ["Wash Car","Pickup Kids","Cash Check"]

#Add 2 lists into one list
to_do_list = [other_events,grocery_list]
print(to_do_list)
print((to_do_list[1][1]))

#To append the item at the end of the list
grocery_list.append('Onions')
print(to_do_list)

#To insert an item to a specific index
grocery_list.insert(1,"Pickle")
print(to_do_list)

#To remove an item from a list
grocery_list.remove("Pickle")
print(to_do_list)

#To sort items
grocery_list.sort()
print(to_do_list)

#To reverse Sort
grocery_list.reverse()
print(to_do_list)


#Delete item from list
del(grocery_list[4])
print(to_do_list)


to_do_list2 =other_events+grocery_list

#Get length of the list
print(len(to_do_list2))

#Get maximum
print(max(to_do_list2))

#Get Minimum
print(min(to_do_list2))


print('\n'*5)


#Tuples
print("**************Tuples**************")

#Tuples cannot be changed after creation like a list
pi_tuple = (3,1,4,1,5,9)

#Change tuple to lists
new_list = list(pi_tuple)

#Change list to tuple
new_tuple =tuple(new_list)

#Get length of tuple
len(new_tuple)

#Get max
min(new_tuple)

#Get min
max(new_tuple)




print('\n'*5)
#Dictionaries/Maps
print("**************Maps**************")
'''Each values has a unique key
And these cannot be combined unlike lists'''


super_villians = {'Fiddler':'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper':'Thomas Peterson'}

#Get the value of a specific key
print(super_villians['Captain Cold'])

#Delete and entry from the map

del super_villians['Fiddler']
print(super_villians)

#Change the value of a key
super_villians['Pied Piper']='Hartley Rathaway'

#Get the length of the map
print(len(super_villians))

#Get value of a key
print(super_villians.get('Pied Piper'))

#Get  the keys of the map
print(super_villians.keys())

#Get the values of the map
print(super_villians.values())






print('\n'*5)
#Conditionals
print("**************Conditionals**************")

age = 30
if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

#multiple conditions

if age>=21:
    print('You are old')
elif age>16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')


#Logical operators = and or not

if((age>=1)and(age<=18)):
    print('You get a birthday')
elif((age==21)or(age>=65)):
    print('You get a birthday')
elif not(age==30):
    print('You dont get a birthday')
else:
    print('You get a birthday yeah')

print('\n'*5)
#Loops
print("**************Loops**************")

for x in range(0,10):
    print(x ,' ' ,end="")


print('\n')

grocery_list = ['Juice','Tomatoes','Potatoes','Bannanas']
for y in grocery_list:
    print(y)


#to define a list to cycle through

for x in [2,4,6,8,10]:
    print(x)

num_list=[[1,2,3],[10,20,30],[100,200,300]]
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


random_num = random.randrange(0,100)
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0,100)


i = 0;
while(i<=20):
    if(i%2 == 0):
        print(i)
    elif(i==9):
        break
    else:
        i+=1
        continue

    i+=1



print('\n'*5)
#methods
print("**************Methods**************")



def addNumbers(fNum,lNum):
    sumNum = fNum+lNum
    return sumNum

print(addNumbers(2,4))




print('\n'*5)
#Strings
print("**************Strings**************")

long_string = "I'll catch you if you fall - The Floor"
#to print the first 3 characters in the string
print(long_string[0:4])

#to print the last 5 characters
print(long_string[-5:])

#to print everything upto last 5 characters
print(long_string[:-5])

#to concatanate strings
print(long_string[0:4] + " be there")

#formatting with strings
#to output a character %c is used
#to output a string %s is used
#to output a signed integer %d is used
#to output a deicmal value with atleast 5 deficmal places %.5f
print("%c is my %s letter and my number %d number is %.5f "%('X','favourite',1,.14))

#to capitalize the first letter of a string
print(long_string.capitalize())

#to find the index of the word
print(long_string.find("Floor"))

#to find if the string is all letters
print(long_string.isalpha())

#to find if string has numbers
print(long_string.isalnum())

#get length of a string
print(len(long_string))

#to replace a specific word in a string
print(long_string.replace("Floor","Ground"))

#to strip whitespaces
print(long_string.strip())

#to split a string
quote_list = long_string.split(" ")
print(quote_list)



print('\n'*5)
#fileio
print("**************File I/O**************")

#Create as well as a open a file
test_file = open("test.txt","wb")

#to output the file mode that has been used
print(test_file.mode)

#to print the file name
print(test_file.name)

#to write text to the file
test_file.write(bytes("Write me to the file\n",'UTF-8'))

#to close a file
test_file.close()

#read from a file
test_file = open("test.txt","r+")

text_in_file = test_file.read()
print(text_in_file)


#to delete a file
#os.remove("test.txt")



print('\n'*5)
#Objects
print("**************Objects**************")

class Animal:
    #None signifies the lack of a value
    ##Preceding names with underscoes means that those variables are private whichh mesns they require getters and setters
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    #constuctor

    def __init__(self,name,height,weight,sound):
        self.__name =name
        self.__weight = weight
        self.__height=height
        self.__sound = sound


#Encapsulation
    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

#Polymorpishm
    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg and say {}".format(self.__name,self.__height,self.__weight,self.__sound)



cat = Animal('Whiskers',33,10,"Meow")
print(cat.toString())

#inheritance

class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

#Oveerriding
    def toString(self):
        return "{} is {} cm tall and {} kg and says {} and his owner is {}".format(self.get_name() , self.get_height(), self.get_weight(), self.get_sound(),  self.__owner)


    def multiple_sounds(self,how_many=None):
        if how_many is None:
            print(self.get_sound())
        else :
            print(self.get_sound()*how_many)




spot = Dog("Spots",53,27,"Ruff","Sheen")
print(spot.toString())

#Polymorpishm

class AnimalTesting:
    def get_types(self,animal):
        animal.get_type()

test_animals = AnimalTesting()
test_animals.get_types(cat)
test_animals.get_types(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()