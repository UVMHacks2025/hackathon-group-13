import sqlite3 # included in standard python distribution

con = sqlite3.connect("food-bank.db")

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

def add_live_food(item_id, name, exp_date, quantity, location):
    query = f"INSERT INTO stock_info VALUES('{item_id}', '{name}', '{exp_date}', {quantity}, '{location}')"
    res = cur.execute(query)
    x = res.rowcount
    assert x == 1

def update_live(col, value, item_id):
    query = f"UPDATE stock_info set {col} = {value} WHERE stock_info.item_id = {item_id}"
    cur.execute(query)

def delete_live(item_id):
    query = f"DELETE FROM stock_info where stock_info.item_id = {item_id}"
    cur.execute(query)

if __name__ == "__main__":
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS food_info;")
    cur.execute("DROP TABLE IF EXISTS stock_info;")

    cur.execute('''
                CREATE TABLE food_info(
                name VARCHAR(100), 
                food_type VARCHAR(100), 
                allergens VARCHAR(100), 
                is_kosher BOOLEAN, 
                is_hallal BOOLEAN, 
                is_vegetarian BOOLEAN, 
                is_vegan BOOLEAN
                )
        ''')
    
    cur.execute('''
                CREATE TABLE stock_info(
                item_id INT, 
                name VARCHAR(100), 
                exp_date DATE, 
                quantity INTEGER, 
                location VARCHAR(100)
                )
        ''')
    
    
    cur.execute("INSERT INTO food_info VALUES('orange', 'fruit', NULL, TRUE, TRUE, TRUE, TRUE)")
    cur.execute("INSERT INTO stock_info VALUES(1, 'orange', '2025-12-01', 1, 'Backshelf')")
    
    con.commit()

    # user_input = input("What food would you like: ")

    x = search_item_by('name', 'orange')
    print(x)

    add_food('apple', 'fruit', 'apples', False, False, False, False)
    add_live_food(2, 'apple', '2025-12-01', 2, 'L1')

    x = search_item_by('name', 'apple')
    print(x)

    update_live('quantity', 3, 2)

    x = search_item_by('name', 'apple')
    print(type(x))

    # delete_live(2)
    # x = search_item_by('name', 'apple')
    # print(x)
