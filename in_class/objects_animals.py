class Food:
    def __init__(self, name, type, calories=100):
        self.name = name
        self.type = type
        self.calories = calories

broccoli = Food("Broccoli", "veggies", 20)
bone_marrow = Food("Bone Marrow", "meat", 100)




class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1
    calories_needed = 100

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")



class Rabbit(Animal):
    species_name = "European rabbit"
    scientific_name = "Oryctolagus cuniculus"
    calories_needed = 200
    play_multiplier = 8
    interact_increment = 4
    num_in_litter = 12

rabbit1 = Rabbit("Mister Wabbit", 3)
rabbit2 = Rabbit("Bugs Bunny", 2)
rabbit1.eat(broccoli)
Animal.eat(rabbit1,broccoli)
rabbit2.interact_with(rabbit1)


class Elephant(Animal):
    species_name = "African Savanna Elephant"
    scientific_name = "Loxodonta africana"
    calories_needed = 8000
    play_multiplier = 4
    interact_increment = 2
    num_tusks = 2

el1 = Elephant("Willaby", 5)
el2 = Elephant("Wallaby", 3)
el1.play(2)
Animal.play(el1,2)
el1.interact_with(el2)
Animal.interact_with(el1,el2)

# create your own animal here
class Horse(Animal):
    species_name = "European Horse"
    scientific_name = "Equus caballus"
    calories_needed = 16000
    play_multiplier = 10
    interact_increment = 10
    

    pass




# write some code to create at least 2 of your animals
horse1 = Horse("big guy", 5)
horse2 = Horse("small guy", 3)

# and have them do some things common to all Animals
horse1.play(2)
Animal.play(horse2,2)
horse2.interact_with(horse1)
Animal.interact_with(horse1, horse2)

# later you'll have them do different/new things specific to them






class Panda(Animal):
    species_name = "Giant Panda"
    scientific_name = "Ailuropoda melanoleuca"
    calories_needed = 6000

    def interact_with(self, other): # override this method
        print(f"I'm a Panda, I'm solitary, go away {other.name}!")


class Lion(Animal):
    species_name = "Lion"
    scientific_name = "Panthera"
    calories_needed = 3000

    def eat(self, food):
        if food.type == "meat":
            super().eat(food) # call the eat methog on the parent class

bones = Food("Bones", "meat", 50)
mufasa = Lion("Mufasa", 10)
mufasa.eat(bones)

class ToddlerElephant(Animal):
    species_name = "Elephant"
    scientific_name = "Loxodonta"
    calories_needed = 8000

    def __init__(self, name, age=0):
        super().__init__(name, age) # call the __init__ method on the parent class
        Animal.__init__(self,name,age) # same thing with explicit reference to Animal
        if age < 1:
            self.calories_needed = 1000
        elif age < 5:
            self.calories_needed = 2000

elly = ToddlerElephant("Ellie", 3)
print(elly.calories_needed)


# example of common interfaces
def partytime(animals):
    """Assuming ANIMALS is a list of Animals, cause each
    to interact with all the others exactly once."""
    for i in range(len(animals)):
        for j in range(i + 1, len(animals)):
            animals[i].interact_with(animals[j])

jane_doe = Rabbit("Jane Doe", 2)
scar = Lion("Scar", 12)
elly = Elephant("Elly", 5)
pandy = Panda("PandeyBear", 4)
partytime([scar, jane_doe, elly, pandy])


# example of identity checking
panda1 = Panda("Pandeybear", 6)
panda2 = Panda("Spot", 3)
panda1.interact_with(panda2)

print(panda1 is panda1)
print(panda1 is panda2)

# FemaleRabbits inherit from Rabbits, which inherit from Animals
# they exhibit composition of objects
class FemaleRabbit(Rabbit):
    def mate_with(self, other): # can make this a method in the Animal class
        if other is not self and other.species_name == self.species_name:
            self.mate = other
            other.mate = self

    def reproduce_like_rabbits(self):
        if self.mate is None:
            print("oh no! better go on ZoOkCupid")
            return
        self.babies = []
        for _ in range(0, self.num_in_litter):
            self.babies.append(Rabbit("bunny", 0))

mr_wabbit = Rabbit("Mister Wabbit", 3)
jane_doe = FemaleRabbit("Jane Doe", 2)
jane_doe.mate_with(mr_wabbit)
jane_doe.reproduce_like_rabbits()
print([babe.name for babe in jane_doe.babies]) 

