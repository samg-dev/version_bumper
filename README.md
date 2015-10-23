# VersionBumper
This repository contains a script for bumping the minor version numbers in a list of packages using regex on a .txt file to locate the minor version number (the third number) and bump it by one. This repo also contains a script for generating an example .txt file to be worked on.

# USAGE
You can run the command:
python example_package_creator.py
to generate a list of packages that you would want to update.

Then run the command:
python minorbumper.py example_packages.txt
to bump all the minor version numbers!

