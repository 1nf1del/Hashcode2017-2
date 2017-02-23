Class endPoint:
    def __init__(id,datacenterLatency):
        self.id = id
        self.datacenterLatency = datacenterLatency
        self.nbRequest = 0
        self.cacheServers = []
    
Class cacheServer:
    def __init__(capacity):
        self.capacity = capacity
        self.content = []
        self.endPoints = []
    
Class request:
    def __init__(vidId,endPoint,nbReq):
        self.vidId = vidId
        self.endPoint = endPoint
        self.nbReq = nbReq
        
Class video:
    def __init__(id,size):
        self.id = id
        self.size = size