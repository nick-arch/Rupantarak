from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import subprocess
import shutil
import os
import gdown

# Custom CSS for buttons, text fields, and popup text
gradient_button_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap');

body {
    font-family: 'Bree Serif', serif;
}

button {
    background: linear-gradient(to right, #FF5733, #FF0000);
    border-radius: 20px;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    font-weight: bold;
    margin: 4px 20px;
    cursor: pointer;
    transition: background 0.4s, transform 0.4s;
    width: 300px;
    font-family: 'Bree Serif', serif;
}
button:hover {
    background: linear-gradient(to right, #FF0000, #FF5733);
    transform: scale(1.00);
}
button:active {
    background: linear-gradient(to right, #FF5733, #FF0000);
    transform: scale(0.75);
}
.password_text {
  background-image: linear-gradient(to right, #FF5733, #FF0000);
  border: none;
  border-radius: 10px;
  padding: 10px 10px;
  color: #fff;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Bree Serif', serif;
}
.password_text:hover {
  background-image: linear-gradient(to right, #FF0000, #FF5733);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}
</style>
"""
display(HTML(gradient_button_css))

custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap');

.widget-label {
    font-size: 14px !important;
    font-family: 'Bree Serif', serif !important;
}
.widget-button {
    font-size: 16px !important;
    font-weight: bold !important;
    font-family: 'Bree Serif', serif !important;
}
.upload-box-text {
    font-size: 14px !important;
    font-family: 'Bree Serif', serif !important;
}
</style>
"""
display(HTML(custom_css))

# Function to download from Google Drive
def download_from_gdrive(url, save_path):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(download_url, save_path, quiet=True)

gdrive_url = 'https://drive.google.com/file/d/12fBmOIu_ZMXBwEDy54AzNCy5zRyK--fE/view?usp=drivesdk'
save_path = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Bypass.zip'
download_from_gdrive(gdrive_url, save_path)

# Function to run the extracted Python file
def run_extracted_file():
    extracted_file_path = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/unzipped/रूपांतरक_Bypass.py'
    if os.path.exists(extracted_file_path):
        try:
            with open(extracted_file_path, 'r') as file:
                exec(file.read())
        except Exception as e:
            print(f"Error running file: {e}")
    else:
        print("Extracted file not found!")

# Function to unlock the ZIP file
def unlock_zip(button):
    password = password_text.value
    try:
        extraction_dir = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/unzipped'
        if os.path.exists(extraction_dir):
            shutil.rmtree(extraction_dir)
        
        command = f'unzip -P "{password}" /content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Bypass.zip -d {extraction_dir}'
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        
        display_success()
        
    except subprocess.CalledProcessError as e:
        display_wrong_password()

# Function to display a success message with a continuously looping animated pop arrow at the bottom
def display_success():
    success_html = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap');

    .success-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #111111, #111111);
        border: 5px solid #222222;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        width: 250px;
        color: #ffffff;
        font-family: 'Bree Serif', serif;
    }
    .success-popup h2 {
        background: linear-gradient(to right, #FF5733, #FF0000);
        font-weight: bold;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Bree Serif', serif;
    }
    .success-popup p {
        background: linear-gradient(to right, FF5733, #FF0000);
        font-weight: bold;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Bree Serif', serif;
    }
    .arrow {
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-top: 20px solid #FF0000;
        animation: arrowPop 0.5s infinite alternate;
    }
    @keyframes arrowPop {
        0% {bottom: -20px;}
        100% {bottom: -15px;}
    }
    </style>
    <div id="success-popup" class="success-popup">
        <h2>रूपांतरक ~ Rupantarak Uncensored Unlocked Successfully!</h2>
        <h3>Run Below Cell To Use The Tool...</h3>
        <div class="arrow"></div>
    </div>
    """
    global success_popup
    success_popup = widgets.HTML(success_html)
    display(success_popup)

# Function to display a message for wrong password
def display_wrong_password():
    wrong_password_html = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap');

    .wrong-password-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(45deg, #111111, #111111);
        border: 5px solid #222222;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        width: 250px;
        height: 100px;
        color: #DC143C;
        font-family: 'Bree Serif', serif;
    }
    .wrong-password-popup h2 {
        color: #ffffff;
        font-weight: bold;
        font-family: 'Bree Serif', serif;
    }
</style>
<div id="wrong-password-popup" class="wrong-password-popup">
    <h2>Wrong password!</h2>
    <p>Please enter the correct password.</p>
</div>
<script>
    setTimeout(function() {
        var popup = document.getElementById("wrong-password-popup");
        popup.style.display = "none";
    }, 3000);
</script>
    """
    global wrong_password_popup
    wrong_password_popup = widgets.HTML(wrong_password_html)
    display(wrong_password_popup)

# Create password input field without a label
password_text = widgets.Password(placeholder='Enter password')
password_text.add_class("password_text")
password_text.layout.width = '250px'
password_text.layout.height = 'auto'

# Create extract button
extract_button = widgets.Button(description='Access रूपांतरक ~ Rupantarak')
extract_button.layout.width = '250px'
extract_button.layout.height = '50px'
extract_button.on_click(unlock_zip)

# Create a container to center the elements with margins
container = widgets.VBox([widgets.Label(''), password_text, widgets.Label(''), extract_button, widgets.Label('')],
                         layout=widgets.Layout(justify_content='center', margin='20px 0'))

# Create another container to center the main container
main_container = widgets.VBox([container], layout=widgets.Layout(justify_content='center', align_items='center'))
main_container.layout.margin = '0px'

# Display main container
display(main_container)


import os
import requests

def create_folders():
    folders = [
        "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T/",
        "/content/Rupantarak/Rupantarak_Pro/Rupantarak_F/",
        "/content/Rupantarak/Rupantarak_Pro/Rupantarak_B/",
        "/content/Rupantarak/Rupantarak_Pro/Rupantarak_O/",
        "/content/Rupantarak/Rupantarak_Pro/Rupantarak_M/"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def download_image_from_google_drive(url, save_path):
    file_id = url.split('/')[-2]
    download_link = f"https://drive.google.com/uc?id={file_id}"
    response = requests.get(download_link)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)

# Example usage:
url1 = "https://drive.google.com/file/d/12ki_2rG70Y96omzFAxz9S0jrwZ_gh1hg/view?usp=sharing"
url2 = "https://drive.google.com/file/d/12gvpIb8Aif070zmfEfZkZz0S28SfK7wa/view?usp=sharing"

save_path1 = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png"
save_path2 = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T/Rupantarak_T_1.png"

create_folders()
download_image_from_google_drive(url1, save_path1)
download_image_from_google_drive(url2, save_path2)
