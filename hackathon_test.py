#server code

from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'welcome!'

@app.route('/get_friends')
def get_friends():
    print(request.args.get('basket'))
    print(type(request.args.get('basket')))
    coming_arr = request.args.get('basket')
    coming_list = json.loads(coming_arr)
    print(type(coming_list))
    print(coming_list)

    # eg: http://127.0.0.1:5000/getfriends?coming_array=[1,2,3,4,5]

    return [1000, 1001, 1002, 1004, 1005]

if __name__ == '__main__':
    app.run()
