s_coordi_list = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]

def str_to_float_coordi (s_coordi):  
    p = s_coordi.split(",") 
    return list (map (float, p))

def str_to_float_coordi_iter(s_coordi_list):
    return map(str_to_float_coordi, s_coordi_list) 

f_coordi_list=list(str_to_float_coordi_iter(s_coordi_list))

print (f_coordi_list)

