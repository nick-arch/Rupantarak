from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import subprocess
import shutil
import os
import gdown
from threading import Timer



gradient_button_css = """
<style>



button {
    background: linear-gradient(to right, #444444, #555555); /* Dark grey gradient */
    border-radius: 20px; /* Rounded corners */
    border: none; /* No border */
    color: white; /* Text color */
    padding: 10px 20px; /* Padding */
    text-align: center; /* Text alignment */
    text-decoration: none; /* No text decoration */
    display: inline-block; /* Display inline-block */
    font-size: 18px; /* Font size */
    font-weight: bold; /* Bold text */
    margin: 4px 20px; /* Margin */
    cursor: pointer; /* Pointer cursor on hover */
    transition: background 0.4s, transform 0.4s; /* Transition effect duration */
    width: 300px; /* Fixed width */
}

/* Hover effect */
button:hover {
    background: linear-gradient(to right, #FF007F, #800080); /* Slightly lighter gradient on hover */
    transform: scale(1.05); /* Slightly increase size */
}

/* Click effect */
button:active {
    background: linear-gradient(to right, #FA8072, #F5F5DC); /* Darker gradient on click */
    transform: scale(0.95); /* Slightly decrease size */
}

.password_text {
  background-image: linear-gradient(to right, #444444, #555555);
  border: none;
  border-radius: 10px;
  padding: 10px 10px;
  color: #fff;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.password_text:hover {
  background-image: linear-gradient(to right, #FF007F, #800080);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}

</style>
"""
# Inject custom CSS into the notebook
display(HTML(gradient_button_css))

# Define the custom CSS style
custom_css = """
<style>
/* Increase font size for labels */
.widget-label {
    font-size: 14px !important; /* Adjust the font size as needed */
}

/* Increase font size and make button text bold */
.widget-button {
    font-size: 16px !important; /* Adjust the font size as needed */
    font-weight: bold !important;
}

/* Increase font size for upload box text */
.upload-box-text {
    font-size: 14px !important; /* Adjust the font size as needed */
}
</style>
"""

# Inject the custom CSS into the notebook
display(HTML(custom_css))


from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import subprocess
import shutil
import os

# Function to download from Google Drive
def download_from_gdrive(url, save_path):
    # Ensure the save path directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Extract the file ID from the URL
    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Download the file using gdown
    gdown.download(download_url, save_path, quiet=True)

# Example usage
gdrive_url = 'https://drive.google.com/file/d/12CJ2yRqgMcdQnFSxPrjVmDly8kZckJUV/view?usp=drivesdk'
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

from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import subprocess
import shutil
import os

# Function to unlock the ZIP file
def unlock_zip(button):
    password = password_text.value
    try:
        # Check if extraction directory exists
        extraction_dir = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/unzipped'
        if os.path.exists(extraction_dir):
            shutil.rmtree(extraction_dir)  # Delete the old extraction directory and its contents
        
        # Extract the new ZIP file
        command = f'unzip -P "{password}" /content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Bypass.zip -d {extraction_dir}'
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        # No need to print output as it's hidden now
        
        # Display success message
        display_success()
        
    except subprocess.CalledProcessError as e:
        # Display wrong password message
        display_wrong_password()
# Function to display a success message with a continuously looping animated pop arrow at the bottom
# Function to display a success message with a continuously looping animated pop arrow at the bottom
def display_success():
    success_html = """
    <style>
    .success-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(135deg, #222222, #222222); /* Popup background gradient */
        border: 2px solid #222222;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        width: 250px; /* Set width */
        color: #ffffff; /* Text color */
    }
    .success-popup h2 {
        background: linear-gradient(to right, #00FF00, #008000); /* Green gradient */
        font-weight: bold;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .success-popup p {
        background: linear-gradient(to right, #FF007F, #800080); /* Pink-purple gradient */
        font-weight: bold;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
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
        border-top: 20px solid #00FF00; /* Arrow color */
        animation: arrowPop 0.5s infinite alternate;
    }
    @keyframes arrowPop {
        0% {bottom: -20px;}
        100% {bottom: -15px;}
    }
    </style>
    <div id="success-popup" class="success-popup">
        <h2>रूपांतरक ~ Rupantarak Uncensored Unlocked Successfully!</h2> <!-- Success text green gradient -->
        <h3>Run Below Cell To Use The Tool...</h3> <!-- Other text pink-purple gradient -->
        <div class="arrow"></div>
    </div>
    """
    global success_popup
    success_popup = widgets.HTML(success_html)
    display(success_popup)

# Call display_success to show the success message with the continuously looping animated pop arrow at the bottom
# Call display_success to show the success message with the continuously looping animated pop arrow at the bottom



# Function to display a message for wrong password
def display_wrong_password():
    wrong_password_html = """
    <style>
    .wrong-password-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: linear-gradient(45deg, #ff0000, #ff0066);
        border: 2px solid #222222;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        width: 250px; /* Set width */
        color: #111111; /* Text color */
    }
    .wrong-password-popup h2 {
        color: #ffffff;
        font-weight: bold;
    }
</style>
<div id="wrong-password-popup" class="wrong-password-popup">
    <h2>Wrong password!</h2>
    <p>Please enter the correct password.</p>
</div>
<script>
    // Hide the popup after 3 seconds
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

# Set width and height for the password field
password_text.layout.width = '250px'
password_text.layout.height = 'auto'

# Create extract button
extract_button = widgets.Button(description='Access रूपांतरक ~ Rupantarak')

# Set width and height for the button
extract_button.layout.width = '250px'
extract_button.layout.height = '50px'

extract_button.on_click(unlock_zip)

# Create a container to center the elements with margins
container = widgets.VBox([widgets.Label(''), password_text, widgets.Label(''), extract_button, widgets.Label('')],
                         layout=widgets.Layout(justify_content='center', margin='20px 0'))

# Create another container to center the main container
main_container = widgets.VBox([container], layout=widgets.Layout(justify_content='center', align_items='center'))

# Modify the layout of the main container to remove any unnecessary space
main_container.layout.margin = '0px'

# Display main container
display(main_container)
