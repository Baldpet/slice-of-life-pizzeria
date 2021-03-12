<div align="center"><img src="https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/logo.png"></div>

Welcome to the Slice of Life Pizzeria. Where you can get your hungry fed!

Check out the live site here: https://baldpet-slice-of-life.herokuapp.com/

## __Contents__

- [Aim of The Site](#aim-of-the-site)
- [UX](#ux)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
    - [Colours](#colours)
    - [Database Plan](#database-plan)
- [Features](#features)
- [Future Goals](#future-goals)
- [Technology Used](#technology-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknoledgements)
- [Disclaimer](#disclaimer)


## __Aim of the Site__

The aim of the site is to provide an ecommerce store to provide take away services for hungry people.
The site is also a platform for the staff to use to co-ordinate orders and update the order status which can be tracked by the user. 

## __UX__

### __User Stories__

There were a number of users that I looked at which each had unique user stories for each of them:  

* Shopper
* Store Owner
* Store Worker

Based on these users I looked at specific user stories that each of them would have, the list of stories is below:

| User Story ID | As a User | I want to be able to...                                                      | So that I can...                                             |
|---------------|-----------|------------------------------------------------------------------------------|--------------------------------------------------------------|
| 1             | Shopper   | View pizzas and Sides                                                        | Select some to purchase                                      |
| 2             | Shopper   | View ingredients                                                             | Determine any alergies                                       |
| 3             | Shopper   | Clearly view the offers                                                      | Decide if the offers are worth it or not                     |
| 4             | Shopper   | View the total of the order at any time                                      | not spend too much and to decide if the order is complete    |
| 5             | Shopper   | Easily register for an account                                               | Have an account and view my profile                          |
| 6             | Shopper   | Easily login and out                                                         | Access my account                                            |
| 7             | Shopper   | Recover my password                                                          | Recover my account if the password was lost                  |
| 8             | Shopper   | Receive an email to confirm registration                                     | Verify my account for security                               |
| 9             | Shopper   | Have a personalised user profile                                             | Save my personal info                                        |
| 10            | Shopper   | Keep a track of my loyalty points                                            | View loyalty points available to me                          |
| 11            | Shopper   | Easily select Pizzas and Sides for the order                                 | Endure I select the correct Pizza/Offer                      |
| 12            | Shopper   | View items in the order to be purchased                                      | Make sure I do not order the incorrect item                  |
| 13            | Shopper   | Able to edit the items in the order                                          | To adjust the order easily if something is not right         |
| 14            | Shopper   | Easily enter my payment details                                              | To get my order quicker and easily                           |
| 15            | Shopper   | View order after checkout                                                    | Confirm what info I have entered is correct                  |
| 16            | Shopper   | Have a tracker to track where my order is                                    | So I can see how long the food is away                       |
| 17            | Shopper   | Receive an email confirmation on checkout                                    | For reciept of payment                                       |
| 18            | Shopper   | Have my address info already available when entering checkout - if logged in | For ease of checkout                                         |
| 19            | Shopper   | Be able to use loyalty points for discount on checkout                       | To make sure of the loyalty points that I have earnt         |
| 20            | Owner     | Add a Product to the store                                                   | To easily add a new item to the store                        |
| 21            | Owner     | Edit/Update a product in the store                                           | In case there is a change or an error with the product       |
| 22            | Owner     | Delete a product from the store                                              | If a product is no longer needed in the store                |
| 23            | Owner     | Add an Offer to the store                                                    | To easily add a new offer to the store                       |
| 24            | Owner     | Edit/Update an Offer in the store                                            | In case there is a change or an error with one of the offers |
| 25            | Owner     | Delete an Offer from the store                                               | If the offer is no longer required                           |
| 26            | Worker    | View a submitted order                                                       | So that they can start to cook it                            |
| 27            | Worker    | Update the status of an order                                                | So that the order is updated on the pizza tracker ID: 16     |
| 28            | Worker    | Complete an order                                                            | Complete the order so that it removes it from their system   |

### __Wireframes__

I created wireframes for desktop, tablet and mobile devices.

I collated the wireframes into views as per the different users of the site, the wireframes are detailed below:

#### __Shopper Views__

The shopper views detail the story of their movement through the site from the home page through to tracking their order.

The wireframes are the following:
* Home 
* Offers 
* Offers Detailed 
* Pizzas 
* Custom Pizza 
* Sides and Drink 
* Checkout
* Checkout Confirmation 
* Pizza Tracker 
* Account Info

The shopper wireframes can be found [here](https://github.com/Baldpet/slice-of-life-pizzeria/tree/master/wireframes/client_views).

#### __Staff Views__

The staff will also be able to use the site to see orders to cokk them and then update the order status to eventually complete the orders clearing them from their view. 

The wireframes are the following:
* Order Tracker

The staff wireframes can be found [here](https://github.com/Baldpet/slice-of-life-pizzeria/tree/master/wireframes/staff_views). 

#### __Store Manager Views__

This area is reserved for the store manager for them to manage the offers and the products throughout the site.

During development the product management page evolved to have the amend and the delete functionality here rather than on the Pizza or the Drink and Sides pages. 
The reason for doing this was to keep all of the manager transactions in one neat area.

The wireframes are the following:
* Product Management
* Add Deal Form
* Add Offer Form

The Manager wireframes can be found [here](https://github.com/Baldpet/slice-of-life-pizzeria/tree/master/wireframes/store_manager_views).  

### __Colours__

Working through the design process I did some market research to decide on colouring for the site.  

Generally sites looking to sell items to the public need to be free from other distraction other than the item you are selling, therefore the background needed to be white.
As Pizzerias are generally associated with the country that they originated I have included Green and Red in my colour design tied in to Italy's flag.  

I used [Coolors](www.coolors.co) to create my colour template which is shown below:

![Colour Palettes](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/wireframes/colors.png)  

### __Database Plan__

Using Django as the framework for the site it uses SQL as it's default database structure.  
After taking in to account the pros and cons of using an SQL database, I decided to keep to the Django default.

I then planned out the models and format that I required to fulfill the user stories mentioned.

The resulting database plan is included below:

![Database Design](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/wireframes/database-plan.png)

During the development process I realised that to have more flexibilty and the ability to extend in the future
I would need to add models to the database for 'dough type', 'sauce', 'cheese' and 'toppings'.  
Additionally to implement the customisable pizza I would need to include an 'is_original' within the products model so the custom pizzas were not rendered in places they were not needed.

These adjustments were then implemented to the Databases.

## __Features__

The current list of features that the web site offers is the following:

#### __Site Users__

* Can add offers and products to their order.
* Can add a custom pizza.
* Can proceed through the checkout system easily.
* Can sign up to an account which will keep delivery information for quicker checkout.
* Once singed up can keep and use loyalty points for discounts on their orders.
* Can track the status of their order once they have successfully checked out.

#### __Staff__

* Can track current orders and see what has been ordered.
* Can log where the current order is in preparation.

#### __Store Owner__

* Can amend or delete current products (Pizza, Side or Drink).
* Can amend or delete current offers.
* Can add a new product to the store.
* Can add a new offer to the store.

## __Future Goals__

There are a number of areas that the site can improve or expand after going live:

* At the moment (as there is no actual store) there is no address. As a real store it would be important to detail where people would collect the Pizza from
also for delivery we wouldn't want to be too far away so we would want to set a delivery distance around the address. All of this could be done with a link through Google Maps.

* Hoping that the little slice of life manages to grow it will want to be able to open a new store. So being able to handle different store orders, location only offers and products
and limiting staff views would be a future goal of development.

## __Technology Used__

I have listed the following languages and technology used to produce this project below:

#### __Languages__

* [HTML](https://html.spec.whatwg.org/)
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)
* [Markdown](https://www.markdownguide.org/)

#### __Frameworks and Libraries__

* [Django](https://www.djangoproject.com/)
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
* [Jquery](https://jquery.com/)
* [Font Awesome](https://fontawesome.com/)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

#### __Other Tools__

* [Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450259&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQiA-aGCBhCwARIsAHDl5x9bC1zJqEtjVlXgZgEanVR3iH2jRjnBEaj3uqbSqRWFn_4lothNbpsaAkcJEALw_wcB)
* [Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=483362991544&utm_term=cloudinary&gclid=Cj0KCQiA-aGCBhCwARIsAHDl5x8rPcxjogBlR7KLraEHzRwEN3-0rsYfKn9hfQKK-Tt9ZMas5ijQ-L8aAk03EALw_wcB)
* [Postgres](https://www.postgresql.org/)
* [Heroku](https://www.heroku.com/home)

## __Testing__

Testing was conducted throughout the project, each new feature that was added was checked and tested through using the development browser and via the chrome development tools.

### View current order and amend (User Story 13)

* __Plan__  
    
    * The user should be able to view their current order, detailing which items they are currently in line to purchase.
    
    * From this view they should then be able to amend the order if a mistake has been made, either via deletion of an item or via adjustment of the quanitity ordered.

* __Implementation__  

    To do this I created a 'bag' page which can view the entire order easily in one place.
    I then added buttons to each item of 'delete' and 'amend'.  
    The delete removes the item from the order entirely.  
    The amend button interacts with the product itself, if it is a side or a drink it gives the option to change the quantity.
    However if it is a Pizza then it gives an additional option to adjust the size of the product ordered.


* __Test__

    On testing when the delete button is pressed, it removes the product from the order and updates he page so that the user can now see the item is removed.  
    When the Amend button is pressed it brings up a modal detailing the options for amendment on the checkout page. This was correctly showing as different for the Pizza and the other products.

* __Result__

    The Delete and the Amend functionality works as planned. 

* __Verdict__

    The test has passed all the criteria and works as planned.

### Add an offer to the store (User Story 23)

* __Plan__  
    
    * The store owner should be able to easily add a new offer to the store.

    * This offer should be able to consist of any different product and the amount be adjustable.

* __Implementation__  

    I created a general area that the store owner can use to manage all the products and offers, within this area I created a page which consists of a form to create a new offer.  
    I implemented the option to have between 1-3 products in an offer, which can be any products within the store currently. The value of the deal can then be set at any amount that the owner likes.  
    On submission the form will create a new offer in the offers database, this will then automatically appear within the 'offers' menu on the site. 


* __Test__

    ~~On testing the form did fail due to the options within the categories for item1, item2 and item3 containing the Custom Pizza option.
    This created a status 500 error and did not process the form~~ 

    Fixed: On finding the error I excluded the Custom Pizza option from the categories selection via forms.py. 
    

* __Result__

    With the resulting fix the form now validates correctly and posts to the offers database.

* __Verdict__

    On fixing the error mentioned in the result, the offer form now completes correctly and passes the criteria set out.
    

### Update the status of an Order (User Story 27)

* __Plan__  
    
    * The user should be able to view all orders currently in progress and then update the order to its current status

* __Implementation__  

    To do this I created a page whcih displays all the orders which are currently open, this will allow the staff to see what needs to be cooked for which order.  
    I then created some buttons for these orders (Preparing, Cooking, Delivering and Complete). These buttons when clicked update the order status within the database holding the order.
    This status is then used to update the pizza tracker for the client (User story 16).

    This process is handled through Javascript using: 
    ```javascript
    'fetch()'
    ```

    The Preparing, Cooking and Delivering will then highlight on the staff page to also show the status of the order.

    The Complete button will remove the order from this page as the order is now complete.

    As this should only be accessible to staff members I have limited this to only staff members via Django.

* __Test__

    On testing the order viewing page rendered correctly showing the order contents as well as rendering the buttons for each order.  
    In addition when pressing each button the staff are able to update the status of the order which then refreshes the page and updates the relevant status.  
    When the Complete button is pressed it successfully updated the order to complete which then removes it from the order tracker page for the staff.
    

* __Result__

    The order tracker page worked functionally and and all the buttons performed their assigned tasks.

* __Verdict__

    The test has passed all the criteria and works as planned.



### Feedback

I recieved feedback from multiple friends and family who were able to give the app a try.

In general there were no major issues or failures, however it was a good chance to see which areas required some touch ups for the user experience.

## __Known Issues & Resolutions__

There are a few known issues which will need to be address in a future update:

* The file upload when adding a new offer or product allows you to attach a file, however when the form is submitted
it does not actually attach the image file to the product. Therefore the product or offer is added without the image.  

    The image can be added through the Django admin section manually but needs to be fixed for the store manager forms.

* There is an issue with the discount logic in the bag. Originally the discount was added seperately to the products
which meant that if a discount was added and then the customer adjusted the products it would not remove the discount.
This caused issues of negative sales or significant abuse of this.  

    To alleviate this issue I made the delete and amend buttons run through logic testing if this item was currently in a discount offer,
if the item was included then it would remove the discount.

    Although this makes sure that there is not any abuse of the discount system it creates some user functionality issues that they may change something
    which deletes the discount that they wanted to keep.

## __Deployment__

I created the Slice of Life Pizzeria project using Github, from there I used [Gitpod](https://gitpod.io/) to write my code. 
Then I used commits to git followed by "git push" to my GitHub repository. 
I've deployed this project to Heroku and used "git push heroku master" to make sure my pushes to GitHub were also made to Heroku. 

This project can be ran locally by following the following steps based on the Gitpod IDE:

You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

To clone the project: 

1. From the application's repository, click the "code" button and download the zip of the repository.
    Alternatively, you can clone the repository using the following line in your terminal:

    ``` 
    git clone https://github.com/Baldpet/slice-of-life-pizzeria.git
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. In the development environment Django will install SQLite, you will need to run the following on your terminal:

    ```
    1. python3 manage.py makemigrations
    2. python3 manage.py migrate
    ```

    This will create the required databases in your SQLite.
    You can of course use your preferred database provider, you may need to seek their installation instructions.

1. In your IDE you will need to make some environment variables, which will be the following:
    ```
    DEVELOPMENT = True
    SECRET_KEY = Your key
    STRIPE_PUBLIC_KEY = Your key
    STRIPE_SECRET_KEY = Your key
    STRIPE_WH_SECRET = your key 
    ```

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 manage.py runserver. 
    ```
    
### To deploy your project on Heroku, use the following steps: 

1. Firstly you will need to run the collectstatic command as follows in your IDE:
    ```
    python3 manage.py collectstatic
    ```
1. Then login to your Heroku account and create a new app. Choose your region. 
1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your IDE environment
    ```
    SECRET_KEY = Your key
    STRIPE_PUBLIC_KEY = Your key
    STRIPE_SECRET_KEY = Your key
    STRIPE_WH_SECRET = Your key
    DISABLE_COLLECTSTATIC = 1
    ```
1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 


## __Credits__

There were a number of sources used throughout the project which I would like to credit:

* Pictures were sourced through various places:
    * [Pexels](https://pexels.com/)

There was also some code utilised which is highlighted in comments within the code.

## __Acknoledgements__

I was lucky enough to have two mentors throughout the project and would like to acknoledge my mentor [Anthony Ngene](https://github.com/tonymontaro) who helped me to set up the initial idea and get started. 
I would then like to acknoledge the help [Simen Daehlin](https://github.com/Eventyret) gave in allowing me to fulfill the true potential of the project.

Lastly I would like to acknoledge my fiancee, family and friends who have helped with their feedback and suggestions on the structure and the testing of the project.

## __Disclaimer__

This project has been made solely for educational purposes and is not for commercial use.