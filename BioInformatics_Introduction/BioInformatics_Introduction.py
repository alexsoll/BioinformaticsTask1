import sys

def Task1():
    res = 0
    pattern = input()
    genome = input()
    for i in range (len(genome)):
        if (pattern == genome[i:i + len(pattern)]):
            res += 1
    print(res)
    return res

def OtherTask1Method(pattern, genome):
    tmpstr = genome
    res = 0
    while(True):
        p = tmpstr.find(pattern, 0, len(tmpstr))
        if (p != -1):
            res += 1
            tmpstr = tmpstr[p + 1:len(tmpstr) + 1]
        else:
            return res



def Task2():
    genome = input()
    k = int(input())
    tmpstr = genome
    d = {}
    for i in range (len(genome)):
        kmers = tmpstr[i: i + k]
        if (len(kmers) < k):
            break
        res = OtherTask1Method(kmers, genome)
        d[kmers] = res
    d = sorted(d.items(), key=lambda item: (-item[1]))
    i = 0
    print(d[i][0])
    while(True):
        i += 1
        if (d[i][1] == d[i - 1][1]):
            print(d[i][0])
        else:
            break


def OtherTask2Method(genome, k):
    tmpstr = genome
    d = []
    for i in range (len(genome)):
        kmers = tmpstr[i: i + k]
        if (len(kmers) < k):
            break
        res = Task1(kmers, genome)
        if [kmers,res] not in d:
            d.append([kmers, res])
    d.sort(key=lambda x: (-x[1]))
    i = 0
    print(d[i][0])
    while(True):
        i += 1
        if (d[i][1] == d[i - 1][1]):
            print(d[i][0])
        else:
            break


def Task3():
    pattern = input()
    tmpstr = ''
    res = ''
    for i in range (len(pattern)):
        if (pattern[i] == 'A'):
            tmpstr += 'T'
            continue
        if (pattern[i] == 'C'):
            tmpstr += 'G'
            continue
        if (pattern[i] == 'G'):
            tmpstr += 'C'
            continue
        if (pattern[i] == 'T'):
            tmpstr += 'A'
            continue
    res = tmpstr[:: -1]
    print(res)


Task3()
##Task2()
##OtherTask2Method("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)        
##OtherTask1Method('ATAT', 'GATATATGCATATACTT')
##Task1()