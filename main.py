from openal import *

story_point = '1.3'

AUDIO_PATH = "audio\\"

def contains_dollar(line):
    return any(char == "$" for char in line)

def play_audio(audio_name, audio_fx):
	player = Listener()
	audio = oalOpen(AUDIO_PATH + audio_name)
	audio.play()
	match audio_fx:
		case "FW":
			audio.set_direction((0,0,1))
		case "FW-Pitch":
			audio.set_direction((0,0,1))
			audio.set_pitch(0.6)
		case "FW-Gain":
			audio.set_direction((0,0,1))
			player.set_gain(2.5)
		case "R":
			audio.set_position((1,0,0))
		case "L":
			audio.set_position((-1,0,0))
		case "UP":
			audio.set_position((0,1,1))
		case "DOWN":
			audio.set_position((0,-1,0))
		case "DOWN-Pitch":
			audio.set_position((0,-1,0))
			audio.set_pitch(0.7)
		case "DOWN-R":
			audio.set_position((1,-1,0))
		case "Gain":
			player.set_gain(2.5)
		case "Gain-Pitch":
			player.set_gain(2.5)
			audio.set_pitch(1.5)

user_option = ''
audio_name = ""
audio_fx = ""
with open('story.txt', 'r', encoding='utf-8') as file:
	for line in file:
		if line.startswith(story_point):
			for line in file:
				if not contains_dollar(line):
					print(line, end='')
				else:
					audio_name = file.readline().strip()
					audio_fx = file.readline().strip()
					play_audio(audio_name, audio_fx)
					for line in file:
						if not contains_dollar(line):
							print(line, end='')
						else:
							user_option = input()
							story_point += '.' + str(user_option)
							oalQuit()
							break
					break
