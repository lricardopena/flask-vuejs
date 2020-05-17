from flask import Flask
from routes.controllers_routes import controllers_pages
from routes.views_routes import views_pages


# Tell that the views are going to be under the folders views
app = Flask(__name__,  template_folder='views')

# Add all the routes to the view pages only
app.register_blueprint(views_pages)

# Add the controllers calls
app.register_blueprint(controllers_pages)

# Add all kind of methods to the controller
rule_to_add = [r for r in list(app.url_map.iter_rules()) if r.rule == '/<path:path>'][0]

if __name__ == "__main__":
    app.run(debug=True)
