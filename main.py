import turtle
import random



screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('black')

t = turtle.Turtle()

# menu
t.penup()
t.goto(0,200)
t.pendown()
t.pencolor("white")
t.write("Background Colors",font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-75,100)
t.pendown()
t.pencolor("tan")
t.write("1. Tan",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,50)
t.pendown()
t.pencolor("azure")
t.write("2. Azure",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,0)
t.pendown()
t.pencolor("aquamarine")
t.write("3. Aquamarine",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(-75,-50)
t.pendown()
t.pencolor("darkkhaki")
t.write("4. DarkKhaki",font=("arial",20,"normal"),align="left")

t.penup()
t.goto(0,-150)
t.pendown()
t.pencolor("white")
t.write("Choose a Color",font=("arial",30,"normal"),align="center")

choose=int(input("Choose a color: "))
if choose ==1:
     screen.bgcolor("tan")
elif choose ==2:
     screen.bgcolor("azure")
elif choose == 3:
    screen.bgcolor("aquamarine")
else:
    screen.bgcolor("aquamarine")

name = input("Enter your name: ")
num1 = random.randint(-100,100)
num2 = random.randint(-100,100)

sum = num1+num2
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
operation = random.randint(1,4)



t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("blue")
t.write(name,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("green")
t.write(num1,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pencolor("green")
t.write("+",font=("arial",30,"normal"),align="center")
t.pendown()

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("hotpink")
t.write(num2,font=("arial",30,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("red")
t.write("=",font=("arial",30,"normal"),align="center")
t.pendown()

ans = int(input("Please enter your answer: "))


t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("red")
t.write(symbol,font=("arial",30,"normal"),align="center")
t.pendown()

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("black")
t.write("your answer is:" +str(ans),font=("arial",30,"normal"),align="center")
t.pendown()

if ans == sum:
    screen.bgcolor('dodgerblue')
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor("black")
    t.write("your answer is: CORRECT" ,font=("arial",30,"normal"),align="center")
    t.pendown()
else:
    screen.bgcolor('darkorange')
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor("black")
    t.write("your answer is: INCORRECT" ,font=("arial",30,"normal"),align="center")
    t.pendown()
    operation= random.randint(1,4)
    if operation == 1:
        #add
        num1 = random.randint(-100,100)
        num2 = random.randint(-100,100)

        solution = num1 + num2
    elif operation == 2:
        # subract
        num1 = random.randint(-100,100)
        num2 = random.randint(-100,100)

        solution = num1 - num2
    elif operation == 3:
        # multiply
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)

        solution = num1 * num2

    elif operation == 4:
        symbol = "/"
        #divide
        num1=random.radint(-10,10)
        num2 = random.randint(-1,10)
        sign = random.randint(1,2)
        if sign == 2:
            num2 = -1*num2

        solution = num1/ num2







# THIS IS THE LAST LINE OF CODE
turtle.done()