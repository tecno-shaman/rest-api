import flask

from . import db_session
from .jobs import Works
from flask import jsonify, make_response, request

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    works = db_sess.query(Works).all()
    return jsonify(
        {
            'jobs':
                [item.name for item in works]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_news(jobs_id):
    db_sess = db_session.create_session()
    works = db_sess.query(Works).get(jobs_id)
    if not works:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'job': works.to_dict(only=('name',))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not 'name' in request.json:
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    job = Works(name=request.json['name'])
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'id': job.id})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    works = db_sess.query(Works).get(job_id)
    if not works:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(works)
    db_sess.commit()
    return jsonify({'success': 'OK'})
