# This script requires a .txt where each line corresponds to one dependancy.
# You can get this by copying and pasting it from BitBucket. This file is
# referred to here as 'repos.txt. The script will bump the minor version
# of all the dependancies by one.
#
# Run this script in the shell like so: 
# 'python minorbump.py repos.txt'
#
# Your output will be a .txt file by the name of new_repos.txt and you can
# then use this to copy and paste into the relevant setup.py

from sys import argv
import re

script, txt = argv

def readLines(txt):
    """Reads the lines of a .txt file and appends them all to a list."""

    with open(txt, 'r') as f:
        
        repos = f.readlines()
        return repos

def bumpMinorVersion(repos):
    """Increases the minor version of a repo by one"""

    bumped_repos = []

    for repo in repos:
        
        # Find each occurence of the version number and capture the third number
        minor_version = re.findall('==\d+.\d+.(\d+)', repo)
        
        bumped_minor_version = int(minor_version[0]) + 1

        bumped_minor_version = str(bumped_minor_version)

        # This is our regex string
        regex_string = r'\g<1>%s' % bumped_minor_version

        # Operate the regex command on the old repo
        bumped_repo = re.sub(r'(==\d+.\d+.)\d+', regex_string, repo)

        bumped_repos.append(bumped_repo)

    return bumped_repos

def writeNewRepos(bumped_repos):
    """Takes a list and writes it line by line to 'new_<txt>.txt"""

    with open('new_' + txt, 'w') as f:
        
        for bumped_repo in bumped_repos:
   
            f.write(bumped_repo)

repos = readLines(txt)

bumped_repos = bumpMinorVersion(repos)

writeNewRepos(bumped_repos)

