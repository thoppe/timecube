# Timecube

*Dev Notes:*

How to build a 2x2 framed video, example:

    ffmpeg -i Sunset1_frames.mp4 -i Sunset1_height.mp4 -i Sunset1_width.mp4 -f lavfi -i color=s=1920x1080 -filter_complex "[0:v][1:v] hstack=2 [h1];[2:v][3:v] hstack=2 [h2]; [h1][h2] vstack=2 [prescale]; [prescale] scale=1920:1080" -c:v libx264 -crf 18 -preset veryfast -shortest test.mp4