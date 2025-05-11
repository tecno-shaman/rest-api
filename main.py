from flask import Flask, render_template, redirect, request, make_response, session, abort, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data import db_session, jobs_api
from data.jobs import Works

from sqlalchemy import or_
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(
    days=365
)


# login_manager = LoginManager()
# login_manager.init_app(app)

# @login_manager.user_loader
# def load_user(user_id):
#     db_sess = db_session.create_session()
#     return db_sess.query(User).get(user_id)

def main():
    db_session.global_init("db/jobs.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    main()
