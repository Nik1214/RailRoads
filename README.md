# RailRoads
Finds the shortest path between two railroad stations in the US using A* search algorithm. A graph, where the nodes are the railroad stations and the edges are railway tracks that connect stations, with the edge weights being the eudlicidan distance between the two stations, is created once and serialized using the pickle method for future use. This is done as the creation of this graph is computationally heavy.

  file1.txt contains a list of railroad station ID and its coordinates
	
  file2.txt contains a list of "edges" or connections between railroad stations, based of ID. Edges are considered by directional
	
	file3.txt contains a list of railroad station names and their ID
	
	IDCoordinates.txt is the serialized data structure containing the railroad station ID and its coordinates
	
	names.txt is the serialized data structure containg the name of the railroad station and its ID
	
	neighbors.txt is the serialized data structure of the graph
	
	RailroadPickle.py creates all the data structures and serializes them
	
	Railtemp.py uses an A* algorithm to find the shortest path between two railroad stations
	
	soltuions.txt contains the output. The output format is: starting railroad station ID, starting railroad station ID, distance of shortest path, and time to perform calculation
	
	test.txt conatins test cases
