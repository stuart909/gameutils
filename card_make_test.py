from PIL import Image, ImageDraw, ImageFont

width = 400
height = 600
center = (width//2, height//2)
white = (255,255,255)
black = (0,0,0)

# do the Tkinter canvas drawings (visible)
def cardpath(p):
    try:
        path = input('%s\nQ for quit\nWindows ex - C:\\path\\file.png\nLinux ex - /path/file.png\nEnter path with filename: ' % p)
        if path == 'Q': exit()
        
    except:
        print('String handling error, input valid path and filename\n')
        
    return path

def cardget(p):
    try:
        get = Image.open(cardpath(p))
    except:
        print('Text input error, input valid path and filename\n')
        cardget(p)
    try:
        get = get.resize((width-40, height-40), Image.ANTIALIAS)
    except:
        print('Error handling image, is this a valid PNG image?\n')
        cardget(p)

    return get

cobra = cardget('-I-I-Source Image Filename-I-I-')


#c.create_rectangle(20, 20, 386, 586, width=4)

# do the PIL image/draw (in memory) drawings
# PIL create an empty image and draw object to draw on
# memory only, not visible
img = Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(img)
img.paste(cobra,(int(width/2-180),int(height/2-280)))

#frame
draw.rectangle([width/2-180, height/2-280, width/2+180, height/2+280], fill=None, outline=black, width=4)

#card type
titleFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 24)
typeMsg = "Jackpot!"
w, h = draw.textsize(typeMsg, font=titleFont)
draw.rectangle([width/2-w/2-20, 0, width/2+w/2+20, 30], fill=white, outline=black, width=2)
draw.text(((width-w)/2, 4), typeMsg, fill=black, font=titleFont)



#card title
titleMsg = "Tactical"
w, h = draw.textsize(titleMsg, font=titleFont)
#skills
data = ("Athletics","Battle","Boating","Driving","Fighting","Notice","Piloting","Riding","Shooting","Survival","Tracking")
skill_h = 411 if len(data)>=10 else 391
draw.rectangle([(width/2)-w/2-60, 260, (width/2)+w/2+60, skill_h], fill=white, outline=black, width=2)
#title
draw.rectangle([(width/2)-w/2-20, 250, (width/2)+w/2+20, 280], fill=white, outline=black, width=2)
draw.text(((width-w)/2, 254), titleMsg, fill=black, font=titleFont)



#desc
botFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 12)
botMsg = "This is a test message that means the card is a test."
w, h = draw.textsize(botMsg, font=botFont)
draw.rectangle([width/2-w/2-10, height-h-20, width/2+w/2+10, height], fill=white, outline=black, width=2)
draw.text(((width-w)/2, 578), botMsg, fill=black, font=botFont)


x = 120
y = 260
for i,j in enumerate(data):
    if (i+1)%3==0:
        x=240
    elif (i+1)%2==0:
        x=180
    else:
        x=120
    if i%3 == 0:
        y=y+30
    coords = (x,y)
    w, h = draw.textsize(j, font=botFont)
    draw.text(coords, j, fill=black, font=botFont)
    

    

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
def save(i):
    try:
        i.save(cardpath('-O-O-Output Filename-O-O-'))
    except:
        print('Error writing file to disk, valid path and/or filename?\n')
        save(i)

save(img)    

img.show()
#root.mainloop()
