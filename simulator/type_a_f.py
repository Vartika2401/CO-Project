#register_list = [r0,r1,r2,r3,r4,r5,r6,flags]
register_list = ['0000000000000000','0000000000001000','0000000000000011','0000000000000000','0000000000000000','0000000000000000','0000000000000000']


def add_func(machine_ins):
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    sum = bin(int(register_list[reg1],2) + int(register_list[reg2],2))
    sum = sum[2:]

    if (len(sum)>16):
        register_list[reg3] = '1111111111111111'
        print("add : owerflow flag is set")
        # owerflow flag is set
    elif (len(sum)<16):
        sum = (16 - len(sum))*"0" + sum
    register_list[reg3] = sum


def sub_func(machine_ins):
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    diff = int(register_list[reg1],2) - int(register_list[reg2],2)
    if (diff < 0):
        register_list[reg3] = '1111111111111111'
        print("sub : owerflow flag is set")
        # owerflow flag is set
    else:
        diff = bin(diff)
        diff = diff[2:]

        if (len(diff)<16):
            diff = (16 - len(diff))*"0" + diff
        register_list[reg3] = diff


def mul_func(machine_ins):
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    prod = bin(int(register_list[reg1],2) * int(register_list[reg2],2))
    prod = prod[2:]
    if (len(prod)>16):
        register_list[reg3] = '1111111111111111'
        print("add : owerflow flag is set")
        # owerflow flag is set
    elif (len(prod)<16):
        prod = (16 - len(prod))*"0" + prod
    register_list[reg3] = prod


def xor_func(machine_ins):
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)

    reg1_val = int(register_list[reg1],2)
    reg2_val = int(register_list[reg2],2)
    
    reg3_val = bin(reg1_val ^ reg2_val)
    reg3_val = reg3_val[2:]

    if (len(reg3_val)<16):
        reg3_val = (16 - len(reg3_val))*"0" + reg3_val
    register_list[reg3] = reg3_val


def or_func(machine_ins):
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)

    reg1_val = int(register_list[reg1],2)
    reg2_val = int(register_list[reg2],2)
    
    reg3_val = bin(reg1_val | reg2_val)
    reg3_val = reg3_val[2:]

    if (len(reg3_val)<16):
        reg3_val = (16 - len(reg3_val))*"0" + reg3_val
    register_list[reg3] = reg3_val


def and_func(machine_ins):
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)

    reg1_val = int(register_list[reg1],2)
    reg2_val = int(register_list[reg2],2)
    
    reg3_val = bin(reg1_val & reg2_val)
    reg3_val = reg3_val[2:]

    if (len(reg3_val)<16):
        reg3_val = (16 - len(reg3_val))*"0" + reg3_val
    register_list[reg3] = reg3_val


#add_func("1000000001010011")
#print("add: ",register_list)
#add_func("1000000001010011")
#print("add: ",register_list)
#sub_func("1000000001010011")
#print("sub: ",register_list)
#mul_func("1000000001010011")
#print("mul: ",register_list)
#xor_func("1000000001010011")
#print("xor: ",register_list)
#or_func("1000000001010011")
#print("or: ",register_list)
#and_func("1000000001010011")
#print("and: ",register_list)