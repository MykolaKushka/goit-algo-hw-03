import matplotlib.pyplot as plt
import numpy as np  

def koch_curve(order, size):
    if order == 0:
        return [(0, 0), (size, 0)]
    else:
        points = koch_curve(order - 1, size / 3)
        new_points = []
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            sx = p1[0] + dx / 3
            sy = p1[1] + dy / 3
            tx = p1[0] + 2 * dx / 3
            ty = p1[1] + 2 * dy / 3
            ux = sx + (tx - sx) * 0.5 - (ty - sy) * (3 ** 0.5) / 2
            uy = sy + (tx - sx) * (3 ** 0.5) / 2 + (ty - sy) * 0.5
            new_points.append(p1)
            new_points.append((sx, sy))
            new_points.append((ux, uy))
            new_points.append((tx, ty))
        new_points.append(points[-1])
        return new_points

def koch_snowflake(order, size):
    curve = koch_curve(order, size)
    points = curve[:]
    angle = 120
    for _ in range(2):
        rotated_points = [(x * np.cos(np.radians(angle)) - y * np.sin(np.radians(angle)), 
                           x * np.sin(np.radians(angle)) + y * np.cos(np.radians(angle))) 
                          for (x, y) in curve]
        curve = rotated_points
        for p in rotated_points:
            points.append(p)
        angle += 120
    return points

def main(order):
    size = 400
    snowflake = koch_snowflake(order, size)
    x, y = zip(*snowflake)
    
    plt.figure(figsize=(8, 8))
    plt.plot(x, y)
    plt.title(f"Koch Snowflake of order {order}")
    plt.axis('equal')
    plt.show()

# Запит рівня рекурсії у користувача
order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
main(order)
