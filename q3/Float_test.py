def bfloat_to_float(num):
    exp_num = int(num[0:3],2)
    deci_num = int(num[3:],2)
    val = (1+(deci_num/32))*(2**(exp_num))
    return val

def float_to_bfloat(num):
    num_l = num.split(".")
    int_binary = bin(int(num_l[0]))[2:]
    if (len(num_l) == 1):
        n_deci_val = 0
    else:
        n_deci_val = len(num_l[1])

    exp = 0
    if (len(int_binary) > 1):
        exp = len(int_binary) - 1
    #print("exp : ",exp)

    now_num = int(float(num)*(2**n_deci_val))
    #print("now_num : ",now_num)
    float_binary = bin(now_num)[2:]
    #print("float_binary : ",float_binary)

    exp_b = bin(exp)[2:]
    if (len(exp_b)<3):
        exp_b = (3-len(exp_b))*'0' + exp_b
    elif (len(exp_b)>3):
        return -1
    #print(exp_b)

    mantissa = float_binary[len(float_binary)-exp-n_deci_val:]
    if (len(mantissa)<5):
        mantissa = mantissa + (5-len(mantissa))*'0'
    elif (len(mantissa)>5):
        return -1
    #print(mantissa)

    float_arithmatic = exp_b + mantissa
    return float_arithmatic

print(bfloat_to_float("00110000"))
# print(float_to_bfloat("3"))