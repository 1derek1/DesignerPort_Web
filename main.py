from os import curdir
import string,cgi,time
from flask import Flask, jsonify, request, render_template, Response, json, url_for
from werkzeug.utils import secure_filename
from os.path import join as pjoin
from http.server import BaseHTTPRequestHandler, HTTPServer

class StoreHandler(BaseHTTPRequestHandler):
    store_path = pjoin(curdir, 'store.json')

upload_folder = '/path/to/the/uploads'
extension = {'png', 'jpg', 'jepg'}

app = Flask(__name__)
app.config['upload_folder'] = upload_folder

@app.route("/")

#def allow_file(filename);
    #return '.' in filename and \
        #filename.rsplit('.', 1)[1].lower() in extension

#def uploadfile();
    #if file.filename == '':
        #flash('No selected file')
        #return redirect(request.url)

def get():
    test = {
    }
    return Response(render_template("index.html", result=test, mimetype="text/html"))


if __name__ == "__main__":
    app.run(debug=True);
