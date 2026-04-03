from core.supabase_client import supabase
import os
from typing import Dict

class FileTransfer:
    def __init__(self, current_user_id: str):
        self.current_user_id = current_user_id
        self.bucket_name = 'files'  # Assume bucket name

    def upload_file(self, file_path: str, receiver_id: str) -> Dict:
        try:
            filename = os.path.basename(file_path)
            with open(file_path, 'rb') as f:
                file_data = f.read()

            # Upload to storage
            supabase.storage.from_(self.bucket_name).upload(filename, file_data)

            # Get public URL
            file_url = supabase.storage.from_(self.bucket_name).get_public_url(filename)

            # Save metadata
            metadata = {
                'sender_id': self.current_user_id,
                'receiver_id': receiver_id,
                'filename': filename,
                'file_url': file_url
            }
            response = supabase.table('file_metadata').insert(metadata).execute()
            return response.data[0]
        except Exception as e:
            print(f"Error uploading file: {e}")
            return None

    def download_file(self, file_url: str, save_path: str) -> bool:
        try:
            response = supabase.storage.from_(self.bucket_name).download(file_url.split('/')[-1])
            with open(save_path, 'wb') as f:
                f.write(response)
            return True
        except Exception as e:
            print(f"Error downloading file: {e}")
            return False