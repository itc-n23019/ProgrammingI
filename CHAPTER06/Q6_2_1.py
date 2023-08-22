class Cylinder:
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = float(radius)
        self.height = float(height)

    def calc_base_area(self):
        pi = Cylinder.pi
        r = self.radius
        return pi * r * r

    def calc_side_area(self):
        pi = Cylinder.pi
        r = self.radius
        h = self.height
        return 2 * pi * r * h

    def calc_surface_area(self):
        c = self.calc_base_area()
        s = self.calc_side_area()
        return 2 * c + s

    def calc_volume(self):
        c = self.calc_base_area()
        h = self.height
        return c * h

    def show_results(self):
        r = self.radius
        h = self.height
        s = self.calc_surface_area()
        v = self.calc_volume()
        print('半径: {:.1f}, 高さ: {:.1f}, 表面積: {:.1f}, 体積: {:.1f}'.format(r, h, s, v))

c1 = Cylinder()
c1.show_results()
c2 = Cylinder(1.0, 3.0)
c2.show_results()
c3 = Cylinder(2.0, 1.0)
c3.show_results()
c4 = Cylinder(2.0, 3.0)
c4.show_results()

