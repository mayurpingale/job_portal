from modules.candidate import Candidate
from flask import Flask
from flask_restful import Resource, Api, request
from flask_cors import CORS, cross_origin

from modules.jobd import job_description 
from modules.candidate import Candidate
from modules.show import show
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#CORS(app, resources={r"/*": {"origins": ["https://karyam.herokuapp.com/"]}})

api = Api(app)


# routing
api.add_resource(show,'/')
api.add_resource(job_description,'/jobd')
api.add_resource(Candidate,'/candidate')

if __name__ == '__main__':
    if(os.getenv("enviornment_production") == "True"):
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(debug=True)
