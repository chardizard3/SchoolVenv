from vpython import *

ballR=0.50;
wallT=0.1;
wallL=10;
wallW=48;
wallH=40

botwall = box(pos=vector(0,-wallH/2,0), color=color.white, size=vector(wallW,wallT,wallL))
topwall = box(pos=vector(0,wallH/2,0), color=color.white, size=vector(wallW,wallT,wallL))
leftwall = box(pos=vector(-wallW/2,0,0), color=color.white, size=vector(wallT,wallH,wallL))
rightwall = box(pos=vector(wallW/2,0,0), color=color.white, size=vector(wallT,wallH,wallL))
backwall = box(pos=vector(0,0,-wallL/2), color=color.white, size=vector(wallW, wallH, wallT))

marble = sphere(radius=ballR,color=color.red, make_trail=True)

velocity = vector(1, 1, 1)
dt = 1

while True:
    rate(10)
    marble.pos = marble.pos + velocity * dt
    if abs(marble.pos.y) > wallH/2 - ballR:
        velocity.y = -velocity.y
    if abs(marble.pos.x) > wallW/2 - ballR:
        velocity.x = -velocity.x
    if abs(marble.pos.z) > wallL/2 - ballR:
        velocity.z = -velocity.z
