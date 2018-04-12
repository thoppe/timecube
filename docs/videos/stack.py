import os

cmd = '''ffmpeg -i {name}_height.mp4 -i {name}_width.mp4 -i {name}_frames.mp4 -f lavfi -i color=s=1920x1080 -filter_complex "[0:v][1:v] hstack=2 [h1];[2:v][3:v] hstack=2 [h2]; [h1][h2] vstack=2 [prescale]; [prescale] scale=1920:1080" -c:v libx264 -crf 18 -preset veryfast -shortest ../{name}_all.mp4'''

NAMES = ['clouds1', 'sunrise1', 'Rural1', 'Sunset1']

for name in NAMES:
    os.system(cmd.format(name=name))
