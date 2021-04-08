# Link to CodeSkulptor: http://www.codeskulptor.org/#user43_88XwhI1jk1BhNAT.py

#1- import simplegui & random modules
import simplegui 
import random
#2- create object-related global variables: 'WIDTH', 'HEIGHT', 
#   'BALL_RADIUS', 'score', 'paddle_vel', 
#   'paddle_pos', 'ball_pos', 'gravity', 'ball_vel', 'drift', 
#   'pad-width', 'highscore' (NOTE: values are in pixels):
WIDTH = 800
HEIGHT = 400
BALL_RADIUS = 20
score = 0
paddle_vel = 0
paddle_pos = WIDTH / 2
ball_pos = [WIDTH / 2 , HEIGHT / 2]
gravity = 0.5
ball_vel = [0, 0]
drift = 0 
pad_width = 150
highscore = 0
ball_border = "Blue"
ball_main = "DarkBlue"
coin_pos = random.randint(20, 780), random.randint(200, 300)
coin_radius = 15
powerup_pos = random.randint(20, 780), random.randint(200, 300)
powerup_radius = 15
powerdown_pos = random.randint(20, 780), random.randint(200, 300)
powerdown_radius = 15
#Test Functions
image = simplegui.load_image('https://pyrosmaniagames.files.wordpress.com/2014/03/gameover.png')
soundtrack = simplegui.load_sound('http://ptrgames.weebly.com/uploads/9/9/5/9/99594468/%E2%99%AApirate101_soundtrack_marleybone_main_theme%E2%99%AB.mp3')
bounce = simplegui.load_sound('http://ptrgames.weebly.com/uploads/9/9/5/9/99594468/cartoon_bounce_sound_effect.mp3')
#8- define a new function called 'spawn_ball()'. This function 
#   should describe the ball's initial physics:
def spawn_ball():
    global ball_vel, gravity, drift, ball_pos, paddle_pos
    ball_pos = [WIDTH / 2, 180]
    gravity = 0.5
    ball_vel = [0, 0]
    drift = random.choice ([-0.1, -0.05, -0.07, -0.02, 0.1, 0.05, 0.07, 0.02])
    paddle_pos = 360
    
#7- define a new function called 'new_game()'. This function 
#   should simply spawn a new ball and reset score to 0:
def new_game():
    global score, pad_width, coin_pos, powerup_pos, powerdown_pos
    soundtrack.rewind()
    score = 0
    spawn_ball()
    soundtrack.play()
    pad_width = 150
    coin_pos = random.randint(20, 780), random.randint(200, 300)
    powerup_pos = random.randint(20, 780), random.randint(200, 300)
    powerdown_pos = random.randint(20, 780), random.randint(200, 300)
    
#10- define a new function called 'draw()' and have it handle 
#    drawing 'o' for objects. Also, include object-related variables:
def draw(o):
    global score, paddle_pos, paddle_vel, ball_pos, ball_vel, gravity, drift, pad_width, highscore, ball_border, ball_main, coin_pos, coin_radius, powerup_pos, powerup_radius, powerdown_pos, powerdown_radius
    o.draw_image(image, (600 / 2, 400 / 2), (1200 / 2, 400 / 2), (350, 200), (400, 200))
    o.draw_circle(ball_pos, BALL_RADIUS, 2, ball_border, ball_main)
    o.draw_circle(coin_pos, coin_radius, 2, "Yellow", "Black")
    o.draw_circle(powerup_pos, powerup_radius, 2, "Blue", "Black")
    o.draw_circle(powerdown_pos, powerdown_radius, 2, "Red", "Black")
    o.draw_polygon([[paddle_pos, 350], [paddle_pos, 360], [paddle_pos + pad_width, 360], [paddle_pos + pad_width, 350]], 3, "Cyan", "DarkBlue")
    

#11- run the program to see if you have successfully created 
#    a ball & a paddle

#12- now the ball and paddle velocity, and give the ball gravity:
    paddle_pos += paddle_vel
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    ball_vel[0] += drift
    ball_vel[1] += gravity
    
