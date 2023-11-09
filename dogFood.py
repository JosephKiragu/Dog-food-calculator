def calculate_ingredients(use_preselected=True, custom_ingredients=None):
    if custom_ingredients is None:
        custom_ingredients = {}
        
    # Preselected ingredients and their weights
    preselected = {
        "maize": 5,
        "soya": 5,
        "wheat_pollard": 5,
        "wheat_bran": 10,
        "ochungaa": 10,
        "omena": 10,
        "rice": None
    }
    
    # If the user chooses custom ingredients, update the preselected dictionary
    if not use_preselected:
        for ingredient, weight in custom_ingredients.items():
            if ingredient in preselected:
                preselected[ingredient] = weight
    
    # User input for rice quantity if not provided in custom ingredients
    if preselected["rice"] is None:
        rice_weight = float(input("Enter the quantity of rice (in kg): "))
        preselected["rice"] = rice_weight
    
    # Calculate the total weight of the main ingredients
    total_main_ingredients_weight = sum(preselected.values())
    
    # Calculate additional ingredients based on the total weight
    micros = {}
    micros["Dog Premix"] = total_main_ingredients_weight / 1000 # 1kg for every 1 tonne
    micros["Toxin Binder"] = 2 * (total_main_ingredients_weight / 1000) # 2kg for every 1 tonne
    micros["Bone Meal"] = 30 * (total_main_ingredients_weight / 1000) # 30kg for every 1 tonne
    
    # Calculate the total weight
    total_weight = total_main_ingredients_weight + sum(micros.values())
    print("Ingredients and their weights:")
    for ingredient, weight in preselected.items():
        print(f"{ingredient}: {weight} kg")
    for micro_ingredient, weight in micros.items():
        print(f"{micro_ingredient}: {weight} kg")

    return total_weight

def main():
    print("Welcome to the Dog Food Calculator!")
    
    while True:
        choice = input("Do you want to select a preselected basket? (yes/no/exit): ").strip().lower()
        if choice == "exit":
            print("Exiting the program.")
            break

        custom_ingredients = {}
        if choice == "no":
            # Gather all custom ingredients
            while True:
                ingredient = input("Enter the ingredient (maize/soya/wheat_pollard/wheat_bran/ochungaa/omena/rice) or 'done' to finish : ")
                if ingredient == "done":
                    break
                if ingredient in ["maize", "soya", "wheat_pollard", "wheat_bran", "ochungaa", "omena", "rice"]:
                    weight = float(input(f"Enter the quantity for {ingredient} (in kg): "))
                    custom_ingredients[ingredient] = weight
                else:
                    print("Invalid ingredient. Please enter a valid ingredient or 'done' to finish.")

        # Calculate ingredients
        total_weight = calculate_ingredients(use_preselected=(choice == "yes"), custom_ingredients=custom_ingredients)
        print(f"\nThe total weight of the dog food ingredients is: {total_weight:.2f} kg")

        continue_choice = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if continue_choice != "yes":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
