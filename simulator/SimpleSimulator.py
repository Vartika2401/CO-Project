import sys
register_list = ['0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000']
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
          "hlt": ["01010", "f"]

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
def rs(instruction):
    global PC
    global register_list
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg == register_dict["R" + str(i)]:
            print(int(imm,2))
            if int(imm,2)>16:
                register_list[i]="0000000000000000"
            else:
                register_list[i]=register_list[i][0:16-int(imm,2)]
                while len(register_list[i])<16:
                    register_list[i]="0"+register_list[i]
                print(register_list[i])
    PC+=1
def ls(instruction):
    global PC
    global register_list
    reg = instruction[5:8]
    imm = instruction[8:]
    for i in range(7):
        if reg == register_dict["R" + str(i)]:
            print(int(imm, 2))
            if int(imm, 2) > 16:
                register_list[i] = "0000000000000000"
            else:
                register_list[i] = register_list[i][int(imm, 2):]
                while len(register_list[i]) < 16:
                    register_list[i] = register_list[i]+"0"
                print(register_list[i])
    PC+=1
def add_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)
    sum = bin(int(register_list[reg1], 2) + int(register_list[reg2], 2))
    sum = sum[2:]
    PC+=1
    if (len(sum) > 16):
        register_list[reg3] = '1111111111111111'
        print("add : owerflow flag is set")
        # owerflow flag is set
    elif (len(sum) < 16):
        sum = (16 - len(sum)) * "0" + sum
    register_list[reg3] = sum
def sub_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)
    diff = int(register_list[reg1], 2) - int(register_list[reg2], 2)
    PC+=1
    if (diff < 0):
        register_list[reg3] = '1111111111111111'
        print("sub : owerflow flag is set")
        # owerflow flag is set
    else:
        diff = bin(diff)
        diff = diff[2:]

        if (len(diff) < 16):
            diff = (16 - len(diff)) * "0" + diff
        register_list[reg3] = diff
def mul_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)
    prod = bin(int(register_list[reg1], 2) * int(register_list[reg2], 2))
    prod = prod[2:]
    PC+=1
    if (len(prod) > 16):
        register_list[reg3] = '1111111111111111'
        print("add : owerflow flag is set")
        # owerflow flag is set
    elif (len(prod) < 16):
        prod = (16 - len(prod)) * "0" + prod
    register_list[reg3] = prod
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
    PC+=1
    if (len(reg3_val) < 16):
        reg3_val = (16 - len(reg3_val)) * "0" + reg3_val
    register_list[reg3] = reg3_val
def or_func(machine_ins):
    global PC
    global register_list
    reg1 = int(machine_ins[7:10], 2)
    reg2 = int(machine_ins[10:13], 2)
    reg3 = int(machine_ins[13:16], 2)

    reg1_val = int(register_list[reg1], 2)
    reg2_val = int(register_list[reg2], 2)

    reg3_val = bin(reg1_val | reg2_val)
    reg3_val = reg3_val[2:]
    PC +=1
    if (len(reg3_val) < 16):
        reg3_val = (16 - len(reg3_val)) * "0" + reg3_val
    register_list[reg3] = reg3_val
def and_func(machine_ins):
    global PC
    PC+=1
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
    register_list[reg3] = reg3_val
def ld(instruction):
    global mem
    global  register_list
    global PC
    PC += 1
    reg = instruction[5:8]
    mem_add = instruction[8:]
    register_list[int(reg,2)]=mem[int(mem_add,2)]
def st(instruction):
    global register_list
    global mem
    global PC
    PC += 1
    reg = instruction[5:8]
    mem_add = instruction[8:]
    a = int(mem_add,2)
    mem[a]=register_list[int(reg,2)]
def jmp(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    PC=mem_add
def jlt(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    l=register_list[6][13]
    if l==1:
        PC=mem_add
    else:
        PC+=1
def jgt(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    g=register_list[6][14]
    if g==1:
        PC=mem_add
    else:
        PC+=1
def je(machine_ins):
    global PC
    global register_list
    mem_add=machine_ins[9:]
    e=register_list[6][15]
    if e==1:
        PC=mem_add
    else:
        PC+=1
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
        temp_flag = register_list[6]
        temp_flag = list(temp_flag)
        temp_flag[14] = '1'
        register_list[6] = ''.join(temp_flag)
    elif reg1_val < reg2_val:
        temp_flag = register_list[6]
        temp_flag = list(temp_flag)
        temp_flag[13] = '1'
        register_list[6] = ''.join(temp_flag)
    else:
        temp_flag = register_list[6]
        temp_flag = list(temp_flag)
        temp_flag[15] = '1'
        register_list[6] = ''.join(temp_flag)

    PC += 1
MEM = sys.stdin
output = sys.stdout
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
    output.write(b_pc(PC))
    if instruction[:5] == "10000":
        add_func(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10001":
        sub_func(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10010":
        movi(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10100":
        ld(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10101":
        st(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10110":
        mul_func(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11000":
        rs(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11001":
        ls(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11010":
        xor_func(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11011":
        or_func(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11100":
        and_func(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11111":
        jmp(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "01100":
        jlt(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "01101":
        jgt(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "01111":
        je(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10011":
        movreg(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "10111":
        divide(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11101":
        invert(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "11110":
        cmp(instruction)
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
    elif instruction[:5] == "01010":
        for items in range(7):
            output.write(register_list[items])
        output.write("\n")
        for i in range(256):
            output.write(mem[i]+"\n")
        break
