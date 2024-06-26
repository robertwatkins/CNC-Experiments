gcode = [""]
gcode.append("T2 M6;")
gcode.append("G0  Z1.0000 G43 H1;")
gcode.append("G90;")
gcode.append("S2000 M3;")
gcode.append("G21;")
gcode.append("G0 Z5;")
gcode.append("G0 X100 Y100 F100;")

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
    gcode.append(f"G1 X{x:.2f} Y{y:.2f} Z{z:.2f} F100")

gcode.append("G1 Z-2.5;")
gcode.append("G1 X200 Y100 F100;")
gcode.append("M5;")
gcode.append("G0 Z30;")

# Print or save gcode
for line in gcode:
    print(line)
