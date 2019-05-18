

import itertools
def ThreeAddUpToHundred(a1,a2,a3,a4,a5):
    result = 0
    if 10*(a1+a4)+a2+a3+a5 == 100:
        result = 1
    return result

def FiveAddUpToHundred(comb):
    result = 0
    for s1 in (-1,1):
        for s2 in (-1,1):
            for s3 in (-1,1):
                for s4 in (-1,1):
                    for s5 in (-1,1):
                        if s1*(10*comb[0]+comb[1])+s2*(10*comb[2]+comb[3])+s3*comb[4]+s4*(10*comb[5]+comb[6])+s5*(10*comb[7]+comb[8])==100:
                            result = 1
    return result
                            

a = list(itertools.permutations(list(range(1,10))))


for comb in a:
    if ThreeAddUpToHundred(comb[2], comb[3], comb[4], comb[7], comb[8]) and FiveAddUpToHundred(comb) and comb[5]>comb[0] and comb[7]>comb[0] and (10*comb[0]+comb[1])>2*(10*comb[2]+comb[3]) and 10*comb[2]+comb[3]>comb[4]+17 and 10*comb[7]+comb[8]>(10*comb[0]+comb[1])+17:
        print(comb)