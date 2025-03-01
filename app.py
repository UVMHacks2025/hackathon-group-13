from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('item_inventory.html')

@app.route("/subpage")
def newpage():
    return render_template('new_item.html')

if __name__ =='__main__':
    app.run()
