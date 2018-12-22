#%%


from flask import Flask, jsonify, request
server = Flask("Server Running on port 5000")

@server.route('/upload-graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)
    

@server.route('/http://127.0.0.1:5000/degrees_of_separation/<origin>/<destination>', methods=['POST'])
def get_degrees_of_separation(graph, origin, destination): 
    
    def find_path(graph, start, end, path=[], weight=0):
    path = path + [{"node": start, "weight": weight}]
    if start == end:
        return path
    if not start in graph:
        return None
    for conn in graph[start]:
        if conn["node"] not in path:
            newpath = find_path(graph, conn["node"], end, path, conn["weight"])
            if newpath is not None:
                return newpath

    
    
    print(graph, origin, destination)
server.run()
