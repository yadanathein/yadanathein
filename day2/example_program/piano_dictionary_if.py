import winsound
import msvcrt
piano_notes = {'c':262 ,'d':294,'e':330,'f':350,'g':392,'a':440,'b':494}
while True:
    key = msvcrt.getwch()
    if key in piano_notes.keys():
        winsound.Beep(round(piano_notes[key]), 300)
