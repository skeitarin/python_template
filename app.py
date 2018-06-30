from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    mes = "Hello World in templates"
    list = ["a1", "a2", "a3"]
    dict = {"name":"John", "age":24}
    bl = True
    return render_template('index.html', message=mes, list=list, dict=dict, bl=bl)

@app.route("/get")
def get():
    get_args = request.args.get("msg", "Not defined")
    return "Hello Wolrd " + get_args

@app.route("/post", methods=['POST'])
def post():
    post_args = request.form["msg"]
    return "Hello Wolrd " + post_args

if __name__ == "__main__":    
    app.debug = True
    app.run()