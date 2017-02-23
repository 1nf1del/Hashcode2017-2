class EndPoint:
    def __init__(id,datacenterLatency):
        self.id = id
        self.datacenterLatency = datacenterLatency
        self.nbRequest = 0
        self.cacheServers = []
    
class CacheServer:
    def __init__(capacity):
        self.capacity = capacity
        self.content = []
        self.endPoints = []
    
class Request:
    def __init__(vidId,endPoint,nbReq):
        self.vidId = vidId
        self.endPoint = endPoint
        self.nbReq = nbReq
        
class Video:
    def __init__(id,size):
        self.id = id
        self.size = size