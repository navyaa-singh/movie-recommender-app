import pickle
import bz2
import os
import gdown  # This helper library handles the download

# 1. Your Google Drive File ID
file_id = '1-gmcKrv_9FYmu7P9NxnXEla1GWwGF3m1' 
url = f'https://drive.google.com/uc?id={1-gmcKrv_9FYmu7P9NxnXEla1GWwGF3m1}'
output = 'similarity.pbz2'

# 2. This checks if the file is already there; if not, it downloads it
if not os.path.exists(output):
    gdown.download(url, output, quiet=False)

# 3. Now load it as we did before
def load_similarity():
    with bz2.BZ2File(output, 'rb') as f:
        return pickle.load(f)

similarity = load_similarity()