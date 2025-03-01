import sqlite3

# Establishing connection to db
con = sqlite3.connect("food-bank.db", check_same_thread=False)
cur = con.cursor()


def search_item_by(type, food_item):
    query = f"Select food_info.name, food_info.food_type, food_info.allergens, food_info.is_kosher, food_info.is_hallal, food_info.is_vegetarian, food_info.is_vegan, stock_info.exp_date, stock_info.quantity, stock_info.location, stock_info.item_id FROM food_info inner join stock_info on stock_info.name = food_info.name WHERE food_info.{type}='{food_item}'"
    res = cur.execute(query)
    x = res.fetchall()
    return x 
    

def add_food(name, food_type, allergens, is_kosher, is_hallal, is_vegetarian, is_vegan):
    query = f"INSERT INTO food_info VALUES('{name}', '{food_type}', '{allergens}', {is_kosher}, {is_hallal}, {is_vegetarian}, {is_vegan})"
    res = cur.execute(query)
    x = res.rowcount
    assert x == 1
    con.commit()


def add_live_food(name, exp_date, quantity, location):
    query = f"INSERT INTO stock_info (name, exp_date, quantity, location) VALUES ('{name}', '{exp_date}', {quantity}, '{location}')"
    res = cur.execute(query)
    x = res.rowcount
    assert x == 1
    con.commit()


def update_live(col, value, item_id):
    query = f"UPDATE stock_info set {col} = {value} WHERE stock_info.item_id = {item_id}"
    cur.execute(query)
    con.commit()


def delete_live(item_id):
    query = f"DELETE FROM stock_info where stock_info.item_id = {item_id}"
    cur.execute(query)
    con.commit()

def get_val(col, item_id):
    query = f"SELECT {col} FROM stock_info WHERE item_id = {item_id}"
    res = cur.execute(query)
    return res.fetchone()


def get_db():
    query = "SELECT * FROM stock_info"
    res = cur.execute(query)
    return res.fetchall()
