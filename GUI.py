"""
Old Stuff -

#from PIL import ImageTk, Image  # For Images - Probably not needed in the end

"""


"""
Needed packages/imports - 

* tkinter (included in Python?) 
* python-vlc (NEED ACTUAL VLC INSTALLED TO USE) -> pip install python-vlc
* FileUtils.py - Local File from Dr. Stokke (CS160)

"""

#
# IMPORTS
#

from tkinter import *
from tkinter import ttk
import os, vlc, FileUtils

# To Do:
# 1. DONE - Add a second frame buttons are closer together/not dependent on the image
# 2. DONE - Open & Play Video -> python-vlc
# 3. HALF DONE. Finish buttons - Improve Video File Selection + Add Buttons for play, pause, etc
# 4. Move status text
# 5. Fix ability to replay the same video + stopping.

def openMedia(displayArea):
    global player 
    
    # Probably add a check if player/media null and run seperate process depending on.
    
    # Create vlc instance.
    Instance = vlc.Instance()
    # Create the player
    player = Instance.media_player_new()
    # Open the media
    media = Instance.media_new(FileUtils.selectOpenFile("Select A Video File.", filetypes=["*.mp4", "MP4 FILES"]))
    #Put the media on the player/instance
    player.set_media(media)
    
    #Event for finished playing.
    playerEvent = player.event_manager()
    playerEvent.event_attach(vlc.EventType.MediaPlayerEndReached, stopMedia)
    
    # Set the canvas where the video will render - May need to add a platform check in the future.
    player.set_hwnd(displayArea.winfo_id())
    # Mute it
    player.audio_set_mute(True)
    return
    
#
# Play/Pause
# Check states and play or pause accordingly. Change title to match.
#

def playPauseMedia():
    # idle/close=0, opening=1, playing=3, paused=4, stopping=5, ended=6, error=7
    if (player.get_state()) in [0, 4, 6]: 
        if (player.play()) == 0:
            lab3["text"] = "VIDEO PLAYING"

#
# Stop Media or if the video has finished update the title.
#

def stopMedia(event):
    if player.get_state() != 6:
        player.stop()
        print(player.get_state())
        lab3["text"] = "VIDEO STOPPED"
    else:
        lab3["text"] = "VIDEO FINISHED"

    
"""
* Color Pallete:
* Background - gray20
* Text - TBD
* Buttons - RoyalBlue3
* Error - #CF6679


*** START OF GUI COMPONENTS ***
"""   
# 
# ROOT/WINDOW
#

root = Tk()
root.title("Independent MoCap Application")

ico = PhotoImage(file = ('UE5Icon.png'))
root.iconphoto(False, ico)
root.configure(background='gray20')

#
# FRAMES
#

frm2 = Frame(root, bg="gray20")
frm3 = Frame(root, bg="gray20")

#
# CANVAS FOR VIDEO
#

lab3 = Label(frm3, text="VIDEO PLAYER", font="bold", fg='RoyalBlue3', bg='gray20', padx=10, pady=10)
lab3.grid(row=0, column=0, columnspan=3)
vP = Canvas(frm3, bg="black", bd=5)
vP.configure(width= 720, height= 480)
vP.grid(row=1, column=0, rowspan= 4, columnspan= 3, padx=50, pady=(0, 10))

#
# BUTTONS
#
but1 = Button(frm2, text= "Open File", font="bold", bg="RoyalBlue3", padx= 10, pady= 10, command=lambda: openMedia(vP)).grid(row=0, column=0, pady=(0, 10), sticky= "e")
but2 = Button(frm2, text= "Display Webcam", font="bold", bg="RoyalBlue3", padx= 10, pady= 10).grid(row=0, column=1, padx=5, pady=(0, 10))
but3 = Button(frm2, text= "Landmark", font="bold", bg="RoyalBlue3", padx= 10, pady= 10).grid(row=0, column=2, pady=(0, 10), sticky= "w")


but4 = Button(frm3, text = "<<", font="bold", bg="RoyalBlue3", padx= 5, pady= 5).grid(row=5, column=1, sticky="w")
but5 = Button(frm3, text = "Play/Pause", font="bold", bg="RoyalBlue3", padx= 0, pady= 5, command=playPauseMedia).grid(row=5, column=1)
but6 = Button(frm3, text = ">>", font="bold", bg="RoyalBlue3", padx= 5, pady= 5, command=lambda: stopMedia(0)).grid(row=5, column=1, sticky="e")

#
# DISPLAY FINISHED FRAMES
#

frm2.grid(column=0, row=1)
frm3.grid(column=0, row=0, pady=(0, 5))

#
# EVENT LOOP
#
root.mainloop()