'''
Usage:
  stitch.py [--load_dest=<s>] [--save_dest=<s>] [--name=<s>] [--bitrate=<n>] [--fps=<n>]

Options:
  -h --help     Show this screen.
  --load_dest=<s>    Directory to save the output [default: data/stitch].
  --save_dest=<s>    Directory to save the output [default: output/].
  --name=<s>         Name used in create_frames.py.
  --bitrate=<n>      Bitrate for output video [default:6000].
  --fps=<n>          Frames per second for output video [default:30].
'''

import numpy as np
from tqdm import tqdm
import h5py
import os, docopt, sys, cv2, glob, gc
import joblib

args = docopt.docopt(__doc__, version='Video Unroll 0.1')

os.system('mkdir -p "{}"'.format(args["--save_dest"]))

args["--load_dest0"] = os.path.join(args["--load_dest"],
                                    args["--name"], "width")

args["--load_dest1"] = os.path.join(args["--load_dest"],
                                     args["--name"],"height")

args["f_movie0"] = os.path.join(args["--save_dest"],
                                args["--name"] + '_width.avi')

args["f_movie1"] = os.path.join(args["--save_dest"],
                                args["--name"] + '_height.avi')

args["--bitrate"] = int(args["--bitrate"])


print "Starting width video"
cmd = "avconv -r {--fps} -i {--load_dest0}/%08d.png -b:v {--bitrate} {f_movie0}"
cmd = cmd.format(**args)
print cmd
os.system(cmd)

print "Starting height video"
cmd = "avconv -r {--fps} -i {--load_dest1}/%08d.png -b:v {--bitrate} {f_movie1}"
cmd = cmd.format(**args)
print cmd
os.system(cmd)
