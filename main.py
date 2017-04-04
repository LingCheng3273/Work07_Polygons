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
add_sphere(matrix, 200, 200, 200, 50, .1)
#matrix_mult(make_rotX(20), matrix)
#matrix_mult(make_rotY(20), matrix)
#matrix_mult(make_rotZ(20), matrix)
print "done"
draw_polygons(matrix, screen, color)
display(screen)
