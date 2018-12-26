#%%


from flask import Flask, jsonify, request
server = Flask("Server Running on port 5000")

@server.route('/upload-graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)
    

@server.route('/degrees-of-separation/<origin>/<destination>', methods=['PUT'])
def find_path(origin, destination, graph='', path=[]):
        
    
    graph = request.get_json()
    
    graph = jsonify(graph)
    
#    graph = dict(graph)

    # first thing, we add the current start to the path
    path = path + [origin]
    
    
    # then , if the start is the same as the end, we have finished, we can
    # return the path!
    if origin == destination:
        return jsonify(path)
    
    # Also, if the start is *not* in the graph, we return None
    if origin not in graph:
        return jsonify(None)

    # Here we iterate over all of start's edges
    for node in graph[origin]:
        # if the edge is not in the path (we haven't visited it yet)
        if node not in path:
            # We try to find its path to end
            newpath = find_path(node, destination, graph, path)

            # and, if it didn't return None, we return the path 
            if newpath is not None:
                            # We try to find its path to end
            newpath = find_path(node, destination, graph, path)

            # and, if it didn't return None, we return the path 
                if newpath is not None:
                    return jsonify(newpath)

server.run()
