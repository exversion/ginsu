from flask import Flask
from src import app
from config import config

ginsu = app.create_app()

if __name__== '__main__':
	ginsu.config['SERVER_NAME'] = 'localhost:1111'
	ginsu.run(debug = True)