import os  # import the os module to interact with the operating system
import time  # import the time module to use time-related functions
from replit import audio  # import the audio module from replit to play audio files


def play():  # define a function named play
    source = audio.play_file('audio.wav')  # create an audio source from the file 'audio.wav'
    source.paused = False  # set the paused attribute of the source to False
    while True:  # start an infinite loop
        for i in range(1, 4):  # loop through the numbers 1, 2 and 3
            if i == 1:  # if i is 1
                print("Playing")  # print "Playing"
            elif i == 2:  # else if i is 2
                print("The")  # print "The"
            else:  # else (i must be 3)
                print("Music")  # print "Music"
            time.sleep(1)  # wait for one second
            os.system("cls")  # clear the screen
            i += 1  # increment i by 1 (this is not necessary since i is already changing in the for loop)
        print("press something for Exit")  # print "press something for Exit"
        Exit = input()  # get user input and assign it to Exit
        if Exit == "":  # if Exit is an empty string
            break  # break out of the while loop
        else:  # else (Exit is not an empty string)
            continue  # continue the while loop (this is not necessary since the loop will continue anyway)


while True:  # start another infinite loop
    print("MUSİC PLAYER")  # print "MUSİC PLAYER"
    time.sleep(1)  # wait for one second
    os.system("cls")  # clear the screen
    print("""🎶MyPOD Music Payer🎶
  Press 1 to Play
  Press 2 to Exit
  Press anything else to see the menu again
  """)  # print a multi-line string with the menu options
    ans = input(">")  # get user input and assign it to ans
    if ans == "1":  # if ans is "1"
        time.sleep(1)  # wait for one second
        os.system("cls")  # clear the screen
        print("Playing some proper tunes")  # print "Playing some proper tunes"
        time.sleep(1)  # wait for one second
        os.system("cls")  # clear the screen
        play()  # call the play function defined earlier
    elif ans == "2":  # else if ans is "2"
        break  # break out of the while loop
    else:  # else (ans is neither "1" nor "2")
        continue  # continue the while loop (this is not necessary since the loop will continue anyway)
