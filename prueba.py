# import PyOpenAL (will require an OpenAL shared library)
from openal import * 

# import the time module, for sleeping during playback
import time

AUDIO_DIRECTORY = "audio\\"

# open our wave file
source = oalOpen(AUDIO_DIRECTORY + "rain.wav")

# Configura la posición del sonido (derecha)
source.set_position((1.0, 0.0, 0.0))  # (x, y, z)

# and start playback
source.play()

# check if the file is still playing
while source.get_state() == AL_PLAYING:
	# wait until the file is done playing
	time.sleep(1)

# release resources (don't forget this)
oalQuit()