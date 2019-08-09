import os
import sys
import traceback
import datetime
import glob
import codecs

import vobject

def Merger(dir, dest):

	os.chdir(dir)
	mergedCalendar = vobject.iCalendar()

	for file in glob.glob("*.ics"):

		print("Opening '%s'.." % file)
		f = open(file, 'rb')

		print("Reading '%s'.." % file)
		contents = f.read()
		contents = contents.decode('utf-8')
		f.close()

		components = vobject.readComponents(contents, validate=False)

		for component in components:
			for child in component.getChildren():
				add_entry = True

				if child.name == 'VERSION':
					add_entry = False
				if child.name == 'PRODID':
					add_entry = False
				if add_entry:
					mergedCalendar.add(child)
	print("Writing iCalendar file '%s'.." % dest)
	f = open(dest, 'wb')
	f.write(mergedCalendar.serialize(validate=False).encode('utf-8'))
	f.close()

	print("Done.")