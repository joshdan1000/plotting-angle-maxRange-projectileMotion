import matplotlib.pyplot as graph
import numpy

# CONSTANTS 
gravity = 9.80665
initialHeight = 100
initialVelocity = 10

def xComponent(angle):
    return initialVelocity * numpy.cos(numpy.radians(angle))

def yComponent(angle):
    return initialVelocity * numpy.sin(numpy.radians(angle))

# initialHeight + (yComponent(angle) * time) - (0.5 * gravity * (time ** 2))


def flightTime(angle):

    a = (-0.5 * gravity)
    b = yComponent(angle)
    c = initialHeight

    discriminant = (b ** 2) - (4 * a * c)
    return (-b - numpy.sqrt(discriminant))/ (2 * a)


def projectileRange(angle):
    return xComponent(angle) * flightTime(angle)



# main loop

x = numpy.linspace(0, 90, 100)
y = projectileRange(x)              

graph.xlabel("Angle / degrees")
graph.ylabel("Range / meters")
graph.title("Projectile Motion: Range vs. Launch Angle")

graph.plot(x, y)

graph.grid(True)
graph.show()
 