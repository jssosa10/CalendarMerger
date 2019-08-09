#!/bin/env/python
# -*- coding: utf8 -*-

import os
import sys
import traceback
import datetime
import glob
import codecs

from configparser import ConfigParser
from optparse import OptionParser, Option, OptionGroup

# 3rd party libs
import vobject

from merger import Merger


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
        Merger(options.dir,options.icalfile)
        sys.exit(0)

    sys.exit(1)
