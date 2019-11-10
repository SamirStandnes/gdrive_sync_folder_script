import os
from pydrive.drive import GoogleDrive 
#from file_content import file_content

def upload_handler(gauth, os_root_path, gdrive_root_folder_id):
	# Google authentication 
	drive = GoogleDrive(gauth)
	dir_dict = {os_root_path: gdrive_root_folder_id}

	#For each dir path starting from os_root_path by os.walk()
	for dirpath, dirnames, files in os.walk(os_root_path):
		print(dirpath, dirnames)
		#print(files)
		for file in files:
			#print(dir_dict, file, str('in ' + dirpath))
			new_file = drive.CreateFile({'title': file, "parents": [{"kind": "drive#fileLink", "id": dir_dict[dirpath]}]})  # Create GoogleDriveFile instance to parentID.
			file_path = os.path.join(dirpath, file)
			new_file.SetContentFile(file_path) # Set content of the file from given string.
			print(new_file)
			new_file.Upload()
		#for this path create a folder
		for dirname in dirnames:
			#print(dirname)
			new_folder = drive.CreateFile({'title': dirname, "parents":  [{"id": dir_dict[dirpath]}], "mimeType": "application/vnd.google-apps.folder" })
			new_folder.Upload()
			dir_dict[os.path.join(dirpath, dirname)] = new_folder['id']
			#print(new_folder['id'])
	
	#print(dir_dict)

