from openal import * 
import time

story_point = '1'

AUDIO_PATH = "audio\\"

def contains_dollar(line):
    return any(char == "$" for char in line)

audio_name = ""
user_option = ''
audio_fx = ""
with open('historia.txt', 'r', encoding='utf-8') as file:
	for line in file:
		if line.startswith(story_point):
			for line in file:
				if not contains_dollar(line):
					print(line, end='')
				else:
					audio_name = file.readline().strip()
					audio_fx = file.readline().strip()
					audio = oalOpen(AUDIO_PATH + audio_name)
					audio.play()
					time.sleep(1)
					oalQuit()
					for line in file:
						if not contains_dollar(line):
							print(line, end='')
						else:
							user_option = input()
							story_point += '.' + str(user_option)
							break
					break
