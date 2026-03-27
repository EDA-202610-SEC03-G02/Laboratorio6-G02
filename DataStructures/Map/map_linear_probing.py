from DataStructures.Map import map_entry as me
import random as rd
from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mf

def rehash(my_map):
    new_table = new_map(my_map["size"], my_map["limit_factor"], my_map["prime"])
    for i in range(my_map["capacity"]):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        value = me.get_value(entry)
        if key is not None and key != "empty":
            put(new_table, key, value)
    my_map["table"] = new_table["table"]
    my_map["capacity"] = new_table["capacity"]
    my_map["size"] = new_table["size"]
    my_map["current_factor"] = new_table["current_factor"]

    return new_table
    

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
    scale = rd.randint(1,prime-1)
    shift = rd.randint(0,prime-1)
    my_list = al.new_list()
    for i in range(capacity):
        map_entry = me.new_map_entry(None, None)
        al.add_last(my_list, map_entry)
    current_factor = 0
    return {"prime": prime,
            "capacity" : capacity,
            "scale": scale,
            "shift":shift,
            "table": my_list,
            "current_factor": current_factor,
            "limit_factor": load_factor,
            "size": 0 
    }     

def find_slot(my_map, key, hash_value):
    capacity = my_map["capacity"]
    table = my_map["table"]
    
    first_empty = None
    
    while True:
        entry = al.get_element(table, hash_value)
        key_actual= me.get_key(entry)
        
        if key_actual is None:
            if first_empty is not None:
                return False, first_empty
            return False, hash_value
        
        if key == key_actual:
            return True, hash_value
        
        if key_actual == "empty":
            if first_empty is None:
                first_empty = hash_value
                
        hash_value = (hash_value + 1) % capacity

def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)

    found, pos = find_slot(my_map, key, hash_value)

    if found:
    
        entry = al.get_element(my_map["table"], pos)
        me.set_value(entry, value)

    else:
        
        entry = me.new_map_entry(key, value)
        
        al.change_info(my_map["table"], pos, entry)
        
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)

    return my_map

def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_value)
    return found

def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_value)
    if found:
        entry = al.get_element(my_map["table"], pos)
        return me.get_value(entry)
    return None
    
def remove(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_val)

    if found:
        al.change_info(my_map["table"], pos, me.new_map_entry("empty", None))
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]

    return my_map

def size(my_map):
    return my_map["size"]


