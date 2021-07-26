# AMAZECART
An e-commerce platform which allows to shop and pay across a wide selection of digital products and categories using Django and deployed on Heroku platform.

## OBJECTIVES
•	Creating the product catalog models, adding them to the administration site, and building the basic views to display the catalog

•	Building a shopping cart system using Django sessions to allow users to keep selected products while they browse the site.

•	Creating the form and functionality to place orders on the site.

## APPROACH
The whole project was divided into set of modules and the modules were built independently and then clubbed to form a complete webapp.
The modules were:
•	Frontend HTML pages: Basic HTML pages of the complete project were created. 

•	Dynamic URL linking of the pages: All the pages created for the frontend were dynamically linked to each other, using links we passed the required data for the next page to render.

•	Creating views and models: Views contain the functions which will fetch the data from database and will pass this data to the HTML pages to render the data; models are used to create tables for the database.

•	Adding CSS to the frontend: The basic HTML pages which were created in the first module were given styling’s and work on aesthetics of the pages was done.
    Each team member worked on one module and then all the modules were clubbed to complete the project.


## FEATURES

### User
•	User can register to Amazecart.

•	User can login into his account.

•	User can view different categories of Products and the quantity of that particular product.

•	User can add products in cart.

•	User can enter address for delivery.

### Admin
•	Admin can login using his credentials.

•	Admin can perform CRUD operations on users.

•	Admin can perform CRUD operations on products.

## DESIGN

![Test Image 9](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/9.PNG)



## IMPLEMENTATION DETAILS

### Home Page:

![Test Image 1](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/1.PNG)


### Login Page: 
From this page the user as well as the admin can login using his credentials. If the user is new to this portal, he/she can register to Amazecart using Signup option..

![Test Image 2](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/2.PNG)




### Signup Page: 
From this page the fresher user can create his account into Amazecart by providing the details asked. 
 
![Test Image 3](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/3.PNG)


### Products Page:
From this page the user visiting Amazecart can know about the different categories of products like camera , mobile phones etc. From this page the user can select the product for knowing the detailed specification of that particular product.
 
![Test Image 4](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/4.PNG)
 
 
### Cart Page: 
From this page the user will get the list of products selected. If required the user can change the quantity attribute in the cart also directly from this page. The Price of a product * quantity is calculated and summed for all the products and displayed in the cart.
 
![Test Image 5](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/5.PNG)


### Checkout Page: 
From this page the user can enter the details like name, address, mail ID as the details are essential for delivering the products.

![Test Image 6](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/6.PNG)
 
### Product’s Detail Page: 
The user can view the product details and enter the quantity and click on add to cart. This will add the product and the quantity selected into the car

![Test Image 7](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/7.PNG)
 

### Admin Panel: 
Using the admin panel the admin can perform the CRUD operations on the user details and also on the Products

![Test Image 8](https://github.com/ApoorvaJinde/AmazeCart/blob/master/images/8.PNG)
 
## CONCLUSION AND FUTURE SCOPE
It was a great opportunity to work on such a project, where we got to learn and know more about some good technologies such as Django, node, Bootstrap, java script, html and CSS.

About Amazecart, it is an application helpful for users to view and order the different digital products , the demand of such applications always remain high as we all have experienced in this pandemic that the online shopping has proved to be  much safer than offline shopping.  

With this mode of shopping we get the provision of receiving the products to our door steps unlike the offline mode where we need to wander different shops to purchase our required products.

Thus, adapting to application such Amazecart will be more beneficial for users who can access the products anywhere and anytime.

