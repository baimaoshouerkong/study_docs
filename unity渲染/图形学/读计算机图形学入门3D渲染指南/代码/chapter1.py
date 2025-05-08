import numpy as np
import matplotlib.pyplot as plt


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
        closest_t = float("inf")
        closest_sphere = None
        for s in sphere:
            t1, t2 = self.SphereIntersection(O, D, s)
            if t1 is not None:
                if (
                    t1 > t_min
                    and t1 < t_max
                    and (closest_sphere is None or t1 < closest_t)
                ):
                    closest_t = t1
                    closest_sphere = s
                if (
                    t2 > t_min
                    and t2 < t_max
                    and (closest_sphere is None or t2 < closest_t)
                ):
                    closest_t = t2
                    closest_sphere = s
        if closest_sphere is not None:
            return closest_sphere.color
        return np.array([0, 0, 0])


if __name__ == "__main__":
    # 设置画布尺寸（像素数量）
    width, height = 800, 800
    canvas = Canvan(1, 1, 1)
    canvas.InitView(1, 1)
    O = np.array([0, 0, 0])

    # 创建图像数组
    image = np.zeros((height, width, 3))

    # 计算步长
    step_x = canvas.view.Cw / width
    step_y = canvas.view.Ch / height

    # 遍历每个像素
    for i in range(height):
        y = canvas.view.Ch / 2 - i * step_y  # 从上到下渲染
        for j in range(width):
            x = -canvas.view.Cw / 2 + j * step_x  # 从左到右渲染

            X, Y, Z = canvas.CanvasToViewport(x, y)
            D = np.array([X, Y, Z])
            D = D / np.linalg.norm(D)
            color = canvas.TraceRay(O, D, canvas.sphere_list, 0.1, 100)

            # 将颜色存储到图像数组（颜色值范围从0-255转换到0-1）
            image[i, j] = color / 255.0

    # 显示渲染结果
    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis("off")  # 隐藏坐标轴
    plt.title("Ray Tracing Result")
    plt.show()
