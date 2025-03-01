import sqlite3 # included in standard python distribution

con = sqlite3.connect("food-bank.db")

def search_item_by(type, food_item):
    query = f"Select food_info.name, food_info.food_type, food_info.allergens, food_info.is_kosher, food_info.is_hallal, food_info.is_vegetarian, food_info.is_vegan, stock_info.exp_date, stock_info.quantity, stock_info.location FROM food_info inner join stock_info on stock_info.name = food_info.name WHERE food_info.{type}='{food_item}'"
    res = cur.execute(query)
    x = res.fetchall()
    return x 
    

def add_food(name, food_type, allergens, is_kosher, is_hallal, is_vegetarian, is_vegan):
    query = f"INSERT INTO food_info VALUES('{name}', '{food_type}', {allergens}, {is_kosher}, {is_hallal}, {is_vegetarian}, {is_vegan})"
    res = cur.execute(query)
    x = res.rowcount
    assert x == 1

def add_live_food(item_id, name, exp_date, quantity, location):
    query = f"INSERT INTO stock_info VALUES('{item_id}', '{name}', '{exp_date}', {quantity}, '{location}')"
    res = cur.execute(query)
    x = res.rowcount
    assert x == 1


if __name__ == "__main__":
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS food_info;")
    cur.execute("DROP TABLE IF EXISTS stock_info;")

    cur.execute("CREATE TABLE food_info(name, food_type, allergens, is_kosher, is_hallal, is_vegetarian, is_vegan)")
    cur.execute("CREATE TABLE stock_info(item_id, name, exp_date, quantity, location)")
    
    cur.execute("INSERT INTO food_info VALUES('orange', 'fruit', NULL, TRUE, TRUE, TRUE, TRUE)")
    cur.execute("INSERT INTO stock_info VALUES('1', 'orange', '1/22/1', 1, 'Backshelf')")
    
    con.commit()

    # user_input = input("What food would you like: ")

    x = search_item_by('name', 'orange')
    print(x)

    add_food('apple', 'fruit', 'NULL', False, False, False, False)
    add_live_food(1, 'apple', '1/22/34', 2, 'L1')

    x = search_item_by('name', 'apple')
    print(x)



    # query = f"Select * FROM food_info WHERE name='{user_input}'"

    # query2 = f"SELECT name from food_info where food_info.name = orange"
    # res = cur.execute(query)
    # x = res.fetchall()
    # print(x)






