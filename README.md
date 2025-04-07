💻 Project Title: SmartFoodDeliverySystem
📌 Objective:
To develop a Django-based web application that enables full CRUD (Create, Read, Update, Delete) operations for managing Restaurants, Food Items, and Orders in a structured and user-friendly way. The application will allow users to browse food items, place orders, and manage data using the Django Admin Panel and custom web interfaces.

🔧 Core Features:
Restaurants Management

Create, update, view, and delete restaurant entries.

Restaurants will be associated with food items.

Food Items Management

List all available food items.

Add new food items with details like name, description, price, and associated restaurant.

Edit/update existing food items.

Delete food items.

Filter food items based on selected restaurant.

Order Management

Place an order by selecting one or more food items.

Assign the order to a specific restaurant.

Track and update the status of an order (e.g., Pending, Confirmed, Delivered).

View order details.

🏗️ Application Structure:
Django App Name: SmartFoodDeliverySystem

📁 Models:
Restaurant

name (CharField)

location (CharField)

contact_info (CharField or EmailField)

FoodItem

name (CharField)

description (TextField)

price (DecimalField)

restaurant (ForeignKey → Restaurant)

Order

food_items (ManyToManyField → FoodItem)

customer_name (CharField)

order_date (DateTimeField)

status (ChoiceField – Pending, Confirmed, Delivered)

🌐 Functional Requirements:
Use Django Admin Panel to:

Manage Restaurants, Food Items, and Orders efficiently.

Use Django Templates/Views/Forms to:

List all Food Items

Add a new Food Item

Update a Food Item

Delete a Food Item

Filter Food Items by Restaurant

Place an Order

Update Order Status

Class-based or Function-based Views:

Either approach can be taken based on developer preference.

📝 Assumptions:
The application is for a delivery service that connects multiple restaurants to users.

No user login system is required at this stage.

Orders are placed anonymously using the customer's name only.

Payment integration is not required.

