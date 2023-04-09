from PIL import Image, ImageDraw, ImageFont

XPos,YPos = 50,50

name = 'Corey_Randall'

logo = Image.open('bracket/static/images/PNG_Files/BlackHawksCircle.png')
bkgd = Image.new('RGBA', logo.size, (0,0,0,0))
mask = Image.new('RGBA', logo.size, 0)

draw = ImageDraw.Draw(mask)
draw.ellipse((0,0,100,100), fill='green')

bracket = Image.open('bracket/static/images/Brackets/'+name+'_Base.png')
overlay = Image.composite(logo, bkgd, mask)
bracket.paste(overlay, (int(XPos), int(XPos)))

greenCir = Image.open('bracket/static/images/PNG_Files/GreenCircle.png')
bracket.paste(greenCir, (XPos-12,YPos-12), greenCir)

bracket.show()