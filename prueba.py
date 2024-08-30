from openal import * 
import time

AUDIO_PATH = "audio\\"

audio = oalOpen(AUDIO_PATH + "tv_noise.wav")
audio.play()

while audio.get_state() == AL_PLAYING:
	time.sleep(1)

oalQuit()