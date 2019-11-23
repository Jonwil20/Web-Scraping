import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

conn='mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

mongo = client.mars_db
mongo.mars_info.drop()


@app.route("/")
def index():
    mars = mongo.mars_db.find_one()
    return render_template("index.html", mars = mars)

@app.route('/scrape')
def scraper():
    mars = mongo.db.mars_db
    mars_info_data = scrape_mars.scrape_all()
    mars.update({}, mars_info_data, upsert=True)
    return "hello" #redirect ("/", code=302)
    