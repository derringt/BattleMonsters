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
        self.db.ev = {}
        self.db.ev['hp'] = 0
        self.db.ev['att'] = 0
        self.db.ev['def'] = 0
        self.db.ev['spatt'] = 0
        self.db.ev['spdef'] = 0
        self.db.ev['spd'] = 0

        self.db.base = {}
        self.db.base['hp'] = 1
        self.db.base['att'] = 1
        self.db.base['def'] = 1
        self.db.base['spatt'] = 1
        self.db.base['spdef'] = 1
        self.db.base['spd'] = 1

        self.db.xp = 0
        self.db.lvl = 1
        self.db.xp_type = "Unknown"

        self.db.species = "MissingNo"
        self.db.dex = 0
        self.db.types = ("Normal", "")

        self.db.gender = "None"

    def after_spawn(self):
        t = csv.DictReader(open("world/monsters/monster_list.csv"))
        for row in t:
            if row['species'] == self.db.species: break

        self.db.base['hp']  = row['hp']
        self.db.base['att'] = row['att']
        self.db.base['def'] = row['def']
        self.db.base['spatt'] = row['spatt']
        self.db.base['spdef'] = row['spdef']
        self.db.base['spd'] = row['spd']

        self.db.dex = row['dex']

        self.db.gender = set_gender(row['gender'])

        self.db.types = (row['type1'], row['type2'])
