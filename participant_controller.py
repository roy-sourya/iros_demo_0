from controller import Robot

# Initialize the robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Obtain waypoints
waypoints = []
waypoints_string = robot.getCustomData().split()
for i in range(10):
    waypoints_element = [float(waypoints_string[2*i]), float(waypoints_string[2*i+1])]
    waypoints.append(waypoints_element)
print('Waypoints:', waypoints)

# Initialize devices
motor_left = robot.getDevice('wheel_left_joint')
motor_right = robot.getDevice('wheel_right_joint')
gps = robot.getDevice('gps')

motor_left.setVelocity(0.0)
motor_right.setVelocity(0.0)

motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

gps.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    print('Hello World from Python!', gps.getValues())
    motor_left.setVelocity(5.0)
    motor_right.setVelocity(5.0)
    if gps.getValues()[0] > -1.5:
        break

print('Bye from Python!')
