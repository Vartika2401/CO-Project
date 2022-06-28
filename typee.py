def typee(opcode, register_dict, list_instr):
    if list_instr[1]=='FLAGS':
        print(f'ERROR, {list_instr[0]} cannot be used with FLAGS register')
        return
    for keys in opcode.keys():
        if str(list_instr[0]).lower() == str(keys).lower():
            op = opcode[keys][0]
    ans = op+"00000000000"

