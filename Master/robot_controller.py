

import numpy as np

previous_state = [0,-1]
command_string =''
NO_TURN = [0,0]
TURN_90 = [-1,-1]
TURN_270 = [1,1]
square_distance = int(2000/45)
output_file = 'Output/robot_commands.txt'


def get_robot_commands(path):
    global previous_state, command_string
    command_string += 'def when_started1():\n'
    for index, point in enumerate(path):
        if index < len(path)-1:
            delta_x = np.subtract(path[index+1],path[index])
            imu_data = np.subtract(delta_x,previous_state)
            #print(delta_x)
            #print(imu_data)
            previous_state = delta_x

            if (imu_data == NO_TURN).all():
                command_string+='\tdrivetrain.turn_for(LEFT, 0, DEGREES)\n'
            elif (imu_data == TURN_90).all():
                command_string+='\tdrivetrain.turn_for(LEFT, 90, DEGREES)\n'
            elif (imu_data == TURN_270).all():
                command_string+='\tdrivetrain.turn_for(LEFT, 270, DEGREES)\n'
            command_string+= '\tdrivetrain.drive_for(FORWARD, {}, MM)\n'.format(square_distance)
    command_string += 'vr_thread(when_started1)\n'
    
    print(command_string)
    with open (output_file, 'w') as robot_io:
        robot_io.write(command_string)