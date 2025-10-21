import random
import os

os.system('cls' if os.name == 'nt' else 'clear')
x = int() # temporary variable
l = []    # temporary list

intents = ["Attack", "Defend"]

class player():
    def __init__(self, name, attack, defence, max_health, potions):
        self.name = name
        self.atk = attack
        self.base_defence = defence
        self.defence = defence
        self.max_health = max_health
        self.health = max_health
        self.potions = potions # this is just a list of potions
    
    def attack(self, enemy_defence):
        if self.atk - enemy_defence > 0:
            return self.atk- enemy_defence
        else:
            return 0
    
    def defend(self):
        return self.defence*3
        

    
class monster():
    def __init__(self, name, attack, defence, max_health):
        self.name = name
        self.atk = attack
        self.base_defence = defence
        self.defence = defence
        self.max_health = max_health
        self.health = max_health

    def attack(self, player_defence):
        if self.atk - player_defence > 0:
            return self.atk - player_defence
        else:
            return 0
    
    def defend(self):
        return self.defence*3
    
i = str(input("What would you like to name your lil bro: "))
Player = player(i, 30, 5, 100, ["Explosive Potion"])
Goblin = monster("Goblin", 15, 5, 200)

def use_potion(enemy):
    enemy.health-=20
    print(f"{enemy.name} took 20 damage!")

def battle(player, enemy):
    actions = ["attack", "defend", "use potion", "potion",'1','2','3']

    while True:
        intent = random.choice(intents)
        print(f"{enemy.name} {enemy.health}/{enemy.max_health}\n{player.name} {player.health}/{player.max_health}\nEnemy Intent: {intent}\nWhat would you like to do?\nAttack/Defend/Use Potion")
        action = str(input("=> "))
        while action.lower() not in actions:
            action = str(input("=> "))

        if action.lower() == "attack" or action.lower() == '1':
            enemy.health -= player.attack(enemy.defence)
            print(f"{enemy.name} took {player.attack(enemy.defence)} damage!")   
        
        elif action.lower() == "defend" or action.lower() == '2':
            player.defence = player.defend()
            print(f"{player.name} increased their defense to {player.defence}!")
        
        elif action.lower() == "use potion" or action.lower() == "potion" or action.lower() == '3':
            enemy.health-=20
            print(f"{enemy.name} took 20 damage!")
        
        else:
            print("111OYYY SOMETHING WENT WRONG!!! HELP!!!")
            break

        
        if enemy.health <= 0:
            print(f"{enemy.name} has been defeated!")
            break
        
        
        enemy.defence = enemy.base_defence

        if intent == "Attack":
            player.health -= enemy.attack(player.defence)
            print(f"{player.name} took {enemy.attack(player.defence)} damage!")
        
        elif intent == "Defend":
            enemy.defence = enemy.defend()
            print(f"{enemy.name} increased their defense to {enemy.defence}!")

        else:
            print("222OYYY SOMETHING WENT WRONG!!! HELP!!!")
            break

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
        
        i = "yes"
        while i.lower() != "":
            i = str(input("Say ok:"))
        
        os.system('cls' if os.name == 'nt' else 'clear')
        player.defence = player.base_defence

battle(Player, Goblin)