# --------- SNAKE GAME - DEV. SESSION 10 ---------

import pygame
import random

pygame.init() # initialize pygame module

# define color code
custom_white = (255, 246, 233)
snake_color = (26, 26, 29)
custom_red = (174, 68, 90)
end_txt_color = (61, 3, 1)
end_scr_color = (255, 170, 170)


# --------- X ---------

# game_window (screen size) variables
scr_width = 900
scr_hight = 600

game_window = pygame.display.set_mode((scr_width, scr_hight)) # setting game_window (size)

# --------- X ---------


clock = pygame.time.Clock() # virtusl clock : for time reference in game
font = pygame.font.SysFont(None, 27) # setting font style & size

# functionto print text in game_window
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

def s_text_screen(text, color, x, y):
    font = pygame.font.SysFont(None, 23)
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])


def plot_snake(game_window, color, snake_list, snake_size):

    for x,y in snake_list:
        pygame.draw.rect(game_window, snake_color, [x, y, snake_size, snake_size])


#  --------- GAME CONTROLS ---------

# game loop
def game_loop():
    
    pygame.display.set_caption("19|SNAKE-PyGame") # setting title for game_window
    pygame.display.update() # reflect display updates

    # game specific variables
    exit_game = False
    over_game = False
    snake_x = 435
    snake_y = 300
    snake_size = 15
    fps = 60
    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, scr_width/1.5)
    food_y = random.randint(20, scr_hight/1.5)

    score = 0
    init_velocity = 5
    
    # snake length values: variables
    snake_list = []
    snake_length = 120

    while not exit_game:

        if over_game: # game over contition
            game_window.fill(end_scr_color)

            # game over message prompt
            text_screen("Game Over! Press ENTER to continue", end_txt_color, 295, 250)
            s_text_screen("Press SPACE-BAR to EXIT", snake_color, 365, 270)

            for control in pygame.event.get(): # record inputs
                if control.type == pygame.QUIT: # enable cross button to close game_window (program)
                        exit_game = True
                
                if control.type == pygame.KEYDOWN: # record keyboard inputs
                    
                    if control.key == pygame.K_RETURN: # record 'Enter'/'Return' key
                        game_loop() # restart game (game_loop)
                    
                    if control.key == pygame.K_SPACE: # record 
                        exit_game = True


        else:
            for control in pygame.event.get(): # record game controls (keys & mouse-pointer)
                
                if control.type == pygame.QUIT: # enable cross button to close game_window (program)
                    exit_game = True
                
                if control.type == pygame.KEYDOWN: # record keys pressed
                    
                    if control.key == pygame.K_RIGHT: # move right
                        velocity_x = init_velocity
                        velocity_y = 0

                    if control.key == pygame.K_LEFT: # move left
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if control.key == pygame.K_UP: # move up
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if control.key == pygame.K_DOWN: # move right
                        velocity_y = init_velocity
                        velocity_x = 0
            
            snake_x += velocity_x
            snake_y += velocity_y

            # snake & food logic
            if abs(snake_x - food_x) < 12 and abs(snake_y - food_y) < 12:
                score += 1
                # food controls
                food_x = random.randint(20, scr_width/1.5)
                food_y = random.randint(20, scr_hight/1.5)
                
                # snake length controls
                snake_length += 5

            # game_window color (set to white)
            game_window.fill(custom_white)

            # game_window : reflect text
            text_screen("SCORE: " + str(score *10), custom_red, 5, 5)

            # snake food
            pygame.draw.rect(game_window, custom_red, [food_x, food_y, snake_size, snake_size])

            # snake head
            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if snake_head in snake_list[:-1]:
                over_game == True

            # game_over logic
            if snake_x < 0 or snake_x > scr_width or snake_y < 0 or snake_y > scr_hight:
                over_game = True

            # game elements
            # SYNTAX --> pygame.draw.rect(screen_window, color, [x, y, length, width])
            # pygame.draw.rect(game_window, snake_color, [snake_x, snake_y, snake_size, snake_size]) # snake head (rectangle element)
            
            plot_snake(game_window, snake_color, snake_list, snake_size)

        pygame.display.update()
        
        clock.tick(fps) # set FPS in respect to clock

    pygame.quit()
    quit()

game_loop() # run game_loop function