import inspect
import pydoc

from flask import Blueprint, request, render_template
from werkzeug.routing import Rule


controllers_pages = Blueprint('controllers', __name__)
# controllers_pages.url_map.add(Rule('/', endpoint='index'))

@controllers_pages.route('/')
@controllers_pages.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@controllers_pages.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    module_str, class_name, params = return_module_path(path)

    file_instance = pydoc.locate(module_str)
    if file_instance is None:
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404

    # Method
    method_request = request.method.lower()
    elements_in_file = inspect.getmembers(file_instance)
    elements_filter = [x for x in elements_in_file if type(x[1]) == type and x[1].__module__ == module_str
                       and x[0].lower() == class_name]
    if len(elements_filter) == 0:
        # note that we set the 404 status explicitly
        return render_template('404.html'), 404

    try:
        class_type_call = elements_filter[0][1]
        function_call = getattr(class_type_call(request), method_request)
        sig = inspect.signature(function_call)
        if len(sig.parameters) == 0:
            return function_call()
        elif len(sig.parameters) == len(params):
            return function_call(*params)
        elif len(sig.parameters) < len(params):
            return function_call(*params[:len(sig.parameters)])
        else:
            return render_template('404.html'), 404
    except AttributeError as ex:
        return render_template('404.html'), 404


def return_module_path(path):
    path = path.replace("-", "_")
    is_api_call = path.startswith("api/")
    folder_name = 'controllers'
    if is_api_call:
        path = path[path.index("/") + 1:]
        folder_name = 'api'
    elements_query = path.split("/")
    # Filename
    filename = elements_query[0]
    class_name = elements_query[1]
    params = elements_query[2:]
    module_str = '.'.join([folder_name, filename])
    return module_str, class_name, params
