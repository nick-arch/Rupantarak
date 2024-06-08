import gdown
import os

def download_image_from_gdrive(gdrive_url, save_path):
    """
    Download an image from Google Drive and save it to a specified path.

    Parameters:
    gdrive_url (str): The Google Drive URL of the file.
    save_path (str): The path where the file should be saved.
    """
    file_id = gdrive_url.split('/')[-2]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    gdown.download(download_url, save_path, quiet=True)

gdrive_urls = [
    'https://drive.google.com/file/d/10z1_ukVfDNQxB96MmTs34VUAd5UkgA-u/view?usp=drivesdk',
    'https://drive.google.com/file/d/10z1_ukVfDNQxB96MmTs34VUAd5UkgA-u/view?usp=drivesdk',
    'https://drive.google.com/file/d/10Eih3BT8wtdtqlIik5S0fy4Tx6RBJ3z3/view?usp=drivesdk',
    'https://drive.google.com/file/d/10z1_ukVfDNQxB96MmTs34VUAd5UkgA-u/view?usp=drivesdk',
    'https://drive.google.com/file/d/10z1_ukVfDNQxB96MmTs34VUAd5UkgA-u/view?usp=drivesdk'
]

save_paths = [
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_B/Rupantarak_B_0.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_O/Rupantarak_Output.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Me.jpg',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_T/Rupantarak_T_1.png',
    '/content/Rupantarak/Rupantarak_Pro/Rupantarak_M/trimmed_video.mp4',
]

for url, path in zip(gdrive_urls, save_paths):
    download_image_from_gdrive(url, path)

downloaded_files = os.listdir('/content')
