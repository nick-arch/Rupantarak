from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
import subprocess
import shutil
import os
import io
import sys
from threading import Timer
import os
import gdown

def download_from_gdrive(url, save_path):
    # Ensure the save path directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Extract the file ID from the URL
    file_id = url.split('/d/')[1].split('/')[0]
    download_url = f'https://drive.google.com/uc?id={file_id}'
    
    # Download the file using gdown
    gdown.download(download_url, save_path, quiet=True)

# Example usage
gdrive_url = 'https://drive.google.com/file/d/11k-mc0MyH48Q84tt0hcdnbGT1pAtnJJn/view?usp=drivesdk'
save_path = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Bypass.zip'

download_from_gdrive(gdrive_url, save_path)

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
    background: linear-gradient(to right, #555555, #666666); /* Slightly lighter gradient on hover */
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
  background-image: linear-gradient(to right, #FA8072, #F5F5DC);
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
            background-color: #F5F5DC;
            border: 2px solid #FA8072;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            width: 250px; /* Set width */
        }
        .wrong-password-popup h2 {
            color: #ff0066;
        }
        .wrong-password-popup p {
            color: #333333;
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
extract_button = widgets.Button(description='Access रूपांतरक ~ Bypass)

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
