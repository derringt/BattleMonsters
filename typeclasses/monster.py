from evennia import DefaultObject
import random as r
import csv

def set_gender(rate):
    if rate < r.randint(0,255):
        return "female"
    else:
        return "male"

class Monster(DefaultObject):
    "Battle Monster"
    def at_object_creation(self):
        # PID = 32-bit random integer
        self.db.pid = r.getrandbits(32)

        # Each IV goes from 0-31
        self.db.iv = {}
        self.db.iv['hp'] = int(r.getrandbits(5))
        self.db.iv['att'] = int(r.getrandbits(5))
        self.db.iv['def'] = int(r.getrandbits(5))
        self.db.iv['spatt'] = int(r.getrandbits(5))
        self.db.iv['spdef'] = int(r.getrandbits(5))
        self.db.iv['spd'] = int(r.getrandbits(5))

        # EVs start at 0
        self.db.ev = { 'hp': 0,
                       'att': 0,
                       'def': 0,
                       'spatt': 0,
                       'spdef': 0,
                       'spd': 0 }

        #Empty dictionary for base stats (based on species)
        self.db.base = {}

    def after_spawn(self):
        t = csv.DictReader(open("world/monsters/monster_list.csv"))
        for row in t:
            if row['species'].lower() == self.db.species.lower(): break

        self.db.species = self.db.species.lower().title()
        self.db.base['hp']  = int(row['hp'])
        self.db.base['att'] = int(row['att'])
        self.db.base['def'] = int(row['def'])
        self.db.base['spatt'] = int(row['spatt'])
        self.db.base['spdef'] = int(row['spdef'])
        self.db.base['spd'] = int(row['spd'])

        self.db.dex = int(row['dex'])

        self.db.gender = set_gender(int(row['gender']))

        self.db.types = (row['type1'], row['type2'])

        self.db.lvl_rate = row['lvl_rate']

#    def set_xp(number, self):
