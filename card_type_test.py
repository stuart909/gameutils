import random

challenge_types = ("Tactical", "Covert", "Technical", "Interactive")
challenge_skills = {
    "Tactical":("Athletics","Battle","Boating","Demolitions","Driving","Fighting","Notice","Piloting","Riding","Shooting","Survival","Tracking"),
    "Covert":("Computers","Electronics","Research","Notice","Stealth","Thievery"),
    "Technical":("Academics","Computers","Electronics","Healing","Research","Spellcasting","Repair","Science","Psionics","Techno-Wizardry"),
    "Interactive":("Persuasion","Intimidation","Taunt","Performance","Research","Psionics","Spellcasting","Occult","Academics")
    }
challenge_modifiers = {
    "Disaster!":["This challenge is against the enemy leadership die at -4.",1],
    "SNAFU":["This challenge is against the enemy leadership die.",2],
    "Major Issue":["This challenge is rolled at a -4.",3],
    "Interference":["This challenge is rolled at a -2.",5],
    "Situation Normal":["This challenge is rolled with no penalty.",9],
    "Bit of Luck":["This challenge is rolled with a +2",3],
    "Jackpot!":["This challenge is rolled at a +2.  Gain a d8 contact with relevant focus type.",1]
    }

def label(x):
    return {x:{"skills":challenge_skills[x]}}

def mod(x,y):
    x.update({"mod":(y,challenge_modifiers[y][0])})
    return x

cards = []
hand = []
discard = []

for i in challenge_types:
    for k,v in challenge_modifiers.items():
        for j in range(v[1]):
            cards.append(mod(label(i),k))
            
def n():
    return random.randint(0, len(deck))

def draw(num=1):
    for i in range(num):
        x = n()
        card = deck[x]
        deck.remove(card)
        hand.append(card)
    show_hand()

def shuffle():
    for i in hand:
        deck.append(i)
    hand.clear()
    random.shuffle(deck)

def show_hand(h=hand):
        for i in hand:
            key_name = [*i][0]
            skills = i[key_name]['skills']
            mod_name = i['mod'][0]
            mod_desc = i['mod'][1]
            print(key_name+'\n'+'Skills: \n'+str(skills)+'\n'+mod_name+'\n'+mod_desc+'\n\n----\n')
        print('Deck = '+str(len(deck)))
deck = cards
random.shuffle(deck)

