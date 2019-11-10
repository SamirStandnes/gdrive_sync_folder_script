from pydrive.drive import GoogleDrive 
from delete_items_in_gdrive_folder import delete_items_in_gdrive_folder
from upload_handler import upload_handler
from pydrive.auth import GoogleAuth
from datetime import datetime

def upload(path, folder_id):

	""" Initial Authentication, local """
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()

	# Gdrive folder id, if you want hard code it
	#folder_id = ''
	
	#print(drive, vars(gauth))

	# Empty Gdrive folder
	delete_items_in_gdrive_folder(gauth, folder_id)

	#Path to folder for sync if you want to hard code it
	#path = '' 

	#Upload handler for folder path and Grdrive folder
	upload_handler(gauth, path, folder_id)

	with open('./update_log.txt', 'a') as update_log:
		update_log.write( '\n' + 'Synced with GDrive on ' + str(datetime.now()))


""" If you decide to hard code the Google Drive folder ID and Directory Path into the upload function 
	you dont have to read the folder_sync_registrer below. You can just remove the code and uncomment
	the upload call below this section
"""

import csv
with open('folder_sync_registrer.txt', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
    	upload(row[0], row[1])
    	


#upload()	



	

