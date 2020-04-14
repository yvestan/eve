from omxplayer.player import OMXPlayer
from pathlib import Path
from gpiozero import Button
import time

# le repertoire de stockage des videos
videoDirectory = '/home/pi/Desktop/live/OK/'

# le chemin vers la video complete
VIDEO_PATH = Path(videoDirectory + "COMPLET-MACMINI.mp4")

# definir les actions sur les differents boutons
buttons = [
    {
        'name': 'DECIMATE-END', 
        'couleur': 'rose',
        'gpio': 26, 
        'start': 0, 
        'end': 10,
        'type': 'video',
    },{
        'name': 'DECIMATE-START', 
        'couleur': 'violet',
        'gpio': 19, 
        'start': 11, 
        'end': 19,
        'type': 'video',
    },{
        'name': 'RED', 
        'couleur': 'rouge',
        'gpio': 13, 
        'start': 25, 
        'end': 29,
        'type': 'static',
    },{
        'name': 'WHITE', 
        'couleur': 'blanc',
        'gpio': 6, 
        'start': 35, 
        'end': 39,
        'type': 'static',
     },{
        'name': 'BLACK', 
        'couleur': 'noir',
        'gpio': 24, 
        'start': 45, 
        'end': 49,
        'type': 'static',
      },{
        'name': 'TRIANGLE',
        'couleur': 'jaune',
        'gpio': 18, 
        'start': 55, 
        'end': 58,
        'type': 'static',
    }
]

# ne lance pas omxplayer
testButton = False

# creer l'instance des boutons
for button in buttons:
    button['button'] = Button(button['gpio'])

# le RED par defaut
current = buttons[4]

# la boucle est active jusqu'a ce qu'on quitte
running = True

print('---> Lancement de la boucle...')

# creer une instance de OMXPlayer
if testButton == False:
    player = OMXPlayer(VIDEO_PATH)
    player.play()
    player.set_position(current['start'])

while running:
    
    changeCurrent = False

    if current['type'] == 'static':
        if player.position()>current['end']:
            player.set_position(current['start'])
    elif current['type'] == 'video':
        if player.position()>current['end']:
            player.pause()
        
    for button in buttons:
        if button['button'].is_pressed:
            print('- On affiche ' + button['name'])
            if current['type'] == 'video':
                player.play()
            changeCurrent = True
            current = button

    if changeCurrent:
        if testButton == False:
            player.set_position(current['start'])
        print('- En cours : ' + current['name'])

