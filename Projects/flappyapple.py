# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
# create your player character
s1 = create_sprite("applecore",0,0)
# set background
set_background("skyyy7777")
# set the starting value for variable
points = 0
# Section 3: Controls
# define controls
def move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)

# pick keys for each control
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

# Section 4: Game Loop
window.listen()
timer = 0
obstacles = []
lives = 3
while True:
	time.sleep(0.1)
	timer += 1 
	s1.goto(s1.xcor(), s1.ycor()-10)
	if timer % 50 == 0:
		y_position = random.randint (-250, 250)
		s2 = create_sprite ("woworm (1)",300,y_position)
		s2.setheading(180)
		obstacles.append(s2)
	for s2 in obstacles:
		s2.forward(10)
		if get_distance(s1,s2) < 50:
			lives -= 1
			s1.hideturtle()
	 
    
 	# code for automatic actions
	if s1.ycor() > 250: 
		break 

	if lives == 0:
		break
	
	if s1.ycor() < -160:
		break 



	window.update()

	# if :
	#	break
	

print ("Game Over!")
s3 = turtle.Turtle()
s3.write("Game Over!",font = ("Arial", 40, "normal"))
window.update()
time.sleep(2)