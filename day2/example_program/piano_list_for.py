
import string
import winsound
from time import sleep
from winsound import Beep
from msvcrt import getwch
while True :
    key=getwch()

    if key == 'a':
        winsound.Beep(440, 300)
    elif key == 'b' :
        winsound.Beep(493, 300)
    elif key == 'c' :
        winsound.Beep(261, 300)
    elif key == 'd' :
        winsound.Beep(293, 300)
    elif key == 'e' :
        winsound.Beep(329, 300)
    elif key == 'f' :
        winsound.Beep(349, 300)
    elif key == 'g' :
        winsound.Beep(392, 300)
    elif key == 'q' :
        happy_birthday = [392, 392, 440, 392, 262, 494, 392, 392, 440, 392, 294, 262, 392, 392, 392, 330, 262, 494, 440,
                          349, 349, 330, 262, 294, 262]
        for i in happy_birthday:
            winsound.Beep(i, 750)
        break








