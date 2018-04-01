'''
Usage:
  reframe.py [--load_dest=<s>] [--save_dest=<s>] [--name=<s>] [--duration=<n>] [--fps=<n>]

Options:
  -h --help     Show this screen.
  --load_dest=<s>    Directory to save the output [default: data/stitch].
  --save_dest=<s>    Directory to save the output [default: data/reframe].
  --name=<s>         Name used in create_frames.py.
  --duration=<n>     Seconds of duration [default:15].
  --fps=<n>          Frames per second for output video [default:30].
'''

from tqdm import tqdm
import h5py
import os, docopt, sys, cv2, glob, gc
import joblib
import numpy as np

args = docopt.docopt(__doc__, version='Video Unroll 0.1')


args["load_dest0"] = os.path.join(args["--load_dest"],
                                    args["--name"], "width")

args["load_dest1"] = os.path.join(args["--load_dest"],
                                     args["--name"],"height")

args["save_dest0"] = os.path.join(args["--save_dest"],
                                    args["--name"], "width")

args["save_dest1"] = os.path.join(args["--save_dest"],
                                     args["--name"],"height")


args["load_dest2"] = os.path.join("frames", args["--name"])
args["save_dest2"] = os.path.join(args["--save_dest"],
                                     args["--name"],"frames")


os.system('rm -rf "{}"'.format(args["save_dest0"]))
os.system('rm -rf "{}"'.format(args["save_dest1"]))
os.system('rm -rf "{}"'.format(args["save_dest2"]))

os.system('mkdir -p "{}"'.format(args["save_dest0"]))
os.system('mkdir -p "{}"'.format(args["save_dest1"]))
os.system('mkdir -p "{}"'.format(args["save_dest2"]))

F_IMAGES0 = sorted(glob.glob(os.path.join(args['load_dest0'], '*')))

N = len(F_IMAGES0)
M = int(int(args["--fps"]) * float(args["--duration"]))
cmd = "ln -s {} {}"
print args["save_dest0"], N, M

for k,x in (enumerate(np.linspace(0, N, M-1))):
    f_output = os.path.join(args["save_dest0"], "%08d.png"%k)
    f_input = os.path.join('../../../..',
                           args["load_dest0"], "%08d.png"%int(x))
    os.system(cmd.format(f_input, f_output))



#######################################################################


F_IMAGES1 = sorted(glob.glob(os.path.join(args['load_dest1'], '*')))

N = len(F_IMAGES1)
M = int(int(args["--fps"]) * float(args["--duration"]))
cmd = "ln -s {} {}"
print args["save_dest1"], N, M

for k,x in (enumerate(np.linspace(0, N, M-1))):
    f_output = os.path.join(args["save_dest1"], "%08d.png"%k)
    f_input = os.path.join('../../../..',
                           args["load_dest1"], "%08d.png"%int(x))
    os.system(cmd.format(f_input, f_output))


#######################################################################


F_IMAGES1 = sorted(glob.glob(os.path.join('data',
                                          args['load_dest2'], '*')))

N = len(F_IMAGES1)
M = int(int(args["--fps"]) * float(args["--duration"]))
cmd = "ln -s {} {}"
print args["save_dest2"], N, M

for k,x in (enumerate(np.linspace(0, N, M-1))):
    f_output = os.path.join(args["save_dest2"], "%08d.jpg"%k)
    f_input = os.path.join('../../../',
                           args["load_dest2"], "%08d.jpg"%int(x+1))

    os.system(cmd.format(f_input, f_output))
