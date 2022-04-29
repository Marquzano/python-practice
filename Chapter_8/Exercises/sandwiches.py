def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient.title())

make_sandwich('wheat', 'mustard', 'ham', 'provolone')
make_sandwich('rye', 'ham')
make_sandwich('whole grain', 'seitan', 'vegan cheese', 'grilled peppers', 'grilled onions', 'spicy mustard')