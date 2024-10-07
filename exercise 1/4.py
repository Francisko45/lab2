def get_shape_name(sides):
    if sides == 3:
        return "Трикутник"
    if sides == 4:
        return "Чотирикутник"
    if sides == 5:
        return "П'ятикутник"
    if sides == 6:
        return "Шестикутник"
    return "Невідома фігура"  

sides_list = [2, 3, 4, 5, 6]

for sides in sides_list:
    shape_name = get_shape_name(sides)
    print(f"Кількість сторін: {sides} -> {shape_name}")
