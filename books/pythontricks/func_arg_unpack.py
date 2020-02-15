
vec_list = [1, 2, 3,]
vec_tup = (1, 2, 3,)
vec_dict = {'x': 1, 'y': 2, 'z': 3,}
vec_gen = (x for x in range(3))

def prin_vec(x, y, z):
    print(f'<({x}, {y}, {z})>') 

prin_vec(1,2,3)
prin_vec(*vec_tup)
prin_vec(*vec_list)
prin_vec(**vec_dict)
prin_vec(*vec_gen)
