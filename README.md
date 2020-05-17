# flask-vuejs
This repo contains a basic MVC arquitecture using flask as base (python 3).

## Routes
The route of this frameworks if very similar on how the route of codeigniter works with a function of flask-restful esquema qith the actions (GET, PUT, DELETE, etc). This frameworks first is going to see if the route exist in the view and in case that doesn't exist is going to looking for the controller with the following logic depend on the prefix:

| Primer encabezado | Segundo encabezado |
| ------------- | ------------- |
| Contenido de la celda  | Contenido de la celda  |
| Contenido de la celda  | Contenido de la celda  |


'/<file_controller>/<class_name>' => the rest of the URL it will be the params for the function (GET, POST, DELETE) function

## Views
You can add the static calls of the views in the file routes/views_routes.py, this you can add static views or even with VUE and make async calls from the documents (using the logic of templete render of flask).

All the views need to be located under the folder "views" because in this folder is where we put the template folder.

## Controllers

The controllers needs to be under the folder "controllers" from this folder the framework is going to search first the name of the file  after the name of the class, the framework automatically gets the name of the classes in the file searched an put it in lower case to find them, for example the call to "example.com/example_other/add/20?add1=1&add2=2&add3=3". 

## API calls
All the api calls needs to start with the sufix "api/"

