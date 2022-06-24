def typed(opcode, register_dict, list_instr):
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]

    for reg in register_dict.keys():
        if str(list_instr[1]).lower() == str(reg).lower():
            r = register_dict[reg]
    mem_add = str(bin(var.index(list_instr[2])+count))[2:]
    while len(mem_add)!=8:
        mem_add="0"+mem_add
    ans = op+r+mem_add
    output.write(ans+"\n")