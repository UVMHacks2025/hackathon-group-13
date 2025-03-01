from flask import Flask, render_template, request
import db_utils

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    # DATABASE STUFF dict 
    results= []

    if request.method == "POST":
        name = request.form.get("name")
        quantity = request.form.get("quantity")
        exp_date = request.form.get("expiration-date")
        location = request.form.get("location")
        db_utils.add_live_food(name, quantity, exp_date, location)

    results = db_utils.get_db()
    print(results)
    
    return render_template('item_inventory.html', results=results)


@app.route("/new_item", methods=['GET', 'POST'])
def new_item():        
    return render_template('new_item.html')

if __name__ =='__main__':
    # create_db.create_food_info_table(cur=cur)
    # create_db.create_stock_table(cur=cur)
    # create_db.add_food(cur, 'orange', 'fruit', 'orange', True, True, True, True)
    # create_db.add_live_food(cur, 1, 'orange', '2025-01-12', 2, "L1")
    # res = create_db.search_item_by(cur, 'name', 'orange')
    # print(res[0])
    app.run(debug=True)
