# TUPLES
# what will this code print and why?
def move_and_dup_coordinates(x, y):
    tup = x, y = x + 1, y + 1
    tup += tup
    return tup
 
x, y = 5, 10
x, y = move_and_dup_coordinates(x, y)[2:]
print((x,y))

# LIST COMPREHENSIONS 
# this is the format: [<map expression> for <element> in <iterable expression> if <filter expression>]
# what will this code print?
odds = [1, 3, 5, 7, 9]
evens = [(num + 1) for num in odds]
print(evens)

# what will this code print?
temps = [60, 65, 71, 67, 77, 89]
hot = [temp for temp in temps if temp > 70]
print(hot)

# what will this list comprehension produce and what will be printed?
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'm', 'n', 'o', 'p']
word = [letters[i] for i in [3, 4, 6, 8]]
print(word)

# OK, YOUR TURN!
def divisors(n):
    """Returns all the divisors of N.

    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    # return one list comprehension here
    return [i for i in range(1, n) if n % i == 0]

print(divisors(12))

# frontloaded 
def is_odd(n):
    return n % 2 == 1

def front(s, f):
    """Return S but with elements chosen by F at the front.
    >>> front(range(10), is_odd)  # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    # return one list comprehension here
    return [i for i in s if f(i)] + [i for i in s if not(f(i))]

print(front(range(10), is_odd))

# DICTIONARY COMPREHENSIONS 
# this is the format: {<key expression> : <value expression> for <element> in <iterable expression> if <filter expression>}
# Notice the curly braces {} that contain a dictionary instead of square brackets [] that contain a list

# what will this code print?
squares = {x: x*x for x in range(2,10)}
print(squares) 

# what will this print?
numbers = [['two',2], ['three',3], ['four',4]]
products = {x : y*y for x,y in numbers if y % 2 == 0}
print(products)
print(products['four'])

# OK, YOUR TURN FOR SOME FUN!
def translate(sentence,dict):
    """ returns the corresponding word-for-word translation of SENTENCE using the words in DICT """
    # write your code here
    pass

def create_translator_dict(list_of_pairs):
    """ returns a dictionary created from LIST_OF_PAIRS, 
        which is a list of lists which each contain a pair of two words: 
        the first word is the source word and the second word is its translation
    """
    # write your code here, using a single dictionary comprehension
    pass

my_dict = create_translator_dict([['this','esto'],['is','es'],['a','una'],['test','prueba']])
print(translate('this is a test',my_dict))   # "esto es una prueba"