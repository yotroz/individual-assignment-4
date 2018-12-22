#%%


from flask import Flask, jsonify, request
server = Flask("Server Running on port 5000")

@server.route('/upload-graph', methods=['POST'])
def upload_graph():
    body = request.get_json()
    return jsonify(body)
    

@server.route('/http://127.0.0.1:5000/degrees_of_separation/<origin>/<destination>', methods=['POST'])
def get_degrees_of_separation(graph, origin, destination): 
    
    
    print(graph, origin, destination)
server.run()
