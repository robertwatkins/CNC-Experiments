import gcode

tools = []
tools.append(gcode.tool(2,"90deg 5mm Conical"))
this_machine = gcode.machine("MillRite","GRBL", \
                             ["T2 M6;","G0  Z1.0000 G43 H1;","G90;","S2000 M3;","G21;","G0 Z5;","G0 X100 Y100 F100;"], \
                             ["G1 Z-2.5;","G1 X200 Y100 F100;","M5;","G0 Z30;"])

project = gcode.project(tools, this_machine)

start_depth = 0
end_depth = -2.5
steps = 100  # Number of steps for interpolation
x_increment = 200 / steps
y_increment = 100 / steps
z_increment = (end_depth - start_depth) / steps

for i in range(1, steps + 1):
    x = i * x_increment
    y = i * y_increment
    z = start_depth + i * z_increment
    command = f"G1 X{x:.2f} Y{y:.2f} Z{z:.2f} F100"
    project.commands.append(command)

project.finalize()

#show all details of the project
#print(project)

#show just the resulting gcode
for command in project.commands:
    print(command)
