import turtle
import math
bob = turtle.Turtle()
bob.delay = 1.0
print(bob)

def square(t, length):
	for i in range(4):
		t.fd(length)
		t.lt(45)

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360/n)

polygon(bob, 100, 10)

turtle.mainloop()

# fixed 
ádfádfádfádfádf
