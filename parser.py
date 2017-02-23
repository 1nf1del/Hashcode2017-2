import objects as o
path="kittens.in"

def parsing(path):
    data = open(path,'r')
    lines = data.read().splitlines()
    data.close()
    firstLine = line[0].split(' ')
    V,E,R,C,X = int(firstLine[0]),int(firstLine[1]),int(firstLine[2]),int(firstLine[3]),int(firstLine[4])
    videos = lines[1].split(' ')
    requests = lines[-R:]
    endpoints = lines[2:-R]
    globalCacheServers = {}
    globalEndPoints = {}
    globalRequests = []

    c=0
    for i in range(E):
        currentLine = endpoints[c].split(' ')
        idE = i
        latency = currentLine(int(currentLine[0]))
        cacheServerNumber =  currentLine(int(currentLine[1]))
        cacheServers =[]
        c=c+1
        for j in range(cacheServersNumber):
            currentLine = endpoints[c].split(' ')
            idServer = currentLine(int(currentLine[0]))
            latencyServer = currentLine(int(currentLine[1]))
            if i in globalCacheSever:
                globalCacheServer[i].endPoint.append({'endpoint':idE; 'latency' = latencyServer})
            else:
                globalCacheServer[i] = o.CacheServer(idServer,X)
                globalCacheServer[i].endPoint.append({'endpoint':idE; 'latency' = latencyServer})
            cacheServers.append(idServer)
            c=c+1
        globalEndPoints[idE] = o.Endpoint(idE, cacheServers, latency))
    for r in requests:
        currentLine = r.split(' ')
        vidId = int(currentLine[0])
        endPoint = int(currentLine[1])
        nbReq = int(currentLine[2])
        globalRequests.append(o.Request(vidId,endPoint,nbReq))
    return (V,E,R,C,X,globalCacheServers,globalEndPoints,globalRequests)

(V,E,R,C,X,s,e,r) = parsing(path)
print(V,E,R,C,X)
print(r[5])


