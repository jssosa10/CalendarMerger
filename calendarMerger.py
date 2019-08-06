#!/bin/env/python
# -*- coding: utf8 -*-

import os
import sys
import traceback
import datetime
import glob
import codecs

from ConfigParser import ConfigParser
from optparse import OptionParser, Option, OptionGroup

# 3rd party libs
import vobject


__AUTHOR__ = u"Juan Sosa"
__YEAR__ = "2019"
__VERSION__ = "0.0.1"


if __name__ == "__main__":
    banner  = u" %s" % (__VERSION__)
    banner += u" (c) %s %s" % (__AUTHOR__, __YEAR__)

    examples = []
    examples.append("")

    usage = "\n".join(examples)

    parser = OptionParser(version="%prog " + __VERSION__, usage=usage, description=banner)

    parser.add_option("--dir", "-d", action="store", type="string", dest="dir", help="Files match (Default: *.ics)", default="*.ics")
    parser.add_option("--ical", "-i", action="store", type="string", dest="icalfile", help="iCalendar file output")

    (options, args) = parser.parse_args()

    if options.icalfile == "":
        options.icalfile = None


    if options.icalfile != None:
        options.icalfile = os.path.realpath(options.icalfile)
        os.chdir(options.dir)
        ##files = glob.glob(options.files)

        combinedCalendar = vobject.iCalendar()

        for i in glob.glob("*.ics"):
            print "Opening '%s'.." % i
            f = open(i, 'rb')

            print "Reading '%s'.." % i
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
                        combinedCalendar.add(child)
            
                

        # Write iCal file
        print "Writing iCalendar file '%s'.." % options.icalfile
        f = open(options.icalfile, 'wb')
        f.write(combinedCalendar.serialize(validate=False))
        f.close()

        print "Done."
        sys.exit(0)

    sys.exit(1)
