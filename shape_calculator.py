class Rectangle:
    width = 0
    height = 0

    def __init__(self, w, h) :
        self.width = w
        self.height = h
    
    def set_width(self, w) :
        self.width = w
    
    def set_height(self, h) :
        self.height = h

    def get_area(self) :
        res = self.width * self.height
        return res
    
    def get_perimeter(self) :
        res = 2 * self.width + 2 * self.height
        return res

    def get_diagonal(self) :
        res = ((self.width ** 2 + self.height ** 2) ** .5)
        return res

    def get_picture(self) :
        if self.width > 50 or self.height > 50 :
            res = "Too big for picture."
        else :
            res = ""
            for i in range(self.height) :
                for j in range(self.width) :
                    res = res + '*'
                res = res + '\n'
        return res

    def get_amount_inside(self, shape) :
        fit_wide = int(self.width / shape.width)
        fit_height = int(self.height / shape.height)
        fit_times = fit_wide * fit_height
        return fit_times  

    def __str__(self) :
        res = f"Rectangle(width={self.width}, height={self.height})"
        return res


class Square(Rectangle):

    def __init__(self, length) :
        self.width = length
        self.height = length

    def set_side(self, length) :
        self.width = length
        self.height = length

    def set_width(self, w) :
        self.width = w
        self.height = w

    def set_height(self, h) :
        self.width = h
        self.height = h

    def __str__(self) :
        res = f'Square(side={self.width})'
        return res