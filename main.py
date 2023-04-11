
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy as alc
from flask_cors import CORS, cross_origin
import os
from dotenv import load_dotenv
from google.cloud.sql.connector import Connector
import sqlalchemy
load_dotenv()


app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI_TEST') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


CORS(app)

#connect to the database
db = alc(app)




class CARMDI(db.Model):
    __tablename__ = 'CARMDI'
    
    ActualNB = db.Column(db.String(250), nullable = True,primary_key=True)
    CodeDesc = db.Column(db.String(250), nullable = True,primary_key=True)
    PRODDATE = db.Column(db.String(250), nullable = True)
    Chassis = db.Column(db.String(250), nullable = True)
    Moteur= db.Column(db.String(250), nullable = True)
    dareaquisition= db.Column(db.String(250), nullable = True)
    PreMiseCirc= db.Column(db.String(250), nullable = True)
    CouleurDesc= db.Column(db.String(250), nullable = True)
    TypeDesc= db.Column(db.String(250), nullable = True)
    MarqueDesc= db.Column(db.String(250), nullable = True)
    UtilisDesc= db.Column(db.String(250), nullable = True)
    Prenom= db.Column(db.String(250), nullable = True)
    Nom= db.Column(db.String(250), nullable = True)
    Addresse= db.Column(db.String(250), nullable = True)
    NomMere= db.Column(db.String(250), nullable = True)
    TelProp= db.Column(db.String(250), nullable = True)
    NoRegProp= db.Column(db.String(250), nullable = True)
    AgeProp= db.Column(db.String(250), nullable = True)
    BirthPlace= db.Column(db.String(250), nullable = True)
    HorsService= db.Column(db.String(250), nullable = True)


@app.route('/view',methods=["POST"])
def view():
    number=request.json["Number"]
    
    # from app, get the db instance

    cars = CARMDI.query.filter_by(ActualNB=str(number)).all()

    # response list consisting user details
    response = list()
 
    for car in cars:
        response.append({
            "ActualNB" : car.ActualNB,
            "Code": car.CodeDesc,
            "PRODDATE":car.PRODDATE,
            "Chassis":car.Chassis,
            "Moteur":car.Moteur,
            "dareaquisition":car.dareaquisition,
            "PreMiseCirc":car.PreMiseCirc,
            "CouleurDesc":car.CouleurDesc,
            "MarqueDesc":car.MarqueDesc,
            "TypeDesc":car.TypeDesc,
            "UtilisDesc":car.UtilisDesc,
            "Prenom":car.Prenom,
            "Nom":car.Nom,
            "Addresse":car.Addresse,
            "NomMere":car.NomMere,
            "NoRegProp":car.NoRegProp,
            "TelProp":car.TelProp,
            "AgeProp":car.AgeProp,
            "BirthPlace":car.BirthPlace,
            "HorsService":car.HorsService,
        })
    


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
 
    for telnum in telNumbers:
        response.append({
            "Prenom":telnum.Prenom,
            "Nom":telnum.Nom,
            "Addresse":telnum.Addresse,
            "NomMere":telnum.NomMere,
            "TelProp":handle_tel_num(telnum.TelProp),
            "AgeProp":telnum.AgeProp,

        })
 
    return make_response({
        'message': response
    }, 200)




if __name__ == "__main__":
    # serving the app directly
    app.run()