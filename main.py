from flask import Flask
from flask import request
from flask import render_template

from app.box_part import BoxPart

app = Flask(__name__)
app.config.from_pyfile('config/config.cfg')

@app.route("/", methods=['GET'])
def index():
  return render_template("index.html")

@app.route("/ping")
def ping():
  return "pong"

@app.route("/box", methods=['POST'])
def create_box():
  box_params = request.get_json()
  dimensions = { dimension: box_params[dimension] for dimension in BoxPart.dimensions() }
  bp = BoxPart(dimensions, box_params['volume_removed'] or 0)
  return bp.to_step()

if __name__ == "__main__":
  app.run(host="0.0.0.0")
