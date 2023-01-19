import argparse
import graph_helper as graph
import pprint
import sys
import datetime


# Parser to take the system argument
parser = argparse.ArgumentParser(description="This program is to get the shortest path between airports")

parser.add_argument("number_nodes", help="Number of nodes")
parser.add_argument("number_edges", help="Number of edges")
args = parser.parse_args()

if __name__ == "__main__":

    graph_obj = graph.Graph()
    n = int(args.number_nodes)
    p = int(args.number_edges)
    E = graph_obj.get_edge_vertices(n, p)
    for val in E:
        graph_obj.add_node(val[0], val[1])

    pprint.pprint(graph_obj.dict)

    #get two random nodes
    rand_node_arr = graph_obj.get_two_rand_node(n)
    #print('Edges of the Graph:',graph.add_edges())
    start_time = datetime.datetime.now()
    min_hop_path = graph_obj.bfs_shortest_path(rand_node_arr[0], rand_node_arr[1])
    end_time = datetime.datetime.now()
    total_time_taken = (end_time - start_time)
    total_time_taken_ns = (int(total_time_taken.total_seconds() * 1000000))
    graph_obj.write_op(min_hop_path, total_time_taken_ns,rand_node_arr[0],rand_node_arr[1])
    print('Shortest path BFS between ',rand_node_arr[0],'and',rand_node_arr[1],':', min_hop_path)


