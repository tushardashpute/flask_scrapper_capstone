# flask dashboard setup

from flask import Flask, render_template
import random

from scrapper import scrape_quotes, quotes_to_df

app = Flask(__name__) # Tells flask to create the app - an object - so it knows where to find the templates, static files, etc.

# @app.route("/")
# def hello():
#     return "Hello, World!"


@app.route("/")
def dashboard():
    quotes = scrape_quotes(limit=10)
    df = quotes_to_df(random.sample(quotes,10))
    # return render_template("dashboard.html", tables=[df.to_html(classes="data", header="true")], titles=df.columns.values)
    # converts the Dataframe DF into an html table
    return render_template("dashboard.html",tables=[df.to_html (classes='data')],titles=df.columns.values)
 
if __name__ == "__main__":
    app.run(debug=True)