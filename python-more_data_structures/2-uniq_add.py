#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Siyahını toplusuna (set) çevir – təkrarlananlar silinir
    result = 0
    for number in unique_numbers:
        result += number
    return result
