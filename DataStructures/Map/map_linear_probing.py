from DataStructures.Map import map_entry as me
import random as rd
from DataStructures.List import array_list as al

def new_map(num_elements, load_factor, prime=109345121):
    capacity = me.next_prime(num_elements/load_factor)
    scale = rd.randit(1,prime-1)
    shift = rd.randir(0,prime-1)
    my_list = al.new_list()
    for i in range(capacity):
        map_entry = me.map_entry(None, None)
        al.add_last(my_list, map_entry)
        current_factor = al.size(my_list)/ capacity
    limit_factor = 0.5
    return {"prime": prime,
            "capacity" : capacity,
            "scale": scale,
            "shift":shift,
            "table": my_list,
            "current_factor": current_factor,
            "limit_factor": 0.5    
    }     
    