from flask import Flask, render_template, url_for, request
import random

app = Flask(__name__)

@app.route("/random")
def random_greet():
    greet = ["hello", "你好", "Bonjue"]
    name = ["Jhon", "Jane", "Jack"]
    i = random.randint(0, len(greet) - 1)
    j = random.randint(0, len(name) - 1)
    result = greet[i] + name[j]
    return render_template("random.html", result= result)

@app.route("/product")
def product():
    products = [
    ("Milk", 3.59123),
    ("Bread", 2.96332),
    ("Rice", 0.64111)
]
    return render_template("product.html", pro = products)

articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]

@app.route("/articles")
def list_articles():
    return render_template("articles.html", articles=articles)

authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "jane",
        "likes" : [
            200
        ]
    }
]

posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]
transformed_posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they.",
        "likes": "John, Jane",
        "name": "John"
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating.",
        "name": "John"
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which.",
        "likes": "John",
        "name": "Jane"
    }
]

@app.route("/posts")
def list_posts():
    return render_template("posts.html", posts=transformed_posts)


if __name__ == "__main__":
    app.run(debug=True)