# Milestone 4 : Wine Nation 

## 


As the final project of the course, my aim is to create a full-stack site based around business logic used to control a centrally owned dataset and to provide paid access to the site's data and services using all technologies such as HTML, CSS, JAvascript, Python, Django, relational databases and Stripe payments.

The project is an Ecommerce site for a wine shop specializing in Eastern European wines, which also has a subscription-based wine delivery service that allows shoppers to purchase wines at a better price than buying individual bottles, the longer the subscription period the lower the price per bottle.

Please see the link to the live page here: https://winenation.herokuapp.com/


## UX

### Project goals 

#### Target audience: 

- Wine lovers
- Eastern European Immigrants looking for their favourite wines
- People who are organizing a party
- People who like to experiment and try out new things
- People who are regular wine drinkers and would like to receive wine by post on a regulat basis

#### Site owner's goals:

- Promote their shop
- Generate more business through the webhop and the subscription service
- Attract more suppliers 
- Popularize wine from this lesser known region

#### Visitor's goals

- Purchase products shown on the website in a safe and secure way
- Learn about the subscription options

### User stories

Viewing and navigation

As a user I want to be able to view a list of wines and decide what to purchase and select them.
As a user I want to be able to view individual product details and find description, price, image.
As a user I want to be able to identify deals and offers easily, take advantage of savings and discounts.
As a user I want to be able to view what services the company's offering.
As a user I want to learn more about the company and the purpose of the site.	
As a user I want to be able to easily register for a personal account to see my profile and order history.
As a user I want to be able to easily log in and out of my personal account.
As a user I want to be able to recover my password so I can have access to my account even if I forgot my password.
As a user I want to receive an email confirmation after registering in order to verify my account has been created.
As a user I want to be able to save and update my payment information, delivery and billing address, see order history and current subscription.
	
Sorting and searching	

As a user I want to be able to sort a category of products, find the best priced products in a category, or sort the products in the category alphabetically.
As a user I want to be able to sort multiple categories of products simultaneously.
As a user I want to be able to search for a product by name or description.
As a user I want to be able to easily see what I've searched for and the number of results	.
			
Purchasing and checkout

As a user I want to be able to easily select the quantity of the product when purchasing it to ensure I don't accidentally select the wrong product or quantity.
As a user I want to be able to view items in my bag to identify total cost of purchase, price and number of items I am going to buy.
As a user I want to be able to adjust the quantity of individual items in the bag in order to make changes to my purchase.
As a user I want to be able to easily enter payment information to be able to check out quickly.
As a user I want to feel my personal and payment information is stored securely	so that I can happily provide sensitive information needed for checkout.
As a user I want to be able to view an order confirmation after checkout	to verify I haven't made a mistake.
As a user I want to be able to receive an email confirmation after checkout so that I have a confirmation for the record.
			
Admin and store management	

As a store owner I want to be able to add a product or subscription to the shop to extend the range of items for sale if needed.
As a store owner I want to be able to edit/update products, change product details such as price, description.
As a store owner I want to be able to delete products  to avoid I don’t advertising items that are no longer available and misleading customers.



### Design


### Wireframes



## Features

### Existing Features

#### Landing page




#### About us page



#### Wines page



#### Wine details page



#### Subscriptions


#### Shopping bag


#### Checkout


#### Register

#### Login

#### Admin functions


#### Error handling


### Features left to implement


## Information architecture

### Database Choice

During the development stage I worked with Django's default sqlite3 database, which I later changed to
a PostgreSQL database which is provided by Heroku as an add-on.

### Data modelling

#### Product app

