
#importing packages
import turtle
import random
import sys
import time


"""position of snakes on the board"""
snakes = {
        8 : 3,
        20 : 1,
        24 : 14
        }

"""position of ladders on the board"""
ladders = {
        5 : 15,
        9 : 12,
        18 : 23
        }

"""coordinates corresponding to their position on board"""
coordinates = {
        1: (-250, -230), 2: (-135, -230) , 3: (-15, -230) , 4:(105, -230) , 5:(225, -230) ,
        10: (-250, -80), 9: (-135, -110) , 8: (-15, -110), 7: (105, -110) , 6: (225, -110) ,
        11: (-250, 10) , 12: (-135, 10) , 13: (-15, 10) , 14: (105, 10) , 15: (225, 10) ,
        20: (-250, 130) , 19:(-135, 130) , 18:(-15, 130) , 17: (105, 130), 16:(225, 130) ,
        21: (-250, 250), 22: (-135, 250) , 23:(-15, 250) , 24:(105, 250) , 25: (225, 250)
        }



"""Function to make box (of blue colour),"""
#it has 3 input parameters...
#t = turtle
#x = x-coordinate
#y = y-coordinate
def draw_box(t,x,y):
    t.penup()
    t.speed(0)
    t.pensize(3)
    t.color("blue")
    t.goto(x,y)
    t.pendown()
    for i in range(0,4):
        t.hideturtle()
        board.forward(120)
        board.right(90)


"""Function to write the square numbers on the board"""
#it has 4 input parameters...
#t = turtle
#x = x-coordinate
#y = y-coordinate
def write_num(t,x,y,text):
    t.penup()
    t.speed(0)
    t.pensize(3)
    t.color("red")
    t.goto(x,y)
    t.pendown()
    t.write(text,font=("Verdana",15, "bold"))





"""Function to add image to the turtle,"""
#it has 3 input parameters...
#x = x-coordinate
#y = y-coordinate
def addImage(x, y, img):
    tr = turtle.Turtle()
    tr.shape(img)
    tr.penup()
    tr.goto(x, y)
    return tr


def addImage1(x, y, img):
    tr = turtle.Turtle()
    tr.shape(img)
    tr.penup()
    tr.speed(0)
    tr.goto(x, y)
    return tr

"""Function to fetch the dice value, using random's randint package"""
def get_dice_value():
    dice_value = random.randint(1, 6)
    if dice_value == 1:
        d1 = addImage1(-350, 0, "dice1.gif")

    elif dice_value == 2:
        d2 = addImage1(-350, 0, "dice2.gif")

    elif dice_value == 3:
        d3 = addImage1(-350, 0, "dice3.gif")

    elif dice_value == 4:
        d4 = addImage1(-350, 0, "dice4.gif")

    elif dice_value == 5:
        d5 = addImage1(-350, 0, "dice5.gif")

    else:
        d6 = addImage1(-350, 0, "dice6.gif")

    return dice_value



"""Function to find the final-position of a player after rolling the dice """
def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > 25:
        print(f"You need {25-old_value} to win this game.")
        return old_value

    if player_name == "Big Bad Bull:":
        player_turtle = bull
    else:
        player_turtle = cow

    value = current_value
    moveTurtle(player_turtle, value)

    if current_value in snakes:
        final_value = snakes[current_value]
    elif current_value in ladders:
        final_value = ladders[current_value]
    else:
        final_value = current_value

    return final_value




"""Function to move the respective turtles/players """
def moveTurtle(player_turtle, value):
    player_turtle.speed(2)
    return player_turtle.goto(coordinates[value])




"""Function to check if the player has won"""
def check_win(player_name, position):
    if 25 == position:
        win = turtle.Turtle()
        newScreen = turtle.Screen()
        newScreen.bgcolor("white")
        newScreen.addshape("win.gif")
        addImage(0, 0, "win.gif")
        print("Congratulations " + player_name.rstrip(":"))
        time.sleep(3)
        sys.exit(1)




"""Main function to start the game"""
def start():
    print("\nNew Game!")

    player1, player2 = "Big Bad Bull:", "Fluffy Cow:"
    player1_cur_pos, player2_cur_pos = 0, 0

    while True:
        p1 = input(f"\n{player1} Hit enter to roll the dice: ")
        dice_value = get_dice_value()
        player1_cur_pos = snake_ladder(player1, player1_cur_pos, dice_value)
        print(f"You're on square: {player1_cur_pos}")
        moveTurtle(bull, player1_cur_pos)
        check_win(player1, player1_cur_pos)



        p2 = input(f"\n{player2} Hit enter to roll the dice: ")
        dice_value = get_dice_value()
        player2_cur_pos = snake_ladder(player2, player2_cur_pos, dice_value)
        print(f"You're on square: {player2_cur_pos}")
        moveTurtle(cow, player2_cur_pos)
        check_win(player2, player2_cur_pos)




if __name__ == "__main__":
    turtle.title("Snake & Ladders")
    turtle.setup(width=800, height=700)

    #Drawing game's board 5x5
    board = turtle.Turtle()
    for i in range(0,5):
        for j in range(0,5):
            draw_box(board, -300 + j*120, -175 + i*120)



    #writing numbers on the board
    #numbers 1-5
    num = 1
    for i in range(0, 5):
        write_num(board, -285+ i*120, -200, num)
        num += 1

    #numbers 6-10
    num = 10
    for i in range(0, 5):
        write_num(board, -285+ i*120, -80, num)
        num -= 1

    #numbers 11-15
    num = 11
    for i in range(0, 5):
        write_num(board, -285+ i*120, 40, num)
        num += 1

    #numbers 16-20
    num = 20
    for i in range(0, 5):
        write_num(board, -285+ i*120, 160, num)
        num -= 1

    #numbers 21-25
    num = 21
    for i in range(0, 5):
        write_num(board, -285+ i*120, 280, num)
        num += 1




    #Adding images to the game: snakes, ladders, players
    screen = turtle.Screen()
    screen.addshape("snake.gif")
    screen.addshape("snake2.gif")
    screen.addshape("snake3.gif")
    screen.addshape("ladder.gif")
    screen.addshape("ladder2.gif")
    screen.addshape("ladder3.gif")
    screen.addshape("bull.gif")
    screen.addshape("cow.gif")
    screen.addshape("dice1.gif")
    screen.addshape("dice2.gif")
    screen.addshape("dice3.gif")
    screen.addshape("dice4.gif")
    screen.addshape("dice5.gif")
    screen.addshape("dice6.gif")

    snake1 = addImage(120, 110, "snake.gif")
    snake2 = addImage(0, -150, "snake2.gif")
    snake3 = addImage(-240, -50, "snake3.gif")
    ladder = addImage(-110, -60, "ladder.gif")
    ladder2 = addImage(5, 170, "ladder2.gif")
    ladder3 = addImage(243, -120, "ladder3.gif")
    bull = addImage(-250, -230, "bull.gif")
    cow = addImage(-250, -260, "cow.gif")

    #Main function to start the game.
    start()


    screen.mainloop()
    turtle.done()
