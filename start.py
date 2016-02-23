'''
This program can be used to learn notes position easily. Note name is shown
as well as a voice says it and
you are given few seconds before the next note. Your task is to play
the note before next note is displayed. Best of luck.'''
import winsound
from random import randint
from time import sleep
notes=["A","A#","B","C","C#","D","D#", "E", "F", "F#", "G", "G#"] #storing the notes


#Here starts just for fun part
winsound.PlaySound(("ready.wav"),winsound.SND_FILENAME)
print "Get ready for the game"
winsound.PlaySound(("game.wav"),winsound.SND_FILENAME)
for i in range(3,0, -1):
    print i
    winsound.PlaySound((str(i)+".wav"),winsound.SND_FILENAME)
    sleep(1)
print "START"
winsound.PlaySound(("start.wav"),winsound.SND_FILENAME)
sleep(1)
#Here it ends


#Here starts the main part
l=len(notes)-1
for i in range(50): # change the number in range to how many times you want to practice
    rnd=randint(0, l)
    print notes[rnd]
    winsound.PlaySound((notes[rnd]+".wav"),winsound.SND_FILENAME)    # playing the respective voice
    sleep(1)        #change for adjusting wait period b/w two notes
