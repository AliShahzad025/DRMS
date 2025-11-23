from flask import Flask
from api.user_routes import user_bp
from api.admin_routes import admin_bp
from api.ngo_routes import ngo_bp
from api.sos_routes import sos_bp
from api.volunteer_routes import volunteer_bp
from api.resource_routes import resource_bp 
from api.victim_routes import victim_bp
app = Flask(__name__)   # <-- CREATE APP FIRST

# OPTIONAL: Debug route
@app.route('/debug_routes')
def debug_routes():
    return "Routes are working!"

# Register blueprints AFTER creating the app
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(ngo_bp)
app.register_blueprint(sos_bp)
app.register_blueprint(volunteer_bp)
app.register_blueprint(resource_bp)  
app.register_blueprint(victim_bp)
if __name__ == "__main__":
    app.run(debug=True)
