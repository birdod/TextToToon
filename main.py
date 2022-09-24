from email.mime import image
import subprocess
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
PASTE_X_START = 10
PASTE_Y_START = 10

def input_to_list(paragraph):
    return paragraph.split(".")

def make_image(message):

    # Image size
    W = int(512 - 2*PASTE_X_START)
    H = int(512//6)
    bg_color = 'rgb(255, 255, 255)'
    
    # font setting
    font = ImageFont.truetype("arial.ttf",16)
    font_color = 'rgb(0, 0, 0)'
    
    image =Image.new('RGB', (W, H), color = bg_color)
    draw = ImageDraw.Draw(image)

    lines = textwrap.wrap(message, width=40)
  
    x_text = 20
    y_text = 10
    for line in lines:
        width, height = 1,10
        draw.text((x_text, y_text), line,font=font, fill=font_color)
        y_text += height        
    image.save('./{}/{}.png'.format(timestamp,message))

def merge_image(message_name, image_name):
    ret_image = Image.open("./{}/{}.png".format(timestamp,image_name))
    message = Image.open("./{}/{}.png".format(timestamp,message_name))
    ret_image.paste(message,(PASTE_X_START,PASTE_Y_START))
    return ret_image

def fake():
    new_image = Image.new('RGB',(512,512), (250,250,250))
    new_image.save('./{}/{}'.format(timestamp,'fake.png'))
    return 'fake'

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
os.mkdir('./'+str(timestamp))
paragraph = input()
lines = input_to_list(paragraph)
for i,line in enumerate(lines):

    p = subprocess.call(['python', 'GENMODEL/txt2img.py', '--prompt', line, '--outdir', timestamp])
    make_image(line)
    #image_name = fake()
    merge_image(line, image_name).save('./{}/{}.png'.format(timestamp,i))
    os.remove("./{}/{}.png".format(timestamp,image_name))
    os.remove("./{}/{}.png".format(timestamp,line))
