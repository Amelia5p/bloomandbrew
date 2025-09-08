# Bloom and Brew

Bloom and Brew is a full-stack e-commerce website built with Django. It sells fresh flower bouquets and artisan coffee, as well as gift bundles that combine both. Users can browse products, search by keyword or category, and place secure online orders through a simple checkout process.

The live link can be found here - [Bloom and Brew](https://bloom-and-brew-2265123bf17d.herokuapp.com/)

![Am I Responsive](static/readme-images/responsive.png)

## Table of Contents

<details>
<summary>View Table of Contents</summary>

- [Bloom and Brew](#bloom-and-brew)
  * [Table of Contents](#table-of-contents)
  * [Agile Development- Epics and User Stories](#agile-development--epics-and-user-stories)
  * [EPIC 1: E-commerce & Payments](#epic-1--e-commerce---payments)
    + [User Stories:](#user-stories-)
      - [#1 User Story: Browse Products](#-1-user-story--browse-products)
      - [#2 User Story: View Product Detail](#-2-user-story--view-product-detail)
      - [#3 User Story: Add Items to Cart](#-3-user-story--add-items-to-cart)
      - [#4 User Story: Checkout with Stripe](#-4-user-story--checkout-with-stripe)
      - [#5 User Story: View Past Orders](#-5-user-story--view-past-orders)
      - [#6 User Story: Create Products (Admin)](#-6-user-story--create-products--admin-)
      - [#7 User Story: Update or Delete Products (Admin)](#-7-user-story--update-or-delete-products--admin-)
  * [EPIC 2: UX Design & Front-End](#epic-2--ux-design---front-end)
    + [User Stories:](#user-stories--1)
      - [#8 User Story: User-Friendly Layout](#-8-user-story--user-friendly-layout)
      - [#9 User Story: Feedback Messages](#-9-user-story--feedback-messages)
      - [#10 User Story: Simple Admin UI](#-10-user-story--simple-admin-ui)
      - [#17 User Story: View Custom 404 Page](#-17-user-story--view-custom-404-page)
      - [#16 User Story: Understand the Site Purpose](#-16-user-story--understand-the-site-purpose)
  * [EPIC 3: Marketing Tools](#epic-3--marketing-tools)
    + [User Stories:](#user-stories--2)
      - [#14 User Story: Subscribe to Newsletter](#-14-user-story--subscribe-to-newsletter)
      - [#15 User Story: View Facebook Page](#-15-user-story--view-facebook-page)
  * [EPIC 4: Authentication & Role Based Access](#epic-4--authentication---role-based-access)
    + [User Stories:](#user-stories--3)
      - [#11 User Story: Register and Login](#-11-user-story--register-and-login)
      - [#12 User Story: Admin Access](#-12-user-story--admin-access)
  * [Business Plan and Marketing Strategy](#business-plan-and-marketing-strategy)
  * [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Features](#features)
    + [Navigation Bar](#navigation-bar)
    + [Footer](#footer)
    + [Home Page](#home-page)
      - [Hero section](#hero-section)
      - [Bundles and Newsletter](#bundles-and-newsletter)
      - [Featured Picks](#featured-picks)
      - [CTA](#cta)
    + [Shop All Products](#shop-all-products)
    + [Shop Blooms](#shop-blooms)
    + [Shop Brews](#shop-brews)
    + [Shop Bundles](#shop-bundles)
    + [Shopping Cart](#shopping-cart)
    + [Order Success](#order-success)
    + [My Orders/ Order History](#my-orders--order-history)
    + [About Us/ Contact Us](#about-us--contact-us)
    + [Profile](#profile)
    + [Sign Up](#sign-up)
    + [Log In Page/ Success](#log-in-page--success)
    + [Log Out Page/ Success](#log-out-page--success)
    + [Error pages](#error-pages)
    + [Success Messages](#success-messages)
    + [Newsletter](#newsletter)
  * [Future Features](#future-features)
  * [CRUD Functionality](#crud-functionality)
  * [Data Model](#data-model)
    + [Checkout App](#checkout-app)
      - [Order](#order)
      - [OrderItem](#orderitem)
    + [Products App](#products-app)
      - [Product](#product)
      - [Review](#review)
    + [Profiles App](#profiles-app)
      - [UserProfile](#userprofile)
- [Testing](#testing)
  * [General Testing](#general-testing)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
  * [General Tests](#general-tests)
    + [Lighthouse](#lighthouse)
  * [Browser Testing](#browser-testing)
  * [Homepage Tests](#homepage-tests)
  * [Product App Tests](#product-app-tests)
  * [Checkout App Tests](#checkout-app-tests)
  * [Cart App Tests](#cart-app-tests)
  * [Profile App and Order History Tests](#profile-app-and-order-history-tests)
  * [Security Features](#security-features)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
  * [Deployment - Heroku](#deployment---heroku)
  * [Cloning Repository](#cloning-repository)
    + [<ins> Step 1: </ins>](#-ins--step-1----ins-)
    + [<ins> Step 2:</ins>](#-ins--step-2---ins-)
    + [<ins>Step 3: </ins>](#-ins-step-3----ins-)
    + [<ins>Step 4: </ins>](#-ins-step-4----ins-)
    + [<ins> Result: </ins>](#-ins--result----ins-)
  * [Forking Repository](#forking-repository)
    + [<ins>Step 1:</ins>](#-ins-step-1---ins-)
    + [<ins>Step 2:</ins>](#-ins-step-2---ins-)
    + [<ins>Step 3: </ins>](#-ins-step-3----ins--1)
    + [<ins>Result:</ins>](#-ins-result---ins-)
  * [Languages](#languages)
    + [Programs used](#programs-used)
  * [Bugs](#bugs)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

  </details>

## Agile Development- Epics and User Stories
This project was managed using a GitHub Kanban Project board with Epics and User Stories.
Link: [Kanban Board](https://github.com/users/Amelia5p/projects/8)


## EPIC 1: E-commerce & Payments
### User Stories:

#### #1 User Story: Browse Products
As a user I want to browse all products so that I can choose what to purchase.

#### #2 User Story: View Product Detail
As a user I want to view the details of a product so that I can make an informed purchase decision.

#### #3 User Story: Add Items to Cart
As a user I want to add items to a cart so that I can buy multiple things in one checkout.

#### #4 User Story: Checkout with Stripe
As a user I want to pay for my order using Stripe so that I can complete my purchase securely.

#### #5 User Story: View Past Orders
As a user I want to view my previous orders so that I can track what I’ve purchased.

#### #6 User Story: Create Products (Admin)
As an admin I want to create new products so that I can update the store with new inventory.

#### #7 User Story: Update or Delete Products (Admin)
As an admin I want to edit or remove existing products so that I can manage inventory changes.


## EPIC 2: UX Design & Front-End
### User Stories:

#### #8 User Story: User-Friendly Layout
As a user I want to navigate easily on mobile and desktop so that I can shop from any device.

#### #9 User Story: Feedback Messages
As a user I want to see clear messages when actions succeed or fail so that I understand what happened.

#### #10 User Story: Simple Admin UI
As an admin I want a simple interface so that I can manage content without confusion.

#### #17 User Story: View Custom 404 Page
As a user I want to see a helpful 404 page when I visit a broken link so that I’m not confused and I'm redirected easily.

#### #16 User Story: Understand the Site Purpose
As a user I want to understand what the site is selling so that I can decide if it's relevant to me.

## EPIC 3: Marketing Tools
### User Stories:

#### #14 User Story: Subscribe to Newsletter
As a user I want to sign up for the newsletter so that I can receive news and offers.

#### #15 User Story: View Facebook Page
As a user I want to view the Facebook business page so that I can connect with the brand.

## EPIC 4: Authentication & Role Based Access 
### User Stories:

####  #11 User Story: Register and Login
As a user I want to create an account and log in so that I can view my orders.

####  #12 User Story: Admin Access
As an admin I want to access a private page so that I can manage products securely.

## Business Plan and Marketing Strategy

<details>
<summary>View Business Plan and Marketing Strategy including Facebook Mockups</summary>

<br>

![Business Plan (1)](static/readme-images/plan1.png)  
![Business Plan (2)](static/readme-images/plan2.png)  
![Business Plan (3)](static/readme-images/plan3.png)
![Facebook](static/readme-images/facebook.png)

</details>

## Design

#### Colour Scheme

This particular colour scheme was chosen to reflect the calm and earthy feel of the brand. The soft tones of Tea Green , Misty Rose, and Isabelline create a light, fresh look suitable for flowers and gift products. The richer shades of Beaver and Rose Ebony add warmth and depth, helping to balance the overall design — especially for the coffee product pages.

![Colour Palette](static/readme-images/colour-palette.png)

#### Imagery

The product shots were created using Photo Recreator AI. Other images used were sourced from Pexels free images.

#### Fonts

The site uses two main fonts to support brand personality and readability:

Playfair Display is used for headings. It gives the site an elegant and refined look, which suits the flower and gift elements of the brand.

Poppins is used for body text. Its clean, modern style makes content easy to read across all screen sizes.

![Playfair Display](static/readme-images/playfair-display.png)

![Poppins](static/readme-images/poppins.png)

#### Wireframes
Wireframes were created at the start of the project to plan the layout, structure, and user flow before development. This helped ensure a consistent design and smooth user experience across all pages.

<details>
<summary>View Wireframes</summary>

<br>

![Wireframes](static/readme-images/wireframes.png)

</details>


## Features

### Navigation Bar

- The navigation at the top of each page provides easy access to all main sections of the website.

![Navigation Bar](static/readme-images/navbar1.png)

![Navigation Bar 2](static/readme-images/navbar2.png)

![Navigation Bar 3](static/readme-images/navbar3.png)



### Footer

- The footer is at the bottom of each page and contains social links. I made sure these links opened in another tab to prevent users from being driven away from the site.

![Footer](static/readme-images/footer.png)

### Home Page

#### Hero section
- Purpose of the site is revealed right away. Eye-catching image and introduction text help set the tone and guide the user into the site.

![Hero Section](static/readme-images/hero-section.png)

#### Bundles and Newsletter
- Highlights bundle deals and encourages users to sign up for the newsletter.

![Bundle/ Newsletter](static/readme-images/bundle-newsletter.png)

#### Featured Picks
- Shows selected popular or seasonal items on the homepage to catch user interest.

![Featured Picks](static/readme-images/featured-section.png)

#### CTA
- A clear call-to-action encouraging users to start shopping right away.

![Home cta](static/readme-images/home-cta.png)

### Shop All Products
- Displays the full range of available products with filters and search functionality.

![Shop All](static/readme-images/shop-all.png)

### Shop Blooms
- Displays all flower-related products.

![Shop Blooms](static/readme-images/shop-blooms.png)

### Shop Brews
- Displays all coffee-related products.

![Shop Brews](static/readme-images/shop-brews.png)

### Shop Bundles
- Combines flowers and coffee into curated gift bundles.

![Shop Bundles](static/readme-images/shop-bundles.png)

### Shopping Cart
- Lets the user view, update, or remove items before checking out.

![Shopping Cart](static/readme-images/shopping-cart.png)

### Order Success
- Confirms the order has been placed and thanks the user.

![Order Success](static/readme-images/order-success.png)

### My Orders/ Order History
- Shows a summary of all previous orders made by the user.

![My orders](static/readme-images/my-orders.png)

![Order History](static/readme-images/order-history.png)


### About Us/ Contact Us
- Introduces the brand and gives context about the company and its value, contact information provided also.

![About Us](static/readme-images/about-us.png)

### My Wishlist
- Shows the users saved items in a wishlist ordered by date added.
![Wishlist](static/readme-images/wishlist.png)

![Wishlist1](static/readme-images/wishlist1.png)

![Wishlist2](static/readme-images/wishlist2.png)


### PromoCode 
- Users can add a promocde to get a discount.
![Promocode](static/readme-images/promocode.png)

### Profile
- Users can view and manage their saved details here.

![My Profile](static/readme-images/my_profile.png)

### Sign Up
- When a user signs up, a profile is automatically created for them, the user can add to and edit the profile.

![Sign Up](static/readme-images/signup.png)


### Log In Page/ Success
-Allows existing users to log in and confirms successful login.

![Log in](static/readme-images/login.png)

![Signed in](static/readme-images/signed-in.png)


### Log Out Page/ Success
- Confirms successful logout and ends the user session.
![Log Out](static/readme-images/logout.png)

![Logged Out](static/readme-images/logged-out.png)


### Error pages
- Custom 404 page shown when a user tries to access a page that doesn't exist.

![Error](static/readme-images/error-404.png)


### Success Messages
- Success messages are shown on every action made by the user.

![Success](static/readme-images/subscribe-success.png)

### Newsletter
- The User can sign up to receive the newsletter easily on the landing page.

![Newsletter](static/readme-images/newsletter.png)

## Future Features

In the future the following features would further improve the site:
- Add functionality to save the user's cart if they log out and back in, once more products are added, this was not needed so a session-based cart was used as the product range is quite small.


## CRUD Functionality

- Full CRUD functionality is implemented on the site. User's can Create, Read, Update and Delete both their cart and their profile information.

## Data Model
- The data models for the project are shown below. 

![DB Schema](static/readme-images/erd.png)

### Checkout App
#### Order

- Description: Represents a customer's order including personal details, payment info, and address.

`order_number:` A unique identifier for the order, generated automatically.

`reference_code:` A second unique identifier used for tracking or verification.

`user:` ForeignKey to the UserProfile model, representing the user who placed the order.

`full_name:` Full name of the customer.

`email_address:` Customer's email address.

`contact_number:` Phone number of the customer.

`address_line_1:` First line of the shipping address.

`address_line_2:` Second line of the shipping address (optional).

`town:` Town or city of the shipping address.

`county:` County of the shipping address.

`postal_code:` Postal or ZIP code.

`country:` Country selected using Django Countries.

`created_on:` Timestamp when the order was created.

`subtotal:` The subtotal cost of all items before delivery.

`delivery_fee:` Delivery charge, waived for orders over €50.

`total_due:` The final total amount to be paid.

`cart_snapshot:` Text snapshot of the cart contents at the time of order.

`stripe_pid:` Stripe PaymentIntent ID for reference.

#### OrderItem

- Description: Represents an individual item within an order.

`order:` ForeignKey to the Order model the item belongs to.

`product:` ForeignKey to the Product model for the purchased item.

`quantity:` Number of units ordered for that product.

`item_total:` Total price for this item (product price × quantity), calculated automatically.

#### PromoCode  

- Description: Represents a discount code that can be applied to orders.  

`code:` Unique code entered by the customer.  

`percent_off:` Percentage discount applied to the subtotal.  

`is_active:` Whether the promo code is currently valid and usable. 

### Products App
#### Product

- Description: Represents items available for sale in the store, including bouquets, coffee, and gift bundles.

`name:` Name of the product.

`sku:` A unique stock keeping unit for internal reference.

`description:` A detailed description of the product.

`category:` The product type – bouquet, coffee, or bundle.

`price:` Standard selling price of the product.

`special_offer_price:` Optional discounted price if on special offer.

`image:` Product image stored via Cloudinary.

`stock:` Quantity of the item available in inventory.

`slug:` URL-friendly version of the product name, generated automatically.

`is_featured:` Marks the product to be shown in the "Featured Picks" section.

`bundle_of_the_week:` Highlights a product as the weekly featured bundle.

#### Review
- Description: Stores user-submitted reviews, including star rating and optional written feedback.

`product:` ForeignKey to the Product being reviewed.

`user:` ForeignKey to the User who wrote the review.

`rating:` Star rating from 1 to 5.

`comment:` Optional written comment left by the user.

`created_on:` Timestamp of when the review was submitted.

Reviews are ordered with the newest first and a user can only leave one review per product.

#### Wishlist  

- Description: A collection of products saved by a user for future reference. Each user has one wishlist.  

`user:` One-to-one relationship with the User who owns the wishlist.

`created_on:` Timestamp of when the wishlist was created.  

#### WishlistItem  

- Description: Represents an individual product saved in a user's wishlist.  

`wishlist:` ForeignKey to the Wishlist it belongs to.

`product:` ForeignKey to the Product saved to the wishlist.  

`added_on:` Timestamp when the product was added.  

### Profiles App
#### UserProfile

- Description: Stores additional information about each user, such as saved shipping details and contact number. Automatically created or updated when a User is saved.

`user:` One-to-one relationship with Django's built-in User model.

`phone:` Optional phone number for contact.

`address_1:` First line of the user's saved address.

`address_2:` Second line of the address (optional).

`city:` City or town name.

`county:` County name.

`country:` Country field using django-countries.

`postcode:` Postal or ZIP code.

The profile is created automatically when a new user is registered, using Django signals.


# Testing

## General Testing

### HTML

All HTML was passed through the W3C validator with no errors.

![HTML](static/readme-images/html-validation.png)

| Page                   | Result     |
|------------------------|------------|
| base.html              | No errors  |
| home.html              | No errors  |
| about.html             | No errors  |
| add-product.html       | No errors  |
| add-review.html        | No errors  |
| delete_product.html    | No errors  |
| delete_review.html     | No errors  |
| edit_product.html      | No errors  |
| edit_review.html       | No errors  |
| manage_products.html   | No errors  |
| product_detail.html    | No errors  |
| product_list.html      | No errors  |
| shop_blooms.html       | No errors  |
| shop_brews.html        | No errors  |
| shop_bundles.html      | No errors  |
| cart.html              | No errors  |
| checkout_success.html  | No errors  |
| checkout.html          | No errors  |
| order_history.html     | No errors  |
| edit_profile.html      | No errors  |
| profile.html           | No errors  |
| login.html             | No errors  |
| signup.html            | No errors  |
| 404.html               | No errors  |
| 500.html               | No errors  |


### CSS

All CSS was passed through W3C validator with no errors.

![CSS Validation](static/readme-images/css-validation.png)

### JavaScript

All JavaScript was passed through JShint with no errors.

![JS Validation](static/readme-images/js-validation.png)

### Python

All Python code was passed through the PEP8 CI linter with no errors.

![Python Validation](static/readme-images/python-validation.png)

## General Tests

| Test             | Action                                                                 | Success Criteria                                                 |
| --------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------- |
| **Homepage loads**  | Navigate to website URL                                            | Page loads with no errors                     |
| **Links**          | Click on each navigation link, CTAs, buttons, logo, and footer links  | Correct page loads or correct action performed, new tab opens if applicable |
| **Form validation** | Enter data into each input field, ensuring only valid data is accepted  | Form does not submit until correct data is entered, and an error message is shown |
| **Responsiveness**  | Resize viewport window from 320px upwards using Chrome DevTools. Test various devices  | Page layout remains intact and adapts correctly to different screen sizes |

### Lighthouse

Lighthouse validation was run on all pages (both mobile and desktop) and tested for performance, accessibility, best practices and SEO.

![Lighthouse](static/readme-images/lighthouse.png)

## Browser Testing
The Website was tested on Google Chrome, Firefox, Safari browsers with no issues.


## Homepage Tests
<details>
<summary>Expand test details</summary>

| Test                             | Action                                                                 | Success Criteria                                                       |
|----------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Hero Section CTA Clickability    | - Click on "Shop Now" button in the hero section                       | - Redirects to the product listing page                                |
| Featured Products Display        | - Verify the featured products section loads                           | - Exactly 4 featured products are shown with consistent layout         |
| Bundle of the Week Display       | - Scroll to the "Bundle of the Week" section                           | - One bundle product and accompanying image are displayed              |
| Product Card Responsiveness      | - Resize browser on featured products section                          | - All product cards remain the same size and stack cleanly             |
| Hero Section Layout              | - View hero section on various screen sizes                            | - Text and image columns stack correctly on smaller screens            |
| CTA Button Placement             | - Check "Shop Now" placement above bundle section                      | - Button appears visually within the hero section background           |
| Product Image Display            | - Confirm each product card contains an image                          | - All product images are present and not stretched or broken           |
| Navigation Link Functionality    | - Click on nav links like "Brews", "Blooms", "Bundles"                 | - Each link leads to the correct filtered product page                 |
| Cart Icon Display                | - Add product to cart and check cart icon                              | - Cart count updates and badge is visible in navbar                    |
| Homepage Load Performance        | - Open homepage with dev tools open (network tab)                      | - Page assets load within acceptable time (<3s on fast connection)     |


</details>

## Product App Tests

<details>
<summary>Expand test details</summary>

| Test                           | Action                                                             | Success Criteria                                                    |
|--------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| Product Grid Display           | Visit the product listing page                                     | Products display in 3-column layout with name, image, price, category |
| Product Card Link Functionality| Click on product image or name                                     | Redirects to the correct product detail page                        |
| Search Bar Functionality       | Enter search term and submit                                       | Products matching the term appear; irrelevant ones are excluded     |
| Category Filter Functionality  | Select a category and submit                                       | Only products in selected category are shown                        |
| Sort Option Functionality      | Select "Price: Low to High" or "Name: Z-A" and submit              | Products reorder accordingly                                        |
| Reset Button                   | Click the "Reset" button                                           | Clears filters and displays all products                            |
| No Results Message             | Enter nonsense in search or filter to an empty result              | "No products found..." message is shown                             |
| Discount Price Display         | Find a discounted product                                          | Special price shows with original price struck through              |
| Image Display Check            | Inspect product cards                                              | Product image loads and is proportionate                            |
| Back to Top Button Functionality| Scroll down and click "Back to Top"                                | Smooth scrolls page back to top                                     |


| Test                           | Action                                                             | Success Criteria                                                    |
|--------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| Product Info Display           | Visit product detail page                                          | Product name, image, description, category, and price are shown     |
| Discount Display               | View a discounted product                                          | Shows discount price and original price with strikethrough          |
| Out of Stock Message           | View a product with stock = 0                                      | "Out of stock" appears, Add to Cart is hidden or disabled           |
| Add to Cart Functionality      | Choose quantity and submit                                         | Product added to cart, success message appears                      |
| Quantity Validation            | Enter quantity beyond available stock                              | Prevents adding more than available; shows error or restricts input |
| Review Section Visibility      | Scroll to reviews                                                  | Reviews list shows if reviews exist; message shown if none exist    |
| Review Auth Display            | Visit as anonymous vs logged-in user                               | Login prompt for guests; “Write a Review” button for users          |
| Review Edit/Delete Buttons     | Logged-in reviewer views their review                              | Edit/Delete buttons shown only to author                            |
| Review Star Rating Display     | View reviews                                                       | Star rating (filled/empty) reflects review rating accurately        |
| Review Toggle                  | Click “Show all reviews” or “Show fewer reviews”                   | Expands or collapses review list appropriately                      |


</details>

## Checkout App Tests

<details>
<summary>Expand test details</summary>

| Test                            | Action                                                                   | Success Criteria                                                                 |
|---------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Checkout Form Loads             | Go to checkout with items in cart                                    | Form displays with Stripe card element and order summary                        |
| Checkout Redirect With Empty Cart | Try visit checkout with empty cart                                      | At least 1 item needed to checkout-“Your cart is empty” shown.                          |
| Stripe Card Element Loads       | Inspect checkout page                                                    | Stripe element is visible, no JS errors                                         |
| Valid Stripe Payment            | Use test card `4242 4242 4242 4242`, submit form                          | Order completes and redirects to confirmation page                              |
| Declined Card Error             | Use test card `4000 0000 0000 0002`, submit form                          | Stripe shows "Your card was declined", no order saved                           |
| Order Saved to DB               | Complete payment and check admin/DB                                       | Order and OrderItem records created with correct values                     |
| Cart Clears After Checkout      | Complete order, then visit cart                                      | Cart is empty and displays empty cart message                                   |
| Confirmation Page Accuracy      | Visit checkout/success after purchase                                | Order number and confirmation message are displayed                             |
| Delivery and Subtotal Calculation | Add items to cart and go to checkout                              | Subtotal, delivery fee, and total due are calculated and displayed accurately   |
| Stripe JavaScript Loads         | Inspect page source for Stripe scripts                                   | JS loaded with valid public key and client secret      |

</details>

## Cart App Tests

<details>
<summary>Expand test details</summary>

| Test                        | Action                                                                | Success Criteria                                                        |
|-----------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------|
| Cart Page Loads             | Visit cart                                                        | Cart table displays products, prices, quantities, and totals           |
| Update Quantity             | Change quantity input and click “Update”                              | Quantity updates and total recalculates                                |
| Remove Item                 | Click × “Remove” button                                               | Item is removed and cart updates accordingly                           |
| Empty Cart Message          | Visit cart with no items                                          | Displays: “Your cart is empty.” with button to start shopping          |
| Add Excessive Quantity      | Attempt to add quantity beyond available stock                        | Form prevents submission or shows validation error                     |
| Proceed to Checkout         | Click “Proceed to Checkout”                                           | Redirects to checkout if cart has items                            |
| Continue Shopping Button    | Click “Continue Shopping”                                             | Redirects to full product listing page                                 |
| Cart Total Accuracy         | Add items, update quantities, and review totals                       | cart.get_total_price` reflects correct calculation                    |
| Cart Icon Badge Updates     | Add/remove items and observe cart icon in navbar                      | Count badge updates in real time                                       |

</details>

## Profile App and Order History Tests

<details>
<summary>Expand test details</summary>

| Test                      | Action                                                                   | Success Criteria                                                             |
|---------------------------|--------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Profile Page Loads        | Visit profile while logged in                                        | Shows username, email, address, and buttons for edit and order history      |
| Edit Profile Form Loads   | Go to profile/edit                                                   | Form is pre-filled with user data                                           |
| Save Profile Changes      | Update fields and submit                                                 | Redirects to profile page with updated information                          |
| Required Field Validation | Clear required fields and submit                                         | Errors shown for empty fields                                               |
| Order History Lists Orders| Go to order-history with past orders                                 | Orders display with numbers, dates, items, total, and status                |
| Order History Empty State | Visit order-history with no orders                                   | Message: “You haven't placed any orders yet.” is displayed                  |
| Order Details Display     | Check content of order summary                                           | Includes items, quantities, total due, and created date                     |
| Buttons Function Properly | Click “Edit My Details” and “My Orders” buttons                          | Routes correctly to respective views                                        |

</details>

## Security Features

### User Authentication
Authorisation is required to reach certain pages such as the Admin Panel. Requesting these pages while unauthorised will not work.

### Form Validation
Incorrect or in certain cases empty data in forms is not accepted and the user is made aware of this.

### Database Security
The Database URL, Secret Keys, APIs etc. are stored in the env.py file to prevent unwanted connections.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.


## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Login to the Heroku dashboard and create a new app.
2. Connect your GitHub repository to your Heroku app.
3. Set environment variables in the Config Vars section of the Settings tab.
4. In the Deploy tab, enable automatic deploys from your GitHub repository.
5. Click the "Deploy Branch" button to deploy the app.
6. Once the app has been deployed, click the "Open App" button to view the app.

-  Under 'Config Vars' the following variables to be set:

    - `DATABASE_URL` - the URL for your Postgres database.
    ( Used dj-database-url, Heroku auto-configured everything from DATABASE_URL — no need to split it up manually.)
    - `HOST` - the host for your database.
    - `PORT` - the port for your database.
    - `CLOUDINARY_API_KEYS` - API Keys to host images.
    - `EMAIL_HOST_USER` - Email address
    - `MAILCHIMP_API_KEYS` - API Keys for Mailchimp.
    - `STRIPE KEYS`- For card payments 

    - Django settings:
    - `SECRET_KEY` - the secret key for your Django project. (kept in .env file)
    - `DEBUG` - set to `True` for development, `False` for production.

## Cloning Repository

### <ins> Step 1: </ins>

From the <a href="https://github.com/Amelia5p/bloomandbrew/" target="_blank">GitHub repository</a> click on the 'code' button.

### <ins> Step 2:</ins>

Click 'local' on the top of the drop down menu and copy the URL.

### <ins>Step 3: </ins>

Open Git Bash on windows and change the working directory to the location where you want the cloned directory.

### <ins>Step 4: </ins>

Type 'Git clone' followed by a space and paste the URL previously copied, hit enter.

### <ins> Result: </ins> 

You now have a local copy of the Github repository.

## Forking Repository

### <ins>Step 1:</ins>

From the <a href="https://github.com/Amelia5p/bloomandbrew/" target="_blank">GitHub repository</a> click on the 'fork' button in the top right corner of the page. 

### <ins>Step 2:</ins> 

Choose to copy only the main branch or all branches to the new fork.

### <ins>Step 3: </ins>

Click Create a Fork.

### <ins>Result:</ins>

There is now a forked copy on GitHub.


## Languages

- Python
- HTML
- CSS
- Javascript

### Programs used
- [Django](https://www.djangoproject.com/): main python framework used in the development of this project.
- [Heroku](https://dashboard.heroku.com/login) - used as the cloud based platform to deploy the site on.
- [Balsamiq](https://balsamiq.com/) - used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - used for overall development and testing.
- [Font Awesome](https://fontawesome.com/) - used for icons.
- [GitHub](https://github.com/) - used for agile tool.
- [Google Fonts](https://fonts.google.com/) - used to import fonts.
- [W3C](https://www.w3.org/) - used for HTML & CSS Validation.
- [PEP8 CI Linter](https://pep8ci.herokuapp.com/) - used to validate all the Python code.
- [Jshint](https://jshint.com/) - used to validate javascript.
- [Favicon](https://favicon.io/) - used to create the favicon.
- [Mermaid](https://mermaid.live/) - used to create the database schema design
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/):Framework for developing responsiveness and styling
- [Am I responsive](https://ui.dev/amiresponsive) used for responsive picture
- [Coolors](https://coolors.co/) used for creating colour palette
- [Stripe](https://stripe.com/ie) used for taking payments
- [Pexels](https://www.pexels.com/) used free images


## Bugs
- Responsive-layout issue: Navbar overflowed on screens under 480 px width. Fix: Introduced mobile media-queries and stacked links.
- Cart issue: User was able to add in 99 of one item when there was only 50 in stock. Fix:  implement a validation check in the view that handles adding products to the cart.
- Meta Descriptions: These were being rendered in the HTML. Fix: removed these issues by reorderig HTML.
- If a product had a discount, the base price was still being shown in order history. Fix: Updated OrderItem.save() to snapshot the total at checkout.
- Some orders were being saved to the database with a total of €0. Fix: add signals to compute item_total and auto-recalculate order totals and fixed old ones by making fix_orders.py file in the root and running it through the shell.

## Credits
- [Code Institute - Walkthrough Project](https://github.com/Code-Institute-Solutions/boutique_ado_v1_sourcecode)

## Acknowledgements 
This is the fifth and final project, created for the Code Institutes Full Stack Web Developer (eCommerce) course. I would like to thank my cohort facilitator and the Code Institute team for their support.