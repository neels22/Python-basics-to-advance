


class Line():
    def __init__(self,coordinate1,coordinate2) :
        
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2 

    def distance(self):
        x1,y1 = self.coordinate1
        x2,y2 = self.coordinate2

        return ( ((x2-x1)**2)  +((y2-y1)**2)  )**0.5
    

    def slope(self):
        x1,y1 = self.coordinate1
        x2,y2 = self.coordinate2

        return (y2-y1) / (x2-x1)
    


# sending the coordinates as a tuple 
# doing tuple unpacking 

c1 = (3,2)  
c2 = (3,7)

myline = Line(c1,c2)
distance_between_points = myline.distance()
print("distance between two pionts is ",distance_between_points," units")
        