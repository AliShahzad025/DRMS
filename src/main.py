from flask import Flask
from api.user_routes import user_bp
from api.admin_routes import admin_bp
from api.ngo_routes import ngo_bp
from api.sos_routes import sos_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(ngo_bp)
app.register_blueprint(sos_bp)
if __name__ == "__main__":
    app.run(debug=True)
