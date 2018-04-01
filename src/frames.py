'''
Usage:
  create_frames.py [--start_time=<t0>] [--duration=<t1>] [--save_dest=<s>] [--name=<s>] [--fps=<n>] [--extension=<s>] <f_movie> 

Options:
  -h --help     Show this screen.
  --start_time=<t0>  Start time in seconds [default: 0:0:0].
  --duration=<t1>    Duration in seconds [default: 5].
  --save_dest=<s>    Directory to save the output [default: data/frames].
  --name=<s>         Alternate name of the project
  --fps=<n>          Frames per second [default: 30]
  --extension=<s>    Extension (jpg or png)
'''
import numpy as np
from tqdm import tqdm
import os, docopt, sys, cv2, math

args = docopt.docopt(__doc__, version='Video Unroll 0.1')

# Check if the file is valid
assert(os.path.exists(args["<f_movie>"]))

vcap = cv2.VideoCapture(args["<f_movie>"])
assert(vcap.isOpened())

# Create space to store the images
if args["--name"] is None:
    args["--name"] = os.path.basename(args["<f_movie>"])

args["--save_dest"] = os.path.join(args["--save_dest"], args["--name"])

os.system('mkdir -p "{--save_dest}"'.format(**args))

width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
#fps = vcap.get(cv2.CAP_PROP_FPS)
frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)


cmd = 'avconv  -threads auto -q:v 1 -r {--fps} -an -y "{--save_dest}/%08d.{--extension}"  -ss {--start_time} -t {--duration} -i {<f_movie>}'
cmd = cmd.format(**args)
os.system(cmd)
