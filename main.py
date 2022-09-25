from email.mime import image
from datetime import datetime
from helpfunc import *
import subprocess
import os
import argparse


parser = argparse.ArgumentParser()
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
parser.add_argument('--outdir', type=str, default=timestamp)

dirname = parser.parse_args().outdir
if not os.path.exists(dirname):
    os.mkdir('./'+str(dirname))


paragraph = input()
lines = input_to_list(paragraph)

for i,line in enumerate(lines):
    p = subprocess.call(['python', 'diffusion.py', '--prompt', line, '--outdir', dirname])
    make_textbub(line,dirname)
    merge_image(line + "_text", line + "_image", dirname).save('./{}/{}.png'.format(dirname,i))
    os.remove(os.path.join(dirname,line + "_text.png"))
    os.remove(os.path.join(dirname,line + "_image.png"))