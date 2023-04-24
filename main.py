import dropbox

# Replace this with your access token
access_token = 'sl.BdLDglgVb1kVRPcHeVAW_wauXso020Rj37Wtbxjmnadk2oeTSBcuUIG1A9tLRpgAAsfRxHPgWvt5wBK75T_cS36cO4du8fK_yAa9UUNFHmQ-Yj9xe__94fOcBWPpA8B8w1CaBZ12rPQ'

# Create a Dropbox client object
dbx = dropbox.Dropbox(access_token)

'''# Upload a file
with open('example.txt', 'rb') as f:
    dbx.files_upload(f.read(), '/example.txt')
'''

# List files in a folder
result = dbx.files_list_folder('/Family Room/CBCT/FINAL DICOMS/JAWS')
for entry in result.entries:
    print(entry.name)
    ext = entry.name.split('.')[1]
    print(ext)

# Download a file
"""with open('downloaded_example.zip', 'wb') as f:
    metadata, res = dbx.files_download('/To_test/alexandrabnissen.zip')
    f.write(res.content)"""

# Delete a file
# dbx.files_delete('/example.txt')
