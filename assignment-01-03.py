""" 
3. Write a code that generates a nested list with 2D point coordinates to generate a XY point grid.
Expected result: list_points = [[[x1,y1], [x1,y2], ..., [x1,yn]], ..., [[xm,y1], ..., [xm,yn]]]
"""
import matplotlib.pyplot as plt

x_size = 10
y_size = 6

xy_point_grid = []

### insert code here
for x in range(x_size):
    row = []
    for y in range(y_size):
        row.append([x, y])
    xy_point_grid.append(row)


print(xy_point_grid)

print(xy_point_grid)

def display_pt(xy_point_grid):
    for row in xy_point_grid:
        for pt in row:
            plt.plot(pt[0], pt[1], 'bo')

plt.figure()
display_pt(xy_point_grid)
plt.axis('equal')
plt.show()