from display import *
from draw import *
from parserp import *
from matrix import *
from writescript import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

writescript('script')
parse_file( 'script', edges, transform, screen, color )
