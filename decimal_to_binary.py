def decimal_to_binary(n):
    converted_num_list = []
    n = int(n)
    while n > 0:
        rem = n%2
        converted_num_list.append(rem)
        n = n//2
    converted_num_list = converted_num_list[::-1]
    converted_num=''.join(converted_num_list) 
    return converted_num