import os
import sys
from datetime import datetime
import time

#--------------------------------------------------------------------------------------------------------------------------
# Script function
def executeTask(sourceFolder, replicaFolder, logFile, period):
	# Log
	print('-----------------------------------------------------------------------')
	print('INFO - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Executing replication')

	# Obtain list of files from folders
	try:
		sourceFiles = os.listdir(sourceFolder)
	except WindowsError:
		print('ERROR - Windows cannot find the folder path from source folder')
		sys.exit()

	try:
		replicaFiles = os.listdir(replicaFolder)
	except WindowsError:
		print('ERROR - Windows cannot find the folder path from replica folder')
		sys.exit()

	# Initialize list of new files, same files
	new = []
	same = []
	deleted = []

	if (replicaFolder != []):
		for file in replicaFiles:
			if (file not in sourceFiles):
				deleted.append(file)

	if (sourceFiles != []):
		for file in sourceFiles:
			if (file in replicaFiles):
				same.append(file)
			elif (file not in replicaFiles):
				new.append(file)

	#--------------------------------------------------------------------------------------------------------------------------
	# Creation of new files

	for file_name in new:
		#Copy file information from Source Folder
		with open(sourceFolder + '/' + file_name) as file:
			file_text = file.read()

		#Paste file information to Replica Folder	
		with open(replicaFolder + '/' + file_name, 'w') as file:
			file.write(file_text)
			
			# Log console
			print('INFO - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Creation of file ' + file_name + ' in \'' + replicaFolder + '\'')
			# Log file
			with open(logFile, 'a') as f2:
				f2.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Creation of file ' + file_name + ' in \'' + replicaFolder + '\'\n')

	#--------------------------------------------------------------------------------------------------------------------------
	# Modification of files

	for file_name in same:
		# Obtain file1 (source) data
		with open(sourceFolder + '/' + file_name) as file:
			file1 = file.read()
		with open(replicaFolder + '/' + file_name) as file:
			file2 = file.read()
		# Compare content in files	
		if (file1 == file2):
			pass
		else:
			with open(replicaFolder + '/' + file_name, 'w') as file:
				file.write(file1)

			# Log console
			print('INFO - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Copying of file ' + file_name + ' from \'' + sourceFolder + '\' to \'' + replicaFolder + '\'')
			# Log file
			with open(logFile, 'a') as f2:
				f2.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Copying of file ' + file_name + ' from \'' + sourceFolder + '\' to \'' + replicaFolder + '\'\n')

	#--------------------------------------------------------------------------------------------------------------------------
	# Removal of files

	for file_name in deleted:
		os.remove(replicaFolder + '/' + file_name)

		# Log console
		print('INFO - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Deletion of file ' + file_name + ' from \'' + replicaFolder + '\'')
		# Log file
		with open(logFile, 'a') as f2:
			f2.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Deletion of file ' + file_name + ' from \'' + replicaFolder + '\'\n')

	#--------------------------------------------------------------------------------------------------------------------------
	# Log
	print('INFO - ' + datetime.now().strftime("%m/%d/%Y, %H:%M:%S.%f") + ' - Finished replication')

	# Time Period
	time.sleep(period)