Products

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
SKU | sku | models.CharField | max_length=254
Name | name | models.CharField | max_length=254
Description | description | models.TextField | ()
Price | price | models.DecimalField | max_digits=6, decimal_places=2
Image_url | image_url | models.URLField | max_length=1024, null=True, blank=True
Image | image | models.ImageField | upload_to='', null=True, blank=True
Category | category |models.ForeignKey | 'Category', null=True, blank=True, on_delete=models.SET_NULL
Winery | winery | models.CharField | max_length=254, null=True, blank=True
Country | country | models.CharField | max_length=254, null=True, blank=True
Variety | variety | models.ForeignKey | 'Variety', null=True, blank=True, on_delete=models.SET_NULL, max_length=254
Vintage | vintage | models.IntegerField | null=True, blank=True
Region | region | models.ForeignKey | 'Wine_region', null=True, blank=True, on_delete=models.SET_NULL, max_length=254
Alc_vol | alc_vol | models.DecimalField | null=True, blank=True, max_digits=6, decimal_places=2
Pairing | pairing | models.CharField | max_length=254, null=True, blank=True
Is_a_subscription | is_a_subscription | models.BooleanField | default=False

Category

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
Name | name | models.CharField | max_length=254
Friendly_name | friendly_name | models.CharField | max_length=254

Variety

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
Name | name | models.CharField | max_length=254
Friendly_name | friendly_name | models.CharField | max_length=254

Wine_region

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
Name | name | models.CharField | max_length=254
Friendly_name | friendly_name | models.CharField | max_length=254


#### Profile app

User Profile

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
User| user | models.OneToOneField | User, on_delete=models.CASCADE
Phone Number | default_phone_number | models.CharField | max_length=20, null=True, blank=True
Street Address 1| default_street_address1 | models.CharField | max_length=80, null=True, blank=True
Street Address 2| default_street_address2 | models.CharField | max_length=80, null=True, blank=True
Town or City| default_town_or_city | models.CharField | max_length=40, null=True, blank=True
County, State or Locality| default_county | models.CharField | max_length=80, null=True, blank=True
Postcode| default_postcode | models.CharField| max_length=20, null=True, blank=True
Country| default_country | CountryField| blank_label='Country', null=True, blank=True

#### Checkout app

Order

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
Order number| order_number | models.CharField| max_length=32, null=False, editable=False
User Profile| user_profile | models.ForeignKey  | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
Full Name | full_name | models.CharField | max_length=50, null=True, blank=True
Email| email | models.CharField | max_length=254, null=True, blank=True
Phone number | phone_number | models.CharField | max_length=20, null=False, blank=False
Country | country | CountryField| blank_label='Country *', null=True, blank=True
Postcode| postcode | models.CharField| max_length=20, null=True, blank=True
Town or City| town_or_city | models.CharField | max_length=40, null=True, blank=True
Street Address 1| street_address1 | models.CharField | max_length=80, null=True, blank=True
street_address2 | models.CharField | max_length=80, null=True, blank=True
County | county | models.CharField | max_length=80, null=True, blank=True
Date | date| models.DateTimeField| auto_now_add=True
Delivery cost | delivery_cost| models.DecimalField| max_digits=6, decimal_places=2, null=False, default=0
Order total | order_total| models.DecimalField| max_digits=10, decimal_places=2, null=False, default=0
Grand total | grand_total| models.DecimalField| max_digits=10, decimal_places=2, null=False, default=0
Original bag | original_bag| models.TextField| null=False, blank=False, default=''
Stripe Pid | stripe_pid| models.models.CharField| max_length=254, null=False, blank=False, default=''


Order Line item

Name | Key | Field Type | Validation
------------ | ------------- | ------------- | ------------- 
Order | order | models.ForeignKey| Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
Product | product | models.ForeignKey  | Product, null=False, blank=False, on_delete=models.CASCADE
Quantity | quantity | models.IntegerField | null=False, blank=False, default=0
Item Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False


## Technologies Used

### Languages

- HTML5 

- CSS3 

- JavaScript

- Python3

- Jinja templating language

### Libraries and frameworks



### Tools

- Balsamiq app for creating wireframes.

- [Am I responsive?](http://ami.responsivedesign.is/) to demonstrate responsiveness in this README file.

- [Font Awesome](https://fontawesome.com/) for icons.

- [Google Fonts](https://fonts.google.com/)

- [Icons 8](https://icons8.com/) for sidenav icons

### Databases




## Testing


### Testing in different browsers



### Testing against the user stories



### Validation


### Problems encountered


## Deployment

### Local deployment


### Heroku deployment


## Credits

### Code



### Content and Media



## Acknowledgements


## Disclaimer 


