import random

class Human:
    def __init__(self, name='Human', game=None):
        self.name = name
        self.game = game
        self.gladness = 50
        self.home = True
        self.satiety = 50
        self.money = 100
        self.alive = True
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('Happy')
            self.gladness += 10
            self.satiety += 2
            self.money -= 15


    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", '\n')
        human_indexess = self.name + "'s indexess"
        print(f"{human_indexess:=^50}", '\n')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexess = "Home indexes"
        print(f"{home_indexess:^50}", '\n')
        Game_indexess = "Game indexes"
        print(f"{Game_indexess:=^50}", '\n')
        # Home Work - Написать код, который выводит всю инфу о машине, т.е. бренд, кол бензина и тех ссотояние
    def is_alive(self, day):
        if self.satiety <= 0:
            print("have to eat")
            return False
        elif self.gladness <= 0:
            print("ahhh i have depresion")
            return False
        elif self.money <= -500:
            print("ahhh i don't have money")
            return False

    def live(self, day):
        if self.is_alive(day) == False:
            return False
        if self.satiety <= 0:
            print("have to eat")
            self.eat()
        elif self.gladness <= 0:
            print("ahhh i have depresion")
            self.chill()
        elif self.money <= -100:
            print("ahhh i don't have money")
            self.work()


        self.days_indexes(day)
        dice = random.randint(1, 4)
        if dice == 1:
            print('lets play')
            print(f'Money - {self.money}')
            print(f'Satiety - {self.satiety}')
            print(f'Gladness - {self.gladness}')
            home_indexess = "Home indexes"
            print(f"{home_indexess:^50}", '\n')
            Game_indexess = "Game indexes"
            print(f"{Game_indexess:=^50}", '\n')
        if dice == 2:
            print('lets chill')
            print(f'Money - {self.money}')
            print(f'Satiety - {self.satiety}')
            print(f'Gladness - {self.gladness}')
            home_indexess = "Home indexes"
            print(f"{home_indexess:^50}", '\n')
            Game_indexess = "Game indexes"
            print(f"{Game_indexess:=^50}", '\n')
            self.gladness += 15
            self.money -= 11
        if dice == 3:
            print("i go to buy delicacies")
            self.money -= 10
        if dice == 4:
            print('I go to clean house')
            self.gladness += 20
            print(f'Money - {self.money}')
            print(f'Satiety - {self.satiety}')
            print(f'Gladness - {self.gladness}')
            home_indexess = "Home indexes"
            print(f"{home_indexess:^50}", '\n')
            Game_indexess = "Game indexes"
            print(f"{Game_indexess:=^50}", '\n')
        if self.satiety < 10:
            print("I'll go eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('....')
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money <= 20:
            print("I'll go ask my mom for money")

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Game:
    def __init__(self, game_list):
        self.game = random.choice(list(game_list))
        self.game.gladness = game_list[self.game]['Gladness']



game_list = {
    "Rust": {"Gladness": 5},
    "Dota 2 ": {"Gladness": 4},
    "Roblox": {"Gladness": 2},
    "Samp": {"Gladness":0}}



brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14}}


simson = Human(name = "simson")
for day in range(1,8):
    if simson.live(day) == False:
        break