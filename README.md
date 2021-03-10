<div align="center">
[![Logo](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/logo.png)](#)
</div>


## __Contents__

- [Aim of The Site](#aim-of-the-site)
- [UX](#ux)
    - [Client Stories](#client-stories)
    - [Database Plan](#database-plan)
    - [Wireframes](#wireframes)
    - [Colours](#colours)
- [Features](#features)
- [Future Goals](#future-goals)
- [Technology Used](#technology-used)
- [Testing](#testing)
    - [Validation](#validation)
    - [Screen Sizes](#screen-sizes)
    - [Site Links](#site-links)
    - [Deployment Test](#deployment-test)
    - [Multiple Browsers](#multiple-browsers)
    - [Feedback](#feedback)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknoledgements)
- [Disclaimer](#disclaimer)


## __Aim of the Site__

Welcome to the Slice of Life Pizzeria.

The aim of the site is to provide an ecommerce store to provide take away services for hungry people.
The site is also a platform for the staff to use to co-ordinate orders and update the order status which can be tracked by the user. 

Check out the live site here: #
## __UX__

### __Client Stories__

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

### __Database Plan__

Using Django as the framework for the site it uses SQL as it's default database structure.  
After taking in to account the pros and cons of using an SQL database, I decided to keep to the Django default.

I then planned out the models and format that I required to fulfill the user stories mentioned.

The resulting database plan is included below:

![Database Design](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/database-plan.png)

During the development process and through discussion with my mentor I realised that to have more flexibilty and the ability to extend in the future
I would need to add models to the database for 'dough type', 'sauce', 'cheese' and 'toppings'.  
Additionally to implement the customisable pizza I would need to include an 'is_original' within the products model.

These adjustments were then implemented to the Database.

### __Wireframes__

I created wireframes for desktop, tablet and mobile devices.

The wireframes are detailed below:

#### __Client Views__

![Home](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/home.png)  
![Offers](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/offers.png)  
![Offers Form](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/offer-form.png)  
![Pizzas](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/pizzas.png)  
![Custom Pizza](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/customise.png)  
![Sides and Drink](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/sides-and-drinks.png)  
![Checkout](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/checkout-amount.png)  
![Checkout Confirmation](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/confirmation-order.png)  
![Pizza Tracker](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/pizza-tracker.png)  
![Account Info](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/account-info.png)  

#### __Staff Views__

![Order Tracker](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/order-tracker.png)  

#### __Store Manager Views__

![Product Management](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/product-management.png)  
![Add Deal Form](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/add-a-deal.png)  
![Add Offer Form](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/add-a-product.png)  

### __Colours__

Working through the design process I did some market research and spoke with my mentor to decide on colouring for the site.  

Generally sites looking to sell items to the public need to be free from other distraction other than the item you are selling, therefore the background needed to be white.
As Pizzerias are generally associated with the country that they originated I have included Green and Red in my colour design tied in to Italy's flag.  

I used www.coolors.co to create my colour template which is shown below:

![Colour Palettes](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/colors.png)  

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
* [Postgres Database](https://www.postgresql.org/)
* [Font Awesome](https://fontawesome.com/)
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)

#### __Other Tools__

* [Stripe](https://stripe.com/gb?utm_campaign=paid_brand-UK_en_Search_Brand_Stripe-2032860449&utm_medium=cpc&utm_source=google&ad_content=355351450259&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=Cj0KCQiA-aGCBhCwARIsAHDl5x9bC1zJqEtjVlXgZgEanVR3iH2jRjnBEaj3uqbSqRWFn_4lothNbpsaAkcJEALw_wcB)
* [Cloudinary](https://cloudinary.com/?utm_source=google&utm_medium=cpc&utm_campaign=Rbrand&utm_content=483362991544&utm_term=cloudinary&gclid=Cj0KCQiA-aGCBhCwARIsAHDl5x8rPcxjogBlR7KLraEHzRwEN3-0rsYfKn9hfQKK-Tt9ZMas5ijQ-L8aAk03EALw_wcB)

## __Testing__

Testing was conducted throughout the project, each new feature that was added was checked and tested through using the development browser and via the chrome development tools.

### Validation

HTML, CSS, Javascript and Python code has been checked by online validators and any suggestions adjusted.
 

### Screen Sizes

 

### Site Links

I have fully tested all the links on the site to make sure that they go through to the correct page.  
  

### Deployment Test

The website was tested on deployment through the app hosting site Heroku, no bugs or problems were detected upon deployment.  

### Multiple Browsers

I have undertaken some tests on other popular browsers to see if there are any bugs that I have picked up.  
The website has loaded on all browsers and devices tested which are shown:  
 
    * Microsoft Edge
    * Firefox
    * Chrome
    * Samsung Mobile (Android)
    * Safari Mobile

No visual or other bugs were detected on any of the browsers mentioned.

### Feedback

I recieved feedback from multiple friends and family who were able to give the app a try.

In general there were no major issues or failures, however it was a good chance to see which areas required some touch ups for the user experience.

## __Known Issues & Resolutions__


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

1. Login to your Heroku account and create a new app. Choose your region. 
1. Ensure the Procfile and requirements.txt files exist are present and up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
1. The Procfile should contain the following line:
    ```
    web: gunicorn slice_of_life_pizzeria.wsgi:application
    ```
1. You will need to run the collectstatic command as follows:
    ```
    python3 manage.py collectstatic
    ```
1. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
1. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
1. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WH_SECRET, DISABLE_COLLECTSTATIC):
1. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment".
1. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.
1. In order to commit your changes to the branch, use git push to push your changes. 


## __Credits__

There were a number of sources used throughout the project which I would like to credit:

* Pictures were sourced through various places:
    * https://pexels.com/

There was also some code utilised which is highlighted in comments within the code.

## __Acknoledgements__

I was lucky enough to have two mentors throughout the project and would like to acknoledge my mentor [Anthony Ngene](https://github.com/tonymontaro) who helped me to set up the initial idea and get started. 
I would then like to acknoledge the help [Simen Daehlin](https://github.com/Eventyret) gave in allowing me to fulfill the true potential of the project.

Lastly I would like to acknoledge my fiancee, family and friends who have helped with their feedback and suggestions on the structure and the testing of the project.

## __Disclaimer__

This project has been made solely for educational purposes and is not for commercial use.