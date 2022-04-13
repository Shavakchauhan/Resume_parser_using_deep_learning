from flask import Flask, Response, request
import json
from NamedEntity import *
import flask
from tika import parser
from werkzeug.utils import secure_filename
import os
import pandas as pd


app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'
app.config['UPLOAD_EXTENSIONS'] = ['pdf']


def pdf_to_text(filepath):
  '''Extracts the text data from the pdf'''
  raw = parser.from_file(filepath)
  text = raw['content']
  return text

def preprocess(text):
  text = "".join([s for s in text.splitlines(True) if s.strip("\r\n")])
  # text = re.sub('[^A-Za-z0-9\n]+', ' ', text)
  return text


@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route("/predict_entity", methods=["POST"])
def predict_entity():
    f = request.files['file']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    text = pdf_to_text('uploads/'+filename)    
    entity_dict = NamedEntityService.get_entities(text)
    df = pd.DataFrame(list(entity_dict.items()))
    # df.to_csv('result.csv')

    return flask.render_template('result.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

    # return Response(json.dumps(entity_dict), status=200, mimetype='application/json')
    


if __name__ == "__main__":
    app.run(port = 5000, debug=True, threaded=True)