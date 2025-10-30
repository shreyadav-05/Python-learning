#create a class (2-D vector)and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self ,x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

        def __repr__(self):
            return f"Vector2D({self.x},{self.y})"
        
        def as_tuple(self):
            return(self.x, self.y)
        
        class vector3D(Vector2D):
            def __init__(self,x: float = 0.0, y: float = 0.0, z: float = 0.0 ):
                super().__init__(x, y)
                self.z = z

                def __repr__(self):
                    return f"Vector3D({self.x},{self.y},{self.z})"
                
                def as_tuple(self):
                    return (self.x,self.y,self.z)