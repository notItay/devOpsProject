from flask import Flask, request
import os
import signal

from db_connector import DbConnector

"""
The REST API gateway will be: 127.0.0.1:5000/users/<USER_ID>
"""
app = Flask(__name__)
db = DbConnector()

GET = 'GET'
POST = 'POST'
DELETE = 'DELETE'
PUT = 'PUT'
STATUS_OK = 'ok'
STATUS_ERROR = 'error'
SUCCESS = 200
INTERNAL_SERVER_ERROR = 500


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.route('/users/<user_id>', methods=[GET, POST, DELETE, PUT])
def user(user_id):
    if request.method == GET:
        '''
         returns the user name stored in the database for a given user id.
         On success: return JSON : {“status”: “ok”, “user_name”: <USER_NAME>} + code: 200
         On error: return JSON : {“status”: “error”, “reason”: ”no such id”} + code: 500
         '''
        try:
            user_name = db.get_user_name(user_id)
            return {'status': STATUS_OK, 'user_name': user_name}, SUCCESS
        except Exception:
            return {'status': STATUS_ERROR, 'reason': 'user does not exist'}, INTERNAL_SERVER_ERROR

    elif request.method == POST:
        '''
        will accept user_name parameter inside the JSON payload.
        A new user will be created in the database with the
        id passed in the URL and with user_name passed in the request payload.
        ID has to be unique!
        On success: return JSON : {“status”: “ok”, “user_added”: <USER_NAME>} + code: 200
        On error: return JSON : {“status”: “error”, “reason”: ”id already exists”} + code: 500

        '''
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            db.insert_user(user_id, user_name)
            return {'status': STATUS_OK, 'user_added': user_name}, SUCCESS
        except Exception:
            return {'status': STATUS_ERROR, 'reason': 'id already exists'}, INTERNAL_SERVER_ERROR

    elif request.method == DELETE:
        '''
        will delete existing user (from database).
        On success: return JSON : {“status”: “ok”, “user_deleted”: <USER_ID>} + code: 200
        On error: return JSON : {“status”: “error”, “reason”: ”no such id”} + code: 500
        '''
        try:
            db.delete_user(user_id)
            return {'status': STATUS_OK, 'user_deleted': user_id}, SUCCESS
        except Exception:
            return {'status': STATUS_ERROR, 'reason': 'no such id'}, INTERNAL_SERVER_ERROR

    elif request.method == PUT:
        '''
        will modify existing user name (in the database).
        On success: return JSON : {“status”: “ok”, “user_updated”: <USER_NAME>} + code: 200
        On error: return JSON : {“status”: “error”, “reason”: ”no such id”} + code: 500
        '''
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            db.update_user_name(user_id, user_name)
            return {'status': STATUS_OK, 'user_updated': user_name}, SUCCESS
        except Exception:
            return {'status': STATUS_ERROR, 'reason': 'no such id'}, INTERNAL_SERVER_ERROR

    else:
        raise NotImplementedError


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5000)
