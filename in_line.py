def in_line(point1, point2, x):
    k = (point1[1] - point2[1]) / (point1[0] - point2[0])
    delta_y = k * (x - point1[0])
    return point1[1] + delta_y


