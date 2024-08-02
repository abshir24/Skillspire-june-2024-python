class Boxer:
    def __init__(self,size, strength, wins, losses):
        self.size = size
        self.strength = strength
        self.wins = wins
        self.losses = losses

    def printStats(self):
        print(f'Size: {self.size}')
        print(f'Strength: {self.strength}')
        print(f'Wins: {self.wins}')
        print(f'Losses: {self.losses}')


boxer1 = Boxer(181, 99, 10,0)

boxer2 = Boxer(180, 98, 9,1)

print("Boxer 1 Stats: ")
boxer1.printStats()

print('--------------------------------------------------------')

print("Boxer 2 Stats: ")
boxer2.printStats()