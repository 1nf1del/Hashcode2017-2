from parser import *
from parser_out import *
for (i,endPoint) in e.items():
    endPoint.assignRequestsToEndPoint(r)

sortedEndPoints = [v for k,v in sorted(e.items(),key= lambda e: e[1].nbRequest, reverse = True)]

for e in sortedEndPoints:
    minLatency = e.datacenterLatency
    reserved = None
    for csIndex in e.cacheServers:
#        print(csIndex, e.epId, '\n',e)
        if not(s[csIndex].isUsed) and s[csIndex].endPoints[e.epId]['latency'] < minLatency:
            reserved = csIndex
            minLatency = s[csIndex].endPoints[e.epId]['latency']
    if not (reserved == None):
        s[reserved].isUsed = True
        e.reservedServer = reserved
    else:
        e.reservedServer = None

for e in sortedEndPoints:
    if not(e.reservedServer == None): 
        usefulVids = [req for req in r if req.endPoint == e.epId] 
        sortedUsefulVids = sorted(usefulVids, key = lambda r: r.nbRequest, reverse = True)
        while not (sortedUsefulVids ==[]):
            u=sortedUsefulVids.pop(0)
            if v[u.vidId].size < s[e.reservedServer].freeSpace:
                s[e.reservedServer].addContent(v[u.vidId])

parsingOut(s,'kitten.out')





