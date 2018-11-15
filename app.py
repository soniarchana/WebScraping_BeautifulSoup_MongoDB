#################################################
# Import Dependencies
#################################################

#  Import Flask
from flask import Flask, jsonify, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection to mars_mission_app
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_mission_app"
mongo = PyMongo(app)


#################################################
# Flask Routes
#################################################

# Define what to do when a user hits the index route
@app.route("/")
def index():
	mars_data = mongo.db.collection.find_one()
	return render_template("index.html", mars_data=mars_data)
	



# Define what to do when user clicks scrape function route
@app.route("/scrape")
def scraper():
    mars_data = mongo.db.mars_data
    mars_mission_data = scrape_mars.scrape()
    mars_data.update({}, mars_mission_data, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)