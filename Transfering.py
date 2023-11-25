import dropbox

class TransferData:
    def __init__(self, acess_token):
        self.acess_token = acess_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.acess_token)
        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    acess_token = "sl.BqgdO_PGkLavEnUvjgx87J4QWj6ia9T6GjM4vuuODLxY49bhR5oL1utU0CotF_otEYptXbMC1UILZxOsJzdKi6a2luThC-Cc5dOGeeukIiXlrdDcVLRt3gnPA47GlVHQWPXMZa-H4lnT"
    
    transferdata = TransferData(acess_token)
    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to uplaod to DropBox: ")
   
    transferdata.uplaod_file(file_from, file_to)

main()
