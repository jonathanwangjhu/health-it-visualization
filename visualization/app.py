from flask import Flask, flash, redirect, render_template, request, session, abort
from bokeh.embed import server_document
app = Flask(__name__)

@app.route("/")
def hello():
    script=autoload_server(model=None,app_path="/main",url="http://localhost:5006")
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
