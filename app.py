from flask import Flask, render_template

app = Flask(__name__)

#python -m virtualenv {envname}
#fix image is not working and move it to static folder
def read():
    with open("dreams.txt", 'r') as f:
        return [line for line in f]
        #return "filenotfound"

@app.route('/')
def homepage():
    readed = read()
    return render_template('base.html', sname = readed)

@app.route('/moon')
def moon():
    return render_template("MoonQuake.html")

@app.route('/cat')
def cat():
    return render_template("Cat.html")

if __name__ == "__main__":
    app.run(debug=True)
