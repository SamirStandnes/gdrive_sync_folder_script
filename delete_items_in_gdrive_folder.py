
from pydrive.drive import GoogleDrive

def delete_items_in_gdrive_folder(gauth, folder_id):
	
	""" Passed in authentication to drive object """
	drive = GoogleDrive(gauth)
	#print(drive)

	""" Iterate through passed passed gdrive folder (via folder_id) and delete all the items in it."""
	item_list = drive.ListFile({'q': "'{folder_id}' in parents and trashed=false".format(folder_id=folder_id)}).GetList()
	for item in item_list:
		#print('title: %s, id: %s' % (item['title'], item['id']))
		delete_item = drive.CreateFile({'id': item['id']})
		delete_item.Delete()
		#print('Deleted title: %s, id: %s' % (item['title'], item['id']))

	