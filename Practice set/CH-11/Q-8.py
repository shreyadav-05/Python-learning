#Override the __len__() method on vector of problem 5 to display the dimension of the vector.
class vector:
    def __init__(self, l):

        self.l = l

    def __add__(self,other):
        result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other .x + self.y * other.y + self.z * other.z
        return result
    
    def __len__(self):
        return len(self.l)
    

    
    #test the implementation
v1 = vector({1, 2, 3})
print(len(v1))
          
    
 