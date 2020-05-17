# flask-vuejs
This repo contains a basic MVC arquitecture using flask as base (python 3) :exclamation: **This is a work on progress and it's not ready to production, used it under your own risk** :exclamation:.

## Routes
The route of this frameworks if very similar on how the route of codeigniter works with a function of flask-restful esquema qith the actions (GET, PUT, DELETE, etc). This frameworks first is going to see if the route exist in the view and in case that doesn't exist is going to looking for the controller with the following logic depend on the prefix:
- **Controller**  */<file_controller>/<class_name>/* => the rest of the URL it will be the params for the function programed under in the path *controllers/<file_controller>.py* and class *<clas_name>* with name function with any the following methods: get, post, put, delete, patch, just like flask-restful but with a siglthy modification. **See the section Controllers for further details**.
- **API** */api/<file_api>/<class_name>/* => the rest of the URL it will be the params for the function programed under in the path *api/<file_api>.py* and class *<clas_name>* with name function with any the following methods: get, post, put, delete, patch, just like flask-restful but with a siglthy modification. **See the section Api for further details**.
 
 Examples
| Method | URL | path of the file to searcher | Class | Function to call | Brief explanation |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | 
| GET | */example/helloworld/luis*  |  'controller.example.py' | HelloWorld | get | We are making a get method **without** a prefix *api/* so therefore the framework is going to search under the folder *controllers* the file *example.py* and the class *HelloWorld* (could it be also *helloworld* or *Helloworld*) and is going to call the function *get* of the class *HelloWorld* and is going to send the param *luis* to the function. |
| POST | */example/helloworld/luis/ignore1*  |  'controller.example.py' | HelloWorld | post | The explanations is very similar to the previous one, but if the function *get* don't recive more than one parameter, then the other parameters is going to be ignored and it is going to call the *post* function. |
| POST | */api/example/helloworld/luis*  |  'api.example.py' | HelloWorld | post | We are making a get method **with** a prefix *api/* so the framework is going to search under the folder *api* the file *example.py* and the class *HelloWorld* (could it be also *helloworld* or *Helloworld*) and is going to call the function *get* of the class *HelloWorld* and is going to send the param *luis* to the function. |


## Views
You can add the static calls of the views in the file routes/views_routes.py, this you can add static views or even with VUE and make async calls from the documents (using the logic of templete render of flask).

All the views need to be located under the folder "views" because in this folder is where we put the template folder.

## Controllers

The controllers needs to be under the folder "controllers" from this folder the framework is going to search first the name of the file  after the name of the class, the framework automatically gets the name of the classes in the file searched an put it in lower case to find them, also reeplaces any *-* (hyphen) in case that the controller name or the class name have it (in the URL) and only these two. You can see example of this in the table above. Every class created in this folder needs to have the inheritant of the class *BaseController* you can acced to the request by the variable *my_request* from the class you can see an example of all this in the following code:
```
from controllers.base import BaseController


class HelloWorld(BaseController):
    def get(self, name):
        return {'Hi': 'Hello {}!'.format(name)}

    def post(self):
        json_request_send = self.my_request.get_json()
        return {'JSON sent': json_request_send}


class Add(BaseController):
    def get(self, number):
        number = int(number)
        return {'result': number + 2}
```
Here we create this file with two possible functions, if we save this save file as: *example.py* under the folder *controllers* then we call these functions with any of the following examples:

| Method | URL | path of the file to searcher | Class | Function to call | Brief explanation |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | 
| GET | */example/helloworld/luis*  |  'controller.example.py' | HelloWorld | get | The framework is going to search the file *example.py* in the path *controllers* and is going to instanciate the class *HelloWord* and run the function *get* because for the method. |
| POST | */example/helloworld/luis*  |  'controller.example.py' | HelloWorld | post | The explanations is very similar to the previous one, but if the function *get* don't recive more than one parameter, then the other parameters is going to be ignored and it is going to call the *post* function. |
| GET | */example/add/20*  |  'controller.example.py' | Add | get | We are making a get method so the framework is going to call the function *get*. |

## API calls
All the api calls needs to start with the sufix "api/". This calls follow almost the same structure of the controllers, with the diference that this classes needs to be under the folder *api* and all the classes need to inheritance the **BaseApi** class and if you want to get access to the request you can found it in the variable *my_request* (just like the controller). For example this code:
```
from flask import jsonify
from api.base import BaseApi


class Hello(BaseApi):
    def get(self, name):
        return jsonify({
            "Name": name
        })

```
Here we create this file with two possible functions, if we save this save file as: *example.py* under the folder *api* then we call this functions with any of the following example:


| Method | URL | Path of the file to searcher | Class | Function to call | Brief explanation |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | 
| GET |*/api/example/hello/luis*  |  'api.example.py' | Hello | get | The framework is going to search the file *example.py* in the path *api* because the URL starts with the prefix */api/* and is going to instanciate the class *Hello* and run the function *get* because for the method. |

