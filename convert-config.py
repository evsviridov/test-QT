#!/bin/python

# This Python file uses the following encoding: utf-8
import json
import sys

def readQuestion(f):
    f.readline()

    qFile = {'fName':f.readline().decode('ascii').strip()}
    aFiles = []
    for i in range(4):
        fName = f.readline().decode('ascii').strip()
        isTrue = int(f.readline()) > 0
        if fName != '.':
            aFiles.append({'fName':fName, 'isTrue':isTrue})
    return {'qwe':qFile, 'ans':aFiles}


def readConfig(fileName):
    questions = []
    f = open(fileName, mode="rb")
    totalQuestions = int(f.readline().decode('ascii'))
    for i in range(totalQuestions):
        questions.append( readQuestion(f))
    f.close()
    return questions

if __name__ == "__main__":
    try:
        inFileName = '/home/jack/Downloads/Test МЖГ/Test/lab2.txt'
        inFileName = sys.argv[1]

        questions = readConfig(inFileName)
        jsonConf = json.dumps(questions, indent=2)
        try:
            outFileName= '/home/jack/Downloads/Test МЖГ/Test/lab2.json'
            outFileName= sys.argv[2]
            print('# converting from "', inFileName, '" to "', outFileName, '"', sep='')
            f = open(outFileName, mode='w')
            print(jsonConf, file=f)
            f.close()
        except:
            print(jsonConf)
    except:
        print('Error')
        print('Usage:', sys.argv[0], 'infile [outfile]')
