#CLASS 05

timeline.setMaxID(<id>)










#TASK 04

f = open("path") #f represents a file object, if the file was opened successfully.
#a for append
#r for read
#w for write
#b for the data in the file to be binary

line = f.readline() #reads on line up to a '\n'
contents = f.read() #reads all contents
f.write("line of text\n")
f.close()
f.flush()

#open the file
#while there are lines in the file
    #read a line
    #process the line

def read_file(filename=None):
    line_list = list()
    if filename: #has some kind of value
        count = 0 #this variable is used to count the lines in the file
        f = open(filename, "r")
        line = f.readline()
        while line != "":
            count += 1
            line = line.rstrip() #removes all whitespace from the right side of a line
            print(f"{count}:{line}")
            line_list.append(line)
            line = f.readline()
        f.close()
    else:
        print("Must supply a filename")
    return line_list


def write_file(filename):
    one = list()
    count = 000
    f = open(filename, "w")
    line = ""
    while line != "\n\n":
        line = input("Enter a line:")
        one = one.append(line)
        for something in one:
            f.write({count})
            f.write(something)
            f.write("\n")
    f.flush()
    f.close()


def write_file(filename, line_list=[]):
    response = 0
    while True:
        enter = input("Enter a line: ")
        if enter == "":
            response += 1
            if response == 2:
                break
        else:
            line_list += enter
            if line_list:
                f = open(filename, "w")
                count = 000
                for line in line_list:
                    f.write(count)
                    f.write(line)
                    f.write("\n")
                    count += 1





#CLASS 04

#>>>
import json

#getting a file from the disk/website to our syste,=m, but this only gives text
def load_json_string(filename="sample_tweets.json"):
    contents = ""
    if filename:
        f = open(filename, "r")
        line = f.readline()
        while line != "":
            #print(f"{line}")
            contents = contents + line
            line = f.readline()
        f.close()
    else:
        print("Must supply a filename")
    return json.loads(contents)

#>>> 
tweets = load_json_string('sample_tweets.json')

#print the text
print(json.dumps(tweets[0],indent=4))


#convert the text to json format
def save_dictionary_as_JSON(fname='', data={}):
    if not fname:
        print("Must supply a file name")
        return
    if not data:
        print("There was no data to write")
        return
    f = open(fname, "w")
    f.write(json.dumps(data,indent=4))
    f.close()
    return

save_dictionary_as_JSON("sample2_tweets.json", tweets)








#TASK 02

l1 = []
def counter(count):
    i = 0
    while i <= count:
        l1.append(i)
        i += 1
    print(l1)


def snip(source, start, run):
    l1 = []
    end = range
    while start <= end:
        l1.append(source[start])
        start += 1
    return l1



dictionary = {'word': '', 'definition': '', 'ps': '', 'pronounciation': ''}
def test(word='', definition='', ps='', pronounciation=''):
    dictionary['word'] = word
    dictionary['definition'] = definition
    dictionary['ps'] = ps
    dictionary['pronounciation'] = pronounciation
    return dictionary


entry = {'word': '', 'definition': '', 'ps': '', 'pronounciation': ''}
def test(word='', definition='', ps='', pronounciation=''):
    dictionary['word'] = word
    dictionary['definition'] = definition
    dictionary['ps'] = ps
    dictionary['pronounciation'] = pronounciation
    return dictionary




#CLASS03

#give 5 guesses to guess a number

def guess_a_number(number):
    i = 0
    while i < 5:
        x_str = input("Guess a number:")
        x = int(x_str)
        if x == number:
            print("Correct!")
            return
        elif x < number:
            print("Guess higher")
        elif x > number:
            print("Guess lower")
        i = i + 1
    print("You've run out of guesses!")
    return

        
        

    

#>>> 
pi = "{:.4f}".format(short_pi)
#>>> print(f"The value {pi} is pi to four digits")



def list_file(x):
    if x:
        f = open(x, "r")
        line = f.readline()
        while line != "":
            #print(f"{line}")
            contents = contents + line
            line = f.readline()
        f.close()
    else:
        print("Must provide a file name")
    return contents

import json

json.dumps(contents)

tweet = load_json_string("sample_tweets.json")


#-------------------------------


class Ale(object):
    def __init__(self):
        self.color_notes = ""
        self.aroma_notes = ""
        self.taste_notes = ""
        return
    def __repr__(self):
        return "<object: Ale>"
    def taste(notes):    
        if notes != "":
            taste_notes = notes
        else:
            print("Sip, Savor, Swallow")

b1 = Ale()
print(b1)

PaleAle = Ale()
PaleAle.taste("Nice")


