#!/usr/bin/env python3
# Assumes: Python 3.6+

import argparse
from asyncore import file_dispatcher
import os
import shutil
import yaml
import array
import logging
        

        # with open(filepath, 'r') as f:
        #     resourceFile = yaml.safe_load(f)


# 
#     lines = file.readlines()

# for line in lines:
#     print ("line: {}".format(line))

# no newlines or trailing spaces
def readFileAsLines(filepath):
    lines = []
    with open(filepath, 'r') as file:
        for line in file:
            cleanLine = line.strip()
            if cleanLine == "":
                continue
            lines.append(cleanLine)
    return lines

def grabAndCleanName(lines):
    key = ".. Title"
    if key not in lines:
        return None
    keyIndex = lines.index(key)
    nameIndex = keyIndex + 1
    if len(lines) <= nameIndex:
        return None
    return lines[nameIndex].split("--")[0].strip()

def grabAndCleanDescription(lines):
    startKey = ".. Description"
    endKey = ".. Aliases"
    if startKey not in lines or endKey not in lines:
        return ""
    startIndex = lines.index(startKey)
    endIndex = lines.index(endKey)
    if endIndex - startIndex <= 1:
        return ""
    description = ""
    for i in range(startIndex+1, endIndex):
        descriptionLine = "{}.".format(lines[i].strip(" .-"))
        if descriptionLine == "":
            continue
        description = "{} {}".format(description, descriptionLine)
    return description.strip()

def buildDocLink(urlBase, filepath):
    return "{}{}".format(urlBase, filepath)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs-dir", dest="docsDir", type=str, help="Directory for docs")
    parser.add_argument("--url-base", dest="urlBase", type=str, help="Base URL for building doc link")
    
    args = parser.parse_args()
    docsDir = args.docsDir
    urlBase = args.urlBase
    content = []
    # tempRSTDir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"temp-rst")
    for filename in os.listdir(docsDir):
        if not filename.endswith(".rst"): # or filename == 'index.rst': 
            continue
        filepath = os.path.join(docsDir, filename)
        lines = readFileAsLines(filepath)
        name = grabAndCleanName(lines)
        if name is None:
            continue
        description = grabAndCleanDescription(lines)
        docLink = buildDocLink(urlBase, filepath)
        content.append({
            "name": name,
            "description": description,
            "doclink": docLink
        })
    print(content)

if __name__ == "__main__":
   main()