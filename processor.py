from merger import Merger
from werkzeug import secure_filename
from uuid import uuid4	
from zipfile import ZipFile
import os


def ProcessRequest(file):

	name = str(uuid4())
	base_file_name = "%s-%s" % (name, secure_filename(file.filename))
	file_name = "tmp/%s" % base_file_name
	print(file_name)
	file.save(file_name)
	with ZipFile(file_name , 'r') as zipObj:
		zipObj.extractall("tmp/%s" % name)
	Merger("tmp/%s" % name,os.path.realpath("tmp/combined-%s.ics" % name))