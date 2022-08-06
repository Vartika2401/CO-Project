import sys
register_list = ['0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000']
opcode = {"add": ["10000", "a"],
          "sub": ["10001", "a"],
          "movi": ["10010", "b"],
          "mov": ["10011", "c"],
          "ld": ["10100", "d"],
          "st": ["10101", "d"],
          "mul": ["10110", "a"],
          "div": ["10111", "c"],
          "rs": ["11000", "b"],
          "ls": ["11001", "b"],
          "xor": ["11010", "a"],
          "or": ["11011", "a"],
          "and": ["11100", "a"],
          "not": ["11101", "c"],
          "cmp": ["11110", "c"],
          "jmp": ["11111", "e"],
          "jlt": ["01100", "e"],
          "jgt": ["01101", "e"],
          "je": ["01111", "e"],
          "hlt": ["01010", "f"],
          "addf": ["00000", "a"],
          "subf": ["00001", "a"],
          "movf": ["00010", "b"]

          }
register_dict = {'R0': '000',
                 'R1': '001',
                 'R2': '010',
                 'R3': '011',

                 'R4': '100',
                 'R5': '101',
                 'R6': '110',
                 'FLAGS': '111'}
mem = ["0000000000000000" for i in range(256)]
def movi(instruction):
    global  PC
    global register_list
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg==register_dict["R"+str(i)]:
            register_list[i]="00000000"+str(imm)
    PC+=1
    register_list[7]='0000000000000000'
def rs(instruction):
    global PC
    global register_list
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg == register_dict["R" + str(i)]:
            #print(int(imm,2))
            if int(imm,2)>16:
                register_list[i]="0000000000000000"
            else:
                register_list[i]=register_list[i][0:16-int(imm,2)]
                while len(register_list[i])<16:
                    register_list[i]="0"+register_list[i]
                # print(register_list[i])
    PC+=1
    register_list[7]='0000000000000000'
def ls(instruction):
    global PC
    global register_list
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg == register_dict["R" + str(i)]:
            # print(int(imm, 2))
            if int(imm, 2) > 16:
                register_list[i] = "0000000000000000"
            else:
                register_list[i] = register_list[i][int(imm, 2):]
                while len(register_list[i]) < 16:
                    register_list[i] = register_list[i]+"0"
                # print(register_list[i])
    PC+=1
    register_list[7]='0000000000000000'
def add_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    sum = bin(int(register_list[reg1],2) + int(register_list[reg2],2))
    sum = sum[2:]

    if (len(sum)>16):
        register_list[reg3] = sum[-16:]
        # overflow flag is set
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)

    elif (len(sum)<=16):
        sum = (16 - len(sum))*"0" + sum
        register_list[7] = '0000000000000000'
        register_list[reg3] = sum
    PC+=1
def sub_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    diff = int(register_list[reg1],2) - int(register_list[reg2],2)
    if (diff < 0):
        register_list[reg3] = '0000000000000000'
        # overflow flag is set
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)

    else:
        diff = bin(diff)
        diff = diff[2:]

        if (len(diff)<16):
            diff = (16 - len(diff))*"0" + diff
        register_list[7] = '0000000000000000'
        register_list[reg3] = diff
    PC+=1
def mul_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    prod = bin(int(register_list[reg1],2) * int(register_list[reg2],2))
    prod = prod[2:]
    if (len(prod)>16):
        register_list[reg3] = prod[-16:]
        # overflow flag is set
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)

    elif (len(prod)<=16):
        prod = (16 - len(prod))*"0" + prod
        register_list[7] = '0000000000000000'
        register_list[reg3] = prod

    PC+=1
def xor_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)

    reg1_val = int(register_list[reg1], 2)
    reg2_val = int(register_list[reg2], 2)

    reg3_val = bin(reg1_val ^ reg2_val)
    reg3_val = reg3_val[2:]

    if (len(reg3_val) < 16):
        reg3_val = (16 - len(reg3_val)) * "0" + reg3_val
    register_list[7] = '0000000000000000'
    register_list[reg3] = reg3_val

    PC += 1
def or_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)
    # print(reg1,reg2,reg3)
    reg1_val = int(register_list[reg1], 2)
    reg2_val = int(register_list[reg2], 2)

    reg3_val = bin(reg1_val | reg2_val)
    # print(reg1_val,reg2_val,reg3_val)
    reg3_val = reg3_val[2:]
    # print(reg3_val)

    if (len(reg3_val) < 16):
        reg3_val = (16 - len(reg3_val)) * "0" + reg3_val
    register_list[7] = '0000000000000000'
    register_list[reg3] = reg3_val

    PC += 1
