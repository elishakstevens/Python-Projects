#New class of an animal with 4 attributes
class Animal:
    species = ' '
    sex = True #True is Female, False is Male
    id_num = 0
    age = 0

#Child class that adds 2 diet attributes to Animal class
#True is Yes, False is No
class Diet(Animal):
    carnivore = True 
    herbivore = True

#Child class that adds 2 food chain attributes to Animal class
class FoodChain(Animal):
    role = True #True is predator, False is prey
    related_anatomy = ' '
    
    
