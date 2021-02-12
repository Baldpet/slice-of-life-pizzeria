[![Logo](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/logo.png)](#)

# __Slice of Life Pizzeria__

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
* Site User
* Store Owner
* Store Worker

Based on these users I looked at specific user stories that each of them would have, the list of stories is below:

![User Stories](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/user-stories-1.png)

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

![Colour Palettes](https://github.com/Baldpet/slice-of-life-pizzeria/blob/master/media/MS4-wireframes/add-a-product.png)  

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

* HTML
    * For the base information and structure of the webpages.
* CSS
    * For the styling and beauty of the webpages.
* Javascript
    * For dynamic inputs onto the html and for initialisation of some interactive elements.
* Python
    * For the backend structure of the website.
* SQL
    * For the databases which hold the information required for the site.
* Markdown
    * For the ReadMe file.

#### __Frameworks and Libraries__

* Django Framework
    * Used for the entire structure of the website from the backend to the rendering and information for the frontend.
* Bootstrap
    * Used as a CSS framework to help structure the frontend.
* Jquery
    * For easier targetting and functionality within Javascript.
* Postgres Database
    * This was where the database is stored and accessed. 
* Font Awesome
    * Used as a source of icons used throughout the site.
* Crispy Forms
    * Used as a tool to help structure the Django base forms within a Bootstrap styling.

#### __Other Tools__

* Stripe
    * Used as the payment tool for the ecommerce side of the site.

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

There were a number of steps taken to deploy the website onto Heroku.

1. The code was written on an online IDE - Gitpod, the major changes were written via branches.
2. The branches were then merged together with the master using Git.
3. The code was then pushed to GitHub where it is stored on a public repository.
4. An app was registered on Heroku Apps and then set as a remote git.
5. A Procfile and a requirement.txt file was created so that Heroku can process the git push.
6. The app was then pushed to Heroku
7. The Heroku environment variables were then entered to allow the app to run.
8. The app is then uploaded and live.
9. This would be the deployed version, any changes would be saved on the development version which would be on a branch in github.

The code can be run locally through clone or download on github.  
By opening the repository and and being in the main 'code' section there is a button 'clone or download'.  
This button will provide a link that you can use on your desktop or download as a ZIP file.

## __Credits__

There were a number of sources used throughout the project which I would like to credit:

* Pictures were sourced through various places:
    * https://pexels.com/

There was also some code utilised which is highlighted in comments within the code.



## __Acknoledgements__

I was lucky enough to have two mentors throughout the project and would like to acknoledge my mentor Anthony Ngene who helped me to set up the initial idea and get started. 
I would then like to acknoledge the help Simen Daehlin gave in allowing me to fulfill the true potential of the project.

Lastly I would like to acknoledge my fiancee, family and friends who have helped with their feedback and suggestions on the structure and the testing of the project.

## __Disclaimer__

This project has been made solely for educational purposes and is not for commercial use.