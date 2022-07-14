def ld(register_list,instruction,PC,mem):
    reg = instruction[5:8]
    mem_add = instruction[8:]
    register_list[int(reg,2)]=mem[int(mem_add,2)]
    print(register_list[int(reg,2)])
def st(register_list,instruction,PC,mem):
    reg = instruction[5:8]
    mem_add = instruction[:8]
    a = int(mem_add,2)
    mem[a]=register_list[int(reg,2)]
    print(mem[a])
for i in l_final:
    if i[:5]=="10100":
        ld(register_list,i,PC)
    elif i[:5]=="10101":
        st(register_list,i,PC,mem)
