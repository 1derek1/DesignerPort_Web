import os
from flask import Flask, jsonify, request, render_template, Response
from werkzeug.utils import secure_filename

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
        #"name": "moj helloworld",
        #"description": "Converts JSON to HTML tabular representation",dere
    }
    return Response(render_template("index.html", result=test, mimetype="text/html"))


if __name__ == "__main__":
    app.run(debug=True);
