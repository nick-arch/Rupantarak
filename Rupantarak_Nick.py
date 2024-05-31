
# @title **</h3>रूपांतरक ~ Rupantarak  ○ No Installation<h3>**

import subprocess
import re
import cv2
import time
import base64
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
import os
import numpy as np
import contextlib
from ipywidgets import VBox
from moviepy.editor import VideoFileClip
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from pytube import YouTube
import ipywidgets as widgets
from IPython.display import display, HTML
import threading
from IPython.display import display, Markdown
from IPython.display import HTML
from IPython.display import Javascript
from time import sleep
from google.colab import auth
from google.colab import drive
import gdown
from IPython.display import display, Javascript
from IPython.display import display, clear_output

# Custom CSS for gradient styles
gradient_button_css = """
<style>
body {
    background: linear-gradient(135deg, #111111, #111111);
}

.progress {
    width: 100%;
    height: 30px;
    background-color: #222222;
    border-radius: 15px;
    margin-bottom: 20px;
    overflow: hidden;
}

.progress-bar {
    border-radius: 20px;
    background-image: linear-gradient(to right, lightgreen, lightblue);
}

button {
    background: linear-gradient(to right, #0D47A1, #8E24AA); /* Dark blue to purple gradient */
    border-radius: 20px; /* Rounded corners */
    border: none; /* No border */
    color: white; /* Text color */
    padding: 10px 20px; /* Padding */
    text-align: center; /* Text alignment */
    text-decoration: none; /* No text decoration */
    display: inline-block; /* Display as block */
    font-size: 18px; /* Font size */
    font-weight: bold; /* Bold text */
    margin: 4px 2px; /* Margin */
    cursor: pointer; /* Cursor style */
    transition-duration: 0.4s; /* Transition duration for hover effect */
    width: 300px; /* Fixed width */
}
button:hover {
    background-color: #abedd8;
    color: black;
}

/* Your custom CSS styles for the radio buttons */
.widget-radio-box label {
  background: linear-gradient(to right, #0D47A1, #8E24AA); /* Gradient from #800080 to #2196f3 */
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: white;
  margin-bottom: 10px; /* Add margin between options */
  width: 70px; /* Set width */
}

.gradient-link {
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

.gradient-link:hover {
  background-image: linear-gradient(to right, #0D47A1, #8E24AA);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}

.custom-accordion {
    width: 380px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #222222, #222222) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}

.widget-container {
    border: none !important;
    background-color: #111111 !important; /* Background color changed */
    box-shadow: none !important;
    padding: 10px; /* Added padding */
    border-radius: 5px; /* Added border-radius */
}

.custom-accordion .custom-content {
    background-color: #111111 !important;
    padding: 5px;
}

.custom-image-container {
    background-color: #111111;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    margin: 0px;
    width: auto;
}
.custom-image {
    max-width: 100%;
    max-height: 100%;
    border-radius: 10px;
}
.custom-download-button {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    width: 100%;
    margin-top: 10px;
}
.image-slider {
    display: flex;
    overflow-x: auto;
    width: 100%;
    justify-content: center;
}

.widget-button {
    font-size: 16px !important;
    font-weight: bold !important;
}

.rounded-heading {
    background-color: #333333;
    color: white;
    padding: 5px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
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



from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))



# Define a function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #2196f3, #800080); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
    </div>    """
    display(HTML(logo_html))

# Display the gradient text logo
display_logo()

import ipywidgets as widgets
from IPython.display import display
import time

# Create a container widget
container = widgets.Box(layout=widgets.Layout(justify_content='center', align_items='center'))

# Define the messages
messages = [
    "Installation Successful",
    "ॐ नमः पार्वती पतये, हर-हर महादेव:",
    "Welcome to रूपांतरक ~ Rupantarak by Vishal Sharma",
    "If you like my work, so buy me a Coffee !!",
]

# Create a label widget for the message
message_label = widgets.HTML(
    value=f"<b>{messages[0]}</b>",
    layout=widgets.Layout(font_size='24px', text_align='center')
)

# Add the message label to the container
container.children = [message_label]

# Display the container
display(container)

# Loop through the messages and display them with a delay
for message in messages[1:]:
    time.sleep(3)
    message_label.value = f"<b>{message}</b>"

# Hide the message after 5 seconds
time.sleep(5)

# Clear the container
container.close()
from IPython.display import HTML, display

# Note 1
html_content_1 = '''
<div style="display: flex; justify-content: center; margin-top: 10px; margin-bottom: 10px;">
  <div style="width: 400px; margin: 10px 0;">
    <details id="details1">
      <summary id="summary1" style="border: none; border-radius: 8px; background: linear-gradient(45deg, #222222, #222222); color: white; padding: 3px; text-align: center; cursor: pointer; list-style: none; font-weight: bold; margin-bottom: 10px;">
        <span id="arrow1">➼</span> <b>Tool Information</b>
      </summary>
      <div style="border-radius: 8px; background-color: #222222; padding: 7px; color: white;">
        <b>रूपांतरक ~ Rupantarak</b> is an advanced tool developed by Vishal Sharma designed for creating realistic face swaps in both videos and images. Leveraging cutting-edge machine learning algorithms, this tool allows users to transform their media with high precision and quality.
               <div style="background: linear-gradient(45deg, #8B0000, #5A0000); border-radius: 5px; padding: 10px;">
                <p style="color: white; font-weight: bold;">Ensuring ethical content creation is our priority. That's why our deepfake tool includes a sensitive content filter.</p>
            </div>
        <b>Key Features:</b>
        <ul>
          <li><b>Face Fetching:</b> Automatically detect and fetch faces from uploaded videos or images for transformation.</li>
          <li><b>Private Google Drive Upload:</b> Ensures that processed files are accessible only by the user's account, maintaining privacy and security.</li>
          <li><b>Public Link Download:</b> Allows users to download target videos using public Google Drive shared links.</li>
        </ul>

        <b>How to Use:</b>
        <ol>
          <li><b>Enter Google Drive Shared Link:</b> Provide the shared link of the video or image from your Google Drive that you want to process.</li>
          <li><b>Select Output Format:</b> Choose whether you want the output as an Image or a Video.</li>
          <li><b>Start Upload:</b> Once the file is selected, the upload process starts automatically.</li>
          <li><b>Configure Settings:</b> Adjust the settings according to your preferences:
            <ul>
              <li><b>Many Faces:</b> Decide if you want to process multiple faces in the media (Yes/No).</li>
              <li><b>Execution Provider:</b> Select the processing unit (CPU or CUDA for GPU acceleration).</li>
              <li><b>Reference Face Position:</b> Indicate the position of the reference face you want to use for transformation (1-10).</li>
              <li><b>Reference Frame Number:</b> Specify the frame number to use as the reference (1-10).</li>
              <li><b>Similar Face Distance:</b> Set the threshold for face similarity, ranging from 0.01 to 1.00. Lower values mean higher similarity.</li>
              <li><b>Maximum Memory:</b> Allocate the maximum memory to be used for processing, ranging from 2GB to 10GB.</li>
              <li><b>Output Video Quality:</b> Adjust the quality of the output video. Set a value between 1 and 100, where 1 is the best quality and 100 is the worst.</li>
            </ul>
          </li>
          <li><b>Run रूपांतरक ~ Rupantarak:</b> Execute the tool with your configured settings to generate the processed file.</li>
        </ol>

        <b>Detailed Settings Explanation:</b>
        <ul>
          <li><b>Many Faces:</b> If enabled, the tool will attempt to detect and transform multiple faces within the media. This is useful for group photos or videos with more than one person.</li>
          <li><b>Execution Provider:</b> You can choose between CPU (standard processing) and CUDA (GPU acceleration) depending on your hardware capabilities. CUDA can significantly speed up the processing time if you have a compatible GPU.</li>
          <li><b>Reference Face Position:</b> This setting allows you to specify which face in the sequence should be used as the reference for swapping. This is useful when there are multiple faces and you want to focus on a specific one.</li>
          <li><b>Reference Frame Number:</b> Select a specific frame from the video to be used as a reference point for the face swap. This helps in achieving more accurate transformations.</li>
          <li><b>Similar Face Distance:</b> This is a similarity threshold that determines how closely the faces need to match for a swap to occur. A lower value means higher similarity, which is useful for ensuring precise matches.</li>
          <li><b>Maximum Memory:</b> Allocate the amount of memory you want the tool to use. Higher memory allocation can improve performance but depends on your system’s capabilities.</li>
          <li><b>Output Video Quality:</b> Adjust the quality of the final output. A setting of 1 provides the best quality while 100 offers the lowest quality, which might be useful for reducing file size or faster processing times.</li>
        </ul>

        By utilizing रूपांतरक ~ Rupantarak, you can seamlessly create high-quality face swaps, making it an ideal tool for content creators, filmmakers, and anyone interested in digital transformations.
      </div>
    </details>
  </div>
</div>
<script>
  var details1 = document.getElementById('details1');
  var arrow1 = document.getElementById('arrow1');
  details1.addEventListener('toggle', function(event) {
    if (details1.open) {
      arrow1.textContent = '➷';
    } else {
      arrow1.textContent = '➼';
    }
  });
</script>
'''

