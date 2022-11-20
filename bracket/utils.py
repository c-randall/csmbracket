from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
import numpy as np

import os
import base64
from io import StringIO, BytesIO

def draw_name(bracket,name):
    bw,bh = bracket.size

    font = ImageFont.truetype('bracket/static/Stencil.ttf', size=110)

    draw = ImageDraw.Draw(bracket)
    _,_,tw,th = draw.textbbox((0,0), name, font=font)
    draw.text(((bw-tw)/2,th/2), name, align='center', font=font, fill='black')

def base_bracket(teams):
    xvec = np.array([50, 50, 50, 50, 50, 50, 50, 50, 1250, 1250, 1250, 1250,
                     1250, 1250, 1250, 1250,])

    yvec = np.array([50, 225, 375, 550, 750, 925, 1075, 1250, 50, 225, 375,
                     550, 750, 925, 1075, 1250])

    bracket = Image.open('bracket/static/images/PNG_Files/BareBracket.png')

    for i,n in enumerate(teams):
        overlay = Image.open('bracket/static/images/PNG_Files/'+n+'Circle.png')
        bracket.paste(overlay, (int(xvec[i]), int(yvec[i])))

    bracket.save('bracket/static/images/Brackets/BaseBracket.png', 'PNG')

def master_bracket(teams,colored):
    xvec = np.array([50, 50, 50, 50, 50, 50, 50, 50, 1250, 1250, 1250, 1250,
                     1250, 1250, 1250, 1250, 200, 200, 200, 200, 1100, 1100,
                     1100, 1100, 350, 350, 950, 950, 500, 800, 650])

    yvec = np.array([50, 225, 375, 550, 750, 925, 1075, 1250, 50, 225, 375,
                     550, 750, 925, 1075, 1250, 138, 462, 838, 1162, 138, 462,
                     838, 1162, 300, 1000, 300, 1000, 650, 650, 1214])

    bracket = Image.open('bracket/static/images/PNG_Files/BareBracket.png')
    draw_name(bracket, 'Master')

    for i,n in enumerate(teams):
        if n != "":
            overlay = Image.open('bracket/static/images/PNG_Files/Grey.png')
        elif colored[i]:
            overlay = Image.open('bracket/static/images/PNG_Files/'+n+'Circle.png')
        else:
            overlay = Image.open('bracket/static/images/PNG_Files/'+n+'GreyCircle.png')

        bracket.paste(overlay, (int(xvec[i]), int(yvec[i])))

    bracket.save('bracket/static/images/Brackets/MasterBracket.png', 'PNG')

def first_bracket(name, teams):
    xvec = np.array([200, 200, 200, 200, 1100, 1100, 1100, 1100, 350, 350, 950,
                     950, 500, 800, 650])

    yvec = np.array([138, 462, 838, 1162, 138, 462, 838, 1162, 300, 1000, 300,
                     1000, 650, 650, 1214])

    bracket = Image.open('bracket/static/images/Brackets/BaseBracket.png')

    space_ind = name.index('_')
    draw_name(bracket, name.replace('_', ' ')[:space_ind+2]+'.')

    for i,n in enumerate(teams):
        overlay = Image.open('bracket/static/images/PNG_Files/'+n+'Circle.png')
        bracket.paste(overlay, (int(xvec[i]), int(yvec[i])))

    bracket.save('bracket/static/images/Brackets/'+name+'.png', 'PNG')

def bracket_overlays(name):
    xvec = np.array([200, 200, 200, 200, 1100, 1100, 1100, 1100, 350, 350, 950,
                     950, 500, 800, 650])

    yvec = np.array([138, 462, 838, 1162, 138, 462, 838, 1162, 300, 1000, 300,
                     1000, 650, 650, 1214])

    bracket = Image.open('bracket/static/images/Brackets/'+name+'.png')

    for i,n in enumerate(teams):
        if foreground[i] == -1:
            overlay = Image.open('bracket/static/images/PNG_Files/RedX.png')
            bracket.paste(overlay, (int(xvec[i]), int(yvec[i])), overlay)
        elif foreground[i] == 1:
            overlay = Image.open('bracket/static/images/PNG_Files/GreenCircle.png')
            bracket.paste(overlay, (int(xvec[i]), int(yvec[i])), overlay)

    bracket.save('bracket/static/images/Brackets/'+name+'.png', 'PNG')
