#  This is management script for database migrations and data uploading to database manually.
#  All Product data here is just as sample.

"""
from kebabine import db, USER
from kebabine.models import Product, User


db.create_all()

#   Upload product(s) data to database:

product = Product(
    product='Chicken Kebab in Lavash',
    price=7.00,
    ingredients='Lavash, Chicken meat, Chinese cabbage, Tomatoes, Cucumbers, Pickles',
    extra='Garlic sauce',
    image_filename='kebab1.jpeg',
)

product_1 = Product(
    product='Lamb Kebab in Lavash',
    price=9.50,
    ingredients='Lavash, Lamb meat, Chinese cabbage, Tomatoes, Cucumbers, Pickles',
    extra='Mix Sauce',
)
product_2 = Product(
    product='Beef Kebab in Lavash (spicy)',
    price=9.80,
    ingredients='Lavash, Beef, Chinese cabbage, Tomatoes, Cucumbers, Onions',
    extra='Spicy sauce',
)
product_3 = Product(
    product='Beef Kebab in plate',
    price=8.80,
    ingredients='Beef, Chinese cabbage, Tomatoes, Cucumbers, Onions',
    extra='Garlic sauce',
)

#   Upload user's data to database:

user = User(
    name=USER.name,
    email=USER.email,
    password=USER.password,
)

db.session.add_all([product, product_1, product_2, product_3, user])
db.session.commit()
"""

