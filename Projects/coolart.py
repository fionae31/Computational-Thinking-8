import turtle 
#create turtle 
t = turtle.Turtle()


t.color("pink")
# make the background black 
turtle.Screen().bgcolor("black")



colors = ["PowderBlue", "Aqua", "Cyan", "pink", "LightCyan"]
for i in range ( 100 ):
    t.color( colors[ i % 5 ])
    t.forward( 100 + i)
    t.left( 250 + 1)
    t.left( 250 + 1)
# make the speed 100
    t.speed( 100 )

t.penup()
t.goto ( 250, 100 )
t.pendown()

colors = ["pink", "red", "GreenYellow", "Thistle", "Gold"]
for i in range ( 100 ): 
    t.color( colors[ i % 5 ])
    t.forward( 100 + i)
    t.left( 250 + 1)
    t.left( 250 + 1)

t.penup()
t.goto ( -100, 240)
t.pendown()

colors = ["NavyBlue", "LightPink", "HotPink", "Lavender", "Gold"]
for i in range ( 100 ): 
    t.color( colors[ i % 5 ])
    t.forward( 100 + i)
    t.left( 250 + 1)
    t.left( 250 + 1)

t.penup()
t.goto ( -120, -30)
t.pendown()

colors = ["Darkred", "LightPink", "Cyan", "Violet", "Blue"]
for i in range ( 100 ): 
    t.color( colors[ i % 5 ])
    t.forward( 100 + i)
    t.left( 250 + 1)
    t.left( 250 + 1)

t.penup()
t.goto ( 200, -50)
t.pendown()

colors = ["Blue", "Chartreuse", "Thistle", "Plum", "Magenta"]
for i in range ( 100 ): 
    t.color( colors[ i % 5 ])
    t.forward( 100 + i)
    t.left( 250 + 1)
    t.left( 250 + 1)

turtle.exitonclick()