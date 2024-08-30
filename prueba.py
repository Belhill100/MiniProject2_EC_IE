from openal import * 
import time

AUDIO_DIRECTORY = "audio\\"

source = oalOpen(AUDIO_DIRECTORY + "rain.wav")

source.set_position((0.0, 0.0, -1000000.0))

source.play()

while source.get_state() == AL_PLAYING:
	time.sleep(1)

oalQuit()