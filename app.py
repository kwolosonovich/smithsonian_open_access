import requests

from flask import Flask, render_template, request, flash, redirect, session, g, abort
from flask_debugtoolbar import DebugToolbarExtension
from secure import API_KEY
# from models import Users

app = Flask(__name__)

API_BASE_URL = 'https://api.si.edu/openaccess/api/v1.0/search'

@app.route('/')
def homepage():
   '''Render homepage'''
   
   # test API requests 
   q = "edward hopper"
   api_key = API_KEY
   rows_ = 1000
   
   # search for items
   resp = requests.get(url=API_BASE_URL,
                     params={"q": q,
                              "api_key": api_key,
                              "rows": rows_})
   
   # iterate through the items for image URL
   rows = resp.json()["response"]["rows"]
   image_urls = []
   for row in rows:
      if "online_media" in row["content"]["descriptiveNonRepeating"].keys():
         if "resources" in row["content"]["descriptiveNonRepeating"]["online_media"]["media"][0].keys():
            url = row["content"]["descriptiveNonRepeating"]["online_media"]["media"][0]["resources"][0]["url"]
            image_urls.append(url)
      # if "online_media" in row["content"]["descriptiveNonRepeating"].keys():
      #    link = row["content"]["descriptiveNonRepeating"]["online_media"][
      #          "media"][0]["content"]
      #    image_links.append(link)

   print(resp)
   print(len(image_urls))   
   
   return render_template('homepage.html', image_urls=image_urls)

