from flask import Flask
from api.user_routes import user_bp
from api.admin_routes import admin_bp
from api.ngo_routes import ngo_bp
from api.sos_routes import sos_bp
from api.volunteer_routes import volunteer_bp
from api.resource_routes import resource_bp 
from api.victim_routes import victim_bp
from api.priorityzone_routes import priorityzone_bp
from api.shelter_routes import shelter_bp
from api.task_routes import task_bp
from api.notification_routes import notification_bp
from api.auditlog_routes import auditlog_bp
from api.report_routes import report_bp
from api.feedback_routes import feedback_bp
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
app.register_blueprint(priorityzone_bp)
app.register_blueprint(task_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(auditlog_bp)
app.register_blueprint(report_bp)
app.register_blueprint(shelter_bp)
app.register_blueprint(feedback_bp)

if __name__ == "__main__":
    app.run(debug=True)
