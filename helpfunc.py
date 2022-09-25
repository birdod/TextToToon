from PIL import Image, ImageDraw, ImageFont
import textwrap

PASTE_X_START = 10
PASTE_Y_START = 10

def input_to_list(paragraph):
    return paragraph.split(".")

def make_textbub(message, save_dir):

    # Image size
    W = int(512 - 2*PASTE_X_START)
    H = int(512//6)
    bg_color = 'rgb(255, 255, 255)'
    
    # font setting
    font = ImageFont.truetype("arial.ttf",16)
    font_color = 'rgb(0, 0, 0)'
    
    image =Image.new('RGB', (W, H), color = bg_color)
    draw = ImageDraw.Draw(image)

    lines = textwrap.wrap(message, width=60)
  
    x_text = 20
    y_text = 10
    for line in lines:
        width, height = 1,15
        draw.text((x_text, y_text), line, font=font, fill=font_color)
        y_text += height        
    image.save('./{}/{}_text.png'.format(save_dir,message))

def merge_image(message_name, image_name, save_dir):
    ret_image = Image.open("./{}/{}.png".format(save_dir,image_name))
    message = Image.open("./{}/{}.png".format(save_dir,message_name))
    ret_image.paste(message,(PASTE_X_START,PASTE_Y_START))
    return ret_image

def fake(save_dir):
    new_image = Image.new('RGB',(512,512), (250,250,250))
    new_image.save('./{}/{}'.format(save_dir,'fake.png'))
    return 'fake'