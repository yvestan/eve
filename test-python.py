import pygame
import time

# initier pygame
pygame.init()

# définir l'écran pour les tests
screen = pygame.display.set_mode([500, 500])

# définir les actions sur les différents boutons
buttons = [
    {
        'name': 'RED', 
        'button': 1, 
        'start': 10, 
        'end': 20,
        'type': 'static',
        'key': '1',
        'color': (255,0,0)
    },{
        'name': 'BLACK', 
        'button': 4, 
        'start': 30, 
        'end': 40,
        'type': 'static',
        'key': '2',
        'color': (0,0,0)
    },{
        'name': 'WHITE', 
        'button': 12, 
        'start': 50, 
        'end': 60,
        'type': 'static',
        'key': '3',
        'color': (255,255,255)
    },{
        'name': 'DECIMATE-RIGHT', 
        'button': 16, 
        'start': 50, 
        'end': 60,
        'type': 'video',
        'key': '4',
        'color': (0,0,255)
    }
]

current = buttons[0]

# la boucle est active jusqu'à ce qu'on quitte
running = True

print('---> Lancement de la boucle...')

start_time = time.clock()

while running:
    
    currentTime = time.clock() - start_time;

    if currentTime.is_integer():
        print('===> ' + str(currentTime) + ' secondes / Ca joue ' + current['name'])

    changeCurrent = False

	# on surveille les évènements
    for event in pygame.event.get():

        # si on ferme la fenêtre avec la croix
        if event.type == pygame.QUIT:
            running = False
            print('---> Fermeture du la fenêtre du programme : Bye !')

        # on surveille les éléments au clavier
        elif event.type == pygame.KEYDOWN:

            for button in buttons:
                if event.key == getattr(pygame, 'K_KP' + button['key']):
                    print('- On affiche ' + button['name'])
                    changeCurrent = True
                    current = button

            if event.key == pygame.K_DOWN:
                print('---> Fin du programme : Bye !')
                running = False

    if changeCurrent:
        screen.fill(current['color'])
        pygame.display.flip()

# on quitte le jeu
pygame.quit()
