

from flask import Flask



#Flask App Structure
app = Flask(__name__, static_folder="./data", template_folder="./")


#.....................End Ai...............
#server route working
@app.route('/')
def index():
    return "Lets find server, up and running"


#Get home stories
@app.route('/homeStories', methods=['GET'])
def gethomeStorie():
    status = "get stories"
    return status






if __name__ == "__main__":
    app.run(host='0.0.0.0',port='2020', debug=True)
