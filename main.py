from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print


#parse_file( 'script', edges, transform, screen, color )
matrix= []
#add_polygon(matrix, 100, 100, 100, 100, 200, 200, 300, 200, 200)
add_box(matrix, 100, 100, 100, 50, 50, 50)
draw_polygons(matrix, screen, color)
display(screen)
