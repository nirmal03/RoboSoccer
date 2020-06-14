# Autonmous RoboSoccer

This repository pertains to the files for the B.Tech Project for the Autonomous RoboSoccer

## Steps Plotted towards Goal

### step 1: Knowing the Playfield

[Through analysis](./Documentation/RoboSoccer_Analysis_Combined.pdf) of the field and technologies used in various RoboSoccer bots as well as competitions

- [Various kinds and Complexities](./Documentation/Part I\_Various kinds and Complexities.pdf)
- [Communication Methods and Strategies](./Documentation/Part II_Communication Protocols and Strategies.pdf)
- [The Past, The Present and The Future](./Documentation/"Part III_The Past, The Present and The Future.pdf")

### step 2: Choosing the right approach

After the Analysis was complete, we were familiar with most of the ways we could tackle the problem but we decided to start from simple object detection and taking a modular approach and then adding complexities as the project progresses.

### step 3: Object Detection and Movement

Assumptions :

- 1 vs 1 arrangement
- Color of Ball is fixed and known
- Color of Goal is fixed and known
- Color of Opponent is fixed and known

Used openCV to mask out the boundary of the required object (ball, goal, opponent).
Find Distance and Angle respective to the bot, of the object.
Move the bot as per distance and angle according to following algorithm
[Detailed Algorithms](#)

```python

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

```

### step 4: Transfer of Data between Bot and Central Compute unit

To improve the computing power and reduce latency between detection and respective movement, it was decided to have a separate computing unit that would act as a controling hub and help give directions to the bot.
This can be avoided in view of more powerfull hardware such as Rpi 4b.
This also includes the knowledge whether the ball is captured by self or opponent

###### For Video from RPi to Control Unit

Used ImageZMQ as the transfer medium.
Used server-client architecture

###### For Action from Control Unit to Rpi/Arduino

Preferentially Bluetooth
To be Updated

### To Implement

- Ability to identify teammate and increase crowd.
- Add machine learning to improve object detection and imporve decision making by predicting ball movement and opponent movement.

##### Setup

To be Updated

##### Note:

- Python 3 with OpenCV 4.0 has been used as software base
- Raspberry Pi with Arduino and Pi camera as Hardware base
- This is a work in progress and would be continually updated

###### Update:

- Due to Covid19, getting hands-on the hardware needed was not possible and hence till date we are working with virtuallization and trying to be as close and accurate as possible.
