from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, "r")
    commands = f.readlines()
    for x in range(len(commands)):
        commands[x] = commands[x].rstrip()
    for x in range(len(commands)):
        if commands[x] == "line": #args
            inputs = commands[x + 1].split(" ")
            add_edge(points, int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]), int(inputs[4]), int(inputs[5]))
            x += 1
        elif commands[x] == "ident":
            ident(transform)
        elif commands[x] == "scale":  #args
            inputs = commands[x+1].split(" ")
            scale = make_scale(int(inputs[0]), int(inputs[1]), int(inputs[2]))
            matrix_mult(scale, transform)
            x += 1
        elif commands[x] == "move":  #args
            inputs = commands[x + 1].split(" ")
            translate = make_translate(int(inputs[0]), int(inputs[1]), int(inputs[2]))
            matrix_mult(translate, transform)
            x += 1
        elif commands[x] == "rotate":  #args
            inputs = commands[x + 1].split(" ")
            if inputs[0] == "x":
                rotate = make_rotX(int(inputs[1]))
            elif inputs[0] == "y":
                rotate = make_rotY(int(inputs[1]))
            elif inputs[0] == "z":
                rotate = make_rotZ(int(inputs[1]))
            matrix_mult(rotate, transform)
            x += 1
        elif commands[x] == "apply":
            matrix_mult(transform, points)
        elif commands[x] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif commands[x] == "save": #args
            clear_screen(screen)
            draw_lines(points, screen, color)
            name = commands[x + 1]
            ppm = name[:-4]
            ppm += ".ppm"
            save_ppm(screen, ppm)
            #save_extension(screen, name)
        elif commands[x] == "quit":
            break
