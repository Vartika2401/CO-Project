random = []
file = open("tezt.txt", "r")
output = open("answer.txt","a")
count = 0
var_count = 0
var = []
ans = 0
labels={}
for line in file:
    list_instr = []
    for i in line.split():
        list_instr.append(i)
    if list_instr != [] :
        if list_instr[0] == 'var':
            if list_instr[1] not in opcode.keys() and list_instr[1] not in register_dict.keys():
                var.append(list_instr[1])
                var_count += 1
            else:
                ans = "error"
                output.write(ans)
        else:
            count += 1
            random.append(list_instr)
        if list_instr[0][-1:]==":":
            labels[list_instr[0][0:-1]]=count-1
