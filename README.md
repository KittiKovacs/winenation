# Milestone 4 : Wine Nation 

## 


As this is the final Milestone project of Code Institute's Full stack web developer course, my aim was to create a full-stack site based around business logic used to control a centrally owned dataset and to provide paid access to the site's data and services.

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

I used the Bootstrap front-end framework throughout the development process, mainly for features such as navbar, cards, modals, carousel and the grid layout.

The website's colour scheme is in line with  the theme of the site with black and grey added for contrast. It is dominated by reds, yellow and pink to reflect the colours of red, white and rose wines.
![colour scheme]()

I am using a simple sans-serif font from Google Fonts called Raleway to create a modern look and and easy to read website.


### Wireframes

Wireframes for desktop, tablet and mobile can be found [here](https://github.com/KittiKovacs/winenation/tree/master/wireframes).

The final website is slightly different from what I had in mind originally, as sometimes I found a different solution would be more suitable.

## Features

### Existing Features

#### Age verification

When visiting the website the user is first asked to verify if they are over 18 years of age which is the legal age to purchase alcohol in the UK.
This is to ensure that no underage user can purchase wine online.
[!age verification](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/age_verification.JPG)

If the user clicks "YES" the webste's landing page will display. If the user clicks no, the only option the site offers is to close the page.
[!age verification under 18](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/age_under_18.JPG)

#### navigation

On the top of the page the user can find the main navigation elements, such as the menu items, bag and profile icons and search bar.
[!header navigation](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/header.JPG)
In the center of the page there's the logo and a slogan underneath. On clicking the logo the user can navigate back to the homepage.
Some navigation elements have sub-elements which open in a dropdown, such as the wines page and the profile icon.
[!menu dropdown](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/wines_dropdown.JPG) [!profile dropdown](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/Profile_dropdown.JPG)

On mobile screens the menu items are condensed into a hamburger button and the search icon, profile and bag icons are displayed on top of the page.
[!mobile navigation](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/navigation_mobile.JPG)

On the bottom of the page users can find a footer containing links to external partner sites, social media account and
the shop's physical address and contact details.
[!footer](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/footer.JPG)

In the bottom right corner there is a an upward pointing arrow that takes the user back to the top of the page when clicked.

Another navigation feature on the all wines, red, white and sparkling and dessert wines pages is pagination which is on the bottom of the page in the middle.

#### Landing page
This is created to make a first impression to the user and also to act as a manifesto to the site. 
It features all navigation elements and also a button to take the user straight to the all wines page.
[!landing](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/landing%20image%20and%20button.JPG)

#### About us page
This page describes the purpose of the site with a short description on the top that has a scrolling image as a background,
a more details description about wines and the area, and contains an image carousel on the bottom with user reviews.
The carousel and the parallax scolling background are not displayed on small screens.
[!about us](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/about-1.JPG)[!carousel](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/carousel.JPG)

#### Wines page

This page contains 50 wines divided into 4 categories (Red, White, Rose, Dessert and Sparkling wines).
The user can view all wines on the same page or by individual categories.
[!all wines](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/all_wines.JPG)

If the user is on a category page, they have an option to return to the All wines page.
[!category](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/white_wines.JPG)

There is a sorting option on the top right where the user can sort products alphabetically, by category or by price.
The user is also able to search by keyword.
[!search results](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/search_results.JPG)

The products are displayed on cards that contains the product image, name and the category.
On clicking the product name the user is taken to the product's details page.

#### Wine details page

This page contains more details about the product and gives the opportunity
for the user to choose a quantity by using the quantity selector and add the product to the shopping bag.
[!wine details page](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/wine_details.JPG)

If the item is successfully added to the bag a toast message appears on the top. This gives the user a list of what's in the bag, the product prices and a total.

It also has a link to the bag.
[!success toast](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/success-toast.JPG)

#### Subscriptions

The subscriptions page has a similar structure to the About page, it has a short introduction with a parallax scrolling background (visible on medium viewports and above ),
then some text describing the service and the benefits it offers to users.
[!sucbscription page](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/subscriptions.JPG)

Below this the user can see the subscription types to choose from, each displayed on a card with a description and price.
Here they also have a choice to adjust quantities and add the subscription type to the bag. There isn't a page for each subscription like there is for the wines,
I created one initially but I felt it was redundant and went in a different direction.

[!subscription types](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/subscription_types.JPG)


#### Shopping bag

The user is not automatically redirected to the shopping bag when placing an item in the bag. They can access it by clicking on the
button in the toast message popping up, or by clicking on the bag icon in the top right corner.
The bag page is available for both logged in and non-logged in users, so that it is possible to make purchase as a guest.
The page contains a summary of the user's order: the item's image, name, sku, quantity, price and subtotal.
Subscriptions do not have images so I set a default image to display in case there's no image associated with an item.
[!bag]https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/bag.JPG)

A user can update the item's quantity by using the quantity selector buttons, or remove items from their order. Toast messages will be displayed when a user updates/removes items in the bag.
At the bottom of the page the subtotal, delivery coast and grand total are displayed.
There is a checkout button that takes a user to the checkout page to proceed with the payment, 
and there's also an option for returning to the all wines page in case the user wants to add more items to the bag.
[!checkout button](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/checkout_button.JPG)

#### Checkout

The Checkout page contains the checkout form and the order summary.
[!checkout page](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/checkout1.JPG)

On the right side of the page, there is the Order summary.
This includes short information about items in the order (image, name, quantity of each item in the bag, subtotal, delivery cost, total to pay.),
and a button below this that redirects the users back to the bag in case they need so make some changes. 

