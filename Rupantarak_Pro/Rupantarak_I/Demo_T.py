

# Step 2: Import the necessary libraries
import gdown
import os
from IPython.display import clear_output

# Clear the output after installing
clear_output()

# Step 3: Create a function to download images
def download_image_from_gdrive(gdrive_url, save_path):
    """
    Download an image from Google Drive and save it to a specified path.

    Parameters:
    gdrive_url (str): The Google Drive URL of the file.
    save_path (str): The path where the file should be saved.
    """
    # Extract the file ID from the URL
    file_id = gdrive_url.split('/')[-2]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Download the file using gdown
    gdown.download(download_url, save_path, quiet=True)

# Step 4: Define the Google Drive URLs and save paths
gdrive_urls = [
    'https://drive.google.com/file/d/10z1_ukVfDNQxB96MmTs34VUAd5UkgA-u/view?usp=drivesdk',
    'https://drive.google.com/file/d/10w9Yu7yx6-klXubAkeb0BL1XwKPh2c-4/view?usp=drivesdk',
    'https://drive.google.com/file/d/10Eih3BT8wtdtqlIik5S0fy4Tx6RBJ3z3/view?usp=drivesdk'
]

# Use Colab's file system path
save_paths = [
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Rupantarak_B_0.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_O/Rupantarak_Output.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Me.jpg',
]

# Step 5: Download the images
for url, path in zip(gdrive_urls, save_paths):
    download_image_from_gdrive(url, path)

# Clear the output to hide the download process
clear_output()

# Step 6: Verify that files were downloaded (if needed)
downloaded_files = os.listdir('/content')
