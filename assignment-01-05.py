import math
import matplotlib.pyplot as plt

def display_pl(polyline):
    xs, ys = [], []
    for pt in polyline.points:
        xs.append(pt.x)
        ys.append(pt.y)
    plt.plot(xs,ys)

class Point3d():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    @property
    def data(self):
        return (self.x, self.y, self.z)
    
class Polyline():
    def __init__(self, points):
        self.points = points

    def length(self):
        length = 0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            length += math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2)
        return length

# Create class here
points = [Point3d(0, 0, 0), Point3d(1, 1, 1), Point3d(2, 2, 2), Point3d(3, 3, 3)]
polyline_obj = Polyline(points)

polyline_length = polyline_obj.length()
print(polyline_length)
plt.figure()
display_pl(polyline_obj)
plt.show()
