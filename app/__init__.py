# app/__init__.py

from flask_restx import Api
from flask import Blueprint

# from .main.controller.dashboard_controller import api as template_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )


routes_blueprint = Blueprint('routes', __name__)


