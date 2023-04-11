
from flask import Flask, request, make_response
import os
from dotenv import load_dotenv
from db_cursor import select_cars, select_phone_numbers
from flask_cors import CORS

load_dotenv()

#add cors

app = Flask(__name__)
cors = CORS(app)




@app.route('/view',methods=["POST"])
def view():
    number=request.json["Number"]

#WHERE CARMDI.actualnb = {number}
    cars = select_cars(number)
    # response list consisting user details
    response = list()
 
    [response.append(car) for car in cars]
    

    return make_response({
        'message': response
    }, 200)


def handle_tel_num(telNum):
    output=""
    for ch in telNum:
        if ch.isdigit():
            output+=ch
    
    return output



@app.route('/telnum',methods=["POST"])
def telNum():
    telNumber=request.json["telNumber"]

    response = list()
    telNumbers = select_phone_numbers(telNumber)
    
    [response.append(telNumber) for telNumber in telNumbers]
    

 
    return make_response({
        'message': response
    }, 200)




if __name__ == "__main__":
    # serving the app directly
    app.run()