# mov(reg to reg), div, not, cmp

opcode_dict = {"add":"10000",
                "sub":"10001",
                "movi":"10010",
                "mov":"10011",
                "ld":"10100",
                "st":"10101",
                "mul":"10110",
                "div":"10111",
                "rs":"11000",
                "ls":"11001",
                "xor":"11010",
                "or":"11011",
                "and":"11100",
                "not":"11101",
                "cmp":"11110",
                "jmp":"11111",
                "jlt":"01100",
                "jgt":"01101",
                "je":"01111",
                "hlt":"01010"}

reg_dict ={'R0':'000' ,
            'R1':'001' , 
            'R2':'010' , 
            'R3':'011' , 
            'R4':'100' , 
            'R5':'101' , 
            'R6':'110' , 
            'FLAGS':'111'}

ins = 'mov reg1 reg2'

machine_code = []

ins_list = ins.split()

# if $ in ins:
#    type B

op = opcode_dict.get(ins_list[0])
machine_code.append(op)

machine_code.append('00000')


reg1 = reg_dict.get(ins_list[1])
machine_code.append(reg1)

reg2 = reg_dict.get(ins_list[2])
machine_code.append(reg2)

print(ins_list)

print(machine_code)

#ans = ''.join(machine_code)
#print(ans)