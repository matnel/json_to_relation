import sys
import os

from edxTrackLogJSONParser import EdXTrackLogJSONParser
from input_source import InURI
from json_to_relation import JSONToRelation
from output_disposition import OutputDisposition, OutputFile

format = OutputDisposition.OutputFormat.SQL_INSERTS_AND_CSV

def parse( out, infile, modulestore ):

	logfile = open( out + '/transform.log', 'w')
	outfile = OutputFile( out + '/data', format , options='wb')

	parser = JSONToRelation( InURI( infile ) , outfile, mainTableName='EdxTrackEvent' )
	parser.setParser( EdXTrackLogJSONParser( parser, 'EdxTrackEvent', dbName='Edx', moduleStore = modulestore ) )
	parser.convert()

if __name__ == '__main__':

	if len( sys.argv ) != 4:
		print 'Use'
		print 'berkeleyx {outputfolder} {in_file_or_folder_from_root} {relative_modulestore}'
		quit()

	## check if we have a folder containing data
	fileList = []

	for root, subFolders, files in os.walk(sys.argv[2]):
		for file in files:
			fileList.append(os.path.join(root,file))

	for f in fileList:
		print "Doing", f
		parse( sys.argv[1] , f, sys.argv[3] )

	print "Done"
