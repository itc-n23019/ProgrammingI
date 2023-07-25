s_coordi_list = ["1.0.2.2.3.5", "2.1.3.2.5.5", "1.2.1.3.2.2", "2.1.3.1.4.5"]

def parse_coord(coord_str):
    return list(map(float, coord_str.split('.')))

f_coordi_list = list(map(parse_coord, s_coordi_list))

print(f_coordi_list)

