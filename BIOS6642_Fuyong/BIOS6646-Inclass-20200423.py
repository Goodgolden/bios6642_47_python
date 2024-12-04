class Rectangle:
        def __init__(self, x, y, w, h):
            if w<0 and h<0:
                raise ValueError('Negative')
            self.x=x
            self.y=y
            self.w=w
            self.h=h
        def get_perimeter (self):
            p=2*(self.w+self.h)
            return p
        def get_area(self):
            return self.w*self.h
        def is_inside(self, a, b):
            if (a<(self.x+self.w) and a>self.x) and (b<(self.y+self.h) and b>self.h):
                 return True
            else:
                 return False
##########
def get_overlap_area(r1, r2):
    if (r2.x<(r1.x+r1.w) and r2.x>r1.x) and (r2.y<(r1.y+r1.h) and r2.y>r1.y):
        oa=(r1.x+r1.w-r2.x)*(r1.y+r1.h-r2.y)
        return oa
    else:
        return 0
def get_distance(r1, r2):
    import math
    sq=((r2.x+r2.w/2)-(r1.x+r1.w/2))**2+((r2.y+r2.h/2)-(r1.y+r1.h/2))**2
    return math.sqrt(sq)
#########
r1=Rectangle(2, 3, 5, 7)
r2=Rectangle(5, 9, 2, 8)
print("area: ", r1.get_area(), r2.get_area())
print("perimeter: ", r1.get_perimeter(), r2.get_perimeter())
print("is point(6, 16) in rec1: ", r1.is_inside(6,16))
print("is point(6, 16) in rec2: ", r2.is_inside(6,16))
print("overlap: ", get_overlap_area(r1, r2))
print("distance: ", get_distance(r1, r2))
