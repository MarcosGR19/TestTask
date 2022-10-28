import sys
from functions import executeTask

#--------------------------------------------------------------------------------------------------------------------------	
# Input args
try:
	sourceFolder = sys.argv[1] 
	replicaFolder = sys.argv[2]
	logFile = sys.argv[3]
	period = int(sys.argv[4])
except IndexError, NameError:
	print('ERROR - Any of these arguments are missing: sourceFolderPath replicaFolderPath logFilePath timePeriod')
	sys.exit()
except ValueError:
	print('ERROR - Wrong arguments format type')
	sys.exit()

#--------------------------------------------------------------------------------------------------------------------------

# Truncate log file
with open(logFile, 'w') as f:
		f.truncate()

# Execute function
try:
	while True:
		executeTask(sourceFolder, replicaFolder, logFile, period)
except KeyboardInterrupt:
	print('-----------------------------------------------------------------------')
	print('INFO - Process Ended by KeyboardInterrupt')
else:
	print('ERROR - Wrong arguments format')
	
