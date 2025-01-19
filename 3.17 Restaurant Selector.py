# 3.17 Restaurant Selector
# You have a group of friends coming to visit for your high school reunion, and 
# you want to take them out to eat at a local restaurant. You aren't sure if any 
# of them have dietary restrictions, but your restaurant choices are as follow:

#   Joe's Gourmet Burgers-Vegetarian: No, Vegan: No, Gluten-Free: No
#   Main Street Pizza Company-Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
#   Corner Cafe-Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
#   Mama's Fine Italian-Vegetarian: Yes, Vegan: No, Gluten-Free: No
#   The Chef's Kitchen-Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

# Write a program that asks whether any members of your party are vegetarian, vegan, 
# or gluten-free, to which then displays only the restaurants to which you may take
# the group. Here is an example of program's output:

def restaurant_selector():
    # Ask the user about dietary restrictions
    vegetarian = input("Is anyone in your party a vegetarian? (yes or no) ").strip().lower()
    vegan = input("Is anyone in your party a vegan? (yes or no) ").strip().lower()
    gluten_free = input("Is anyone in your party gluten-free? (yes or no) ").strip().lower()

    # List of restaurants with their dietary options
    restaurants = {
        "Joe's Gourmet Burgers": {"vegetarian": False, "vegan": False, "gluten_free": False},
        "Main Street Pizza Company": {"vegetarian": True, "vegan": False, "gluten_free": True},
        "Corner Cafe": {"vegetarian": True, "vegan": True, "gluten_free": True},
        "Mama's Fine Italian": {"vegetarian": True, "vegan": False, "gluten_free": False},
        "The Chef's Kitchen": {"vegetarian": True, "vegan": True, "gluten_free": True},
    }

    # Filter restaurants based on restrictions
    possible_restaurants = []
    for name, options in restaurants.items():
        if vegetarian == "yes" and not options["vegetarian"]:
            continue
        if vegan == "yes" and not options["vegan"]:
            continue
        if gluten_free == "yes" and not options["gluten_free"]:
            continue
        possible_restaurants.append(name)

    # Display results
    if possible_restaurants:
        print("\nHere are your restaurant choices:")
        for restaurant in possible_restaurants:
            print(f"  {restaurant}")
    else:
        print("\nSorry, there are no restaurants that meet all your dietary restrictions.")

# Run the function
restaurant_selector()
