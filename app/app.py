from flask import Flask, jsonify
from views import UserView

app = Flask("app")


def hello_world():

    return jsonify({'hello': 'world'})



app.add_url_rule('/hw', view_func=hello_world, methods=['GET'])
app.add_url_rule('/user/<int:art_id>', view_func=UserView.as_view('user'), methods=['GET', 'PATCH', 'DELETE'])
app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)
