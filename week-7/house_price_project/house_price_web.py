from flask import Flask, render_template, url_for, request
import json, csv
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeCV
import numpy as np

app = Flask(__name__, static_url_path= "/")
df_all = pd.read_csv(r"C:\Users\Ted_Liu\Documents\greenfox\tedlsx\week-7\house_price_project\estates.csv")
df_all = df_all.drop(columns = ["address", "street_name"])
# display(type(df_all["last_published_date"][0]))
# display(df_all["last_published_date"][0])
for i in range(len(df_all["last_published_date"])):
    df_all.loc[i, "last_published_date"] = df_all.loc[i, "last_published_date"][:4]                                                     
df_all[["num_bathrooms", "num_bedrooms", "num_floors", "num_recepts", "price"]] = df_all[["num_bathrooms", "num_bedrooms", "num_floors", "num_recepts", "price"]].astype("int")
df_all["county"] = df_all["county"].fillna("N")
df_all["new_home"] = df_all["new_home"].fillna("N")
df_all["post_town"] = df_all["post_town"].fillna("N")
df_all["property_type"] = df_all["property_type"].fillna("N")


df_drop_zeroprice = df_all[df_all["price"] != 0]
df_drop_zeroprice["log_price"] = np.log(df_drop_zeroprice["price"])
df_drop_zeroprice = df_drop_zeroprice.drop(columns = ["price"])
df_drop_zeroprice = df_drop_zeroprice.drop(columns = ["new_home"])
df_drop_zeroprice = df_drop_zeroprice.drop(columns = ["num_floors"])

feature_df = df_drop_zeroprice.drop(columns = ["log_price"])
price_df = df_drop_zeroprice[["log_price"]]

feature_df_dummy = pd.get_dummies(feature_df, prefix_sep='_', drop_first=True)

# x_train, x_test, y_train, y_test = train_test_split(feature_df_dummy, price_df, test_size=0.2, random_state=1)

alphas = np.arange(0.01, 10, 0.01).tolist()
alpha_ridge = RidgeCV(alphas)
# Fit the linear regression
model_cv = alpha_ridge.fit(feature_df, price_df)
#best alpha
best_a = model_cv.alpha_

rr = Ridge(alpha=best_a)
rr.fit(feature_df, price_df)

@app.route("/")
def res():
    return render_template("house_find.html")

@app.route("/house_price_web", methods = ["POST"])
def hosue_pred():
    if request.method == 'POST':
                County = request.form['County']
                Code = request.form['Code']
                bathrooms = request.form['bathrooms']
                bedrooms = request.form['bedrooms']
                recept = request.form['recept']

                outcode = Code.split(" ")[0]
                
                with open(r"ukpostcodes.csv") as file:
                    readCSV = csv.reader(file)
                    for row in readCSV:
                        if row["postcode"] == Code:
                            latitude = row["latitude"]
                            longitude = row["longitude"]
                            df = list(County, "2019", latitude, longitude, bathrooms, bedrooms, recept, outcode, post_town, property_type)
                pred = rr.predict(df)
                return pred

if __name__ == "__main__":
    app.run(debug=True)