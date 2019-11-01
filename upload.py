from pydrive.drive import GoogleDrive 
from delete_items_in_gdrive_folder import delete_items_in_gdrive_folder
from upload_handler import upload_handler
from pydrive.auth import GoogleAuth
from datetime import datetime

def upload():

	""" Initial Authentication, local """
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()

	# Gdrive folder id, hard coded
	folder_id = '15vYFyHRd83FZgyfjAJ0XQtl8gm7-3WFy'
	#print(drive, vars(gauth))

	# Empty Gdrive folder
	delete_items_in_gdrive_folder(gauth, folder_id)

	#Path to folder for sync
	path = '/Users/samir/Documents/Project Kodak.nosync/sync notes/' # move to top run file

	#Upload handler for folder path and Grdrive folder
	upload_handler(gauth, path, folder_id)

	with open('./update_log.txt', 'a') as update_log:
		update_log.write('Synced with GDrive on ' + str(datetime.now()))

upload()	



	

