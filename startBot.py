

"""

FOR 1V1

if ball not in captured range
    if ball in vision 
        rotate till ball in center of vision
        move towards ball till in captured range
    else
        rotate till ball in vision


if ball in captured range
    if goal in vision 
        rotate till goal in center of vision
        move towards goal till in captured range
    else
        rotate till goal in vision

"""


from moveBot import rotate_left, rotate_right, moveForward
from findPosition import getAngle, getBallPosition, getDistance, getGoalPosition
from capture import init, getFrame, end

init()


while(True):
    # captured = False
    capturedDistance = 5
    goalDistance = 2
    ball = getBallPosition()
    goal = getGoalPosition()
    ballDist = getDistance(ball)
    goalDist = getDistance(goal)
    if(ballDist > capturedDistance):
        captured = False
    if(captured and goalDist <= goalDistance):
        break
    if(not captured):
        angle = getAngle(ball)
        if(angle != None):
            if(angle < -10):
                rotate_left(abs(angle))
            elif(angle > +10):
                rotate_right(abs(angle))
            else:
                if(ballDist <= capturedDistance):
                    captured = True
                else:
                    moveForward()
                # dist = getDistance(ball)
                # while(dist > capturedDistance):
                #     moveForward()
        else:
            rotate_left(90)

    else:
        angle = getAngle(goal)
        if(angle != None):
            if(angle < -10):
                rotate_left(abs(angle))
            elif(angle > +10):
                rotate_right(abs(angle))
            else:
                moveForward()
        else:
            rotate_left(90)

end()
