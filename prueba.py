# import PyOpenAL (will require an OpenAL shared library)
from openal import * 

# import the time module, for sleeping during playback
import time

# open our wave file
source = oalOpen("test.wav")

# and start playback
source.play()

# check if the file is still playing
while source.get_state() == AL_PLAYING:
	# wait until the file is done playing
	time.sleep(1)

# release resources (don't forget this)
oalQuit()