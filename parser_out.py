from objects import *

def parsingOut(CacheServList,path):
    data=open(path,'w')
    N = 0
    for k,cache in CacheServList.items():
        if cache.freeSpace < cache.capacity:
            N += 1
    data.write("%i" % N)
    for k,cache in CacheServList.items():
        if cache.freeSpace < cache.capacity:
            data.write("\n%i" % cache.csId)
            for i in cache.content:
                data.write(" %i" % i)
    data.write("\n")
    data.close()