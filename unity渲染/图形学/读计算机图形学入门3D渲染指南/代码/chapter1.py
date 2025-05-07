import numpy as np


class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color


class View:
    def __init__(self, Cw, Ch):
        self.Cw = Cw
        self.Ch = Ch


class Canvan:
    def __init__(self, Vw, Vh, Vz):
        self.Vw = Vw
        self.Vh = Vh
        self.Vz = Vz
        self.sphere_1 = Sphere(np.array([0, -1, 3]), 1, np.array([255, 0, 0]))
        self.sphere_2 = Sphere(np.array([2, 0, 4]), 1, np.array([0, 0, 255]))
        self.sphere_3 = Sphere(np.array([-2, 0, 4]), 1, np.array([0, 255, 0]))
        self.sphere_list = [self.sphere_1, self.sphere_2, self.sphere_3]

    def InitView(self, Cw, Ch):
        self.view = View(Cw, Ch)

    def CanvasToViewport(self, x, y):
        return x * self.Vw / self.view.Cw, y * self.Vh / self.view.Ch, self.Vz

    def SphereIntersection(self, O, D, sphere):
        L = sphere.center - O
        tca = np.dot(L, D)
        d2 = np.dot(L, L) - tca * tca
        r2 = sphere.radius * sphere.radius
        if d2 > r2:
            return None, None
        thc = np.sqrt(r2 - d2)
        t1 = tca - thc
        t2 = tca + thc
        return t1, t2

    def TraceRay(self, O, D, sphere, t_min, t_max):
        closest_t = None
        closest_sphere = None
        for s in sphere:
            t1, t2 = self.SphereIntersection(O, D, s)
            if t1 is None and t2 is not None:
                closest_t = t2 if t1 > t2 else t1
                closest_sphere = s
        if closest_t is not None and t_min < closest_t < t_max:
            return closest_sphere.color
        return np.array([0, 0, 0])


if __name__ == "__main__":
    canvas = Canvan(800, 600, 1)
    canvas.InitView(800, 600)
    O = np.array([0, 0, 0])
    for y in range(-300, 300):
        for x in range(-400, 400):
            X, Y, Z = canvas.CanvasToViewport(x, y)
            D = np.array([X, Y, Z])
            D = D / np.linalg.norm(D)
            color = canvas.TraceRay(O, D, canvas.sphere_list, 0.1, 100)
            print(f"Pixel ({x}, {y}): Color: {color}")
