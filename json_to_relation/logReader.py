import sys

from edxTrackLogJSONParser import EdXTrackLogJSONParser
from input_source import InURI
from json_to_relation import JSONToRelation
from output_disposition import OutputDisposition, OutputFile

format = OutputDisposition.OutputFormat.SQL_INSERTS_AND_CSV

if len( sys.argv ) != 4:
	print 'Use'
	print 'berkeleyx {outputfolder} {in_file_or_folder_from_root} {relative_modulestore}'
	quit()

out = sys.argv[1]

print out

logfile = open( out + '/transform.log', 'w')
outfile = OutputFile( out + '/data', format , options='wb')

parser = JSONToRelation( InURI( sys.argv[2] ) , outfile, mainTableName='EdxTrackEvent' )
parser.setParser( EdXTrackLogJSONParser( parser, 'EdxTrackEvent', dbName='Edx', moduleStore = sys.argv[3] ) )
parser.convert()