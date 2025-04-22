import turtle 
#create turtle 
t = turtle.Turtle()
# set speed to 100
t.speed( 100 )

t.color("pink")
# make the background black 
turtle.Screen().bgcolor("black")


t.begin_fill()
colors = ["PowderBlue", "Aqua", "Cyan", "pink", "LightCyan"]
for i in range ( 1000 ):
    t.color( colors[ i % 5 ])
    t.forward( 100 + i)
    t.left( 250 + 1)
    t.left( 250 + 1)
t.end_fill()

turtle.exitonclick()