from flask import Flask, jsonify
from views import UserView

app = Flask("app")


def hello_world():

    return jsonify({'hello': 'world'})



app.add_url_rule('/hw', view_func=hello_world, methods=['GET'])
app.add_url_rule('/users/<int:art_id>', view_func=UserView.as_view('users'), methods=['GET'])

app.run()
