# Plan: python
# user inputs their amount of pizza and people 
# define the price of large small medium pizza

# each square inch pizza
# use floor devide and modulo to compute how many larges and mediums and smalls. 
# add up the totals
# function tip 


## CONSTANTS SHOULD GO BELOW THIS COMMENT ##

PI = 3.14159265
PEOPLE_PER_LARGE = 7
DIAMETER_LARGE = 20 
COST_LARGE = 14.68

PEOPLE_PER_MEDIUM = 3
DIAMETER_MEDIUM = 16
COST_MEDIUM = 11.48

PEOPLE_PER_SMALL = 1 
DIAMETER_SMALL = 12
COST_SMALL = 7.28

'''
#alternate constants used for different numbers

PI = 3.14159265
PEOPLE_PER_LARGE = 9
DIAMETER_LARGE = 24
COST_LARGE = 15.78

PEOPLE_PER_MEDIUM = 5
DIAMETER_MEDIUM = 18
COST_MEDIUM = 13.25

PEOPLE_PER_SMALL = 2
DIAMETER_SMALL = 14
COST_SMALL = 8.39
'''

def radius(diameter):
    return (diameter / 2)
    
def total_price(large_amount, medium_amount, small_amount):
    return (small_amount * COST_SMALL) + (medium_amount * COST_MEDIUM) + (large_amount * COST_LARGE)

def tip_plus_total(total_price):
    tip = total_price * tip_amount
    return (tip + full_order)

def area_large(large_amount):
    return ((PI * radius(DIAMETER_LARGE) **2) * large_amount )

def area_medium(medium_amount):
    return ((PI * radius(DIAMETER_MEDIUM) **2)* medium_amount)

def area_small(small_amount):
    return ((PI * radius(DIAMETER_SMALL) **2) * small_amount)


def main():
    ## YOUR CODE SHOULD GO IN THIS FUNCTION ##
    #input the amount of people 
    total_people = int(input("Please enter how many guests to order for:"))
    #divide to get the amount of large
    large_amount = total_people // PEOPLE_PER_LARGE 
    remaining_people_after_large = total_people % PEOPLE_PER_LARGE

    #divide to get the amount of medium pizzas
    medium_amount = remaining_people_after_large // PEOPLE_PER_MEDIUM
    remaining_people_after_medium = remaining_people_after_large % PEOPLE_PER_MEDIUM
    small_amount = remaining_people_after_medium // PEOPLE_PER_SMALL
    remaining_people_after_small = remaining_people_after_medium % PEOPLE_PER_SMALL
    if remaining_people_after_small > 0 :
        small_amount += 1
    print (f"{large_amount} large pizzas, {medium_amount} medium pizzas, and {small_amount} small pizzas will be needed.")
    # print (f"total before tax: ${total_price(large_amount, medium_amount, small_amount)}")
    

    #calculates the square inches of total
    total_area = area_large(large_amount) + area_medium(medium_amount)+ area_small(small_amount)
    area_per_person = (total_area / total_people)


    print(f'A total of {total_area:.2f} square inches of pizza will be ordered ({area_per_person:.2f} per guest).')

    #user inputs tip amount, calculate tip
    tip_amount = ( int(input("Please enter the tip percentage (i.e. 10 means 10%):")) / 100 ) 


    print (f'The total cost of the event will be: ${total_price(large_amount, medium_amount, small_amount) + (total_price(large_amount, medium_amount, small_amount) * tip_amount):.2f}.')

if __name__ == "__main__":
    main()


#I am running into issues with the total. 