
import os
import json
from flask import Flask, render_template, request, redirect
from processor import ProcessRequest
app = Flask(__name__)

@app.route ('/create',methods=['POST'])
def upload_recurso():

	print(request.files)
	for file in request.files:
		print("llego")
		ProcessRequest(request.files[file])
	return json.dumps('Succesfully upload the files'),200


if __name__ == "__main__":

    app.run(host='', port=9000)