The checkout form on the left asks for the user's personal details and delivery address, and contains a field for the card details to be entered.
The user is can double check how much the card will be charged as the total is displayed below the Complete order button
[!checkout form](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/checkout2.JPG)

If the user doesn't have an account or isn't logged in, there are links to the register and login pages for easier navigation.
For logged in users, a save info checkbox allows the form information to be saved to their profile. For logged in users the form will be pre-populated with this information.

The Stripe functionality is only for testing at the moment, so only entering 4242 4242 4242 4242 card number will result in successfull payment. Expiration date can be any date in future and CVC can be any numbers.
The site is using webhooks to make sure that the order is processed even if when the payment process is interrupted (e.g. if a user accidentally closes the page or browser after clicking "Proceed to payment" button).

If the form is submitted successfully and payment was processed, the user is taken to the checkout sucesss page and a confirmation email is sent to the user's email address at the same time.
If there is something missing from the form, hints are displayed for the users on how to resolve the issue.

#### Checkout Success page

A thank you message informs the customer about the successful completion of the transaction and that they should receive a confirmation email soon.
They are also presented with a table summarizing the order details:
- Order number and date
- Shipping details
- Billing info 
A button below the table redirects user to the All wines page.
Also, a success toast message appears in the top right corner that includes the order number and confirmation email address.
[!checkout success](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/checkout_success.JPG)

### User authentication

These are all part of the Django-allauth package.

#### Register

This allows a user to create a new account. In case the user already has an account, there is a link to the login page for existing users above the form.
The Registration page is only available to non-logged in users.
The form contains fields for an email addres, email address confirmation, username, password" and password (again).
When adding a username, the code compares it against existing email to ensure that it is unique.
[!registration form](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/register.JPG)
If user's input does not meet requirements, the form displays and error. 
When the form is submitted, a verification email is sent to the user's email address to finish the registration process.
[!registration form error](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/registration_error.JPG)

#### Login

The login page features the form with username and password fields. There are 2 buttons below the form, one for logging in and one for returning to the home page. There is also a "remember me" tickbox under the form as well as a link to the reset password feature.
[!login](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/login.JPG)
If the login was successful, the user is redirected to the home page and a toast success message appears in the top right corner.
Otherwise, the form displays a message about incorrect user input.
There is also a link to the sign up page for new users above the form.

#### Profile

Logged in users are able to see their Profile which contains their saved details and order history (if any).
The page displays the username on top, delivery information to the left with a button to update this information. It is pre-populated if the user already has saved information.
To the right there is a short order history with order id, order date, items and order total.

[!profile](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/profile.JPG)

By clicking on the order number the same table displays the user would see after a successful checkout,
and the Toast info message will tell the user that it's a past confirmation for the order number.
The back to profile page button will redirect a user to the Profile page.
[!order history](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/order_history.JPG)

#### Logout

Logged in users have the option to log out by clicking on the "logout" option underneath Profile on the top of the page.
The user is redirected to the logout page where to user has to confirm they want tolog out. 
It will end their session and a toast success message informs them about successful log out. The user is redirected to the home page.
[!logout](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/logout.JPG)

#### Password reset

A user can reset their password to be able to login by entering the email by clicking on the Forgot password lon on the login page.
If they enter their email address and click reset passsword, a link will be sent to the email provided.
The user can create a new password and then login with a new password.
[!password reset](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/password%20_reset.JPG)


#### 404 and 500 error pages

Custom 404 and 500 pages are displayed when this error occurs which give the users a chance to return to the homepage.

#### Admin functions

The Product managment feature is available only for authenticated superusers. 
[!product management link](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/admin1-product%20management%20link.JPG)
The superuser has permission to add new products by filling in the Add New Product or Edit product forms. 

By clicking on the Product management option the user can add a new product by filling in the form. They can upload a photo for each product.
By ticking "is a subscription" they are also able to create a new subscription type.
[!add product form](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/add_product.JPG)

To edit a product, the superuser can click in the Edit option on the product's card. This feature is only visible for superusers.
[! edit product1](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/edit_product.JPG)
They will be taken to the edit product page where they can overwrite the existing details and add a new image.
[! edit product form](https://github.com/KittiKovacs/winenation/blob/d99b7cdb531a29f928be75987bd74ca225cb9e49/wireframes/feature_images/edit_product_1.JPG)

To delete a product the superuser can click on the delete link on the product card. This is also not visible for non-superusers.

All these changed are confirmed in the form of toast messages as well.

### Features left to implement

There are some more features that I feel would improve on the overall user experience and could be beneficial to a real-life shop owner I didn't feel important or got around to implement, but I intend to add them later.

Rating and Customer Reviews
At the moment users have no means to give feedback to the store owner and to each other about the product, which is a quite important feature in a modern webshop.
Users in the future would be able to create, edit and delete their reviews, and give a star (or wine glass)-based rating to each product which would display on the product details page along with the reviews.

User uploaded photos
This feature would allow users to add photos to their reviews as well as an avatar to their profile.

News section
This would be a page for the store owner to potentially post updates, news and offers to the site.

Social account login (Google and Facebook)
This feature would allow users to login using social networks accounts, such as Google and Facebook.


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

- I used the responsive viewer extension in Google Chrome to demonstrate responsiveness in this README file.

- [Font Awesome](https://fontawesome.com/) for icons.

- [Google Fonts](https://fonts.google.com/)

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


