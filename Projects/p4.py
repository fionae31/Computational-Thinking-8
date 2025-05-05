# Section 1 - Helper functions
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite


# Section 2 - Variables
# values are added to variables 
x1 = -200
y1 = -125
x2 = -200
y2 = -20
x3 = -200
y3 = 60
x4 = -200
y4 = 150

# Section 3 - Setup
# background is set and sprites are created 
set_background("castle")
t1 = create_sprite("applecore",x1,y1)
t2 = create_sprite("bike",x2,y2)
t3 = create_sprite("fish",x3,y3)
t4 = create_sprite("kitten",x4,y4)


# # Section 4 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# x2 and x4 are randomly set to choose a speed between the numbers in parentheses, while x1 and x3 are set numbers already
for i in range(30):
	x1 += 6
	x2 += random.randint(0,25)
	x3 += 10
	x4 += random.randint(3,20)
	t1.goto(x1, y1)
	t2.goto(x2, y2)
	t3.goto(x3, y3)
	t4.goto(x4, y4)
	time.sleep(0.1)


# Section 5 - Winner
# this section displays the winner based on previous information 
if x1 >= x2 and x1 >= x3 and x1 >= x4:
	print("player 1 wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
	print("player 2 wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
  print("player 3 wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
  print("player 4 wins!")


turtle.exitonclick()