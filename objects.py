class EndPoint:
    def __init__(self,epId,cacheServers,datacenterLatency):
        self.epId = epId
        self.datacenterLatency = datacenterLatency
        self.nbRequest = 0
        self.cacheServers = cacheServers
        
    def addRequest(self,nbReq):
        self.nbRequest += nbReq

    def assignRequestsToEndPoint(self,reqList):
        for req in reqList:
            if req.endPoint == self.id:
                self.addRequest(req.nbRequest)
    
class CacheServer:
    def __init__(self,csId,capacity):
        self.capacity = capacity
        self.freeSpace = capacity
        self.csId = csId
        self.content = []
        self.endPoints = [] #
        self.isUsed = False
        
    def equality(self,csId):
        return csId == self.csId
    
    def isUsed(self):
        return self.isUsed
    
    def addContent(self,video):
        self.content.append(video.vidId)
        self.freeSpace -= video.size
    
class Request:
    def __init__(self,vidId,endPoint,nbReq):
        self.vidId = vidId
        self.endPoint = endPoint
        self.nbRequest = nbReq
        
class Video:
    def __init__(self,vidId,size):
        self.vidId = vidId
        self.size = size
        