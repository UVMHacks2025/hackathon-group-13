import sqlite3


def create_food_info_table(cur: sqlite3.Cursor):
    cur.execute("DROP TABLE IF EXISTS food_info;")

    cur.execute('''
                CREATE TABLE food_info(
                name VARCHAR(100),
                food_type VARCHAR(100),
                is_common_allergen BOOLEAN,
                is_kosher BOOLEAN,
                is_hallal BOOLEAN,
                is_vegetarian BOOLEAN,
                is_vegan BOOLEAN
                )
                ''')


def create_stock_table(cur: sqlite3.Cursor):
    cur.execute("DROP TABLE IF EXISTS stock_info;")
    
    cur.execute('''
                CREATE TABLE stock_info(
                item_id INT AUTO_INCREMENT PRIMARY KEY, 
                name VARCHAR(100),
                exp_date DATE,
                quantity INTEGER,
                location VARCHAR(100)
                )
                ''')


if __name__ == "__main__":
    con = sqlite3.connect("food-bank.db")
    cur = con.cursor()
    print("Creating food_info table...")
    create_food_info_table(cur)
    print("Creating stock table...")
    create_stock_table(cur)
    print("Tables Created.")
