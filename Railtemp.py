from math import pi , acos , sin , cos
import pickle
import heapq
import queue
import time
import sys
IDtoCoordinates = pickle.load(open("IDCoordinates.txt","rb"))
#print(IDtoCoordinates["1700665"][0])
neighbors = pickle.load(open("neighbors.txt", "rb"))
IDtoNames = pickle.load(open("names.txt", "rb"))
class node(object):
    def __init__(self, ID, parent, goal):
        self.ID = str(ID)
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.goalID = goal
        self.children = list(neighbors[str(self.ID)].keys())
##        if parent != None:
##            self.children.pop((parent.ID))
        self.depth = 0
        
    def __lt__(self,other):
        return(self.f < other.f)
        
    def goalCheck(self, temp):
        if(temp == self.goalID):
            return True
        else:
            return False
    def makeNode(self, ID, parent):
        return node(ID, parent, self.goalID)
    
    def calcG(self, otherNode): #IDs
        return (self.g + self.distance(self.ID,otherNode))
    
    def calcH(self, node):#IDS
        return (self.distance(node, self.goalID))
    
    def distance(self, node, otherNode):#IDS
        node1Lat = str(IDtoCoordinates[str(node)][0])
        node1Lon = str(IDtoCoordinates[str(node)][1])
        node2Lat = str(IDtoCoordinates[str(otherNode)][0])
        node2Lon = str(IDtoCoordinates[str(otherNode)][1])
        return (self.calcd(node1Lat,node1Lon,node2Lat,node2Lon))
               
    def calcd(self, y1,x1, y2,x2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   # if (and only if) the input is strings
   # use the following conversions
       y1  = float(y1)
       x1  = float(x1)
       y2  = float(y2)
       x2  = float(x2)
       if((y1 == y2) and (x1 == x2)):
           return 0
       R   = 3958.76 # miles = 6371 km
       y1 *= pi/180.0
       x1 *= pi/180.0
       y2 *= pi/180.0
       x2 *= pi/180.0
   # approximate great circle distance with law of cosines
       return (acos(sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R)

    def expand(self):
        successors = []
        for c in self.children:
            s = self.makeNode(c,self)
            #s.parent = self
            s.g = (self.calcG(s.ID)) #self.g + edge_cost(self.state,c)
            s.h = (self.calcH(s.ID))
            #s.f = s.g + s.h
            s.depth = self.depth + 1
            s.f = (s.g + s.h)
            successors.append(s)
        return successors

class solver(object):
    def __init__(self):
        temp = 0
        
    def AStar(self,start,end):
        closed = [] 
        fringe = [self.makeNode(start, None, end)] #an ordered list of nodes, sorted by “f”
        self.count = 0
        while (len(fringe) > 0):
            heapq.heapify(fringe)
            n = heapq.heappop(fringe)
            #print(n.ID)
            #print(n.f)
            #print("\n")
            if (n.ID == end):
                #print("here")
                return self.solutionPath(n)
            if(n.ID not in closed):
                closed.append(n.ID)
                for x in n.expand():
                    heapq.heappush(fringe,x)                    
                    
    def solutionPath(self, node):
        return(node.f)
        
    def makeNode(self, ID, parent, goal):
        return node(ID, parent, goal)

def findID(cityName):
    for x in IDtoNames:
        #print(IDtoNames[x])
        if(IDtoNames[x] == str(cityName)):
            return str(x)

temp = solver()
#temp.AStar("4800471","4800445")
#the = node("4801193", None, "4800258")
#print(the.distance("4800797", "4800796"))
#print(the.calcH("4800797")+ the.calcG("4800797"))
inputLines = list(open("test.txt", 'r').read().split("\n"))
printer=open("solutions.txt","w")
#print(“%20s %20s %8.3f %4.3f” % ("4800471", "4800445", temp.AStar("4800471","4800445")), file = outfile)
for line in inputLines:
    temp = solver()
    city = line.split(",")
    (city[0].strip())
    (city[1].strip())
    city1ID = findID(city[0])
    #print(city1ID)
    city2ID = (city[1]).strip()
    city2ID = findID(city2ID)
    #print("here")
    startTime = time.time()
    d = temp.AStar(str(city1ID), str(city2ID))
    finalTime = (time.time() - startTime)
    printer.write("%20s %20s %8.3f %4.3f" % (city1ID, city2ID, d, finalTime))
    printer.write("\n")
printer.close()
print("done")
##temp = solver()
##temp.AStar("4800471","4800445")
##temp.AStar("9100351","8801752")
##temp.AStar("9100069","8801752")
##temp.AStar("8801159","4800100")
