from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        test = request.form.get("test")
        return "test is " + test 
    return render_template('item_inventory.html')

@app.route("/new_item", methods=['GET', 'POST'])
def new_item():        
    return render_template('new_item.html')

if __name__ =='__main__':
    app.run()
