from flask import Flask, jsonify, request, render_template, Response

app = Flask(__name__)


@app.route("/")
def get():
    test = {
        #"name": "moj helloworld",
        #"description": "Converts JSON to HTML tabular representation",dere
    }
    return Response(render_template("index.html", result=test, mimetype="text/html"))


if __name__ == "__main__":
    app.run(debug=True);
