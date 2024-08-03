import random

class BigCat:
    speed = 5 
    strength = 5 
    intelligence = 5 
    health = 5 
    durability=5

class Lion(BigCat):
    def __init__(self):
        self.strength = 50
        self.health = 50

    def king(self, bigcat):
        if isinstance(bigcat, Cheetah):
            random_number = random.randint(1,10)
            
            if(random_number <= 6):
                print("Cheetah has left unscathed")
                return 
        
        bigcat.speed = 0 
        bigcat.strength = 0 
        bigcat.intelligence = 0
        bigcat.health = 0 
        bigcat.durability= 0

        print("The bigcat has been defeated by the Lion")

        return



class Leopard(BigCat):
    def __init__(self):
        self.health = 30
        self.strength = 30
        self.intelligence = 30

    def attack(self, bigcat):
        if isinstance(bigcat,Lion):
            bigcat.king(self)

            return 
        
        if isinstance(bigcat, Cheetah):
            random_number = random.randint(1,10)
            
            if(random_number <= 6):
                print("Cheetah has left unscathed")
                return 
        
        self.health -= 15

class Cheetah(BigCat):
    pass


lion = Lion()
cheetah = Cheetah()
leopard = Leopard()

leopard.attack(cheetah)