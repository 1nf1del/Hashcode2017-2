import objects as o
path="kittens.in"

def parsing(path):
    data = open(path,'r')
    lines = data.read().splitlines()
    data.close()
    firstLine = lines[0].split(' ')
    V,E,R,C,X = int(firstLine[0]),int(firstLine[1]),int(firstLine[2]),int(firstLine[3]),int(firstLine[4])
    videos = lines[1].split(' ')
    vids ={}
    for i,val in enumerate(videos):
        vids[i]=o.Video(i,int(val))
    requests = lines[-R:]
    endpoints = lines[2:-R]
    globalCacheServers = {}
    globalEndPoints = {}
    globalRequests = []

    c=0
    for i in range(E):
        currentLine = endpoints[c].split(' ')
        idE = i
        latency = int(currentLine[0])
        cacheServersNumber =  int(currentLine[1])
        cacheServers = []
        c=c+1
        for j in range(cacheServersNumber):
            currentLine = endpoints[c].split(' ')
            idServer = int(currentLine[0])
            latencyServer = int(currentLine[1])
            if i in globalCacheServers:
                globalCacheServers[i].endPoint[idE]=({'endpoint':idE, 'latency' : latencyServer})
            else:
                globalCacheServers[i] = o.CacheServer(idServer,X)
                globalCacheServers[i].endPoint[idE]=({'endpoint':idE, 'latency' : latencyServer})
            cacheServers.append(idServer)
            c=c+1
        globalEndPoints[idE] = o.EndPoint(idE, cacheServers, latency)
    for r in requests:
        currentLine = r.split(' ')
        vidId = int(currentLine[0])
        endPoint = int(currentLine[1])
        nbReq = int(currentLine[2])
        globalRequests.append(o.Request(vidId,endPoint,nbReq))
    return (V,E,R,C,X,globalCacheServers,globalEndPoints,globalRequests,vids)

(V,E,R,C,X,s,e,r,v) = parsing(path)
print(V,E,R,C,X)
print(r[5])


