import random

class Human:
    def __init__(self, name='Gamer'):
        self.name = name
        self.gladness = 10
        self.satiety = 50
        self.money = 100
        self.sitting_at_the_computer = 0

    def partying(self):
        print("I am going for a walk")
        self.gladness += 12
        self.satiety -= 15
        self.money -= 10

    def eat(self):
        if self.satiety == 0:
            print("I want to eat, so I go to eat")
            self.gladness += 10
            self.satiety += 20
    def school(self):
        print("I would play computer now but I have to go to school")
        self.gladness -= 7
        self.satiety -= 9
    def replayedonthecomputer(self):
        if self.sitting_at_the_computer > 4.5:
            print("Mom: so son, turn off the computer")
            self.gladness -= 5
    def replayedonthecomputertwo(self):
        if self.sitting_at_the_computer > 9:
            print("Mom she goes to turn off the computer to her son and she succeeds")
            self.gladness -= 5
            return False
    def playcomputer(self):
        print('i go to play Rust')
        self.gladness += 9
        self.satiety -= 6
        self.sitting_at_the_computer += 4.5
    def sleep(self):
        print("I'm already tired, I'm going to sleep")
        self.gladness += 1
    def wakingup(self):
        print("A new day will begin with a game of computer")
        self.gladness += 10
        self.satiety -= 4
    def donate(self):
        print("You donated money to steam")
        self.money -= 10
        self.gladness += 5
    def is_alive(self):
        if self.gladness < 0:
            print("Depression....")
            return False
        if self.satiety < 0:
            print("You died of hunger....")
            return False


    def live(self, day):
        if self.is_alive() == False:
            return False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'sitting at the computer = {self.sitting_at_the_computer}')

    def live(self, day):
        day = "Day " + str(day) + " of" + self.name + " Life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.partying()
            self.end_of_day()
        elif live_cube == 2:
            self.wakingup()
            self.end_of_day()
        elif live_cube == 3:
            self.eat()
            self.end_of_day()
        elif live_cube == 4:
            self.playcomputer()
            self.end_of_day()
            self.is_alive()
        elif live_cube == 5:
            self.donate()
            self.end_of_day()

doter = Human(name=' Doter')
for day in range(15):
    if doter.live == False:
        break
    doter.live(day)










# nick = Human(name="DotaPlayer")
# for day in range(1, 365):
#     if nick.live(day) == False:
#         break