class PaleAle(Ale): #inheriting from Ale, everything cascades down.
    def taste(self, notes=""):
        if notes != "":
            taste_notes = notes
        else:
            print("Sip\nSavor\nSwallow")
    def __repr__(self):
        return "f<object: PaleAle>\n\ttaste_notes:{self.taste_notes}\n\taroma_notes:{self.aroma_notes}\n\tcolor_notes:{self.color_notes}"

b2 = PaleAle()
b2.taste()

new_func(PaleAle)



#Creating an instance
b3 = PaleAle()
d1 = dict()
l1 = list()
l2 = list()










#CLASS 02 ======================

#exercise01
shop = ["pickles", "ham", "swiss cheese", "lettuce", "tomato"]
shop = shop + ["mustard", "sprouts", "potato salad"] #add new items

del shop[3] #delete swiss cheese

shop[1] = "turkey" #replace ham with turkey

shop.sort() #sort the list


#exercise02
cleaning = ["sponge", "bleach", "mop", "bucket", "vaccum"]

items = cleaning[0:2] #get two first items from the list
shop = shop + items #add these two items to the end of shop list


#exercise03
ducky = {
    "huey": "nephew",
    "dewey": "nephew",
    "louie": "nephew",
    "donald": "uncle"
}


#exercise04
#a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.

definition1 = {
    "word": "algorithm",
    
    "defined": "a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.",
    "example": "a basic algorithm for division",
    "type": "noun",

    "origin": "greek"
}

definition2 = {
    "word": "portage",
    
    "define1": {
        "defined": "the carrying of a boat or its cargo between two navigable waters.",
        "example": "the return journey was made much simpler by portage",
        "type": "noun"
    },

    "define2": {
        "defined":"the action of carrying or transporting something.",
        "example": "they are incapable of portaging a canoe",
        "type": "verb",

    },
    
    "origin": "french",
}


words = {
    "algorithm": definition1,
    "portage": definition2
}


#exercise05

brian = 0.123
becky = 0.578

if brian >= 0.50:
    print("bigger")
else:
    print("lesser")

if becky > 0.0 and becky <= 0.333:
    print("low")
elif becky > 0.333 and becky <= 0.666:
    print("middle")
else:
    print("high")


#exercise06

#print all items in shop in a separate line
for item in shop:
    print(item)

#print with item number
i = 1
for item in shop:
    print(i, item)
    i = i + 1

#print without mustard
i = 1
for item in shop:
    if item != "mustard":
        print(i, item)
        i = i + 1

#using a while loop
i = 0
while(i < len(shop)):
    print(i+1, shop[i])
    i = i + 1

#using while loop without mustard
i = 0
while(i < len(shop)):
    if(shop[i] != "mustard"):
        print(i+1, shop[i])
        i = i + 1


#exercise07

import random
def numbera():
    k = random.random()
    return k


#generate 20 random numbers
def scores():
    i = 1
    short_scores = []
    while i <= 20:
        short_scores = random.random()
        i = i + 1
        print(short_scores)


#generating a list of 20 random numbers
def scores():
    i = 1
    short_scores = []
    while i <= 20:
        short_scores.append(random.random())
        i = i + 1
    return short_scores


#exercise08

def bin_sort(sample): #sample is a list
    low = list()
    middle = list()
    high = list()
    for s in sample:
        if s > 0.0 and s <= 0.333:
            low.append(s)
        elif s > 0.333 and s < 0.666:
            middle.append(s)
        elif s > 0.666 and s <= 1.0:
            high.append(s)
        else:
            print(s, "was out of bounds")
    
    #add the results in a dictionary
    results = dict()
    results['low'] = low
    results['middle'] = middle
    results['high'] = high
    
    return results
    return low
    return middle


#Quiz02

for item in myList:
    print(item)

def circular(rotation, start):
    return start[rotation:] + start[:rotation]


myList = [['A', 'B', 'C'], [4, 5, 6], [7, 8, 9]]

for item in myList:
    print(item)

i = 0
for item in myList:
    for i in myList:
        if i == 0:
            print("-" + myList[0][0] + "-" + myList[0][1] + "-" + myList[0][2])
        elif i == 1:
            print("*" + myList[1][0] + "*" + myList[1][1] + "*" + myList[1][2])
        elif i == 2:
            print("-" + myList[2][0] + "-" + myList[2][1] + "-" + myList[2][2])







#CLASS 01 ======================

def area(radius):
    pi = 3.1415
    area = pi * radius * radius
    result = "The area of the circle with radius " + str(radius) + " is " + str(area)
    return result

string_1 = "Happy"
string_2 = "New"
string_3 = "Year!"

fact = 1
def factorial(n):
    for i in range(1,n+1):
        fact = fact * i

print ("The factorial of 23 is : ",end="")
print (fact)


#FACTORIAL
def factorial(n):
    i = 1
    r = 1
    while i <= n:
        r = i * r
        i = i + 1
    return r






