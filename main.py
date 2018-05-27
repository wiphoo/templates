***VERSION***
***USAGE***
***NUM_REQUIRED_ARGUMENTS***
#!/usr/bin/env python3
#######################################################################################
#
#	Copyright (c) 2018, Wiphoo (Terng) Methachawalit, All rights reserved.
#
#######################################################################################


#######################################################################################
#
#	STANDARD IMPORTS
#

import sys

from optparse import OptionParser


#######################################################################################
#
#	LOCAL IMPORTS
#


#######################################################################################
#
#	PROGRAM DEFENITIONS
#

#	version of this program
Version = '***VERSION***'

#	program usage, it is a string of an example for how to use this program with arugments
ArgsUsage = '***USAGE***'

#	number of required arugments
NumRequiredArgs = ***NUM_REQUIRED_ARGUMENTS***

#######################################################################################
#
#	GLOBAL VARIABLES
#


#######################################################################################
#
#	HELPER FUNCTIONS
#


#######################################################################################
#
#	CLASS DEFINITIONS
#


#######################################################################################
#
#	MAIN
#


def main():
	''' main function of this program '''
	
	###################################################################################
	#	options parsing

	usage = 'usage: %prog [options] {!r}'.format( ArgsUsage )
	parser = OptionParser( usage=usage, version=Version )
	parser.add_option( '-v', '--verbose',
							action='store_true', dest='verbose', default=True )
	( options, args ) = parser.parse_args()
	
	#	check the required arguments
	if len( args ) != NumRequiredArgs:
	#	the given arguments is not equals the required arguments,
	#		so print the error meessage and exit
		parser.error( 'incorrect number of arguments.' )
		sys.exit( -1 )
	
	###################################################################################
	#	parse arguments / options
	
	
	###################################################################################
	#	main
	

if __name__ == "__main__":
	#	call main function
	main()
