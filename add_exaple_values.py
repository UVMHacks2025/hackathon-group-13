import db_utils
import sqlite3

if __name__ == "__main__":
    example_foods = [
        {"name": "Oranges", "food_type": "Fresh produce", 
         "is_common_allergen": False, "is_kosher": True, 
         "is_hallal": True, "is_vegetarian": True, "is_vegan": True},
        {"name": "Apples", "food_type": "Fresh produce", 
         "is_common_allergen": False, "is_kosher": True, 
         "is_hallal": True, "is_vegetarian": True, "is_vegan": True},
        {"name": "Pasta", "food_type": "Grains", 
         "is_common_allergen": False, "is_kosher": True, 
         "is_hallal": True, "is_vegetarian": True, "is_vegan": True},
        {"name": "White rice", "food_type": "Grains", 
         "is_common_allergen": False, "is_kosher": True, 
         "is_hallal": True, "is_vegetarian": True, "is_vegan": True},
        {"name": "Chicken breast", "food_type": "Meat", 
         "is_common_allergen": False, "is_kosher": True, 
         "is_hallal": True, "is_vegetarian": False, "is_vegan": False},
        {"name": "Bacon", "food_type": "Meat", 
         "is_common_allergen": False, "is_kosher": False, 
         "is_hallal": False, "is_vegetarian": False, "is_vegan": False},
        {"name": "Eggs", "food_type": "Animal products", 
         "is_common_allergen": False, "is_kosher": True, 
         "is_hallal": True, "is_vegetarian": True, "is_vegan": False}
    ]

    example_stock = [
        {"name": "oranges", "exp_date": "2025-04-01", 
         "quantity": 10, "location": "pantry"},
        {"name": "Apples", "exp_date": "2025-04-10", 
         "quantity": 3, "location": "pantry"},
        {"name": "Pork chops", "exp_date": "2025-04-06", 
         "quantity": 5, "location": "freezer"}
    ]

    print("Adding example foods to table...")
    for food in example_foods:
        db_utils.add_food(food["name"], food["food_type"],
                          food["is_common_allergen"], food["is_kosher"],
                          food["is_hallal"], food["is_vegetarian"],
                          food["is_vegan"])
    for stock in example_stock:
        db_utils.add_live_food(stock["name"], stock["exp_date"], stock["quantity"], stock["location"])
    print("Finished")
