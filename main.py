import dropbox
import yaml

class DropboxDownloader:
    def __init__(self, config='config.yaml') -> None:
        self.access_token = self.get_access_token(config)
        self.dbx = dropbox.Dropbox(self.access_token)
    
    def get_access_token(self, config):
        with open(config) as file:
            data = yaml.safe_load(file)
        return data['access_token']
    
    def return_file_name(self, dbx_link):
        self.files_names = []
        cbct_scans = self.dbx.files_list_folder(dbx_link)
        for entry in cbct_scans.entries:
            self.files_names.append(entry.name)
        return self.files_names

downloders = DropboxDownloader()

print(downloders.return_file_name('/Family Room/CBCT/FINAL DICOMS/JAWS'))