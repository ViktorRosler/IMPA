# project all points onto the plane x+y+z=1
# find their convex hull
# check if 'solution' is in this hull

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def subtract(self, p):
    	return Point(self.x - p.x, self.y - p.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

def cross_product(p1, p2):
	return p1.x * p2.y - p2.x * p1.y

def direction(p1, p2, p3):
	return cross_product(p3.subtract(p1), p2.subtract(p1))

def distance_sq(p1, p2):
	return (p1.x-p2.x)**2 + (p1.y - p2.y)**2

def jarvis_march(points):
    # find the leftmost point
    a =  min(points, key = lambda point: point.x)
    index = points.index(a)
    
    # selection sort
    l = index
    result = []
    result.append(a)
    while (True):
        q = (l + 1) % len(points)
        for i in range(len(points)):
            if i == l:
                continue
            # find the greatest left turn
            # in case of collinearity, consider the farthest point
            d = direction(points[l], points[i], points[q])
            if d > 0 or (d == 0 and distance_sq(points[i], points[l]) > distance_sq(points[q], points[l])):
                q = i
        l = q
        if l == index:
            break
        result.append(points[q])

    return result

def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
 
def orientation(p, q, r):
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
        return 1
    elif (val < 0):
        return 2
    else:
        return 0
 
# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def doIntersect(p1,q1,p2,q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    if ((o1 != o2) and (o3 != o4)):
        return True
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
    return False

def is_inside_polygon(points, p):
     
    n = len(points)
     
    # There must be at least 3 vertices
    # in polygon
         
    # Create a point for line segment
    # from p to infinite
    extreme = Point(100000000, p.y)
    count = i = 0
     
    while True:
        next = (i + 1) % n
        if (doIntersect(points[i], points[next], p, extreme)):
                             
            if orientation(points[i], p, points[next]) == 0:
                return onSegment(points[i], p, points[next])                     
            count += 1   
        i = next   
        if (i == 0):
            break
    return (count % 2 == 1)

import sys

sys.stdin = open("802.txt")

for case in range(1,10000):
	mixtures = int(sys.stdin.readline())

	if mixtures == 0:
		break

	m = []
	for i in range(mixtures):
		a = sys.stdin.readline().strip().split()
		x = int(a[0]) / (int(a[0]) + int(a[1]) + int(a[2]))
		y = int(a[1]) / (int(a[0]) + int(a[1]) + int(a[2]))  
		m.append(Point(x,y))

	a = sys.stdin.readline().strip().split()
	x = int(a[0]) / (int(a[0]) + int(a[1]) + int(a[2]))
	y = int(a[1]) / (int(a[0]) + int(a[1]) + int(a[2]))
	goal = Point(x,y)

	# calculate convex hull
	n = jarvis_march(m)

	if case > 1:
		print()
	print("Mixture", case)
	if is_inside_polygon(n,goal):
		print("Possible")
	else:
		print("Impossible")	



