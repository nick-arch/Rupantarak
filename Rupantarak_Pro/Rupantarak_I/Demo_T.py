import subprocess
import threading
import time
from IPython.display import display, HTML
import ipywidgets as widgets

def check_cuda_availability():
    try:
        import torch
        return torch.cuda.is_available()
    except ImportError:
        return False

def update_progress(progress_bar):
    total_duration = 100
    for i in range(total_duration + 1):
        progress_bar.value = (i / total_duration) * 100
        time.sleep(1)

def run_installation():
    if check_cuda_availability():
        display_heading()
        display_cuda_available_message()
        progress_bar = widgets.FloatProgress(
            value=0,
            min=0,
            max=100,
            layout=widgets.Layout(width='90%', margin='0 auto 0 auto')
        )
        display(progress_bar)
        progress_thread = threading.Thread(target=update_progress, args=(progress_bar,))
        progress_thread.start()

        commands = [
            "apt install nvidia-cuda-toolkit --yes",
            "pip install gdown",
        ]
        log_output = widgets.Output(layout={'border': '0px solid black', 'width': '100%', 'height': '300px', 'overflow_y': 'scroll'})
        accordion = widgets.Accordion(children=[log_output])
        accordion.set_title(0, 'Nvidia Cuda Toolkit Installation Logs')
        accordion.selected_index = None
        accordion.add_class("custom-accordion")
        display(accordion)
        
        with log_output:
            for command in commands:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
                for line in iter(process.stdout.readline, ''):
                    print(line, end='')
                process.communicate()
    else:
        display_cuda_not_available_message()

def display_heading():
    heading_html = """
    <style>
        .heading {
            text-align: center;
            font-weight: bold;
            font-size: 24px;
            margin-bottom: 20px;
        }
    </style>
    <div class="heading">
        GPU Acceleration Nvidia Cuda Toolkit Installation
    </div>
    """
    display(HTML(heading_html))

def display_cuda_available_message():
    available_html = """
    <style>
        .available-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #D4EDDA;
            border: 2px solid #28A745;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .available-popup h2 {
            color: #28A745;
        }
        .available-popup p {
            color: #333333;
        }
    </style>
    <div id="available-popup" class="available-popup">
        <h2>CUDA toolkit is available for acceleration!</h2>
        <p>Proceeding with installation...</p>
    </div>
    <script>
        // Function to hide the popup after 2 seconds
        setTimeout(function() {
            var popup = document.getElementById('available-popup');
            popup.style.display = 'none';
        }, 2000);
    </script>
    """
    display(HTML(available_html))

def display_cuda_not_available_message():
    unavailable_html = """
    <style>
        .unavailable-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #F8D7DA;
            border: 2px solid #FFC107;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .unavailable-popup h2 {
            color: #DC3545;
        }
        .unavailable-popup p {
            color: #333333;
        }
    </style>
    <div id="unavailable-popup" class="unavailable-popup">
        <h2>CUDA toolkit is not available for acceleration</h2>
        <p>The CUDA toolkit is not detected in this environment.</p>
        <p>Please make sure you are using a GPU-enabled runtime environment.</p>
    </div>
    <script>
        // Function to hide the popup after 2 seconds
        setTimeout(function() {
            var popup = document.getElementById('unavailable-popup');
            popup.style.display = 'none';
        }, 12000);
    </script>
    """
    display(HTML(unavailable_html))

run_installation()


# Step 1: Install the gdown library outside the function block

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
    'https://drive.google.com/file/d/10xIVD7CDWWZAeCzQQg2kFUBJXiFE9Um0/view?usp=drivesdk'
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
