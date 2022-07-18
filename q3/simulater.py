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

# Type A
def add_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    sum = bin(int(register_list[reg1],2) + int(register_list[reg2],2))
    sum = sum[2:]

    if (len(sum)>16):
        register_list[reg3] = '0000000000000000'
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
        register_list[reg3] = '0000000000000000'
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
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)

    reg1_val = int(register_list[reg1],2)
    reg2_val = int(register_list[reg2],2)
    
    reg3_val = bin(reg1_val ^ reg2_val)
    reg3_val = reg3_val[2:]

    if (len(reg3_val)<16):
        reg3_val = (16 - len(reg3_val))*"0" + reg3_val
    register_list[7] = '0000000000000000'
    register_list[reg3] = reg3_val

    PC+=1

def or_func(machine_ins):
    global PC
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
    register_list[7] = '0000000000000000'
    register_list[reg3] = reg3_val

    PC+=1

def and_func(machine_ins):
    global PC
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
    register_list[7] = '0000000000000000'
    register_list[reg3] = reg3_val
    
    PC+=1

# Type B
def movi(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = machine_ins[8:]
    register_list[reg] = "00000000"+imm

    register_list[7] = '0000000000000000'
    PC+=1

def rs(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = int(machine_ins[8:],2)
    if (imm > 16):
        register_list[reg] = "0000000000000000"
    else:
        register_list[reg] = register_list[reg][imm:]
        register_list[reg] = register_list[reg] + imm*"0"
    
    register_list[7] = '0000000000000000'
    PC+=1
        
def ls(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = int(machine_ins[8:],2)
    if (imm > 16):
        register_list[reg]="0000000000000000"
    else:
        register_list[reg] = register_list[reg][0:(16-imm)]
        register_list[reg] = imm*"0" + register_list[reg]
    
    register_list[7] = '0000000000000000'
    PC+=1

# Type C
def movreg(machine_ins):
    global PC
    global register_list
    reg1 = machine_ins[7:12]
    reg2 = machine_ins[12:]
    reg1_i = int(reg1, 2)
    reg2_i = int(reg2, 2)
    register_list[reg1_i] = register_list[reg2_i]
    PC += 1

def divide(machine_ins):
    global PC
    global register_list
    reg3 = machine_ins[7:12]
    reg4 = machine_ins[12:]
    reg1_i = int(reg3, 2)
    reg2_i = int(reg4, 2)
    q_val = bin(int(register_list[reg1_i], 2) // int(register_list[reg2_i], 2))[2:]
    r_val = bin(int(register_list[reg1_i], 2) % int(register_list[reg2_i], 2))[2:]
    while len(q_val) < 16:
        q_val = '0' + q_val

    while len(r_val) < 16:
        r_val = '0' + r_val

    register_list[0] = q_val
    register_list[1] = r_val
    PC += 1

def invert(machine_ins):
    global PC
    global register_list
    reg1 = machine_ins[7:12]
    reg2 = machine_ins[12:]
    reg1_i = int(reg1, 2)
    reg2_i = int(reg2, 2)
    reg1_val = register_list[reg1_i]
    reg1_val = int(reg1_val, 2)
    reg1_val = ~reg1_val
    reg1_val = bin(reg1_val)[2:]
    while len(reg1_val) < 16:
        reg1_val = '0' + reg1_val

    register_list[reg2_i] = reg1_val
    PC += 1

def cmp(machine_ins):
    global PC
    global register_list
    reg1 = machine_ins[7:12]
    reg2 = machine_ins[12:]
    reg1_i = int(reg1, 2)
    reg2_i = int(reg2, 2)
    reg1_val = int(register_list[reg1_i], 2)
    reg2_val = int(register_list[reg2_i], 2)
    if reg1_val > reg2_val:
        temp_flag = register_list[7]
        temp_flag = list(temp_flag)
        temp_flag[14] = '1'
        register_list[7] = ''.join(temp_flag)
    elif reg1_val < reg2_val:
        temp_flag = register_list[7]
        temp_flag = list(temp_flag)
        temp_flag[13] = '1'
        register_list[7] = ''.join(temp_flag)
    else:
        temp_flag = register_list[7]
        temp_flag = list(temp_flag)
        temp_flag[15] = '1'
        register_list[7] = ''.join(temp_flag)
    PC += 1

# Type D
def ld(instruction):
    global mem
    global  register_list
    global PC
    reg = instruction[5:8]
    mem_add = instruction[8:]
    register_list[int(reg,2)]=mem[int(mem_add,2)]
    PC +=1

def st(instruction):
    global register_list
    global mem
    global PC
    reg = instruction[5:8]
    mem_add = instruction[8:]
    a = int(mem_add,2)
    mem[a]=register_list[int(reg,2)]
    PC +=1

# Type E
def jmp(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    PC=mem_add

def jlt(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    l=register_list[7][13]
    if l==1:
        PC=mem_add
    else:
        PC+=1

def jgt(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    g=register_list[7][14]
    if g==1:
        PC=mem_add
    else:
        PC+=1

def je(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    e=register_list[7][15]
    if e==1:
        PC=mem_add
    else:
        PC+=1

# Floating Point
def addf(machine_ins):      # 1.001 + 0.010 = (2**(-3)) (1001 + 0010)
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    sum = bin(int(register_list[reg1][8:],2) + int(register_list[reg2][8:],2))
    sum = sum[2:]

    if (len(sum)>8):
        register_list[reg3] = '0000000000000000'
        # overflow flag is set
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)

    elif (len(sum)<=8):
        sum = (16 - len(sum))*"0" + sum
        register_list[7] = '0000000000000000'
        register_list[reg3] = sum

    PC+=1

def subf(machine_ins):          # 1.001 - 0.010 = (2**(-3)) (1001 - 0010)
    global PC
    global register_list
    reg1 = int(machine_ins[7:10],2)
    reg2 = int(machine_ins[10:13],2)
    reg3 = int(machine_ins[13:16],2)
    diff = int(register_list[reg1][8:],2) - int(register_list[reg2][8:],2)
    if (diff < 0):
        register_list[reg3] = '0000000000000000'
        # overflow flag is set
        temp_flag = list(register_list[7])
        temp_flag[12] = '1'
        register_list[7] = ''.join(temp_flag)

    else:
        diff = bin(diff)
        diff = diff[2:]

        if (len(diff)<8):
            diff = (16 - len(diff))*"0" + diff
        register_list[7] = '0000000000000000'
        register_list[reg3] = diff

    PC+=1

def movf(machine_ins):
    global PC
    global register_list
    reg = int(machine_ins[5:8],2)
    imm = machine_ins[8:]
    register_list[reg] = "00000000"+imm

    register_list[7] = '0000000000000000'
    PC+=1


MEM = open('tezt.txt','r')
l = []
l_final=[]
for _ in MEM:
    l.append(_)
for i in l:
    l_final.append(i[:16])
# print(l_final)
PC=0
def b_pc(PC):
    b_pc = bin(PC)[2:]
    while len(b_pc)<8:
        b_pc = "0"+b_pc
    return b_pc
for q in range(256):
    instruction = l_final[PC]
    print(b_pc(PC), end=" ")
    if instruction[:5] == "10000":
        add_func(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10001":
        sub_func(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10010":
        movi(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10100":
        ld(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10101":
        st(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10110":
        mul_func(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11000":
        rs(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11001":
        ls(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11010":
        xor_func(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11011":
        or_func(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11100":
        and_func(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11111":
        jmp(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01100":
        jlt(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01101":
        jgt(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01111":
        je(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10011":
        movreg(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "10111":
        divide(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11101":
        invert(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "11110":
        cmp(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "00000":
        addf(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "00001":
        subf(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "00010":
        movf(instruction)
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
    elif instruction[:5] == "01010":
        for items in range(7):
            print(register_list[items],end = " ")
        print()
        # for i in range(256):
        #     print(mem[i])
        break