display(HTML(html_content_1))






from IPython.display import HTML, display

# YouTube video ID
video_id = 'jDCPmySzePw'

# YouTube video URL with required parameters
youtube_url = f'https://www.youtube.com/embed/{video_id}?controls=0&autoplay=1&loop=1&mute=1&playlist={video_id}'

# HTML for the collapsible section with styled button and video container
html_code = f"""
<div style="text-align: center; margin-bottom: 10px;">
  <button style="
      font-weight: bold;
      width: 400px;
      height: 50px;
      border-radius: 15px;
      background: linear-gradient(to right, #FFA500, #FF0000);
      color: white;
      border: none;
      cursor: pointer;
  " type="button" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display=='none'?'block':'none';">
    रूपांतरक ~ Rupantarak ○ Tutorial
  </button>
  <div style="display:none; margin-top: 10px;">
    <div style="
        display: inline-block;
        background-color: #222222;
        border-radius: 15px;
        padding: 10px;
    ">
      <iframe style="
          border-radius: 15px;
      " width="380" height="852" src="{youtube_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
</div>
"""

# Display the HTML
display(HTML(html_code))


import ipywidgets as widgets
from google.colab import auth
from googleapiclient.discovery import build
from IPython.display import display, HTML, clear_output




html_content = '''
<style>
  .divider {
    width: 400px;
    height: 3px;
    background-color: #222222;
    margin: 20px auto 10px auto;
  }
  .heading-container {
    text-align: center;
    border-radius: 10px;
    background-color: #222222;
    padding: 3px;
    margin: 0 auto 20px auto;
    width: 400px;
  }
  .heading {
    font-weight: bold;
    margin: 0;
  }
  .step-heading {
    border-radius: 10px;
    background-color: #222222;
    width: 100px;
    margin: 10px auto;
    text-align: center;
    height: 20px;
  }
</style>
<div class="divider" style="margin-bottom: 10px;"></div>

<div class="step-heading">
  <h4>Step ~ 1</h4>
</div>
'''

display(HTML(html_content))




import ipywidgets as widgets
from google.colab import auth
from googleapiclient.discovery import build
from IPython.display import display, HTML, clear_output

# Function to authenticate and authorize Google Drive access
def authenticate_drive(b):
    with output_auth:
        clear_output()  # Clear previous output
        auth.authenticate_user()  # Perform authentication
        global drive_service
        drive_service = build('drive', 'v3')  # Build Drive service
        update_status()  # Update status after authentication

# Function to update LED indicator
def update_indicator(status):
    if status:
        return '<font size="3" color="green">&#9679;</font>'  # Green
    else:
        return '<font size="3" color="red">&#9679;</font>'  # Red

# Function to update status indicator
def update_status():
    if 'drive_service' in globals():
        status_indicator.value = update_indicator(True)  # Change status to green
        status_text.value = "Status: Authenticated"
    else:
        status_indicator.value = update_indicator(False)  # Change status to red
        status_text.value = "Status: Not Authenticated"

# Set width for the widgets
widget_width = '350px'

# Custom CSS for button styling
custom_css = """
<style>
.auth-button, .note-button {
    background: linear-gradient(to right, #0D47A1, #8E24AA); /* Default gradient */
    border-radius: 20px; /* Rounded corners */
    border: none; /* No border */
    color: white; /* Text color */
    padding: 10px 20px; /* Padding */
    text-align: center; /* Text alignment */
    text-decoration: none; /* No text decoration */
    display: inline-block; /* Display as block */
    font-size: 18px; /* Font size */
    font-weight: bold; /* Bold text */
    margin: 4px 2px; /* Margin */
    cursor: pointer; /* Cursor style */
    transition-duration: 0.4s; /* Transition duration for hover effect */
}

.auth-button {
    background: linear-gradient(to right, #0D47A1, #8E24AA); /* Dark blue to purple gradient */
    width: 330px; /* Fixed width for authentication button */
}

.note-button {
    background: linear-gradient(to right, #222222, #222222); /* Green to yellow gradient */
    width: 350px; /* Fixed width for note button */
}

.collapsible-content {
    background-color: #f0f0f0;
    border-radius: 10px;
    padding: 10px;
}
</style>
"""

# HTML for custom CSS
custom_css_html = HTML(custom_css)
display(custom_css_html)

# Create button for authentication with custom CSS class
auth_button = widgets.Button(description="Authenticate Gdrive", layout=widgets.Layout(height='55px'))
auth_button.add_class("auth-button")  # Apply custom CSS class
auth_button.on_click(authenticate_drive)

# Output widget for displaying status
output_auth = widgets.Output(layout=widgets.Layout(width=widget_width, margin='10px 0'))

# HTML widget for displaying LED indicator
status_indicator = widgets.HTML(layout=widgets.Layout(width='20px', height='20px', margin='10px 0'))  # Increase size for better visibility

# Text widget for displaying status message
status_text = widgets.HTML(value="Status: Not Authenticated", layout=widgets.Layout(width='200px', margin='10px 0'))  # Adjust width as needed

# Update indicator initially
update_status()

# Create a collapsible note using widgets
collapsible_button = widgets.Button(description="Gdrive Authentication ~ Hide & Show", layout=widgets.Layout(width='350px', height='50px'))
collapsible_button.add_class("note-button")  # Apply custom CSS class

# Arrange status text and LED indicator in an HBox with proper alignment
status_box = widgets.HBox([status_text, status_indicator], layout=widgets.Layout(justify_content='space-between', align_items='center', width='330px', margin='10px 0'))
collapsible_content = widgets.VBox([auth_button, status_box, output_auth], layout=widgets.Layout(align_items='center', width=widget_width, margin='10px 0'))

