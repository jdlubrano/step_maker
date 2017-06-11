import os
from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
from tempfile import TemporaryFile

from app.dimension import Dimension
from app.cylindrical_part import CylindricalPart
from app.rectangular_part import RectangularPart

app = Flask(__name__)
app.debug = os.environ.get('DEBUG') or False
app.config['TEMPLATES_AUTO_RELOAD'] = os.environ.get('TEMPLATES_AUTO_RELOAD') or False

def setup_logging():
  if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler

    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler("log/application.log", maxBytes=10000000, backupCount=5)
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)

def extract_dimensions(dimension_fields):
  return { dimension: Dimension(request.form[dimension], request.form["units"]) for dimension in dimension_fields }

@app.route("/", methods=['GET'])
def index():
  app.logger.info("Index rendered: " + request.remote_addr)
  return render_template("index.html")

@app.route("/ping")
def ping():
  app.logger.info("PING: " + request.remote_addr)
  return "pong"

@app.route("/box", methods=['POST'])
def create_box_step():
  rp = RectangularPart(extract_dimensions(RectangularPart.dimensions()),
                       request.form['volume_removed'])

  step_file = rp.export_step(TemporaryFile())
  filename = rp.to_string() + "_DUMMY.STEP"
  app.logger.info("Creating " + filename)

  return send_file(step_file, as_attachment=True, attachment_filename=filename)

@app.route("/cylinder", methods=['POST'])
def create_cylinder_step():
  cp = CylindricalPart(extract_dimensions(CylindricalPart.dimensions()),
                       request.form['volume_removed'])

  step_file = cp.export_step(TemporaryFile())
  filename = cp.to_string() + "_DUMMY.STEP"
  app.logger.info("Creating " + filename)

  return send_file(step_file, as_attachment=True, attachment_filename=filename)

if __name__ == "__main__":
  setup_logging()
  app.run(host="0.0.0.0", port=int(os.environ.get('PORT')))
