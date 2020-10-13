import pygame 
import os 
import sys

BLACK = (0,0,0)

DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800

MOVEMENT_SPEED = 4

ALIEN_MOVEMENT_SPEED = 16
ALIEN_FRAME_DELAY = 20
ALIEN_MOVEMENT_MAX_STEPS = 6

MISSILE_X_OFFSET = 42
MISSILE_Y_OFFSET = 48 
MISSILE_MOVEMENT_SPEED = -16

def draw_alien(index, x, y):
    if index == 0:
        display.blit(alien1_images[alien_frame], (x, y))
    elif index == 1 or index == 2:
        display.blit(alien2_images[alien_frame], (x, y))
    elif index == 3 or index == 4:
        display.blit(alien3_images[alien_frame], (x, y))

def alien_bounds(row, col):
    x = alien_x + (col * alien_x_spacing)
    y = alien_y + (row * alien_y_spacing)
    return (x, y, 96, 96)

def barrier_bounds(index):
    x = barrier_x + (index * barrier_x_spacing)
    return (x, barrier_y, 96, 96)

def hit_barrier(missile_x, missile_y, index):
    x, y, width, height = barrier_bounds(index)
    return not (missile_x < x or missile_x > (x + width) or missile_y < y or missile_y > (y + height))

def hit_alien(missile_x, missile_y, row, col):
    x, y, width, height = alien_bounds(row, col)
    return not (missile_x < x or missile_x > (x + width) or missile_y < y or missile_y > (y + height))

pygame.init()
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Space Defenders')

clock = pygame.time.Clock()

player_image = pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/player.png'))
player_x = DISPLAY_WIDTH // 2
player_y = DISPLAY_HEIGHT - 100

missile_image = pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/missile.png'))
missile_x = 0
missile_y = 0
show_missile = False

barrier_image = pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/barrier.png'))
barrier_x = 150
barrier_x_spacing = 200
barrier_y = DISPLAY_HEIGHT - 250

alien1_images = [
    pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/alien1-1.png')),
    pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/alien1-2.png')),
]
alien2_images = [
    pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/alien2-1.png')),
    pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/alien2-2.png')),
]
alien3_images = [
    pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/alien3-1.png')),
    pygame.image.load(os.path.join(sys.path[0], 'assets/space_invaders/alien3-2.png')),
]

aliens_alive = [
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True],
    [True, True, True, True, True, True, True, True]
]

alien_x = 50
alien_x_spacing = 100
alien_y = 80 
alien_y_spacing = 80

alien_frame = 0
frame_count = 0
alien_movement_steps = 0

game_over = False 
dx = 0
while not game_over:
    # check for user input 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # handle user key presses (moving the player)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                dx = -MOVEMENT_SPEED
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                dx = MOVEMENT_SPEED
            elif event.key == pygame.K_SPACE and not show_missile:
                show_missile = True 
                missile_x = player_x + MISSILE_X_OFFSET
                missile_y = player_y + MISSILE_Y_OFFSET
        
        if event.type == pygame.KEYUP:
            dx = 0

    # update the game state

    player_x += dx

    # check if the missile hits the barriers
    for index in range(4):
        if hit_barrier(missile_x, missile_y, index):
            show_missile = False

    # check if the missile hits the aliens
    for col in range(8):
        for row in range(5):
            if aliens_alive[row][col] and hit_alien(missile_x, missile_y, row, col):
                aliens_alive[row][col] = False 
                show_missile = False
                missile_x = -1
                missile_y = -1

    # update the missile position
    if show_missile:
        missile_y += MISSILE_MOVEMENT_SPEED

        if missile_y < 0:
            show_missile = False

    # animate the aliens
    frame_count += 1
    if frame_count > ALIEN_FRAME_DELAY:
        frame_count = 0

        # move the aliens
        alien_x += ALIEN_MOVEMENT_SPEED
        alien_movement_steps += 1
        if alien_movement_steps >= ALIEN_MOVEMENT_MAX_STEPS:
            # start moving the opposite way
            ALIEN_MOVEMENT_SPEED *= -1
            alien_movement_steps = 0

        # change the animation frame
        alien_frame = (alien_frame + 1) % 2

    # display the graphical elements

    display.fill(BLACK)

    # draw the player
    display.blit(player_image, (player_x, player_y))

    # draw the barriers
    for index in range(4):
        x, y, width, height = barrier_bounds(index)
        display.blit(barrier_image, (x, y))

    # draw the missile
    if show_missile:
        display.blit(missile_image, (missile_x, missile_y))

    # draw the aliens
    for col in range(8):
        for row in range(5):
            if aliens_alive[row][col]:
                x, y, width, height = alien_bounds(row, col)
                draw_alien(row, x, y)

    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()