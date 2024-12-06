# Write a Python program to check whether a point (x,y) is in a triangle or not. There is a triangle formed by three points.
# Input:
# x1,y1,x2,y2,x3,y3,xp,yp separated by a single space.
# Input three coordinate of the circle: 9 3 6 8 3 6
# Radius of the said circle: 3.358
# Central coordinate (x, y) of the circle: 6.071 4.643

import matplotlib.pyplot as plt

def is_point_in_triangle_barycentric(x1, y1, x2, y2, x3, y3, xp, yp):
    denominator = ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3))
    a = ((y2 - y3) * (xp - x3) + (x3 - x2) * (yp - y3)) / denominator
    b = ((y3 - y1) * (xp - x3) + (x1 - x3) * (yp - y3)) / denominator
    c = 1 - a - b
    
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

# Triangle vertices and test point
x1, y1 = 9, 3
x2, y2 = 6, 8
x3, y3 = 3, 6
xp, yp = 6.071, 4.643

# Check if the point is inside the triangle
point_inside = is_point_in_triangle_barycentric(x1, y1, x2, y2, x3, y3, xp, yp)

# Plot the triangle and point
plt.figure(figsize=(8, 8))
plt.plot([x1, x2], [y1, y2], 'b-')
plt.plot([x2, x3], [y2, y3], 'b-')
plt.plot([x3, x1], [y3, y1], 'b-')
plt.fill([x1, x2, x3], [y1, y2, y3], 'lightblue', alpha=0.4)

plt.scatter([x1, x2, x3], [y1, y2, y3], color='blue', label='Triangle Vertices')
plt.scatter(xp, yp, color='red', label=f'Point {"Inside" if point_inside else "Outside"}')

plt.text(x1, y1, 'A', fontsize=12, ha='right')
plt.text(x2, y2, 'B', fontsize=12, ha='right')
plt.text(x3, y3, 'C', fontsize=12, ha='right')
plt.text(xp, yp, 'P', fontsize=12, ha='left')

plt.title("Point in Triangle (Barycentric) Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
