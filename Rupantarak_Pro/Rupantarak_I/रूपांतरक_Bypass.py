from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import subprocess
import shutil
import os
import gdown
from threading import Timer

def download_from_gdrive(url, save_path):
    # Ensure the save path directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Extract the file ID from the URL
    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Download the file using gdown
    gdown.download(download_url, save_path, quiet=True)

# Example usage
gdrive_url = 'https://drive.google.com/file/d/1Dj0NLVTcMCWN49qj_WUvvPQ8GBE-ta-C/view?usp=drivesdk'
save_path = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Bypass.zip'

download_from_gdrive(gdrive_url, save_path)

gradient_button_css = """
<style>

body {
    background: linear-gradient(135deg, #111111, #111111);
}

button {
    background: linear-gradient(to right, #222222, #222222); /* Dark grey gradient */
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
  background-image: linear-gradient(to right, #222222, #222222);
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

# Function to hide the password field and the button
def hide_elements():
    password_text.layout.visibility = 'hidden'
    password_text.layout.height = '0px'
    extract_button.layout.visibility = 'hidden'
    extract_button.layout.height = '0px'
    confirmation_popup.layout.visibility = 'hidden'
    confirmation_popup.layout.height = '0px'
    wrong_password_popup.layout.visibility = 'hidden'
    wrong_password_popup.layout.height = '0px'

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
        color: #ffffff; /* Text color */
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

# Main function to unlock the ZIP file
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
        
        # Hide the password field and the button
        password_text.layout.visibility = 'hidden'
        password_text.layout.height = '0px'
        extract_button.layout.visibility = 'hidden'
        extract_button.layout.height = '0px'
        
        # Clear all output
        clear_output(wait=True)
        
        # Display success message
        
        # Run the extracted Python file
        run_extracted_file()
        
        # Hide the password field and button after 5 seconds
        Timer(5, hide_elements).start()
        
    except subprocess.CalledProcessError as e:
        # Display wrong password message
        display_wrong_password()

# Create password input field without a label
password_text = widgets.Password(placeholder='Enter password')
password_text.add_class("password_text")

# Set width and height for the password field
password_text.layout.width = '250px'
password_text.layout.height = 'auto'

# Create extract button
extract_button = widgets.Button(description='Access रूपांतरक ~ Bypass')

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

from IPython.display import display, HTML

popup_html = """
<style>
.modal {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: transparent;
    padding: 20px;
    border: 2px solid #222222; /* Border color and thickness */
    border-radius: 10px;
    text-align: center;
}

.popup-background {
    background-color: #000; /* Black background */
    padding: 20px;
    border-radius: 10px;
}

.popup-header {
    font-size: 24px;
    font-weight: bold;
    background: -webkit-linear-gradient(left, #00FF00, #008000); /* Green gradient for this text */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.popup-description-gradient {
    font-size: 18px;
    margin: 10px 0;
    background: -webkit-linear-gradient(left, #FF007F, #800080); /* Gradient for this text */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.popup-uncensored {
    font-size: 18px;
    background: -webkit-linear-gradient(left, #ff0000, #ff6666); /* Red gradient for this text */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>

<div id="myModal" class="modal">
  <div class="modal-content">
    <div class="popup-background">
        <div class="popup-header"><b>Enter Password To Access</b></div>
        <div class="popup-description-gradient"><b>रूपांतरक ~ Rupantarak</b></div>
        <div class="popup-uncensored"><b>Uncensored</b></div>
    </div>
  </div>
</div>

<script>
// Automatically hide the modal after 3 seconds
setTimeout(function(){
    var modal = document.getElementById('myModal');
    modal.style.display = 'none';
}, 3000);
</script>
"""

# Display the popup
display(HTML(popup_html))


# Display main container
display(main_container)
