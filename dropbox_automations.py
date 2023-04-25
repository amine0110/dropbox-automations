import dropbox
import yaml
import os
import shutil

class DropboxDownloader:
    def __init__(self, volumes_dir=None, annotations_dir=None, config='utils/config.yaml', volumes_txt='utils/volumes.txt', annotation_txt='utils/annotations.txt') -> None:
        os.makedirs('tmp', exist_ok=True)
        self.access_token = self.get_access_token(config)
        self.dbx = dropbox.Dropbox(self.access_token)
        self.volumes_dir = volumes_dir
        self.annotations_dir = annotations_dir
        self.volumes_txt = volumes_txt
        self.annotation_txt = annotation_txt
    
    def get_access_token(self, config):
        with open(config) as file:
            data = yaml.safe_load(file)
        return data['access_token']
    
    def __ext__(self, name):
        return name.split('.')[1]
    
    def return_txt_file(self, line, out_dir):
        file = open(out_dir,'a+')
        file.write(line)
    
    def return_file_name(self, dbx_link):
        self.files_names = []
        cbct_scans = self.dbx.files_list_folder(dbx_link)
        for entry in cbct_scans.entries:
            self.files_names.append(entry.name)
        return self.files_names
    
    def return_file_name_from_txt(self, txt_file):
        files_names = []
        with open(txt_file, 'r') as file:
            # Iterate through the lines in the file
            for line in file:
                # Print the line (strip() removes any leading/trailing whitespace and newline characters)
                files_names.append(line.strip())
        
        return files_names
    
    def download_one_file(self, file_link, txt_file='utils/volumes.txt'):
        file_name = os.path.basename(file_link)
        print('Downloading:', file_name)
        output_path = os.path.join('tmp', os.path.basename(txt_file).split('.')[0])
        os.makedirs(output_path, exist_ok=True)
        with open(os.path.join(output_path, file_name), 'wb') as f:
            metadata, res = self.dbx.files_download(file_link)
            f.write(res.content)
            self.return_txt_file(file_name + '\n', txt_file)
    
    def download_multiple_files(self, dbx_link, txt_file='utils/volumes.txt'):
        files = self.return_file_name(dbx_link)
        downloaded_files = self.return_file_name_from_txt(txt_file)

        for file_name in files:
            if file_name not in downloaded_files:
                self.download_one_file(dbx_link + '/' + file_name, txt_file=txt_file)
    
    def download_volume_annotation(self):
        if self.annotations_dir:
            self.download_multiple_files(self.annotations_dir, self.annotation_txt)

        if self.volumes_dir:
            self.download_multiple_files(self.volumes_dir, self.volumes_txt)
        

    def __del__(self):
        pass
        # shutil.rmtree('tmp')

downloders = DropboxDownloader(
    volumes_dir='/Family Room/CBCT/FINAL DICOMS/JAWS',
    annotations_dir= '/Family Room/CBCT/Final_Versions/JAWS/split jaws',
)

# print(downloders.return_file_name_from_txt(downloders.volumes_txt))

# downloders.download_volume_annotation()

# downloders.download_multiple_files('/Family Room/CBCT/FINAL DICOMS/JAWS')



# print(downloders.return_file_name('/Family Room/CBCT/FINAL DICOMS/JAWS'))