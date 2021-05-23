from flask import Flask, request
from flask_restful import Resource, Api
from rich.console import Console
from SayMyName import MyName

console = Console()
app = Flask(__name__)
api = Api(app)


@app.route('/mint', methods=['GET'])
def mint():
    contract = MyName()
    console.log("Contract class called..")
    contract.start_creation()
    console.log("Contract creation started..")
    return contract.say_my_name()


if __name__ == '__main__':
    app.run(debug=True)
