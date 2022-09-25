import torch
import argparse
from torch import autocast
from diffusers import StableDiffusionPipeline


parser = argparse.ArgumentParser()
parser.add_argument('--prompt', type=str)
parser.add_argument('--outdir', type=str)
parser.add_argument('--imgname', type=str)

args = parser.parse_args()
prompt = args.prompt
dirname = args.outdir
imgname = args.imgname

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"


pipe = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True)
pipe = pipe.to(device)

with autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5).images[0]  
    
image.save("./{}/{}_image.png".format(dirname,prompt))
