#! /usr/bin/env python

# Copyright (c) 2015 Dave McCoy (dave.mccoy@cospandesign.com)
#
# Nysa is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Nysa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Nysa; If not, see <http://www.gnu.org/licenses/>.


import sys
import os
import argparse
import shutil

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

NAME = os.path.basename(os.path.realpath(__file__))
PAR_DIR = os.path.realpath(os.path.dirname(__file__))
DEMO_NAME = "uart"

DESCRIPTION = "\n" \
              "\n" \
              "Rename the repository to your custom board design\n"

EPILOG = "\n" \
         "\n" \
         "Examples:\n" \
         "\t%s %s\n" \
         "\n" % (NAME, PAR_DIR)

def find_replace_in_file(filename, from_name, to_name):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    if from_name in data:
        f = open(filename, "w")
        print "Found: %s" % filename
        data = data.replace(from_name, to_name)
        f.write(data)
        f.close()

def recursive_find_replace(top_dir, from_name, to_name):
    #print "Dirname: %s" % top_dir
    for root, dirs, files in os.walk(top_dir):
        if ".git" in dirs:
            dirs.remove('.git')
        for name in dirs:
            #print "Keep: %s" % os.path.join(root, name)
            recursive_find_replace(os.path.join(root, name), from_name, to_name)

    for root, dirs, files in os.walk(top_dir):
        for name in files:
            #print "File: %s" % name
            if name.startswith("."):
                continue

            if name.startswith(DEMO_NAME):
                out_file = to_name + name.partition(DEMO_NAME)[2]
                shutil.move(os.path.join(root, name), os.path.join(root, out_file))
                name.replace(DEMO_NAME, out_file)

    for root, dirs, files in os.walk(top_dir):
        for name in files:
            #print "File: %s" % name
            if name.startswith("."):
                continue

            find_replace_in_file(os.path.join(root, name), from_name, to_name)

def rename_board(name_platform, debug = False):
    base_name = os.path.basename(name_platform)
    name = name_platform.partition("nysa-")[2]
    name = name.partition("-platform")[0]

    display_name = name.capitalize()
    while "-" in display_name:
        display_name = display_name.partition("-")[0] + display_name.partition("-")[2].capitalize()
        
    default_display_name = DEMO_NAME.capitalize()
    print "New Name: %s" % name

    board_name = name.replace("-", "_")
    shutil.move(DEMO_NAME, board_name)
    recursive_find_replace(name_platform, DEMO_NAME, board_name)
    print "Board name will be: %s" % display_name

    recursive_find_replace(name_platform, default_display_name, display_name)

def main(argv):
    #Parse out the commandline arguments
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=DESCRIPTION,
        epilog=EPILOG
    )

    parser.add_argument("-d", "--debug",
                        action="store_true",
                        help="Enable Debug Messages")

    args = parser.parse_args()

    print "Running Script: %s" % NAME
    print "Path: %s" % PAR_DIR

    rename_board(PAR_DIR, args.debug)

if __name__ == "__main__":
    main(sys.argv)


