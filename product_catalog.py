from product_data import products

# TODO: Step 1 - Print out the products to see the data that you are working with.

print("Product Catalog:")
for product in products:
    print(product)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.

customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()

    # Add the customer preference to the list
    customer_preferences.append(preference.lower())

    response = input("Do you want to add another preference? (Y/N): ").upper()


# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.

customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.

converted_products = []

for product in products:
    converted_product = {
        "name": product["name"],
        "tags": set(product["tags"])
    }

    converted_products.append(converted_product)


# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with a customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''

    matches = product_tags.intersection(customer_tags)

    return len(matches)


# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''

    recommendations = []

    for product in products:
        match_count = count_matches(product["tags"], customer_tags)

        if match_count > 0:
            recommendations.append({
                "name": product["name"],
                "matches": match_count
            })

    recommendations.sort(
        key=lambda product: product["matches"],
        reverse=True
    )

    return recommendations


# TODO: Step 7 - Call your function and print the results

recommendations = recommend_products(
    converted_products,
    customer_preferences
)

print("\nRecommended Products:")

if recommendations:
    for recommendation in recommendations:
        print(
            f"- {recommendation['name']} "
            f"({recommendation['matches']} match(es))"
        )
else:
    print("No products matched your preferences.")


# DESIGN MEMO:
#
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#
# I used lists, sets, loops, set intersection, and sorting to build
# the product recommendation system. Lists are useful for storing
# the product catalog and collecting customer preferences. I converted
# the customer preferences and product tags into sets because sets
# automatically remove duplicate values and make comparisons efficient.
#
# The count_matches function uses set intersection to find the tags
# that appear in both the product and the customer's preferences. The
# length of the intersection becomes the product's match score. Loops
# are used to collect preferences and process each product. I also use
# sorting to display the products with the highest number of matching
# tags first.
#
# 2. How might this code change if you had 1000+ products?
#
# If the catalog contained 1000 or more products, the program could
# still use sets, but checking every product for every customer could
# become less efficient as the catalog grows. A larger system could
# use a database and create an index that connects each tag to the
# products that contain it. This would allow the program to find
# relevant products without checking every product. A production
# recommendation system could also consider purchase history, product
# ratings, price, and previous customer interactions instead of only
# matching product tags.