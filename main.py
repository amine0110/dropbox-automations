import dropbox
import yaml
import os
import shutil

class DropboxDownloader:
    def __init__(self, config='utils/config.yaml') -> None:
        os.makedirs('tmp', exist_ok=True)
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
    
    def download_one_file(self, file_link):
        file_name = os.path.basename(file_link)
        print('Downloading:', file_name)
        with open(os.path.join('tmp', file_name), 'wb') as f:
            metadata, res = self.dbx.files_download(file_link)
            f.write(res.content)
            self.return_txt_file(file_name, 'utils/volumes.txt')
    
    def return_txt_file(self, line, out_dir):
        file = open(out_dir,'a+')
        file.write(line)

    def __ext__(self, name):
        return name.split('.')[1]
    
    def __del__(self):
        pass
        # shutil.rmtree('tmp')

downloders = DropboxDownloader()
print(downloders.__ext__('/To_test/alexandrabnissen.zip'))
downloders.download_one_file('/To_test/alexandrabnissen.zip')


# print(downloders.return_file_name('/Family Room/CBCT/FINAL DICOMS/JAWS'))