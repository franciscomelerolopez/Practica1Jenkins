from flask import Flask
app = Flask(__name__)

def suma(a,b):
 return a+b

@app.route("/")
def hello():
        res = suma(3,2)
<<<<<<< HEAD
        return "Hola mundo. Primera práctica de Jenkins. Francisco Javier Melero López %s" % (res)
=======
        return "Hello world. Primera práctica de Jenkins .     Francisco Javier Melero López %s" % (res)
>>>>>>> 231796f5f29f6875b9cbfc5c921ba60e709298bd
if __name__ == "__main__":
        app.run(host='0.0.0.0',port=5000)

