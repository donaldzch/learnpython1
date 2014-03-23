__author__ = 'Donald'

from Utils import XMLConverter
from AppClientConfig import AppClientParser
import sys
import argparse
import os

APP_CLIENT = "appClient"
APP_CLIENT_LOG_FILE = 'appclientloader.log'


def _writeToLogFile(clientId, filename, results):
    logFile = open(APP_CLIENT_LOG_FILE, 'a')
    logFile.write("client: %s at %s\n" % (clientId, filename))
    for result in results:
        logFile.write(result + "\n")
    logFile.close()


def _loadClientToDB(parsedFiles):
    print ('loadClientToDB')
    pass


def parse(inputFiles, load=False):
    parsedFiles = []
    errornum = 0
    if os.path.exists(APP_CLIENT_LOG_FILE):
        os.remove(APP_CLIENT_LOG_FILE)
    for inputFile in inputFiles:
        clientDict = XMLConverter.toDict(inputFile[1])
        clientId, results = AppClientParser.parse(clientDict)
        if len(results):
            print ('parse %s client: %s, error: %d' % (inputFile[0], clientId, len(results)))
            _writeToLogFile(clientId, inputFile[0], results)
            errornum += 1
        else:
            parsedFiles.extend([(clientId, inputFile[0], clientDict)])
    print ('Total clients: %d, Error: %d' % (len(inputFiles), errornum))
    if len(inputFiles) == len(parsedFiles) and load:
        _loadClientToDB(parsedFiles)


def _getFiles(inputDir):
    inputFiles = []

    listDirs = os.walk(inputDir)
    for root, dirs, files in listDirs:
        for f in files:
            if os.path.splitext(f)[1] == '.xml':
                inputFiles.extend([(os.path.realpath(os.path.join(root, f)), file(os.path.join(root, f)))])
    return inputFiles


def isdir(parseDirectory):
    inputDir = str(parseDirectory)
    if not os.path.isdir(inputDir):
        raise argparse.ArgumentTypeError('%s is invalid directory path' % inputDir)
    return _getFiles(inputDir)


def isfile(parseFile):
    inputFile = str(parseFile)
    if not os.path.isfile(inputFile):
            raise argparse.ArgumentTypeError('%s is invalid file' % inputFile)
    return os.path.realpath(inputFile), file(inputFile)


def dedup(inputFiles):
    dedupFiles = []
    dedupKeys = []
    for inputFile in inputFiles:
        if inputFile[0] in dedupKeys:
            pass
        else:
            dedupFiles.append(inputFile)
            dedupKeys.append(inputFile[0])
    return dedupFiles


if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser()
    argumentParser.add_argument('-p', '--path', dest='path', type=isdir,
                                help='input valid directory for parse or load')
    argumentParser.add_argument('-f', '--file', dest='file', nargs='*',
                                type=isfile, help='input valid files for parse or load')
    argumentParser.add_argument('-e', '--execute', dest='action', choices=['parse', 'load'],
                                default='parse', help='parse the file or load file to database')
    args = argumentParser.parse_args(sys.argv[1:])
    #print args.action
    #print args.__dict__
    inputFiles = []
    if args.path and len(args.path):
        inputFiles = args.path
    elif args.file and len(args.file):
        inputFiles = dedup(args.file)
    else:
        print "missing input sources"

    if len(inputFiles):
        parse(inputFiles)
