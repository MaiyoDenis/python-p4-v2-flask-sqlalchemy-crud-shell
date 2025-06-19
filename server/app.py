from flask import Flask
from flask_migrate import Migrate

from models import db, Pet

# create a Flask application instance 
app = Flask(__name__)

# configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# configure flag to disable modification tracking and use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

# initialize the Flask application to use the database
db.init_app(app)

# shell context for flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Pet': Pet}


if __name__ == '__main__':
    app.run(port=5555, debug=True)
