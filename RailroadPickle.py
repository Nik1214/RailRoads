from math import pi , acos , sin , cos
import pickle

class node(object):
    def __init__(self,i, la, lo):
        self.ID = i
        self.lat = la
        self.long = l
class makeStructures(object):
    
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
       R   = 3958.76 # miles = 6371 km
       y1 *= pi/180.0
       x1 *= pi/180.0
       y2 *= pi/180.0
       x2 *= pi/180.0
   # approximate great circle distance with law of cosines
       return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
    
    def __init__(self):
        self.IDcoordinates = {}
        self.neighbors = {}
        self.names = {}

    def makeIDCoords(self):
        tempCoordinates= set (line.strip() for line in open("file1.txt"))
        for temps in tempCoordinates:
            parts = temps.split(" ")
            self.IDcoordinates[parts[0]] = ((parts[1]), (parts[2]))
        pickle.dump(self.IDcoordinates, open("IDCoordinates.txt", "wb"))
    def makeNeighbors(self):
        tempNeighbors= set (line.strip() for line in open("file2.txt"))
        for temps in tempNeighbors:
            parts = temps.split(" ")
            #print(parts[0])
            node1Lat = str(self.IDcoordinates[parts[0]][0])
            node1Lon = str(self.IDcoordinates[parts[0]][1])
            node2Lat = str(self.IDcoordinates[parts[1]][0])
            node2Lon = str(self.IDcoordinates[parts[1]][1])
            if(parts[0] not in self.neighbors):
                tempDict = {}
                self.neighbors[parts[0]] =  {}
                self.neighbors[parts[0]][parts[1]] = (self.calcd(node1Lat,node1Lon,node2Lat,node2Lon))
            self.neighbors[parts[0]][parts[1]] = (self.calcd(node1Lat,node1Lon,node2Lat,node2Lon))
            if(parts[1] not in self.neighbors):
                tempDict = {}
                self.neighbors[parts[1]] =  {}
                self.neighbors[parts[1]][parts[0]] = (self.calcd(node2Lat,node2Lon,node1Lat,node1Lon))
            self.neighbors[parts[1]][parts[0]] = (self.calcd(node2Lat,node2Lon,node1Lat,node1Lon))
        pickle.dump(self.neighbors, open("neighbors.txt", "wb"))
        
    def makeNames(self):
        tempNames= set (line.strip() for line in open("file3.txt"))
        for temps in tempNames:
            parts = temps.split(" ")
            if(len(parts) > 2):
                parts[1] = parts[1] + " " + parts[2]
            #print(parts[1])
            self.names[parts[0]] = (parts[1])
        pickle.dump(self.names, open("names.txt", "wb"))

temp = makeStructures()
temp.makeNames()
temp.makeIDCoords()
temp.makeNeighbors()
print(temp.neighbors["4800335"])
