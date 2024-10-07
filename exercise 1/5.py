def is_point_in_rectangle(x1, y1, x2, y2, px, py):
    return x1 <= px <= x2 and y2 <= py <= y1
x1 = 1 
y1 = 7  
x2 = 10 
y2 = 2 
px = 3  
py = 3
if is_point_in_rectangle(x1, y1, x2, y2, px, py):
    print("Точка належить прямокутнику.")
else:
    print("Точка не належить прямокутнику.")
