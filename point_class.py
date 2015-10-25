import math

class Point:
	def __init__(self, x=1, y=1):
		self.move(x, y)

	def move(self, x, y):
		self.x = x
		self.y = y
		
	def reset(self):
		self.move(0, 0)
	def calculate_distance(self, other_point):
		return math.sqrt(
				(self.x - other_point.x)**2 +
				(self.y - other_point.y)**2 )

	
#p1 = Point()
#p2 = Point()
#p1.reset()
#p2.move(5,0,1)
#print(p2.calculate_distance(p1))

#p1.move(3,4,2)

#assert (p1.calculate_distance(p2) == 
#        p2.calculate_distance(p1))

#print(p2.calculate_distance(p1))
#print(p1.calculate_distance(p1))
