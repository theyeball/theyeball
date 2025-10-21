import random

class Player:

    def __init__(self, name, atk, rst, max_health, potions, armor, weapon):
        
        self.name = name
        self.atk = atk 
        # "attack" by itself is a method of this class so i have to rename the attack stat different
        self.base_rst = rst
        self.base_dfc = 10
        self.max_health = self.health = max_health
        self.gold = 0
        
        self.potions: list[str] = potions

        self.poison = 0
        self.blindness = 0
        self.disease = 0 # might be used but prob not yet
        # special combat stats

        self.armor = armor
        self.weapon = weapon
        # these are objects themselves, if we need to refer to their stats then we need to refer to these objects local variables
    
    def attack(self, enemy):
        if self.atk > enemy.dfc:
            return (self.atk - enemy.dfc)*enemy.rst
        else:
            return 0
        
    def defend(self):
        return self.base_dfc + self.armor.dfc
    
    def use_potion(self, name):
        for potion in self.potions:
            if potion.name == name:
                potion.use(self)
                self.potions.remove(potion.name)
                break


class Monster:

    def __init__(self, name, atk, rst, max_health, max_mana, spells):
        self.name = name
        self.atk = atk
        self.rst = rst
        self.max_health = self.health = max_health
        self.max_mana   = self.mana   = max_mana
        self.spells = spells # in the form of a list

    def attack(self, player):
        if self.atk > player.dfc:
            return (self.atk - player.dfc)*player.rst
        else:
            return 0

    def defend(self):
        return self.dfc
    
    def pray(self):
        return self.max_mana/5
    
    def action(self, player_intent):
        if player_intent == "attack":
        elif player_intent == "defend":
        elif player_intent == "use potion":

    

class Armor:

    def __init__(self, name, dfc, rst, cost):
        self.name = name
        self.dfc = dfc
        self.rst = rst
        self.cost = cost

class Weapon:

    def __init__(self, name, atk, cost):
        self.name = name
        self.atk = atk
        self.cost = cost




class Potion:

    def __init__(self, name, function, stat, increase, cost):
        self.name = name
        self.function = function
        self.stat = stat
        self.increase = increase
        self.cost = cost

    def use(self, player):

        if self.stat == "health": # blood vial
            if player.health + self.increase > player.max_health:
                player.health = player.max_health
                return f"Your health ({player.health}/{player.max_health}) was maxed out!"
            else:
                player.health += self.increase
                return f"Your health was increased to {player.health}/{player.max_health}"
            
        elif self.stat == "atk": # strength
            player.atk += self.increase
            return f"Your ATK was increased to {player.atk}"

        elif self.stat == "dfc and rst": # resilience
            player.dfc += self.increase
            player.rst += self.increase
            return f"Your DFC was increased to {player.dfc}\nYour RST was increased to {player.rst}"

blood_vial = Potion("Blood Vial", "Heals back 50 health during combat.", "health", 50)

potion_of_swelling = Potion("Potion of Swelling", "Increases ATK by 10 in the current combat.", "atk", 10)

potion_of_resilience = Potion("Potion of Resilience", "Increases both DFC and RST by 10 in the current combat." "dfc and rst", 10)


class Spell:

    def __init__(self, name, function, stat, increase, cost):
        self.name = name
        self.function = function
        self.stat = stat
        self.increase = increase
        self.cost = cost
    
    def use(self, target):
        if self.stat == "poison":
            target.poison += 7
        elif self.stat == "blindness":
            target.blindness += 10
        elif self.stat == "heal":
            target.health += 40
        elif self.stat == "disease":
            target.disease += 1
        
        