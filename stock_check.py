
from time import sleep
import logging
from pynse import *
import datetime
import json
'''
######STORE ALL SYMBOLS CATCHES############
logging.basicConfig(level=logging.DEBUG)
nse = Nse()

####SELECT SYMBOLS FROM PREDIFINE LIST#######

# opening the text file
with open('symbol.txt','r') as file:

	# reading each line	
    for line in file:

		# reading each word		
        for word in line.split():

			# displaying the words		
            print(word) #check one by one data
            sleep(2)


#######COLLECT DATA INTO JSON############
data = nse.get_quote('ITC') #collect data for perticular symbol (replace ITC to symbol var)
file = open('output.json', 'w')
jfile = json.dump(data, file, default=str) #store into Json file
file.close()
'''
########LOAD AND CONVER DATA INTO INT#########
fp = open('output.json', 'r')
data=json.load(fp)

print('\n\n',data)

start = data['open']
current = data['lastPrice']
top = data['high']
bottom = data['low']


#value puted directly into checker block
###############################CHECKER###################################
highest_point = int(start)
lowest_point = int(current)

starting_point = int(top)
current_point = int(bottom)

current1 = current_point + 2
current2 = current_point - 2

start1 = starting_point + 2
strta2 = starting_point - 2

########CHECK CURRENT POINTS#################################################
if current_point <= starting_point and current_point >= starting_point - 2:
    print('down')
    flag = 1
elif current_point <= starting_point:
    print('too down')
    flag = 0

elif current_point >= starting_point and current_point <= starting_point + 2:
    print('up')
    flag = 2
elif current_point <= starting_point:
    print('too up')
    flag = 3
else:
    print('your logic is wrong...')

#######CHECK HIGH/ LOW#######################

high = highest_point - starting_point
low = starting_point - lowest_point

if high > low:
    print('bullish performance (Up stick is bigger)')
    h = 1
else:
    print('bearish performance (Down stick is bigger)')
    h = 0

if flag == 1 and h == 1:
    print('bearish inverted hammer')
elif flag == 2 and h == 1:
    print('bullish inverted hammer')
elif flag == 1 and h == 0:
    print('bearish vertical hammer')
elif flag == 2 and h == 0:
    print('bullish vertical hammer')
else:
    print('No any hammer')