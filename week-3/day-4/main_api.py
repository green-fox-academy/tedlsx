from flask import Flask, render_template, url_for, request, jsonify
import json

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return '''<h1>API</h1>
<p>A API for reading of movies or series.</p>'''

@app.route("/api/movies", methods = ["GET", "POST"])
def api_all():
        if request.method == "GET":
                with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json") as file:
                        data = json.load(file)           
                        return jsonify(data)

        elif request.method == "POST":
                if request.headers["my_key"] == str(12345):
                        with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json", 'r') as file:
                                data = json.loads(file.read())
                                new_input = request.get_json()
                                data.append(new_input)
                                
                        with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json", "w")as new_file:
                                json.dump(data, new_file)

                        return jsonify(data), 200      
                else:
                                return jsonify({"error": "Invalid API_KEY"}), 403  
                
@app.route("/api/movies/<movie_id>", methods = ["GET", "PUT", "DELETE"])
def api_find(movie_id):
        if request.method == "GET":
                with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json") as file:
                        data = json.load(file)
                        for movie in data:
                                for key in movie:
                                        if key == movie_id:
                                                return jsonify({key: movie[key]}) 

        elif request.method == "PUT":
                with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json") as file:
                        data = json.load(file)
                        count = 0
                        for movie in data:
                                if movie_id in movie:
                                        new_input = request.get_json()
                                        movie[movie_id] = new_input[movie_id]
                                        count = 1
                        if count == 0:
                                return jsonify({"error": f"No movie found with '{movie_id}' ID"}), 404        
                                        
                with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json", "w")as new_file:
                                json.dump(data, new_file)
                return jsonify(data)
                        
                                

        elif request.method == "DELETE":
                if request.headers["my_key"] == str(12345):
                        with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json") as file:
                                data = json.load(file)
                                count = 0
                                for movie in data:
                                        if movie_id in movie:
                                                new_input = request.get_json()
                                                del movie[movie_id]
                                                count = 1
                                if count == 0:
                                        return jsonify({"error": f"No movie found with '{movie_id}' ID"}), 404
                else:
                        return jsonify({"error": "Invalid API_KEY"}), 403
                with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-4\api\movies.json", "w")as new_file:
                                json.dump(data, new_file)
                return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)