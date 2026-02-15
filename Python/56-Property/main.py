class Rectangle:
    def __init__(self,witdh,height):
        self._witdh=witdh
        self._height=height
    
    @property
    def witdh(self):
        return f"{self._witdh:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @witdh.setter
    def witdh(self,new_witdh):
        if new_witdh>0:
            self._witdh=new_witdh
        else:
            print("Width must be greater than zero")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("Height must be greater than zero")
    @witdh.deleter
    def witdh(self):
        del self._witdh
        print("Witdh has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
        



rectangle=Rectangle(3,4)
rectangle.witdh=5

del rectangle.witdh
del rectangle.height

print(rectangle.witdh)
print(rectangle.height)