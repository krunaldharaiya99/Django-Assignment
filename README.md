# Django-Assignment

 - Find 'DjangoAssignment/requirements.txt' file for installing all the project require packages.

Question : 
Make REST APIs of CUSTOM USER based project which is able to (using simpleJWT authentication):
 - Login
 - Signup
 - Product list
 - Create product
 - Get detail of particular product
 - Implement pagination, filter, ordering and sorting.
 - Use standard naming convention and class based concept including admin.py

All of this task has been done by Using The concept of class based function.

The App named "account" having all the APIs related to login, Registration and View User Profile. It also contains custom Autherization permissions in permissions.py file of this app.

The App named "products" has all the opration related to CRUD with using concept of RestAPI. with JWT Token.
for Adding new Product, Updating Perticular Product and For Deleting Any Perticular product you have to provide autherization token and you should be have created autherization token by login api. and make use of that autherization created on login operation to perform operation on Products.