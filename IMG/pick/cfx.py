import pdb
with open('cfx.txt', "r") as f:
    cfx = f.readlines()
    pdb.set_trace()
    resultall = []
    for x in cfx:
        # pdb.set_trace()
        if x[:4] != 'elli':
            print(x)
            resultall.append(x)

with open('cfxw.txt', "w") as writefile:
    for x in resultall:
        writefile.writelines(x)
