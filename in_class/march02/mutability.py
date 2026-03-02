# list mutability

# append() adds a single element to a list
s = [2, 3]
t = [5, 6]
s.append(4)
print(s)
s.append(t)
print(s)

# extend() adds all the elements in one list to another list
s = [2, 3]
t = [5, 6]
s.extend(t)
print(s)
#s.extend(4) 

# pop() removes and returns the last element
s = [2, 3]
t = [5, 6]
t = s.pop()
print(s)
print(t)

# remove() removes the first element equal to the argument
s = [6, 2, 4, 8, 4]
s.remove(4)
print(s)

L = [1, 2, 3, 4, 5]
L2 = [1, 2, 3, 4, 5]
LL = L
print(L is LL) # same list?
print(L2 is L)
print(L==L2) # equivalent list?

# now work through the following 7 examples with a partner and 
# see if you can say what list L will be before you print it

L[2] = 6               # Replacing one element
print(L)

L[1:3] = [9, 8]        # Replacing multiple elements
print(L)

L[2:4] = []            # Deleting elements
print(L)

L[1:1] = [2, 3, 4, 5]  # Inserting elements
print(L)

L[len(L):] = [10, 11]  # Appending
print(L)

L = L + [20, 30]       # What's the difference here?
print(L)
print(LL)

L[0:0] = range(-3, 0)  # Prepending
print(L)


# list mutation in function calls

# A function can change the value of any object in its scope.
def do_stuff_to(x):
    x[0] = 99

four = [1, 2, 3, 4]
print(four[0])
do_stuff_to(four)
print(four[0])

# Even without arguments:
def do_other_stuff():
    four[3] = 99        # four is in the parent (global) frame!

four = [1, 2, 3, 4]
print(four[3])
do_other_stuff()
print(four[3])

 # a tuple is immutable!
four = (1, 2, 3, [4,5])
print(four[0])
do_stuff_to(four)
print(four[0])

# but is this ok?
four[3][1] = 6
print(four)

# mutable default arguments are part of the function object
# each time the function is called, s is bound to the same list in this case
def f(s=[]):
    s.append('x')
    return len(s)

print(f())
print(f())
print(f())

# mutable value in the parent frame can maintain state for a local in function
def make_withdraw_account(initial):
    balance = [initial]              # IMPORTANT: why does this have to be a list?
    
    def withdraw(amount):
        if balance[0] - amount < 0:
            return 'Insufficient funds'
        balance[0] -= amount
        return balance[0]
    
    return withdraw
    
withdraw = make_withdraw_account(100)
print(f'withdrew $25, balance = {withdraw(25)}')
print(f'withdrew $25, balance = {withdraw(25)}')
print(f'withdrew $60, balance = {withdraw(60)}')