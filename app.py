from flask import Flask, render_template, redirect

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of our Flask app.
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_mars"
mongo = PyMongo(app)
# scrape_mars.scrape()

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    mars_data = mongo.db.mars_data.find_one()
    scrape_mars.scrape

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
   # Update the Mongo database using update and upsert=True

    mars_data = mongo.db.mars_data
    mars_scrape = scrape_mars.scrape()
    mars_data.update({}, mars_scrape, upsert=True)


   # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)