# Initially show content
collapsible_content.layout.display = 'flex'

# Define the toggle function
def toggle_content(b):
    if collapsible_content.layout.display == 'none':
        collapsible_content.layout.display = 'flex'
    else:
        collapsible_content.layout.display = 'none'

# Assign the toggle function to the button click event
collapsible_button.on_click(toggle_content)

# Display the collapsible note
display(widgets.VBox([collapsible_button, collapsible_content], layout=widgets.Layout(align_items='center')))


html_content = '''
<style>
  .divider {
    width: 400px;
    height: 3px;
    background-color: #222222;
    margin: 20px auto 10px auto;
  }
  .heading-container {
    text-align: center;
    border-radius: 10px;
    background-color: #222222;
    padding: 3px;
    margin: 0 auto 20px auto;
    width: 400px;
  }
  .heading {
    font-weight: bold;
    margin: 0;
  }
  .step-heading {
    border-radius: 10px;
    background-color: #222222;
    width: 100px;
    margin: 10px auto;
    text-align: center;
    height: 20px;
  }
</style>
<div class="divider" style="margin-bottom: 10px;"></div>

<div class="step-heading">
  <h4>Step ~ 2</h4>
</div>
'''

display(HTML(html_content))




from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))


def file_upload_handler(change):
    uploaded_files_left = file_upload_left.value
    uploaded_files_right = file_upload_right.value
    uploaded_files = {**uploaded_files_left, **uploaded_files_right}
    total_files = len(uploaded_files)
    with output:
        output.clear_output()
        progress_bar_upload.max = total_files
        for i, (filename, file_info) in enumerate(uploaded_files.items(), 1):
            new_filename = 'Rupantarak_T.mp4' if filename.lower().endswith('.mp4') else 'Rupantarak_S.jpg' if filename.lower().endswith(('.png', '.jpg')) else None
            if new_filename:
                with open('/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/' + new_filename, 'wb') as f:
                    f.write(file_info['content'])
                    progress_bar_upload.value = i
        print("Upload success!")
    refresh_file_indicators()

def start_download(button):
    try:
        given_link = link_field.value.strip()

        if given_link == "":
            print("Please enter a link.")
            return
        output.clear_output()
        simulate_progress_download()
        download_file(given_link)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        with output:
            output.clear_output()

def simulate_progress_download():
    max_value = 100
    for i in range(max_value + 1):
        progress_bar_download.value = i
        overall_progress_download.value = f"<b>Progress:</b> {i}%"
        time.sleep(0.1)

