from time import sleep
import pygame

import pygame_menu
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()
running = True
screen = pygame.display.set_mode((1200,800), pygame.RESIZABLE)
clock = pygame.time.Clock()



#Menu to open project
main_menu = pygame_menu.Menu(
	height=100,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=100
   )





def on_resize() -> None:
	"""
	Function checked if the window is resized.
	"""
	global main_menu, SCREEN_HEIGHT, SCREEN_WIDTH
	window_size = screen.get_size()
	new_w, new_h = window_size[0], window_size[1]
	SCREEN_WIDTH = new_w
	SCREEN_HEIGHT = new_h
	main_menu.resize(new_w, new_h)
	print(f'New menu size: {main_menu.get_size()}')


project_name = "" # Name set by whatever's input into name_input below
project = None # Initially set to None so it can be checked if it is 
# set to an actual value of the Menu Class and if it's the current
# menu open, running project_update if true

volume_slider = None
volume_text = None

project_open = False


def open_new_project():
	global project_name, project, SCREEN_WIDTH, SCREEN_HEIGHT
	global volume_slider, volume_text

	project_name = name_input.get_value()

	project = pygame_menu.Menu(
		project_name, 
		SCREEN_WIDTH, 
		SCREEN_HEIGHT, 
		theme=pygame_menu.themes.THEME_DARK
		)


	volume_slider = Slider(screen, 100, 100, 800, 40, min=0, max=99, step=1)
	volume_text = TextBox(screen, 475, 200, 50, 50, fontSize=30)
	volume_text.disable()
	volume_text.setText(volume_slider.getValue())

	"""project.add.range_slider(
		'Volume',
		default_value=35,
		range_values=(0,40),
		rangeslider_id='volsli', # Used to ID this specific range_slider below
		increment=5,
		range_width=80,
		range_text_value_font_height=.5,
		accept_kwargs=True,
		font_size=28
		)"""

	# Uses ID to set position to the topright
	#project.get_widget("volsli").set_position(SCREEN_WIDTH-300, 120)

	main_menu._open(project)

def project_update(): #used to update the projects items (buttons, labels, etc)
	global project, project_open
	global volume_slider, volume_text

	if project_open:
		volume_text.setText(volume_slider.getValue())

def project_close():
	global volume_slider, volume_text, project_open

	if project_open:
		print('Closed Project')
		volume_slider = None
		volume_text = None
		project_open = False



#, align=pygame_menu.locals.ALIGN_LEFT
name_input = main_menu.add.text_input(
	'Name: ',
	default='username',
	maxchar=20,
	align=pygame_menu.locals.ALIGN_LEFT)

main_menu.add.button(
	'Open New Project',
	open_new_project,
	align=pygame_menu.locals.ALIGN_LEFT)

main_menu.add.button(
	'Quit',
	pygame_menu.events.EXIT,
	align=pygame_menu.locals.ALIGN_LEFT)


on_resize()

while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			running = False
			exit()
		if event.type == pygame.VIDEORESIZE:
			# Update the surface
			screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			
			on_resize()
			print(SCREEN_WIDTH, SCREEN_HEIGHT)

	screen.fill((25, 0, 50))
	if isinstance(project, pygame_menu.Menu) and main_menu.get_current() == project:
		project_update()
		project_open = True
	else:
		project_close()

	main_menu.update(events)
	main_menu.draw(screen)


	pygame_widgets.update(events)
	pygame.display.flip()
	clock.tick(60)
#

