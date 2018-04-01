# Install ffmpeg http://ubuntuhandbook.org/index.php/2017/10/ffmpeg-3-4-released-install-ubuntu-16-04/
# https://gist.github.com/mikoim/27e4e0dc64e384adbcb91ff10a2d3678

fps_in = 30
fps_out = 30
bitrate = 60000
extension = jpg
output_duration = 15

source = input/Most-Beautiful-Sunsets-L_KaQfS1hRQ.webm
name = Sunset1
start    = 0:0:0.5
duration = 0:0:14.5

source = input/RuralIllinoisSunset.mp4
name = Rural1
start    = 0:0:30
duration = 3:20:0
fps_in = 0.4

#source = input/Blooming-Rose-Timelapse-Video-2LC-MiLvWqk.webm
#name = Rose1
#start    = 0:0:5
#duration = 0:0:20

#source = input/Most-Beautiful-Sunsets-L_KaQfS1hRQ.webm
#name = Sunset2
#start    = 0:1:05
#duration = 0:0:14

#source = input/Rotting-Fruit-Timelapse-auRkO0Eiqt0.mp4
#name = RottingFruit
#start    = 0:0:05
#duration = 0:0:45


#source = input/Fruit2-aqNf4KJ5x2k.mp4
#name = RottingFruit2
#start    = 0:0:05
#duration = 0:1:00

source = input/sky_with_clouds-YgmIibSnZs0.mp4
name = clouds1
start    = 0:0:01
duration = 0:15:00
fps_in = 6


source = input/sunrise-mT_bZm-lkmM.mp4
name = sunrise1
start    = 0:0:20
duration = 1:10:00
fps_in = 1



frames:
	python frames.py --start $(start) --duration $(duration) --name $(name) --fps $(fps_in) --extension $(extension) $(source)

stitch:
	python stitch.py --name $(name)

#movie:
#	python render.py --bitrate $(bitrate) --fps $(fps_out) --name $(name)

reframe:
	python reframe.py --name $(name) --duration $(output_duration) --fps $(fps_out)

