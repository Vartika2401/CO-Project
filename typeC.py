def typeC(opcode, register_dict, list_instr):
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