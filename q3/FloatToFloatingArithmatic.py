#num = '1.5'   # binary: 1.1, floating=> exp : 000, mantissa : 10000
#num = '3' i.e 1.5*n_deci_val    # binary: 11, floating=> exp : 001, mantissa : 10000

#num = '3.75'    # binary: 11.11, floating=> exp : 001, mantissa : 11100
num = '10.375'   # binary : 1010.011
num_l = num.split(".")
int_binary = bin(int(num_l[0]))[2:]
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

print(exp_b)

mantissa = float_binary[len(float_binary)-exp-n_deci_val:]
if (len(mantissa)<5):
    mantissa = mantissa + (5-len(mantissa))*'0'

print(mantissa)

float_arithmatic = exp_b + mantissa
print(float_arithmatic)