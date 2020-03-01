def writescript(fname):
    f = open(fname, 'w')
    intro = '''
instructions for the field:
line
0 250 -250 500 250 -250
line
500 250 -250 500 250 750
line
500 250 750 0 250 750
line
0 250 750 0 250 -250
line
0 250 250 200 250 250
line
300 250 250 500 250 250
line
250 250 -250 250 250 200
line
250 250 300 250 250 750
instructions for the gaussian surface:
line
200 250 200 300 250 200
line
300 250 200 300 250 300
line
300 250 300 200 250 300
line
200 250 300 200 250 200
line
200 150 200 300 150 200
line
300 150 200 300 150 300
line
300 150 300 200 150 300
line
200 150 300 200 150 200
line
200 150 200 200 350 200
line
200 350 200 300 350 200
line
300 350 200 300 150 200
line
200 350 200 200 350 300
line
200 350 300 300 350 300
line
300 350 300 300 350 200
line
200 150 300 200 350 300
line
300 150 300 300 350 300
    '''
    f.write(intro)

    x1 = 33
    y1 = 100
    y2 = 400
    while x1 < 500:
        z1 = -225
        while z1 < 750:
            f.write('line\n{0} 100 {1} {0} 400 {1}\n'.format(x1, z1))
            f.write('line\n{0} 400 {1} {2} {3} {1}\n'.format(x1, z1, x1 - 5, 395))
            f.write('line\n{0} 400 {1} {2} {3} {1}\n'.format(x1, z1, x1 + 5, 395))
            f.write('line\n{0} 100 {1} {2} {3} {1}\n'.format(x1, z1, x1 - 5, 105))
            f.write('line\n{0} 100 {1} {2} {3} {1}\n'.format(x1, z1, x1 + 5, 105))
            print("bruh!!")
            z1 += 50
        x1 += 50

    outro = '''
ident
rotate
z 10
rotate
x 10
rotate
y 20
apply
display
save
pic.png
'''

    f.write(outro)
    f.close()
