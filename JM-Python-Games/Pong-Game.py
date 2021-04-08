# CodeSkulptor Link: http://www.codeskulptor.org/#user48_H30sjjcl52_0.py

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
#1- import simplegui & random modules
import simplegui
import random
sound = simplegui.load_sound('http://ptrgames.weebly.com/uploads/9/9/5/9/99594468/%E2%99%AApirate101_soundtrack_marleybone_main_theme%E2%99%AB.mp3')
sound2 = simplegui.load_sound('http://ptrgames.weebly.com/uploads/9/9/5/9/99594468/cartoon_bounce_sound_effect.mp3')
image = simplegui.load_image('https://static1.squarespace.com/static/52e5f858e4b05f271de6cece/t/56deb7348259b51411f49fcc/1457436469696/Colorful-Galaxy.jpg?format=2500w')
#2- create object-related global variables: 'WIDTH', 'HEIGHT', 
#   'BALL_RADIUS', 'score', 'paddle_vel', 
#   'paddle_pos', 'ball_pos', 'gravity', 'ball_vel', 'drift', 
#   'pad-width', 'highscore' (NOTE: values are in pixels):
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 10
Score1 = 0
Score2 = 0
paddle1_vel = 0.0
paddle2_vel = 0.0
paddle1_pos = 0.0
paddle2_pos = 0.0
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]
pad_width = 10
pad_height = 80
            
#8- define a new function called 'spawn_ball()'. This function 
#   should describe the ball's initial physics:
def spawn_ball(right):
            global ball_pos, ball_vel
            ball_pos = [WIDTH / 2, HEIGHT / 2]
            if right:
                ball_vel = [random.randrange(2,4), - random.randrange(2,4)]
            else:
                ball_vel = [-random.randrange(2,4), - random.randrange(2,4)]
#7- define a new function called 'new_game()'. This function 
#   should simply spawn a new ball and reset score to 0:
def new_game():
            global score1, score2
            global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
            score1 = 0
            score2 = 0
            paddle1_pos = HEIGHT/2-40
            paddle2_pos = HEIGHT/2-40
            paddle_vel1 = 0.0
            paddle_vel2 = 0.0
            spawn_ball(True)
            sound.play()
            
#10- define a new function called 'draw()' and have it handle 
#    drawing 'o' for objects. Also, include object-related variables:
def draw(o):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel, pad_width, BALL_RADIUS
    
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    image = simplegui.load_image('https://static1.squarespace.com/static/52e5f858e4b05f271de6cece/t/56deb7348259b51411f49fcc/1457436469696/Colorful-Galaxy.jpg?format=2500w')
    o.draw_image(image, [852 / 2, 480 / 2], [852, 480], [WIDTH/2, HEIGHT/2], [WIDTH, HEIGHT])

    o.draw_polygon([[pad_width, paddle1_pos], [pad_width, paddle1_pos + pad_height], [0, paddle1_pos + pad_height], [0, paddle1_pos]], 3, "Green", "Yellow")
    o.draw_polygon([[WIDTH - pad_width, paddle2_pos], [WIDTH - pad_width, paddle2_pos + pad_height], [WIDTH,paddle2_pos + pad_height], [WIDTH, paddle2_pos]], 3, "Green", "Yellow")
    
    o.draw_circle(ball_pos, BALL_RADIUS, 4, "Red", "Blue")
    o.draw_text(str(score1), [WIDTH / 4, 60], 24, "Red", "serif")
    o.draw_text(str(score2), [WIDTH / 1.4, 60], 24, "Red", "serif")
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    
    
    
    
    
    if ball_pos[1] <= BALL_RADIUS:#bounce off ceiling
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:#bounce off floor
        ball_vel[1] = - ball_vel[1]
    
    if ball_pos[0] <= pad_width + BALL_RADIUS:
        if ball_pos[1] < paddle1_pos + 80 and ball_pos[1] > paddle1_pos:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] =  1.1 * ball_vel[0]
            ball_vel[1] =  1.1 * ball_vel[1]
            sound2.play()
        else:
            spawn_ball(True)
            score2 += 1
            
    if ball_pos[0] >= (WIDTH) - (pad_width + BALL_RADIUS):
        if ball_pos[1] < paddle2_pos + 80 and ball_pos[1] > paddle2_pos:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] =  1.1 * ball_vel[0]
            ball_vel[1] =  1.1 * ball_vel[1]
            sound2.play()
        else:
            spawn_ball(False)
            score1 += 1
        
#11- run the program to see if you have successfully created 
#    a ball & a paddle

#12- now the ball and paddle velocity, and give the ball gravity:
    
#17 test whether the ball touches/collides with the paddle
    
     
#18 draw score using 'draw_handler()' function from simplegui


#19 run the final program to see if ball & paddle collide, 
#   score updates, and new game starts at end of previous game. You're done!

#13- run the program to see if your ball falls now

#15- define 2 functions - 'keydown()' and 'keyup()' - and have them handle 
#    'key' for activating game controls using 'KEY_MAP' from simplegui module:
def keydown(key):
    speed = 12
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= speed
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += speed
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= speed
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += speed
        
def keyup(key):
    speed = 12
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel += speed
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel -= speed
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel += speed 
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel -= speed
    elif key == simplegui.KEY_MAP["r"]:
        new_game()
        sound.play()
        
        
#16- run the program to see if you can move your paddle using controls
        
#3- create a window or frame using simplegui module and call it 'f':
f = simplegui.create_frame("Pong", WIDTH, HEIGHT)

#9- call the 'set_draw_handler()' function from simplegui for 'f' 
#   and have it handle 'draw':
f.set_draw_handler(draw)

#14- call the 'set_keydown_handler()' and 'set_keyup_handler()' 
#    function from simplegui for 'f' and have it handle 'keydown' and 'keyup':
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)

#6- call a function named 'new_game()' which we will define next above (#7):
new_game()

#4- call the 'start()' function from simplegui for 'f':
f.start()

#5- run the program to see if you have successfully created a frame)
