from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index4.html')

@app.route("/shop")
def shop_page():
    return "Hello, shop"
    
if __name__ == "__main__":
    app.run(debug=True)
