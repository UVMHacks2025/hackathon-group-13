from flask import Flask, render_template, request
import create_db
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("food-bank.db")

@app.route("/", methods=['GET', 'POST'])
def home():
    # DATABASE STUFF dict 
    results= []

    if request.method == "POST":
        name = request.form.get("name")
        quantity = request.form.get("quantity")
        expr_date = request.form.get("expiration-date")
        location = request.form.get("location")
        
        results.append(name)
        results.append(quantity)
        results.append(expr_date)
        results.append(location)
    
    return render_template('item_inventory.html', results=results)


if __name__ =='__main__':
    cur = con.cursor()
    create_db.create_food_info_table(cur=cur)
    create_db.create_stock_table(cur=cur)
    create_db.add_food(cur, 'orange', 'fruit', 'orange', True, True, True, True)
    create_db.add_live_food(cur, 1, 'orange', '2025-01-12', 2, "L1")
    res = create_db.search_item_by(cur, 'name', 'orange')
    print(res[0])
    app.run()
