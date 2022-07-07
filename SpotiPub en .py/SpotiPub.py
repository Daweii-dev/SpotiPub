import keyboard
import time

print("█▀ █▀█ █▀█ ▀█▀ █ █▀█ █ █ █▄▄")
print("▄█ █▀▀ █▄█  █  █ █▀▀ █▄█ █▄█\n")


while True:
	pass
	if keyboard.read_key() == "*":
		# ouvrir spotyfil
		keyboard.press_and_release('ctrl + alt + s')
		# atendre
		time.sleep(5)
		# fermer spotifil
		keyboard.press_and_release('alt + F4')
		# atendre
		time.sleep(4)
		# ouvrir spotifil
		keyboard.press_and_release('ctrl + alt + s')
		# temps ouveture fenetre 
		time.sleep(4)
		# enlever la pause
		keyboard.press_and_release('space')
		# temps reduire la fenaire
		time.sleep(4)
		# reduire la fenetre 
		keyboard.press_and_release('cmd + down arrow')
		# temps reduire la fenaire 
		time.sleep(0.5)
		# reduire la fenetre 
		keyboard.press_and_release('cmd + down arrow')

# [33m
# \033