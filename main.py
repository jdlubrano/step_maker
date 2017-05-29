from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
from tempfile import TemporaryFile

from app.dimension import Dimension
from app.cylindrical_part import CylindricalPart
from app.rectangular_part import RectangularPart

app = Flask(__name__)
app.config.from_pyfile('config/config.cfg')

def extract_dimensions(dimension_fields):
  return { dimension: Dimension(request.form[dimension], request.form[dimension + "_units"]) for dimension in dimension_fields }

@app.route("/", methods=['GET'])
def index():
  return render_template("index.html")

@app.route("/ping")
def ping():
  return "pong"

@app.route("/box", methods=['POST'])
def create_box_step():
  rp = RectangularPart(extract_dimensions(RectangularPart.dimensions()),
                       request.form['volume_removed'])

  step_file = rp.export_step(TemporaryFile())
  filename = rp.to_string() + ".STEP"

  return send_file(step_file, as_attachment=True, attachment_filename=filename)

@app.route("/cylinder", methods=['POST'])
def create_cylinder_step():
  cp = CylindricalPart(extract_dimensions(CylindricalPart.dimensions()))

  step_file = cp.export_step(TemporaryFile())
  filename = cp.to_string() + ".STEP"

  return send_file(step_file, as_attachment=True, attachment_filename=filename)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
