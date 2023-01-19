from collections import defaultdict 
from itertools import combinations
import random


# Graph Creation Using Adjascency List Representation in Python

class Graph:

    def __init__(graph):
        graph.dict = defaultdict(list)
    
    def get_two_rand_node(graph,n):
        return random.sample(range(1, n+1), 2)
    def get_edge_vertices(graph,n, p):
        Edge = set()
        while len(Edge) < p:
            Edge.add(tuple(random.sample(range(1, n+1), 2)))
        return Edge

    def add_node(graph,node,adjacent_node): 
        graph.dict[node].append(adjacent_node)

    def add_edges(graph): 
        graph_edges = []
        for node in graph.dict: 
            for adjacent_node in graph.dict[node]:
                if (adjacent_node, node) not in graph_edges :
                    graph_edges.append((node, adjacent_node))
        return graph_edges

    


    def bfs_shortest_path(graph, start, end):
        visited = set()
        # enqueue the path
        enqueue = []
        # push the starting path into the queue
        enqueue.append([start])
        while enqueue:
            # get the starting path from the queue
            path = enqueue.pop(0)
            # get the last node from the path
            node = path[-1]
            # check if path found
            if node == end:
                return path
            elif node not in visited:
                # check all adjacent nodes, built a 
                # new path and enqueue it
                for adjacent in graph.dict.get(node, []):
                    new_path = list(path)
                    new_path.append(adjacent)
                    enqueue.append(new_path)
                visited.add(node)
        
    
    def write_op(graph,min_path, time_req,start,end):
        f = open("output.txt", "a")
        f.writelines('\nMin-hop path between ')
        f.writelines(str(start))
        f.writelines(' and ')
        f.writelines(str(end))
        f.writelines(':')
        f.writelines(str(min_path))
        f.writelines('\nTime taken: ')
        f.writelines(str(time_req))
        f.writelines('\n')
