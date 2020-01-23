import turtle

def draw_square(some_turtle):
    for x in range(0,4):
        some_turtle.forward(200)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #create an instance of a turtle named brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    #call the loop of drawing a square
    draw_square(brad)

    for x in range (1,20):
        brad.right(20)
        draw_square(brad)


    window.exitonclick()

draw_art()