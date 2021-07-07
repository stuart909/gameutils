#Written by Stuart Anderson
#Card creator was a card deck creation utility that I wrote that takes a few lists of data
#It requires a file list of images you want to make into cards
#It also requires specific data to be written on the cards.
#The program will go through the list of files, render cards, draw the information on the card, and output to a random file name in the output directory.
#This is a full program written for a one off job for a Savage Worlds game I ran.  It created a lot of cards to be used for a few adventures we had in a VTT client.
#For a simpler program, see cardtest.py

from PIL import Image, ImageDraw, ImageFont
import uuid, random

width = 400
height = 600
center = (width//2, height//2)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blood = (128,0,0)
navy = (0,0,128)
blue = (0,0,255)
green = (0,255,0)
dark_green = (0,77,0)
yellow = (255,255,0)
orange = (255,128,0)
purple = (170,0,255)
fuchsia = (255,0,255)
forest = (0,77,26)
gold = (128,128,0)

read_path = "/media/nfs/VTT/Data/img/cards/"
write_path = "/media/nfs/VTT/Data/img/cards/final/"

files = ('covert_disaster1.png', 'covert_interfere1.png', 'covert_interfere2.png', 'covert_issue1.png', 'covert_issue2.png', 'covert_jackpot1.png', 'covert_luck1.png', 'covert_luck2.png', 'covert_normal1.png', 'covert_normal2.png', 'covert_normal3.png', 'covert_normal4.png', 'covert_snafu1.png', 'covert_snafu2.png', 'diplo_disaster1.png', 'diplo_disaster2.png', 'diplo_interfere1.png', 'diplo_interfere2.png', 'diplo_interfere3.png', 'diplo_interfere4.png', 'diplo_issue1.png', 'diplo_issue2.png', 'diplo_issue3.png', 'diplo_issue4.png', 'diplo_jackpot1.png', 'diplo_luck1.png', 'diplo_luck2.png', 'diplo_luck3.png', 'diplo_normal1.png', 'diplo_normal2.png', 'diplo_normal3.png', 'diplo_normal4.png', 'diplo_normal5.png', 'diplo_normal6.png', 'diplo_snafu1.png', 'diplo_snafu2.png', 'repair_disaster1.png', 'repair_interfere1.png', 'repair_interfere2.png', 'repair_issue1.png', 'repair_jackpot1.png', 'repair_luck1.png', 'repair_luck2.png', 'repair_normal1.png', 'repair_normal2.png', 'repair_normal3.png', 'repair_normal4.png', 'repair_normal5.png', 'repair_snafu1.png', 'tactical_disaster1.png', 'tactical_interfere1.png', 'tactical_interfere2.png', 'tactical_interfere3.png', 'tactical_issue1.png', 'tactical_issue2.png', 'tactical_jackpot1.png', 'tactical_luck1.png', 'tactical_luck2.png', 'tactical_normal1.png', 'tactical_normal2.png', 'tactical_normal3.png', 'tactical_normal4.png', 'tactical_normal5.png', 'tactical_normal6.png', 'tactical_snafu1.png', 'tactical_snafu2.png', 'tactical_snafu3.png')
discard = []
def convert(x, y):
    return [i for i in files if x in i and y in i and i not in discard][0]

    
image_paths = {
    'Tactical':{"Disaster!":"tactical_disaster.png","SNAFU":"tactical_snafu.png","Major Issue":"tactical_issue.png","Interference":"tactical_interfere.png","Situation Normal":"tactical_normal.png","Bit of Luck":"tactical_luck.png","Jackpot!":"tactical_jackpot.png"},
    'Covert':{"Disaster!":"covert_disaster.png","SNAFU":"covert_snafu.png","Major Issue":"covert_issue.png","Interference":"covert_interfere.png","Situation Normal":"covert_normal.png","Bit of Luck":"covert_luck.png","Jackpot!":"covert_jackpot.png"},
    'Technical':{"Disaster!":"repair_disaster.png","SNAFU":"repair_snafu.png","Major Issue":"repair_issue.png","Interference":"repair_interfere.png","Situation Normal":"repair_normal.png","Bit of Luck":"repair_luck.png","Jackpot!":"repair_jackpot.png"},
    'Interactive':{"Disaster!":"diplo_disaster.png","SNAFU":"diplo_snafu.png","Major Issue":"diplo_magor_issue.png","Interference":"diplo_interference.png","Situation Normal":"diplo_normal.png","Bit of Luck":"diplo_luck.png","Jackpot!":"diplo_jackpot.png"}}

challenge_types = ("Tactical", "Covert", "Technical", "Interactive")
challenge_skills = {
    "Tactical":("Athletics","Battle","Boating","Psionics","Driving","Fighting","Notice","Piloting","Riding","Shooting","Survival","Tracking","Spellcasting"),
    "Covert":("Computers","Electronics","Research","Notice","Stealth","Thievery","Psionics*","Spellcasting*"),
    "Technical":("Academics","Computers","Electronics","Healing","Research","Spellcasting","Repair","Science","Psionics","Techno-Wizardry"),
    "Interactive":("Persuasion","Intimidation","Taunt","Performance","Research","Psionics","Spellcasting","Occult","Academics")
    }
challenge_modifiers = {
    "Disaster!":["This challenge is against the enemy leadership die at -4.",1,blood],
    "SNAFU":["This challenge is against the enemy leadership die.",2,red],
    "Major Issue":["This challenge is rolled at a -4.",3,orange],
    "Interference":["This challenge is rolled at a -2.",5,yellow],
    "Situation Normal":["This challenge is rolled with no penalty.",9,blue],
    "Bit of Luck":["This challenge is rolled with a +2",3,navy],
    "Jackpot!":["This challenge is rolled at a +2.  Gain a d8 contact with relevant focus type.",1,gold]
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



class Card:
    def __init__(self, titleMsg, typeMsg, skills, desc, image, color):
        self.id = str(uuid.uuid1())
        self.img = self.pictures(image)
        self.skills = skills
        self.desc = desc
        self.bigFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 24)
        self.smallFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 12)
        self.frame(color)
        self.card_type(typeMsg, color)
        self.card_skills(skills, color)
        self.card_title(titleMsg, color)
        self.card_desc(desc, color)

    def pictures(self, x):
        img = Image.new("RGB", (width, height), white)
        self.draw = ImageDraw.Draw(img)
        img1 = Image.open(read_path+x)
        img1 = img1.resize((width-40, height-40), Image.ANTIALIAS)
        img.paste(img1,(int(width/2-180),int(height/2-280)))
        return img

    def frame(self, c):
        self.draw.rectangle([width/2-180, height/2-280, width/2+180, height/2+280], fill=None, outline=c, width=4)

    def card_type(self, x, c):
        self.w, h = self.draw.textsize(x, font=self.bigFont)
        self.draw.rectangle([width/2-self.w/2-20, 0, width/2+self.w/2+20, 30], fill=white, outline=c, width=2)
        self.draw.text(((width-self.w)/2, 4), x, fill=black, font=self.bigFont)


    def card_title(self, x, c):
        w, h = self.draw.textsize(x, font=self.bigFont)
        self.draw.rectangle([(width/2)-w/2-20, 250, (width/2)+w/2+20, 280], fill=white, outline=c, width=2)
        self.draw.text(((width-w)/2, 254), x, fill=black, font=self.bigFont)

    def card_skills(self, s, c):
        if len(s) > 12:
            skill_h = 441
        elif len(s) > 9:
            skill_h = 411
        elif len(s) > 6:
            skill_h = 391
        elif len(s) > 3:
            skill_h = 361
        else:
            skill_h = 331
        col_w = 0
        for i in s:
            w, h = self.draw.textsize(i, font=self.smallFont)
            col_w = w if w > col_w else col_w
        w = col_w*3+40
        self.draw.rectangle([(width/2)-w/2, 260, (width/2)+w/2, skill_h], fill=white, outline=c, width=2)
        y = 260
        xm=(width/2)-(w/2)+15
        for i,j in enumerate(s):
            print(xm)
            if (i+1)%3==0:
                x=xm+col_w*2+20
                print(str(i)+' - i : x - '+str(x))
            elif (i+1)%2==0:
                x=xm+col_w+10
                print(str(i)+' - i : x - '+str(x))
            else:
                x=xm
                print(str(i)+' - i : x - '+str(x))
            if i%3 == 0:
                y=y+30
                print(str(i)+' - i : y - '+str(y))
            coords = (x,y)
            print('coords - ' + str(coords))
            w, h = self.draw.textsize(j, font=self.smallFont)
            self.draw.text(coords, j, fill=black, font=self.smallFont)

    def card_desc(self, m, c):
        w, h = self.draw.textsize(m, font=self.smallFont)
        self.draw.rectangle([width/2-w/2-10, height-h-20, width/2+w/2+10, height], fill=white, outline=c, width=2)
        self.draw.text(((width-w)/2, 578), m, fill=black, font=self.smallFont)


    def show(self):
        self.img.show()

    def __call__(self):
        self.img.save(write_path+self.id+'.png')

def create_cards():
        for i in cards:
            key_name = [*i][0]
            skills = i[key_name]['skills']
            mod_name = i['mod'][0]
            mod_desc = i['mod'][1]
            mod_color = challenge_modifiers[mod_name][2]
            filename = image_paths[key_name][mod_name]
            c = Card(key_name, mod_name, skills, mod_desc,filename, mod_color)()

def run():
    key = input("input key : ")
    m = input("input mod : ")
    filename = input("input filename : ")
    Card(key,m,challenge_skills[key],challenge_modifiers[m][0],filename,challenge_modifiers[m][2])()
