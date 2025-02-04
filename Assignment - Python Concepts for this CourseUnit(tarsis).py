'''

# 1. List Operations

#creating list of my favorite fruits
fruits = ['Pineapple', 'Banana', 'Apple']

#outputting the first and last fruits from my list of favorite fruits 
print(f'The first fruit in list is {fruits[0]} and the last is {fruits[2]}')

#adding two more fruits at the end of the list
fruits.append('Watermelon')
fruits.append('Mango')
#fruits.insert(4,'Berry')

#outputting the list
print(fruits)

#removing the second fruit
fruits.pop(1)
#fruits.remove('Apple')
#del fruits[1]

#outputting the list
print(fruits)

#reversing the list
print(fruits[::-1])

'''


# 2. Implement Adding and Removing Items from a List
#creating an empty list
items_list = []
def add_items(list_name, item):
    list_name.append(item)
    return(list_name)

print(add_items(list_name=items_list, item=input('Enter item')))


def remove_items(list_name):
    
    if len(list_name) == 0:
        return None
    else:
        return list_name.pop(0)

print(remove_items(list_name=items_list))



'''# 3. Dictionary Operations
# representing the library
library = {
    'Fantasy': ['The Name of the Wind', 'The Buried Giant', 'The Night Circus'],
    'Historical': ['Outlander', 'The Tale of Two Cities', 'The Book Thief'],
    'Mystery': ['The Woman in White', 'Rebecca', 'Gone Girl']

}

#adding book from a genre using dictionary key to access list
library['Fantasy'].append('American Gods')
print(library)

#removing book from a genre using dictionary key to access list
library['Mystery'].remove('Rebecca')
print(library)

#print all books in a specific genre
print(library['Historical'])

#print all keys and values
print('Keys:', list(library.keys()) )
print('Values:', list(library.values()))


#nested dictionary

board = {
    'BoG':{'Vice Chancellor': {'Campus': 'Kampala', 'Name': 'Mulindwa John'}, 'Deputy Vice Chancellor': {'Campus': 'Mukono', 'Name':'Naseef Muhamad'}},
    'Staff': {'HoD': 'Maria Kisakye', 'Lecturer': 'Kenneth Agume'},
    'Guild': {'President': 'Samantha Mwesigye', 'Speaker': 'Patience Nimaro', 'Treasurer': 'Lisa Lusinga'},
    'CRA': {'CRA President': 'Nathan Opira', 'Class Representative':'Travis Ayebazibwe'},
    'Student': {'Easter_sem': ['John', 'Alex', 'Enoch'], 'Advent_sem': ['Jude', 'Revelation', 'Peter']}
}


#printing the top levels of the dictionary
print ('Top level keys:', list(board.keys()))

#printing the second level of the dictionary
print ('Second level keys under "BoG":', list(board['BoG'].keys()))

#printing third level keys of the dictionary
print('Third level keys under "BoG":', list(board['BoG']['Vice Chancellor'].keys()))

for i in list(board['BoG']['Vice Chancellor'].keys()):
    print (i)'''


