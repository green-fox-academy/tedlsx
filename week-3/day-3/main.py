from flask import Flask, render_template, url_for, request
import json, csv


app = Flask(__name__, static_url_path= "/static")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movie/<movie_id>")
def movie(movie_id):
    with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-3\movie" + f"{movie_id}.json", encoding='utf-8') as file:
        data = json.load(file)
        key = list(data.keys())[0]
        val = list(data.values())[0]
        image_link = url_for("static", filename = f"movie{movie_id}.jpg")       

        return render_template("movie.html", movie_title =  key, image_link = image_link , movie_content = val )

@app.route("/find_result")
def go_search():
    return render_template("find.html")


@app.route("/result", methods = ["POST"])
def res():
    with open(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-3\day-3\products.csv") as file:
        readCSV = csv.reader(file, delimiter=';')
        if request.method == 'POST':
            name = request.form['name']
            for row in readCSV:
                if name in row:
                    return render_template("result.html", row = f"name: {row[1]}, price: {row[2]}, qty: {row[3]}") 
                else:
                    return "No such Name, please check!"

if __name__ == "__main__":
    app.run(debug=True)