def and_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)

    reg1_val = int(register_list[reg1], 2)
    reg2_val = int(register_list[reg2], 2)

    reg3_val = bin(reg1_val & reg2_val)
    reg3_val = reg3_val[2:]

    if (len(reg3_val) < 16):
        reg3_val = (16 - len(reg3_val)) * "0" + reg3_val
    register_list[7] = '0000000000000000'
    register_list[reg3] = reg3_val

    PC += 1
def ld(instruction):
    global mem
    global  register_list
    global PC
    global y
    global x
    global mem_dict
    PC += 1
    reg = instruction[5:8]
    mem_add = instruction[8:]
    register_list[int(reg,2)]=mem[int(mem_add,2)]
    mem_dict[x[-1]]=int(mem_add,2)
    register_list[7]='0000000000000000'
def st(instruction):
    global register_list
    global mem
    global PC
    global y
    global mem_dict
    global x
    PC += 1
    reg = instruction[5:8]
    mem_add = instruction[8:]
    a = int(mem_add,2)
    mem[a]=register_list[int(reg,2)]
    mem_dict[x[-1]]=a
    register_list[7]='0000000000000000'
def jmp(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[8:]
    # print(mem_add)
    PC=int(mem_add,2)
    register_list[7]='0000000000000000'
    # print(PC)
def jlt(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[8:]
    l=register_list[7][13]
    if l=='1':
        PC=int(mem_add,2)
    else:
        PC+=1

    register_list[7]='0000000000000000'
def jgt(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[8:]
    g=register_list[7][14]
    if g=="1":
        PC=int(mem_add,2)
    else:
        PC+=1

    register_list[7]='0000000000000000'
def je(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[8:]
    e=register_list[7][15]
    # print(e)
    if e=="1":
        PC=int(mem_add,2)
    else:
        PC+=1
    # print(PC)
    register_list[7]='0000000000000000'
def movreg(machine_ins):
    global PC
    global register_list
    reg1 = machine_ins[10:13]
    reg2 = machine_ins[13:]
    reg1_i = int(reg1, 2)
    reg2_i = int(reg2, 2)
    register_list[reg2_i] = register_list[reg1_i]
    PC += 1
    register_list[7]='0000000000000000'
def divide(machine_ins):
    global PC
    global register_list
    reg3 = machine_ins[10:13]
    reg4 = machine_ins[13:]
    reg1_i = int(reg3, 2)
    reg2_i = int(reg4, 2)
    #print(reg2_i,reg1_i)
    q_val = bin(int(register_list[reg1_i], 2) // int(register_list[reg2_i], 2))[2:]
    r_val = bin(int(register_list[reg1_i], 2) % int(register_list[reg2_i], 2))[2:]
    while len(q_val) < 16:
        q_val = '0' + q_val

    while len(r_val) < 16:
        r_val = '0' + r_val

    register_list[0] = q_val
    register_list[1] = r_val
    PC += 1
    register_list[7]='0000000000000000'
def invert(machine_ins):
    global PC
    global register_list
    reg1 = machine_ins[10:13]
    #print(reg1)
    reg2 = machine_ins[13:]
    #print(reg2)
    reg1_i = int(reg1, 2)
    reg2_i = int(reg2, 2)
    reg1_val = register_list[reg1_i]
    # print(list(reg1_val))
    answer = []
    for i in list(reg1_val):
        x = str(1-int(i))
        answer.append(x)
    reg1_val = "".join(answer)
    while len(reg1_val) < 16:
        reg1_val = '0' + reg1_val

    register_list[reg2_i] = reg1_val

    PC += 1
    register_list[7]='0000000000000000'
def cmp(machine_ins):
    global PC
    global register_list
    reg1 = machine_ins[10:13]
    reg2 = machine_ins[13:]
    reg1_i = int(reg1, 2)
    reg2_i = int(reg2, 2)
    # print(reg1_i,reg2_i)
    reg1_val = int(register_list[reg1_i], 2)
    reg2_val = int(register_list[reg2_i], 2)
    # print(reg1_val,reg2_val)
    if reg1_val > reg2_val:
        # print("g")
        temp_flag = register_list[7]
        temp_flag = list(temp_flag)
        temp_flag[14] = '1'
        register_list[7] = ''.join(temp_flag)
    elif reg1_val < reg2_val:
        # print("s")
        temp_flag = register_list[7]
        temp_flag = list(temp_flag)
        temp_flag[13] = '1'
        register_list[7] = ''.join(temp_flag)
        # print(register_list[7])
    else:
        # print("e")
        temp_flag = register_list[7]
        temp_flag = list(temp_flag)
        temp_flag[15] = '1'
        register_list[7] = ''.join(temp_flag)
        # print(register_list[7])

    PC += 1
def bfloat_to_float(num):
    # print("bfloat to float for",num)
    num = str(num)
    exp_num = int(num[0:3],2)
    # print("exp_num",exp_num)
    deci_num = int(num[3:],2)
    # print("deci_num",deci_num)
    val = (1+(deci_num/32))*(2**(exp_num))
    # print(val)
    return val

def float_to_bfloat(num):
    num = str(num)
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


def addf(machine_ins):      # 1.001 + 0.010 = (2**(-3)) (1001 + 0010)
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    # print(reg1)
    # print(register_list[reg1][8:])
    reg1_val = bfloat_to_float(register_list[reg1][8:])
    # print(reg1_val)
    # print(register_list[reg2][8:])
    reg2_val = bfloat_to_float(register_list[reg2][8:])

    reg3_val = reg1_val + reg2_val
    if (float_to_bfloat(reg3_val) == -1):
        # overflow flag is set
        register_list[reg3] = '0000000011111111'
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)
    else:
        register_list[7] = '0000000000000000'
        register_list[reg3] = '00000000'+float_to_bfloat(reg3_val)
    PC+=1

def subf(machine_ins):          # 1.001 - 0.010 = (2**(-3)) (1001 - 0010)
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    reg1_val = bfloat_to_float(register_list[reg1][8:])
    reg2_val = bfloat_to_float(register_list[reg2][8:])

    reg3_val = reg1_val - reg2_val
    if (float_to_bfloat(reg3_val) == -1 or reg3_val<0):
        # overflow flag is set
        register_list[reg3] = '0000000000000000'
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)
    else:
        register_list[7] = '0000000000000000'
        register_list[reg3] = '00000000'+float_to_bfloat(reg3_val)
    PC+=1

def movf(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = machine_ins[8:]
    register_list[reg] = "00000000"+imm

    register_list[7] = '0000000000000000'
    PC+=1


MEM = sys.stdin
output = sys.stdout
mem_dict = {}

l = []
l_final=[]
for _ in MEM:
    l.append(_)
mem_count=0
for i in l:
    l_final.append(i[:16])
    mem[mem_count]=i[:16]
    # print(mem_count)
    mem_count+=1
# print(l_final)
PC=0
halted = False
x_axis = 0
x =[]
y=[]
def b_pc(PC):
    b_pc = bin(PC)[2:]
    while len(b_pc)<8:
        b_pc = "0"+b_pc
    return b_pc
while halted==False:
    instruction = l_final[PC]
    # print(PC)
    y.append(PC)
    x.append(x_axis+1)
    x_axis+=1
    output.write(str(b_pc(PC))+ " ")
    if instruction[:5] == "10000":
        add_func(instruction)
        for items in range(8):
            output.write(str(register_list[items])+" ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10001":
        sub_func(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10010":
        movi(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10100":
        ld(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10101":
        st(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10110":
        mul_func(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11000":
        rs(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11001":
        ls(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11010":
        xor_func(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11011":
        or_func(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11100":
        and_func(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11111":
        jmp(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01100":
        jlt(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01101":
        jgt(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01111":
        je(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10011":
        movreg(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10111":
        divide(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11101":
        invert(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11110":
        cmp(instruction)
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "00000":
        addf(instruction)
        for items in range(8):
            output.write(register_list[items] + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "00001":
        subf(instruction)
        for items in range(8):
            output.write(register_list[items] + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "00010":
        movf(instruction)
        for items in range(8):
            output.write(register_list[items] + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01010":
        register_list[7]="0000000000000000"
        for items in range(8):
            output.write(str(register_list[items]) + " ")
        output.write("\n")
        # for i in range(256):
        #     print(mem[i])
        halted=True
        break
for i in range(256):
    output.write(str((mem[i])) + "\n")

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.scatter
