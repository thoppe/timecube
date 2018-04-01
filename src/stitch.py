'''
Usage:
  stitch.py [--name=<s>]

Options:
  -h --help     Show this screen.
  --name=<s>    Name used in create_frames.py
'''

from __future__ import division
import numpy as np
from tqdm import tqdm
import h5py
import os, docopt, sys, cv2, glob, gc
import joblib

args = docopt.docopt(__doc__, version='Video Unroll 0.1')
args["--save_dest0"] = "data/stitch/{--name}/width"
args["--save_dest1"] = "data/stitch/height"
args["--load_dest"] = os.path.join("data/frames/", args["--name"])

# Create space to store the images
save_dest0 = os.path.join('data', 'stitch', args["--name"], 'width')
save_dest1 = os.path.join('data', 'stitch', args["--name"], 'height')

os.system('mkdir -p "{}"'.format(save_dest0))
os.system('mkdir -p "{}"'.format(save_dest1))

F_IMAGES = sorted(glob.glob(os.path.join(args["--load_dest"], "*")))
assert(len(F_IMAGES))
print "Found {} images".format(len(F_IMAGES))

sample_img = cv2.imread(F_IMAGES[0])
#hsv = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)

n = len(F_IMAGES)
h, w, c = sample_img.shape


def load_image_width(f, i, j):
    img = cv2.imread(f)
    return img[i:j, :, :]

def load_image_height(f, i, j):
    img = cv2.imread(f)
    return img[:, i:j, :]

dfuncW = joblib.delayed(load_image_width)
dfuncH = joblib.delayed(load_image_height)

batch_size = 50

def stack_resolve(imgs):
    # Stack the images temporally and get them to the right size
    samples, ix, iy, ic = imgs.shape

    img = np.zeros(shape=(ix*samples, iy, ic), dtype=imgs.dtype)

    IDX = np.arange(0, ix)
    for m in range(samples):
        img[IDX*samples+m, :, :] = imgs[m]

    img = cv2.resize(img, (w,h))
    return img


with joblib.Parallel(-1) as MP:
    batch_size = min(n, batch_size)
    unit = h    
    
    for image_k in range(0, n, batch_size):
        f_save0 = os.path.join(save_dest0, "{:08d}.png".format(image_k))
        
        if os.path.exists(f_save0):
            continue

        print "Starting width", image_k

        i = int(np.floor((image_k/n)*unit))
        j = int(np.floor(((image_k+batch_size)/n)*unit))

        ITR = tqdm(F_IMAGES)
        RES = np.array(MP(dfuncW(f, i, j) for f in ITR))

        dm = RES.shape[1]/batch_size
        ITR = np.arange(0, RES.shape[1], dm)

        # This needs to match or something is weird
        assert( len(ITR) == batch_size )

        RES = RES.transpose([1,0,2,3])

        print "Blending and saving"
        for k,x in tqdm(enumerate(ITR)):
            i = int(np.floor(x))
            j = int(np.ceil(x+dm))            
            img = stack_resolve(RES[i:j, :, :, :])

            f_save = os.path.join(
                save_dest0, "{:08d}.png".format(image_k+k))

            #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(f_save, img)
            
        del RES
        gc.collect()

    
    ##############################################################

    unit = w

    for image_k in range(0, n, batch_size):
        f_save1 = os.path.join(save_dest1, "{:08d}.png".format(image_k))
        
        if os.path.exists(f_save1):
            continue

        print "Starting height", image_k

        i = int(np.floor((image_k/n)*unit))
        j = int(np.floor(((image_k+batch_size)/n)*unit))

        ITR = tqdm(F_IMAGES)
        RES = np.array(MP(dfuncH(f, i, j) for f in ITR))

        dm = RES.shape[2]/batch_size
        ITR = np.arange(0, RES.shape[2], dm)

        # This needs to match or something is weird
        assert( len(ITR) == batch_size )

        RES = RES.transpose([2,1,0,3])

        print "Blending and saving"
        for k,x in tqdm(enumerate(ITR)):
            i = int(np.floor(x))
            j = int(np.ceil(x+dm))

            img = stack_resolve(RES[i:j, :, :, :])

            f_save = os.path.join(
                save_dest1, "{:08d}.png".format(image_k+k))

            img = cv2.resize(img, (w, h))
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            cv2.imwrite(f_save, img)
            
        del RES
        gc.collect()
