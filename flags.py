def a(list_instr):
    if list_instr[1]=='FLAGS' or list_instr[2]=='FLAGS' or list_instr[3]=='FLAGS':

        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
    print(opcode[list_instr[0]][0] + "00" + register_dict[list_instr[1]] + register_dict[list_instr[2]] + register_dict[list_instr[3]])


def typeb(opcode, register_dict, list_instr):
    if list_instr[1]=='FLAGS':
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return

    if random[i][0]!="mov":
        for keys in opcode.keys():
            if str(list_instr[0]).lower() == str(keys).lower():
                op = opcode[keys][0]
    else:
        op = "10010"

    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    b = str(bin(int(list_instr[2][1:])))[2:]
    while len(b) != 8:
        b = '0' + b
    mc = op + r + b
    print(mc)




def typeC(opcode, register_dict, list_instr):
    if list_instr[1]=='FLAGS':
        print(f'ERROR')
        return
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r1 = register_dict[reg]

    for reg in register_dict.keys():
        if str(list_instr[2]).lower() == str(reg).lower():
            r2 = register_dict[reg]

    mc = op + '00000' + r1 + r2
    print(mc)


def typed(opcode, register_dict, list_instr):
    if list_instr[1]=='FLAGS' or list_instr[2]=='FLAGS':
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    mem_add = str(bin(var.index(list_instr[2])+count))[2:]
    while len(mem_add)!=8:
        mem_add="0"+mem_add
    print(op+r+mem_add)

def typee(opcode, register_dict, list_instr):
    if list_instr[1]=='FLAGS':
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    mem_add = str(bin(var.index(list_instr[1])+count))[2:]
    while len(mem_add)!=8:
        mem_add="0"+mem_add
    print(op+"000"+mem_add)


