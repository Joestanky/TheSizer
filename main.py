from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
running = True
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()


Name = ""

def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def open_new_project():
	global Name, project
	Name = nameInput.get_value()
	project = pygame_menu.Menu(Name, SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_DARK)
	project.add.range_slider('Volume',default_value=10,range_values=(0,40),rangeslider_id='ransli',
		increment=5, range_width=4)

	mainmenu._open(project)

def level_menu():
    mainmenu._open(level)

mainmenu = pygame_menu.Menu('Welcome', SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_SOLARIZED)
nameInput = mainmenu.add.text_input('Name: ', default='username', maxchar=20, 
		align=pygame_menu.locals.ALIGN_LEFT)

mainmenu.add.button('Open New Project', open_new_project, 
		align=pygame_menu.locals.ALIGN_LEFT)

mainmenu.add.button('Quit', pygame_menu.events.EXIT, 
		align=pygame_menu.locals.ALIGN_LEFT)



level = pygame_menu.Menu('Select a Difficulty', SCREEN_WIDTH, SCREEN_HEIGHT, theme=themes.THEME_BLUE)
level.add.selector('Difficulty:',[('Hard',1),('Easy',2)], onchange=set_difficulty)


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()



	pygame.display.update()
	clock.tick(60)
	mainmenu.mainloop(screen)


