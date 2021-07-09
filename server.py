from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def first_render():
    return render_template("index.html", input1=8, input2=8,colors1 = "red",
     colors2 = "black")

@app.route("/4")
def initial_render2():
    return render_template("index.html", input1=8, input2=4,colors1 = "red",
     colors2 = "black")

@app.route("/<x>/<y>")
def chek_board(x,y):
    input1=int(x)
    input2=int(y)
    return render_template("index.html", input1=input1, input2=input2,colors1 = "red",
     colors2 = "black")

@app.route("/<x>/<y>/<color1>/<color2>")
def color_board(x,y,color1,color2):
    input1=int(x)
    input2=int(y)
    colors1 = str(color1)
    colors2 = str(color2)
    return render_template("index.html", input1=input1, input2=input2, colors1 = color1,
     colors2 = color2)

if __name__ == "__main__":
    app.run(debug = True)