def download_file(given_link):
    try:
        generated_link = generate_direct_link(given_link)
        if generated_link:
            file_format = file_format_radio.value
            if file_format == "Image":
                file_extension = "jpg"
                file_prefix = "S"
            elif file_format == "Video":
                file_extension = "mp4"
                file_prefix = "T"
            save_dir = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/"
            os.makedirs(save_dir, exist_ok=True)
            file_name = f"Rupantarak_{file_prefix}.{file_extension}"
            gdown.download(generated_link, os.path.join(save_dir, file_name), quiet=True)
            if isinstance(generated_link, widgets.Button):
                return
            with download_success_output:
                print("Download completed successfully!")
        else:
            print("Invalid Google Drive Shared Link. Please try again.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        with output:
            output.clear_output()

def extract_file_id(link):
    match = re.search(r"/file/d/([^/]+)", link)
    if match:
        return match.group(1)
    else:
        return None

def generate_direct_link(link):
    file_id = extract_file_id(link)
    if file_id:
        return f"https://drive.google.com/uc?id={file_id}"
    else:
        return None

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0 MB"
    size_mb = size_bytes / (1024 * 1024)
    return f"{size_mb:.2f} MB"

def file_indicator(file_path, file_label):
    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        status = f"<font color='green'>●</font>"
        size_text = f"<i>Size: {convert_size(file_size)}</i>"
    else:
        status = "<font color='red'>●</font>"
        size_text = "<i>File not found</i>"

    status_widget = widgets.HTML(status, layout=widgets.Layout(align_items='center', width='auto'))
    label_widget = widgets.HTML(f"<b>{file_label}</b>", layout=widgets.Layout(align_items='center', width='auto'))
    size_widget = widgets.HTML(size_text, layout=widgets.Layout(align_items='center', width='auto'))

    hbox = widgets.HBox([label_widget, status_widget, size_widget], layout=widgets.Layout(justify_content='flex-start', align_items='center'))

    return hbox

def refresh_file_indicators():
    file_indicators.children = (file_indicator("/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_S.jpg", "Image"),
                                 file_indicator("/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_T.mp4", "Video"))

def clear_all_fields():
    link_field.value = ""
    progress_bar_download.value = 0
    overall_progress_download.value = "<b>Progress:</b> 0%"
    progress_bar_upload.value = 0
    file_upload_left.value.clear()
    file_upload_right.value.clear()
    output.clear_output()

def refresh_indicators(button):
    clear_all_fields()
    refresh_file_indicators()
    with output:
        output.clear_output()
    with download_success_output:
        download_success_output.clear_output()
    file_upload_left._counter = 0
    file_upload_right._counter = 0
    clear_all_fields()
    refresh_file_indicators()

container_width = '350px'
upload_box_width = '135px'
upload_box_height = '60px'

link_field = widgets.Text(placeholder='Enter Google Drive Shared Link', layout=widgets.Layout(width=container_width, height='auto'))
link_field.add_class("gradient-link")

download_button = widgets.Button(description="Start Download",
                                 layout=widgets.Layout(width=container_width, height='55px', margin='10px 0',
                                                      background_color='blue',
                                                      color='white'))

file_format_radio = widgets.RadioButtons(options=["Image", "Video"], description="Save as:", layout=widgets.Layout(width=container_width, height='55px'))
progress_bar_download = widgets.FloatProgress(value=0, min=0, max=100, style={'bar_color': 'teal', 'description_width': 'initial'}, layout=widgets.Layout(width=container_width, height='20px'))
overall_progress_download = widgets.HTML(value="<b>Progress:</b> 0%", layout=widgets.Layout(width=container_width, height='55px'))
file_upload_left = widgets.FileUpload(accept='.png, .jpg', multiple=True, description='Image:', layout=widgets.Layout(width=upload_box_width, height=upload_box_height, margin='0 10px'))
file_upload_right = widgets.FileUpload(accept='.mp4', multiple=True, description='Video:', layout=widgets.Layout(width=upload_box_width, height=upload_box_height, margin='0 10px'))
progress_bar_upload = widgets.FloatProgress(value=0, min=0, max=1, description='Progress :', layout={'width': container_width, 'height': '20px'})
output = widgets.Output(layout={'width': container_width})
download_success_output = widgets.Output(layout={'width': container_width})
refresh_button = widgets.Button(description='Refresh Files Status', layout=widgets.Layout(width=container_width, height='55px', margin='10px 0'))

auto_upload_label = widgets.HTML(
    "<b>Uploading Starts Automatically When You Select File</b>",
    layout=widgets.Layout(margin='10px 0 0 0')
)

centered_label = widgets.HBox([auto_upload_label], layout=widgets.Layout(justify_content='center'))

file_upload_left.observe(file_upload_handler, names='value')
file_upload_right.observe(file_upload_handler, names='value')
download_button.on_click(start_download)
refresh_button.on_click(refresh_indicators)

upload_widgets = widgets.VBox([
    widgets.HBox([file_upload_left, file_upload_right], layout=widgets.Layout(justify_content='center')),
    auto_upload_label,
    progress_bar_upload,
    output
])

file_indicators = widgets.HBox([
    file_indicator("/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_S.jpg", "Image"),
    file_indicator("/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_T.mp4", "Video")
])

download_widgets = widgets.VBox([
    link_field,
    file_format_radio,
    download_button,
    progress_bar_download,
    overall_progress_download
])

centered_container = widgets.VBox([
    download_widgets,
    upload_widgets,
    refresh_button,
    file_indicators,
    download_success_output
], layout=widgets.Layout(width='auto', align_items='center'))

# Collapsible button
collapsible_button = widgets.Button(description="Upload Source Face & Target Video ~ Hide",
                                    layout=widgets.Layout(width='400px', height='50px', margin='10px auto'))
collapsible_button.add_class("note-button")  # Apply custom CSS class

def toggle_interface(button):
    if centered_container.layout.visibility == 'hidden':
        centered_container.layout.visibility = 'visible'
        centered_container.layout.height = 'auto'  # Adjust height to prevent blank space
        button.description = "Upload Source Face & Target Video ~ Hide"
    else:
        centered_container.layout.visibility = 'hidden'
        centered_container.layout.height = '0'  # Set height to 0 when hidden
        button.description = "Upload Source Face & Target Video ~ Show"

collapsible_button.on_click(toggle_interface)

display(widgets.VBox([collapsible_button, centered_container]))

html_content = '''
<style>
  .divider {
    width: 400px;
    height: 3px;
    background-color: #222222;
    margin: 20px auto 10px auto;
  }
  .heading-container {
    text-align: center;
    border-radius: 10px;
    background-color: #222222;
    padding: 3px;
    margin: 0 auto 20px auto;
    width: 400px;
  }
  .heading {
    font-weight: bold;
    margin: 0;
  }
  .step-heading {
    border-radius: 10px;
    background-color: #222222;
    width: 100px;
    margin: 10px auto;
    text-align: center;
    height: 20px;
  }
</style>
<div class="divider" style="margin-bottom: 10px;"></div>

<div class="step-heading">
  <h4>Step ~ 3</h4>
</div>
'''

display(HTML(html_content))



import cv2
import numpy as np
import base64
from IPython.display import display, HTML
from ipywidgets import widgets, VBox, HBox

def fetch_and_show_face(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("No faces detected.")
        return ""

    # Define the border color
    border_color = (17, 17, 17)  # RGB for #111111
    background_color = (17, 17, 17)  # RGB for #111111

    # Process the first detected face only
    (x, y, w, h) = faces[0]

    # Increase the width and height by 70%
    new_w = int(w * 1.7)
    new_h = int(h * 1.7)

    # Calculate the new coordinates, ensuring they stay within image bounds
    new_x = max(0, x - (new_w - w) // 2)
    new_y = max(0, y - (new_h - h) // 2)
    new_w = min(new_w, image.shape[1] - new_x)
    new_h = min(new_h, image.shape[0] - new_y)

    # Crop the face region from the image
    cropped_face = image[new_y:new_y+new_h, new_x:new_x+new_w]

    # Resize the cropped face to fit within a 40px radius circle
    diameter = 2 * 40  # Diameter of the circle
    resized_face = cv2.resize(cropped_face, (diameter, diameter))

    # Create a circular mask for the resized face
    mask = np.zeros((diameter, diameter), dtype=np.uint8)
    cv2.circle(mask, (40, 40), 40, 255, -1)

    # Create a colored background for the mask
    background = np.full((diameter, diameter, 3), background_color, dtype=np.uint8)

    # Apply the circular mask to the resized face
    masked_face = cv2.bitwise_and(resized_face, resized_face, mask=mask)
    inverted_mask = cv2.bitwise_not(mask)
    masked_background = cv2.bitwise_and(background, background, mask=inverted_mask)
    final_face = cv2.add(masked_face, masked_background)

    # Add a 10px rounded border around the circular face
    border_size = 10
    bordered_face = cv2.copyMakeBorder(final_face, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)

    # Create a rounded rectangle mask for the border
    mask_with_border = np.zeros((diameter + 2*border_size, diameter + 2*border_size), dtype=np.uint8)
    cv2.circle(mask_with_border, (40 + border_size, 40 + border_size), 40 + border_size, 255, -1)

    # Apply the rounded border mask
    rounded_bordered_face = cv2.bitwise_and(bordered_face, bordered_face, mask=mask_with_border)

    # Create a final image with the face centered
    final_image = np.full((diameter + 2*border_size, diameter + 2*border_size, 3), background_color, dtype=np.uint8)
    center_x, center_y = (final_image.shape[1] // 2, final_image.shape[0] // 2)
    final_image[center_y - 50:center_y + 50, center_x - 50:center_x + 50] = rounded_bordered_face

    # Encode the final image as base64
    _, buffer = cv2.imencode('.jpg', final_image)
    encoded_image = base64.b64encode(buffer)

    # Display the image without heading
    image_html = """
    <div id="face_preview" style='text-align: center;'>
        <img src='data:image/jpeg;base64,{}' style='border-radius: 50%; border: 4px solid #111111;'>
    </div>
    """.format(encoded_image.decode())

    return image_html

# Display the initial face image
image_html = fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_S.jpg")
image_output = widgets.HTML(value=image_html)

# Define the refresh button
button = widgets.Button(description="Refresh Face")

def refresh_face(btn):
    image_output.value = fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_S.jpg")

button.on_click(refresh_face)

# Create a VBox to contain the button and the image output with a 10px margin
collapsible_content_face = VBox([image_output, button], layout=widgets.Layout(align_items='center', margin='10px 0'))

# Create a collapsible button for the face image
collapsible_button_face = widgets.Button(description="Face Confirmation ~ Hide & Show", layout=widgets.Layout(width='auto', height='50px'))
collapsible_button_face.add_class("note-button")  # Apply custom CSS class

# Initially show content
collapsible_content_face.layout.display = 'flex'

# Define the toggle function for the face image section
def toggle_content_face(b):
    if collapsible_content_face.layout.display == 'none':
        collapsible_content_face.layout.display = 'flex'
    else:
        collapsible_content_face.layout.display = 'none'

# Assign the toggle function to the button click event for the face image section
collapsible_button_face.on_click(toggle_content_face)

# Display the toggle button for the face image section
display(HBox([collapsible_button_face], layout=widgets.Layout(justify_content='center')))

# Display the collapsible content for the face image section
display(collapsible_content_face)







from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))







import os
import base64
import contextlib
from moviepy.editor import VideoFileClip
from ipywidgets import Button, HTML, VBox, Layout, HBox
from IPython.display import display, clear_output

def load_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            image_html = f'''
            <div style="background-color: #222222; border-radius: 5px; padding: 10px; text-align: center;">
                <img src="data:image/png;base64,{image_base64}" style="max-width: 360px; height: auto; border-radius: 5px;" />
            </div>
            '''
            return image_html
    except Exception as e:
        print(f"Error displaying image: {e}")
        return None

def process_video(video_path):
    try:
        # Load video
        clip = VideoFileClip(video_path)

        # Check video duration
        duration = clip.duration

        if duration > 10:
            # Trim the first 10 seconds
            trimmed_clip = clip.subclip(0, 10)
        else:
            # Use the full video
            trimmed_clip = clip

        # Define output path
        output_path = "/content/processed_video.mp4"

        # Write trimmed video
        with open(os.devnull, "w") as f, contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
            trimmed_clip.write_videofile(output_path, codec='libx264', verbose=False)

        # Display the processed video using base64 encoding
        with open(output_path, "rb") as video_file:
            video_base64 = base64.b64encode(video_file.read()).decode('utf-8')
            video_html = f'''
            <div style="background-color: #222222; border-radius: 5px; padding: 10px; text-align: center;">
                <video width="360" height="auto" autoplay style="border-radius: 5px;">
                    <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>
            '''
            return video_html

    except Exception as e:
        print(f"Error processing video: {e}")
        return None

def fetch_files_from_path(directory_path):
    try:
        files = os.listdir(directory_path)
        image_files = [f for f in files if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
        video_files = [f for f in files if f.lower().endswith(('mp4', 'mov', 'avi', 'mkv'))]

        notes_html = ""

        summary_style = "cursor: pointer; background-color: #222222; color: white; border: none; border-radius: 5px; padding: 5px 10px; text-align: center; height: 40px; line-height: 40px;"

        # Load and display images
        for image_file in image_files:
            image_path = os.path.join(directory_path, image_file)
            image_html = load_image(image_path)
            notes_html += f'''
            <div style="margin: 10px 0;">
                <details style="width: 400px; margin: 0 auto;" open>
                    <summary style="{summary_style}">Selected Source Image</summary>
                    {image_html}
                </details>
            </div>
            '''

        # Load, process, and display videos
        for video_file in video_files:
            video_path = os.path.join(directory_path, video_file)
            video_html = process_video(video_path)
            notes_html += f'''
            <div style="margin: 10px 0;">
                <details style="width: 400px; margin: 0 auto;" open>
                    <summary style="{summary_style}">Selected Target Video</summary>
                    {video_html}
                </details>
            </div>
            '''

        return notes_html

    except Exception as e:
        print(f"Error fetching files: {e}")
        return None

# Define the directory path
directory_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/"

# Create HTML output widget for notes
notes_output = HTML()

# Function to fetch and display files from the directory path
def refresh_notes(button):
    if button is not None:
        clear_output(wait=True)
        # Fetch and display the files from the directory path
        notes_html = fetch_files_from_path(directory_path)
        if notes_html:
            notes_output.value = notes_html

# Function to refresh the HTML notes
def refresh(button):
    refresh_notes(button)

# Create Refresh button
refresh_button = Button(description="Refresh Preview",
                        layout=Layout(width='330px', height='40px', margin='10px auto', justify_content='center', align_items='center'))
# Initially show the HTML notes and the Refresh button
notes_output.layout.display = 'flex'
refresh_button.layout.display = 'flex'

# Define a function to toggle the display of HTML notes and the Refresh button
def toggle_interface(button):
    if notes_output.layout.display == 'none':
        notes_output.layout.display = 'flex'
        refresh_button.layout.display = 'flex'
    else:
        notes_output.layout.display = 'none'
        refresh_button.layout.display = 'none'

# Create Toggle Interface button
toggle_interface_button = Button(description="Uploaded Files Preview ~ Hide & Show", layout=Layout(width='auto', height='50px', margin='10px auto'))
toggle_interface_button.style.button_width = 'auto'
toggle_interface_button.on_click(toggle_interface)
toggle_interface_button.add_class("note-button")  # Apply custom CSS class

# Assign the refresh function to the click event of the Refresh button
refresh_button.on_click(refresh)

# Create VBox to contain the buttons and HTML notes
interface_content = VBox([toggle_interface_button, notes_output, refresh_button],
                         layout=Layout(align_items='center', margin='10px 0'))

# Display the interface content
display(interface_content)

html_content = '''
<style>
  .divider {
    width: 400px;
    height: 3px;
    background-color: #222222;
    margin: 20px auto 10px auto;
  }
  .heading-container {
    text-align: center;
    border-radius: 10px;
    background-color: #222222;
    padding: 3px;
    margin: 0 auto 20px auto;
    width: 400px;
  }
  .heading {
    font-weight: bold;
    margin: 0;
  }
  .step-heading {
    border-radius: 10px;
    background-color: #222222;
    width: 100px;
    margin: 10px auto;
    text-align: center;
    height: 20px;
  }
</style>
<div class="divider" style="margin-bottom: 10px;"></div>

<div class="step-heading">
  <h4>Step ~ 4</h4>
</div>

'''

display(HTML(html_content))
from IPython.display import clear_output

# Define optional_commands list
optional_commands = []

# Function to convert seconds to time format
def convert_seconds_to_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours} H, {minutes} M, {seconds} S"

# Function to start the deepfake process
def start_deepfake_process(image_path, video_path, output_path, quality):
    try:
        print("Starting रूपांतरक ~ Rupantarak")
        completed_steps = {"Extracted frames": False, "Source image captured": False}
        start_time = time.time()

        total_frames = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=nb_frames', '-of', 'default=noprint_wrappers=1:nokey=1', video_path]).decode('utf-8').strip()
        total_frames_label.value = f'Total frames: {total_frames}'

        process = subprocess.Popen([
            'python', '/content/Rupantarak/run.py',
            '-s', image_path,
            '-t', video_path,
            '-o', output_path,
            '--keep-frames',
            '--keep-fps',
            *(optional_commands),
            '--temp-frame-quality', '1',
            '--output-video-quality', str(output_video_quality_slider.value),
            '--execution-provider', execution_provider_radio.value,
            '--frame-processor', 'face_swapper', 'face_enhancer'
        ], stderr=subprocess.PIPE, universal_newlines=True)

        progress_pattern = re.compile(r'(\d+)%')
        progress_label.value = "Progress: 0%"

        time_remaining_pattern = re.compile(r'\[(\d+:\d+)\<(\d+:\d+),')
        time_remaining_label.value = "Time remaining: --"

        for line in process.stderr:
            match_progress = progress_pattern.search(line)
            match_time_remaining = time_remaining_pattern.search(line)
            if match_progress:
                progress_percentage = int(match_progress.group(1))
                progress_bar.value = progress_percentage / 100
                progress_label.value = f"Progress: {progress_percentage}%"
                if progress_percentage == 100:
                    if not completed_steps["Extracted frames"]:
                        print("Extracted Frames")
                        completed_steps["Extracted frames"] = True
                    elif not completed_steps["Source image captured"]:
                        print("Capturing Image & Swapping faces")
                        completed_steps["Source image captured"] = True
            if match_time_remaining:
                time_remaining = match_time_remaining.group(2)
                time_remaining_label.value = f"Time remaining: {time_remaining}"

        process.wait()

        end_time = time.time()
        total_time_seconds = end_time - start_time
        total_time_str = convert_seconds_to_time(total_time_seconds)
        print(f"Total time taken: {total_time_str}")

        try:
            output_size = subprocess.check_output(['du', '-h', output_path]).split()[0].decode('utf-8')
            print(f"Output file size: {output_size}")
        except subprocess.CalledProcessError:
            print("18+ Content Not Allowed")

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to trim and display video
def trim_and_display_video(input_file):
    display_width = '400px'

    clip = VideoFileClip(input_file)
    total_duration = clip.duration
    start_time = (total_duration - 10) / 2
    end_time = start_time + 10
    center_trim_clip = clip.subclip(start_time, end_time)

    with open(os.devnull, "w") as f, contextlib.redirect_stdout(f), contextlib.redirect_stderr(f):
        center_trim_clip.write_videofile("/content/Rupantarak/Rupantarak_Pro/Rupantarak_M/trimmed_video.mp4", codec="libx264", verbose=False)

    button = widgets.Button(description="Video Preview", button_style='', layout=widgets.Layout(width=display_width))
    button.style.font_weight = 'bold'

    video_output = widgets.Output(layout=widgets.Layout(display='none', width=display_width), id='video-container')

    def toggle_video_visibility(button):
        if video_output.layout.display == 'none':
            video_output.layout.display = 'block'
        else:
            video_output.layout.display = 'none'

    button.on_click(toggle_video_visibility)

    display(button)
    display(video_output)

    with video_output:
        video_widget = widgets.Video.from_file("/content/Rupantarak/Rupantarak_Pro/Rupantarak_M/trimmed_video.mp4")
        video_widget.layout.width = display_width
        video_widget.layout.height = '240px'
        video_widget.autoplay = True
        video_widget.loop = True
        video_widget.controls = False
        display(video_widget)

# Function to upload video to Google Drive
def upload_video_to_drive(video_file_path, file_name):
    display_width = '400px'

    auth.authenticate_user()
    drive_service = build('drive', 'v3')

    response = drive_service.files().list(q=f"name='{file_name}'", spaces='drive', fields='files(id)').execute()
    existing_files = response.get('files', [])
    if existing_files:
        for file in existing_files:
            drive_service.files().delete(fileId=file['id']).execute()

    file_metadata = {'name': file_name}
    media = MediaFileUpload(video_file_path, mimetype='video/mp4')
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = uploaded_file.get('id')
    file_link = f'https://drive.google.com/uc?id={file_id}&export=download'

    button_html = f'''
    <div style="text-align: center;">
        <button onclick="window.open('{file_link}')" style="background: linear-gradient(135deg, #8E24AA, #0D47A1); color: white; padding: 10px 20px; border: none; border-radius: 15px; cursor: pointer; font-size: 16px; font-weight: bold; text-align: center; text-decoration: none; width: {display_width};">Download Video</button>
    </div>
    '''

    display(HTML(button_html))

# Post process functions
def post_process_function_1(output_file):
    print("Displaying Video Preview...")
    trim_and_display_video(output_file)

def post_process_function_2(output_file):
    print("Uploading to Google Drive...")
    upload_video_to_drive(output_file, "Rupantarak_O_By_Vishal_Sharma.mp4")

# Function to run the deepfake process and subsequent functions
def run_deepfake_process(button):
    output_file = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_O/Rupantarak_O.mp4"
    clear_deepfake_prints()
    delete_existing_file(output_file)
    start_deepfake_process('/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_S.jpg', '/content/Rupantarak/Rupantarak_Pro/Rupantarak_U/Rupantarak_T.mp4', output_file, output_video_quality_slider.value)
    display_note_once()
    print("रूपांतरक ~ Rupantarak process completed.")
    post_process_function_1(output_file)
    post_process_function_2(output_file)

# Function to clear deepfake process prints without affecting other outputs
def clear_deepfake_prints():
    output_container.clear_output(wait=True)

# Function to delete existing file
def delete_existing_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted existing file: {file_path}")


from IPython.display import HTML, display

note_displayed = False

def display_note_once():
    global note_displayed
    if not note_displayed:
        # Note content
        note_content = """
        <div id="note_content" style="display: block; background: #222222; border-radius: 5px; padding: 10px; text-align: center; width: 380px; margin: 0 auto;">
            <div style="background: linear-gradient(45deg, #8B0000, #5A0000); border-radius: 5px; padding: 10px;">
                <p style="color: white; font-weight: bold;">Ensuring ethical content creation is our priority. That's why our deepfake tool includes a sensitive content filter.</p>
            </div>
"""

        # Display the demo note button and content with margin
        display(HTML('<div style="text-align: center; margin-bottom: 10px;"><button onclick="if(document.getElementById(\'note_content\').style.display === \'block\') {document.getElementById(\'note_content\').style.display = \'none\';} else {document.getElementById(\'note_content\').style.display = \'block\'}" style="width: 400px; background: #222222; border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">Things To Know</button></div>'))
        display(HTML(note_content))

        note_displayed = True



# Create widgets for displaying progress
total_frames_label = widgets.Label(value='', layout=widgets.Layout(font_weight='bold', width='300px', text_align='center'))
progress_label = widgets.Label(value='', layout=widgets.Layout(font_weight='bold', width='400px', text_align='center'))
progress_bar = widgets.FloatProgress(value=0.0, min=0.0, max=1.0, step=0.01, layout=widgets.Layout(width='300px', margin='25px auto'))
time_remaining_label = widgets.Label(value='', layout=widgets.Layout(font_weight='bold', width='300px', text_align='center'))



# Button to start the deepfake process with custom style
run_button = widgets.Button(
    description="Start Rupantarak",
    button_style='success',
    layout=widgets.Layout(width='400px', height='55px', margin='25px auto'),
    style={'font_weight': 'bold', 'color': 'white', 'background': 'linear-gradient(135deg, #667eea, #764ba2)', 'font_size': '55px'}
)
# Output container for deepfake process
output_container = widgets.Output(layout=widgets.Layout(width='400px', margin='25px auto'))

# Global variable to track if the note has been displayed
note_displayed = False



# Create radio buttons for "Many Faces" and "Execution Provider" with headings
many_faces_heading = widgets.HTML(value="<h4 class='rounded-heading'>Many Faces</h4>")
execution_provider_heading = widgets.HTML(value="<h4 class='rounded-heading'>Execution Provider</h4>")
many_faces_radio = widgets.RadioButtons(
    options=['Yes', 'No'],
    description='',
    disabled=False
)
execution_provider_radio = widgets.RadioButtons(
    options=['cpu', 'cuda'],
    description='',
    disabled=False
)

# Create sliders for additional options with headings
reference_face_position_heading = widgets.HTML(value="<h4 class='rounded-heading'>Reference Face Position (1-10)</h4>")
reference_face_position_slider = widgets.IntSlider(
    value=1,
    min=1,
    max=10,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    layout=widgets.Layout(width='100%')
)

reference_frame_number_heading = widgets.HTML(value="<h4 class='rounded-heading'>Reference Frame Number (1-10)</h4>")
reference_frame_number_slider = widgets.IntSlider(
    value=1,
    min=1,
    max=10,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    layout=widgets.Layout(width='100%')
)

similar_face_distance_heading = widgets.HTML(value="<h4 class='rounded-heading'>Similar Face Distance (0.01-1.00)</h4>")
similar_face_distance_slider = widgets.FloatSlider(
    value=0.85,
    min=0.01,
    max=1.00,
    step=0.01,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    layout=widgets.Layout(width='100%')
)

max_memory_heading = widgets.HTML(value="<h4 class='rounded-heading'>Maximum Memory (2GB-10GB)</h4>")
max_memory_slider = widgets.IntSlider(
    value=2,
    min=2,
    max=10,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    layout=widgets.Layout(width='100%')
)


# Create a slider for output video quality
output_video_quality_heading = widgets.HTML(value="<h4 class='rounded-heading'>Output Video Quality (1-100)</h4>")
output_video_quality_slider = widgets.IntSlider(
    value=1,
    min=1,
    max=100,
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    layout=widgets.Layout(width='100%')
)

# Update the subprocess command with output video quality
optional_commands.extend([
    "--output-video-quality", str(output_video_quality_slider.value)
])

# Arrange widgets for additional options
additional_options_vbox = widgets.VBox([
    output_video_quality_heading,
    output_video_quality_slider
], layout=widgets.Layout(width='100%'))

# Create accordion for optional options
optional_options_accordion = widgets.Accordion([
    widgets.VBox([
        many_faces_heading,
        many_faces_radio,
        execution_provider_heading,
        execution_provider_radio,
        reference_face_position_heading,
        reference_face_position_slider,
        reference_frame_number_heading,
        reference_frame_number_slider,
        similar_face_distance_heading,
        similar_face_distance_slider,
        max_memory_heading,
        max_memory_slider,
        additional_options_vbox
    ], layout=widgets.Layout(width='100%'))
], layout=widgets.Layout(width='400px', margin='auto', align_items='center', border='2px solid #111111', border_radius='5px'))
optional_options_accordion.set_title(0, 'Options & Advanced Settings')

optional_options_accordion.add_class("custom-accordion")  # Add custom class
# Attach the function to the button click event

# Set up the UI layout
ui = widgets.VBox([
    total_frames_label,
    progress_label,
    progress_bar,
    time_remaining_label,
    optional_options_accordion,
    run_button,
    output_container
], layout=widgets.Layout(align_items='center'))

def on_run_button_clicked(b):
    with output_container:
        clear_output(wait=True)
        run_deepfake_process(b)

# Link the button click event to the function
run_button.on_click(on_run_button_clicked)

# Create a VBox to contain the Rupantarak with a 10px margin
collapsible_content_rupantarak = widgets.VBox([ui], layout=widgets.Layout(align_items='center', margin='10px 0'))

# Create a collapsible button for the Rupantarak
collapsible_button_rupantarak = widgets.Button(description="Start Rupantarak Process ~ Hide & Show", layout=widgets.Layout(width='auto', height='50px'))
collapsible_button_rupantarak.add_class("note-button")  # Apply custom CSS class


# Initially show content
collapsible_content_rupantarak.layout.display = 'flex'

# Define the toggle function for the Rupantarak section
def toggle_content_rupantarak(b):
    if collapsible_content_rupantarak.layout.display == 'none':
        collapsible_content_rupantarak.layout.display = 'flex'
    else:
        collapsible_content_rupantarak.layout.display = 'none'

# Assign the toggle function to the button click event for the Rupantarak section
collapsible_button_rupantarak.on_click(toggle_content_rupantarak)

# Display the toggle button for the Rupantarak section
display(widgets.HBox([collapsible_button_rupantarak], layout=widgets.Layout(justify_content='center')))

# Display the collapsible content for the Rupantarak section
display(collapsible_content_rupantarak)













html_content = '''
<style>
  .divider {
    width: 400px;
    height: 3px;
    background-color: #222222;
    margin: 20px auto 10px auto;
  }
  .heading-container {
    text-align: center;
    border-radius: 10px;
    background-color: #222222;
    padding: 3px;
    margin: 0 auto 20px auto;
    width: 400px;
  }
  .heading {
    font-weight: bold;
    margin: 0;
  }
  .step-heading {
    border-radius: 10px;
    background-color: #222222;
    width: 150px;
    margin: 10px auto;
    text-align: center;
    height: 20px;
  }
</style>
<div class="divider" style="margin-bottom: 10px;"></div>

<div class="step-heading">
  <h4>Things To Know</h4>
</div>
<div class="heading-container" style="margin-bottom: 10px;">
  <h3 class="heading">○~○~○~○~○~○~○~○~○~○~○~○~○~○~○~○~○</h3>
</div>
'''

display(HTML(html_content))

from IPython.display import HTML, display
# @markdown

# Define a function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h3 style='font-family: Andika, sans-serif; font-size 20px; background: -webkit-linear-gradient(left, #8E24AA, #0D47A1); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
    </div>    """
    display(HTML(logo_html))


# Display the gradient text logo
display_logo()




import ipywidgets as widgets
import requests
import time

# Define the form fields
name_field = widgets.Text(
    value='',
    placeholder='Your Name',
    description='Your Name:',
    disabled=False,
    layout=widgets.Layout(width='300px', margin='10px 0'),
    style={'description_width': 'initial'}
)
name_field.add_class("gradient-link")

feedback_field = widgets.Textarea(
    value='',
    placeholder='Your Feedback',
    description='Feedback:',
    disabled=False,
    layout=widgets.Layout(width='300px', height='auto', margin='10px 0'),
    style={'description_width': 'initial'}
)
feedback_field.add_class("gradient-link")

email_field = widgets.Text(
    value='',
    placeholder='Email (Optional)',
    description='Email:',
    disabled=False,
    layout=widgets.Layout(width='300px', margin='10px 0'),
    style={'description_width': 'initial'}
)
email_field.add_class("gradient-link")

submit_button = widgets.Button(
    description='Submit',
    disabled=False,
    button_style='success',
    layout=widgets.Layout(width='300px', height='40px', margin='10px 0')  # Set width, height, and margin
)
submit_button.add_class("gradient-link")

output_field = widgets.Output(layout={'visibility': 'hidden'})  # Hide output by default

# Define the submit function
def on_submit(b):
    with output_field:
        output_field.clear_output()
        name = name_field.value.strip()
        feedback = feedback_field.value.strip()
        email = email_field.value.strip()

        if not name or not feedback:
            print("Name and Feedback are required fields and cannot be empty.")
            return

        # Construct the URL to submit the form
        form_id = '1FAIpQLSd3CQpBkn5_yGRPocSNVkXy6Lx_W5xI0X5z6MVzgzn31wOodw'
        url = f"https://docs.google.com/forms/d/e/{form_id}/formResponse"
        data = {
            'entry.1395913307': name,  # Replace with the actual entry ID for the 'Your Name' field
            'entry.2005839779': feedback,  # Replace with the actual entry ID for the 'Feedback' field
            'entry.1744226297': email  # Replace with the actual entry ID for the 'Email' field
        }

        # Submit the form
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Form submitted successfully!")
            output_field.layout.visibility = 'visible'  # Show output
            # Clear fields
            name_field.value = ''
            feedback_field.value = ''
            email_field.value = ''
            # Hide success message after 2 seconds
            time.sleep(2)
            output_field.layout.visibility = 'hidden'
        else:
            print("Failed to submit the form.")
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text}")

submit_button.on_click(on_submit)

# Define a VBox to contain the form
form_container = widgets.VBox([
    name_field,
    feedback_field,
    email_field,
    submit_button,
    output_field
], layout=widgets.Layout(align_items='center', visibility='hidden', display='none'))  # Initially hide form

# Create a collapsible button for the form
collapsible_button_form = widgets.Button(description="रूपांतरक ~ Feedback ~ Hide & Show", layout=widgets.Layout(width='auto', height='50px'))
collapsible_button_form.add_class("note-button")  # Apply custom CSS class


# Define the toggle function for the form section
def toggle_form(b):
    if form_container.layout.visibility == 'hidden':
        form_container.layout.visibility = 'visible'
        form_container.layout.display = 'flex'  # Show container if hidden
    else:
        form_container.layout.visibility = 'hidden'
        form_container.layout.display = 'none'  # Hide container if visible

# Assign the toggle function to the button click event for the form section
collapsible_button_form.on_click(toggle_form)

# Display the toggle button for the section
display(widgets.HBox([collapsible_button_form], layout=widgets.Layout(justify_content='center')))

# Display the collapsible content for the form section
display(form_container)





import cv2
import numpy as np
import base64
from IPython.display import HTML, display
def download_image_from_drive(file_id, dest_path):
    # Create destination directories if they don't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Google Drive download URL
    url = f"https://drive.google.com/uc?export=download&id={file_id}"

    # Send request to download the file
    response = requests.get(url)
    if response.status_code == 200:
        # Write the content to the file
        with open(dest_path, 'wb') as f:
            f.write(response.content)

file_id = '10Eih3BT8wtdtqlIik5S0fy4Tx6RBJ3z3'
dest_path = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Me.jpg'
download_image_from_drive(file_id, dest_path)


# @markdown

import cv2
import numpy as np
import base64
from IPython.display import display, HTML

def fetch_and_show_image(image_path):
    # Load the original image
    image = cv2.imread(image_path)

    # Define the border color
    border_color = (17, 17, 17)  # RGB for #111111

    # Create a circular mask with a 100px radius
    mask_radius = 100
    mask = np.zeros((2 * mask_radius, 2 * mask_radius, 3), dtype=np.uint8)
    cv2.circle(mask, (mask_radius, mask_radius), mask_radius, (255, 255, 255), -1)

    # Resize the original image to fit within the circular mask
    resized_image = cv2.resize(image, (2 * mask_radius, 2 * mask_radius))

    # Apply the circular mask to the resized image
    masked_image = cv2.bitwise_and(resized_image, mask)

    # Add a border around the circular image
    border_size = 10
    bordered_image = cv2.copyMakeBorder(masked_image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=border_color)

    # Encode the final image as base64
    _, buffer = cv2.imencode('.jpg', bordered_image)
    encoded_image = base64.b64encode(buffer)

    # Clear previous image preview
    display(HTML('<div id="image_preview"></div>'))

    # Display the image without heading
    display(HTML("""
    <script>
    document.getElementById('image_preview').innerHTML = `
        <div style='text-align: center;'>
            <img src='data:image/jpeg;base64,{}' style='border-radius: 50%; border: 10px solid #222222;'>
        </div>
    `;
    </script>
    """.format(encoded_image.decode())))

def display_other_tools():
    # Define the content of the other tools buttons and information
    other_tools_content = """
    <div style="text-align: center;">
        <h3>I'm Vishal Sharma</h3>
        <button onclick="window.open('https://github.com/nick-arch/Rupantarak.git', '_blank')" style="background: linear-gradient(45deg, #8E24AA, #0D47A1); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; display: inline-block; margin-right: 10px;">Repository I Used</button>
        <button onclick="window.open('https://github.com/s0md3v/roop.git', '_blank')" style="background: linear-gradient(45deg, #8E24AA, #0D47A1); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; display: inline-block; margin-right: 10px;">Original Roop Repository</button>
        <div style="margin-top: 20px;">
        </div>
        <button onclick="window.open('https://www.linkedin.com/in/vishalsharma07', '_blank')" style="background: linear-gradient(45deg, #8E24AA, #0D47A1); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; display: inline-block;">My LinkedIn Profile</button>
    </div>
    """
    return other_tools_content

# Collapsible note with rounded corners and background color #222222
collapsible_note = """
<div style="background-color: #222222; border-radius: 10px; width: 400px; padding: 10px; margin: 20px auto; color: white;">
    <button onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none';"
            style="background: linear-gradient(45deg, #8E24AA, #0D47A1); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; width: 380px; margin: 10px auto; display: block;">
        Must knows ~ Hide & Show
    </button>
    <div style="margin-top: 10px; display: block;">
        <div style="text-align: center;">
            <div id="image_preview"></div>
            <script>
            document.getElementById('image_preview').innerHTML = '';
            </script>
            <div>
                """ + display_other_tools() + """
            </div>
        <div id="note_content" style="display: block; background: #222222; border-radius: 5px; padding: 10px; text-align: center; width: 380px; margin: 0 auto;">
            <div style="background: linear-gradient(45deg, #8B0000, #5A0000); border-radius: 5px; padding: 10px;">
                <p style="color: white; font-weight: bold;">Ensuring ethical content creation is our priority. That's why our रूपांतरक ~ Rupantarak tool includes a sensitive content filter.</p>
            </div>
        <div style="margin-bottom: 20px;">
            <p>This tool, रूपांतरक ~ Rupantarak, is designed for creating deepfake videos with high-quality results. It utilizes advanced AI algorithms to seamlessly swap faces in videos while maintaining natural motion.</p>
    <div style="text-align: center;">
        <h3>Additional Functions:</h3>
        <details>
            <summary>Lightning Speed Uploads Using Public Gdrive URL</summary>
            <p>Once you have the shared link, paste it into the tool, select the desired format (image or video), and click "Start Download" to initiate the download process. The tool provides a progress bar to track the download progress, ensuring a seamless experience.</p>
        </details>
        <details>
            <summary>Normal Speed Uploads Using Local Drive</summary>
            <p>Enhances file uploads, matching your internet speed. It dynamically adjusts settings for optimal bandwidth usage, ensuring speedy transfers. This user-friendly tool adapts seamlessly to changing network conditions for efficient uploads.</p>
        </details>
    </div>

        </div>
            <div style="background: #222222; border-radius: 5px; padding: 10px;">
                <p style="font-weight: bold;">If you find this tool helpful, please consider supporting me with a coffee for any amount between $1 and $100.</p>
                <button onclick="window.open('https://www.paypal.com/ncp/payment/7LSWLVQVCLGB6', '_blank')" style="background: linear-gradient(45deg, #FF0000, #FFA500); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">Buy me a Coffee</button>

                <p style="font-weight: bold;"><strong>Other tools:</strong></p>
                <button onclick="window.open('https://colab.research.google.com/drive/1ch7vpHFFdkc4W48xDO3bgLMzhuGMgd8-?usp=sharing&authuser=2', '_blank')" style="background: linear-gradient(45deg, #0D47A1, #8E24AA); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">UXEL Fooocus</button>
                <button onclick="window.open('https://colab.research.google.com/drive/1y_JpEVZuQre_x2DjQ80egg9R0BVuj2wT?usp=sharing#forceEdit=true&sandboxMode=true&scrollTo=z_MMwRYGArTe', '_blank')" style="background: linear-gradient(45deg, #0D47A1, #8E24AA); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">UXEL Vision</button>
                <div style="margin-top: 10px;">
                    <details open>
                        <summary style="cursor: pointer;"><strong>Tool Info</strong></summary>
                        <p><strong>UXEL Vision:</strong> Video upscaler using ESRGAN up to 8K resolution.</p>
                        <p><strong>UXEL Fooocus:</strong> AI image generator using SDXL 1.0 technology</details>
                </div>
            </div>
        </div>        </div>
    </div>
</div>
"""

# Display the collapsible note
display(HTML(collapsible_note))

# Call the function with the provided image path
fetch_and_show_image("/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/Me.jpg")
from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))
# Jay Shree Ram
