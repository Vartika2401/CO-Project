
register_list = ['0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000','0000000000000000']

#type E instructions

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

if op=='11111':
    jmp(machine_ins)

elif op=='01100':
    jlt(machine_ins)

elif op=='01101':
    jgt(machine_ins)

elif op='01111':
    je(machine_ins)





