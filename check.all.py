#Checks all the sound
import winsound
notes=["3","2","1","ready","game","start","A","A#","Bb","B","C","C#","D","D#", "Eb","E", "F", "F#", "G", "G#"]
for item in notes:
    winsound.PlaySound(item+".wav", winsound.SND_FILENAME)
    
