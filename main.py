from time import sleep
import pygame

import pygame_menu
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import ButtonArray
from pygame_widgets.switch import SwitchArray

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

pygame.init()
pygame.display.set_caption('TheSizer')
running = True
screen = pygame.display.set_mode((1200,800), pygame.RESIZABLE)
clock = pygame.time.Clock()


#Theme
main_theme = pygame_menu.themes.THEME_SOLARIZED
main_theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE_TITLE

#Menu to open project
main_menu = pygame_menu.Menu(
	height=100,
    theme=main_theme,
    title='Welcome to TheSizer',
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

volume_slider = None # Used to edit volume
volume_text = None # shows sliders value

volume_slider = Slider(screen,
	SCREEN_WIDTH - 610,
	48,
	520,
	20,
	min=0,
	max=40,
	step=1,
	initial=30
	)

volume_text = TextBox(screen,
	SCREEN_WIDTH-70,
	34,
	60,
	48,
	fontSize=30,
	borderThickness=0,
	colour=(41,41,34),
	textColour=(204, 201, 195)
	)


#Piano Roll
piano_roll_size = (8,12)
notes = []
for i in range(piano_roll_size[0]):
	for j in range(piano_roll_size[1]):
		notes.append('z')


piano_roll = SwitchArray(screen,
	200,
	400,
	(SCREEN_WIDTH-250),(SCREEN_HEIGHT-500),
	(piano_roll_size[0],piano_roll_size[1]),
	border = 2,
	colour=(10,255,11),
	onColours = (200,50,0)
	)

volume_slider._hidden = True
volume_text._hidden = True
piano_roll.hide()

project_open = False # used to check if the 
# project is currently open, and closing stuff
# if it is


# opens up a new menu with the project name
# from earlier and (so far) activates
# volume slider and text when the projects open
def open_new_project():
	global project_name, project, SCREEN_WIDTH, SCREEN_HEIGHT
	global volume_slider, volume_text, piano_roll

	project_name = name_input.get_value()

	project = pygame_menu.Menu(
		project_name, 
		SCREEN_WIDTH, 
		SCREEN_HEIGHT, 
		theme=pygame_menu.themes.THEME_DARK
		)
	
	volume_text.disable() #disables interaction
	volume_slider.setValue(30) #sets to default
	#sets the text to the value
	volume_text.setText(volume_slider.getValue())

	#when hidden, the slider can't be changed or seen
	volume_slider._hidden = False #is True when
	#-project is closed 
	volume_text._hidden = False
	piano_roll.show()



	main_menu._open(project)

#Reason I need this is so that maybe the playhead can play by x
#in time frames and the y's represent the value(actual note)
def Index_To_Tuple(index, constraints):
	col, row = constraints
	x = index//row
	y = index - (row * x)
	return (x,y)

print(Index_To_Tuple(12, piano_roll_size))

def project_update(): #used to update the projects items (buttons, labels, etc)
	global project, project_open
	global volume_slider, volume_text, piano_roll
	global notes

	if project_open: # this constantly sets the text
		volume_text.setText(volume_slider.getValue())



def project_close():
	global volume_slider, volume_text, project_open, piano_roll

	if project_open:
		print('Closed Project')
		#basically closes them
		volume_slider._hidden = True
		volume_text._hidden = True
		piano_roll.hide()
		project_open = False


# Main Menu Set Up
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


#Sets the resized menu and screen
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

