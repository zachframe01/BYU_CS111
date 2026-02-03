# LISTS

attendees = ["Tammy", "Shonda", "Tina"]
print(len(attendees))   # what will this print?

print(attendees[0])   # what will this print?
print(attendees[1])
print(attendees[2])
#print(attendees[3])   # why is this a problem?
print(attendees[-1])   # what will this print?

from operator import getitem   
print(getitem(attendees, 1))  # what will this print?

new_attendees = attendees + ["Alice", "Bob"]
print(new_attendees)  # what will this print?
new_attendees_again = attendees + ["Alice", "Bob"]
print(new_attendees_again == new_attendees)  # True or False?
print(new_attendees_again is new_attendees)  # True or False?

new_attendees_again = new_attendees
print(new_attendees_again is new_attendees)  # True or False?
new_attendees.append("Charlie")
print(new_attendees)  # what will this print?
print(new_attendees_again is new_attendees)  # True or False?

new_attendees.insert(1, "David")
print(new_attendees)  # what will this print?
print(new_attendees_again is new_attendees)  # True or False?

print(attendees * 2)  # what will this print?

from operator import mul
print(mul(attendees,3))  # what will this print?

print("Tammy" in attendees)  # what will this print?

gymnasts = [
             ["Brittany", 9.15, 9.4, 9.3, 9.2],
             ["Lea", 9, 8.8, 9.1, 9.5],
             ["Maya", 9.2, 8.7, 9.2, 8.8]
           ]
print(len(gymnasts))  # what will these lines print?
print(len(gymnasts[0]))
print(gymnasts[1][2])
print(gymnasts[2][0])

# FOR LOOPS

# what does this code do?
sequence = [1, 2, 3, 2, 4, 2, 5]
value = 2
total = 0
i = 0
while i < len(sequence):
    if sequence[i] == value:
        total = total + 1
    i += 1
print(total)

# this version uses a for loop
total = 0
for element in sequence:
    if element == value:
        total = total + 1

print(total)

# what will this code print?
for gymnast in gymnasts:
    for data in gymnast:
        print(data, end="|")

print()

# what will this code print?
pairs = [[1, 2], [2, 2], [3, 2], [4,4]]
same_count = 0
for x, y in pairs:
    print(x)
    if x == y:
        same_count = same_count + 1
print(same_count)

# STRINGS

print('I am a string!')
print("I've got an apostrophe")
print("""The Zen of Python
claims, Readability counts.
Read more: import this.""")
print('The Zen of Python\nclaims, Readability counts.\nRead more: import this.')

# strings are like lists
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
print(len(alfabeto)) # what will these lines print?
print(alfabeto[13] + "andu")
print(alfabeto + ' ¡Ya conoces el ABC!')

# True or False?
initial = 'P'
print(initial[0] == initial)

# True or False?
print('W' in 'Where\'s Waldo')
print('Waldo' in  'Where\'s Waldo')

# what does split() do?
s = "This is a short sentence."
words = s.split()
print(words)
# what if you specify a character?
s = "This sentence\nhas a newline."
words = s.split('\n')
print(words)

# converting case
someString = "Title Case"
print(someString.lower())
print(someString.upper())    

# f strings
artist = "Bette Midler"
song = "The Rose"
place = 10
print("Landing at #" + str(place) + ": '" + song + "' by " + artist)
print(f"Landing at #{place}: '{song}' by {artist}") 

 # formatting decimals
e = 2.718281828459050
print(f"2 decimals: {e:.2f}")
print(f"10 decimals: {e:.10f}")

# what string will be printed?
greeting = 'Ahoy'
noun = 'Boat'
print(f"{greeting*3}, {noun[0:3].upper()}yMc{noun[-1]}Face")

# SLICING

# slicing lists - how does it work?
letters = ["A", "B", "C", "D", "E", "F"]
print(letters[1:4])

print(letters[1:])
# slicing strings - how does it work?
compound_word = "cortaúñas"
print(compound_word[:5])
print(compound_word[5:])

# copying lists
listA = [1, 2, 3]
listB = listA[:]
print(listB) # what will this print?
print(listB==listA) # True or False?
print(listB is listA) # True or False?

listC = list(listA)
print(listC) # what will this print?
print(listC==listA) # True or False?
print(listC is listA) # True or False?


# RANGES
# a range is a sequence of integers

# what will this print?
for i in range(5):
    print(i)    
# what will this print?
for i in range(3,8):
    print(i) 
# what will this print?
for i in range(3,15,3):
    print(i)