#17 test whether the ball touches/collides with the paddle
    if (ball_pos[1] == 330):
        bounce.rewind()
        if(paddle_pos <= ball_pos[0] <= paddle_pos + pad_width):
            ball_vel[1] *= -1
            ball_vel[1] += 0.5
            bounce.play()
            
            drift = random.choice([-0.1, -0.05, -0.07, -0.02, 0.1, 0.05, 0.07, 0.02])
            score += 1
            color = random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Gray"])
            colorborder = random.choice(["DarkRed", "DarkGreen", "DarkBlue", "White"])
            ball_border = colorborder
            ball_main = color
    if ((ball_pos[0] + drift) <0 or (ball_pos[0] + drift) > 800):
        ball_vel[0] *= -1
        
    if (ball_pos[1] > 380):
        if (score > highscore):
            highscore = score
        soundtrack.pause()
        
    if (coin_pos[0] - BALL_RADIUS <= ball_pos[0] <= coin_pos[0] + BALL_RADIUS):
        if(coin_pos[1] - BALL_RADIUS <= ball_pos[1] <= coin_pos[1] + BALL_RADIUS):
            score += 10
            coin_pos = (random.randint(20, 780), random.randint(200, 300))
            
    if (powerup_pos[0] - BALL_RADIUS <= ball_pos[0] <= powerup_pos[0] + BALL_RADIUS):
        if (powerup_pos[1] - BALL_RADIUS <= ball_pos[1] <= powerup_pos[1] + BALL_RADIUS):
            pad_width += 20
            powerup_pos = (random.randint(20, 780), random.randint(200, 300))
    if (powerdown_pos[0] - BALL_RADIUS <= ball_pos[0] <= powerdown_pos[0] + BALL_RADIUS):
        if (powerdown_pos[1] - BALL_RADIUS <= ball_pos[1] <= powerdown_pos[1] + BALL_RADIUS):
            pad_width -= 20
            powerdown_pos = (random.randint(20, 780), random.randint(200, 300))
#18 draw score using 'draw_handler()' function from simplegui
    o.draw_text(str(score), (ball_pos), 24, "White", "serif")
    o.draw_text("Bounce Game", (320, 80), 30, "White", "serif")
    o.draw_text("HighScore: ", (620, 50), 24, "White", "serif")
    o.draw_text(str(highscore), [750, 50], 24, "White", "serif")
    
#19 run the final program to see if ball & paddle collide, 
#   score updates, and new game starts at end of previous game. You're done!

#13- run the program to see if your ball falls now

#15- define 2 functions - 'keydown()' and 'keyup()' - and have them handle 
#    'key' for activating game controls using 'KEY_MAP' from simplegui module:
def keydown(key):
    speed = 12
    global paddle_vel
    
    if key == simplegui.KEY_MAP["left"]:
        paddle_vel -= speed
    elif key == simplegui.KEY_MAP["right"]:
        paddle_vel += speed
def keyup(key):
    speed = 12
    global paddle_vel, pad_width
    
    if key == simplegui.KEY_MAP["left"]:
        paddle_vel += speed
    elif key == simplegui.KEY_MAP["right"]:
        paddle_vel -= speed
    if key == simplegui.KEY_MAP["r"]:
        new_game()
    if key == simplegui.KEY_MAP["up"]:
        pad_width += 20
    if key == simplegui.KEY_MAP["down"]:
        pad_width -= 20
#16- run the program to see if you can move your paddle using controls

#3- create a window or frame using simplegui module and call it 'f':
f = simplegui.create_frame("Bounce Game", WIDTH, HEIGHT)

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
#5- run the program to see if you have successfully created a frame
f.add_label("Left and Right arrow keys to move paddle")
f.add_label("")
f.add_label("Up and Down arrow keys to increase or decrease paddle width")
f.add_label("")
f.add_label("R key to reset")
f.add_label("")
f.add_label("Yellow Circles are worth 10 points")
f.add_label("")
f.add_label("Blue Circles give you increased paddle width")
f.add_label("")
f.add_label("Red Circles give you decreased paddle width")
