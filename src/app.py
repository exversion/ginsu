#!flask/bin/python

from flask import Flask, request, jsonify, Response, send_from_directory
from flask_restful import Resource, Api
import petl, json, logging, io, sys, os, csv

type_supported = {'csv':petl.io.csv.fromcsv,
 'tsv':petl.io.csv.fromtsv,
  'txt':petl.io.text.fromtext,
  'xml':petl.io.xml.fromxml,
  'json':petl.io.json.fromjson,
  'xls':petl.io.xls.fromxls,
  'xlsx':petl.io.xlsx.fromxlsx,
  }


def create_app():

	app = Flask(__name__)
	api = Api(app, catch_all_404s=True)

	logging.basicConfig(filename='exginsu.log', level=logging.DEBUG)



	@app.route('/')

	def index():
		return jsonify({'status': 200, 'success':True, 'message':'Hello. My name is Ginsu!'})



	@app.route('/process/', methods = ['POST'])

	def process_file():
		# {'url':"", 'type':""}
		data = json.loads(request.data.decode('utf-8'))
		url = data.get('url', None)
		ftype = data.get("type", None)
		#Is url valid?


		if ftype not in type_supported.keys():
			return jsonify(dict(status=400, message='file type not supported'))
			

		#Grab file from url
		table = type_supported[ftype](url)
		
		def generate():
			#columns = petl.util.base.header(table)
			data = petl.convertnumbers(table)
			for row in petl.util.base.dicts(data):
				#Process blades here
				print(row)
				yield json.dumps(row)+'\n'
		return Response(generate(), mimetype='application/json')

	#api.add_resource(treeView.dataTree, '/<tree_name>/')
	
	app.config.from_pyfile(os.path.dirname('../config/config.py')+'/../config/config.py')

	#@app.before_request
    #	def write_access_log():
    #		return 'Path: '+request.path

	return app
