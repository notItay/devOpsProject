from flask import Flask
import os
import signal

from .db_connector import DbConnector

"""
The REST API gateway will be: 127.0.0.1:5001/get_user_name/<USER_ID>
"""
app = Flask(__name__)
db = DbConnector()


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


@app.route("/get_user_name/<user_id>")
def get_user_name(user_id):
    user_name = db.get_user_name(user_id)
    if user_name is None:
        user_name = "no such user"
        user_id = "error"
    return "<H1 id = {}> {} </H1>".format(user_id, user_name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=5001)
