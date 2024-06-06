
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
from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))
# Custom CSS for gradient styles
gradient_button_css = """
<style>


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
    background-image: linear-gradient(to right, #FA8072, #F5F5DC);
}

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
    margin: 4px 2px; /* Margin */
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

/* Container for the radio buttons */
.widget-radio-box {
  display: flex;
  flex-direction: column;
}

/* Your custom CSS styles for the radio buttons */
.widget-radio-box label {
  background: linear-gradient(to right, #444444, #555555); /* Gradient from dark grey to lighter grey */
  border-radius: 20px;
  cursor: pointer;
  transition: background 0.3s ease, transform 0.3s ease;
  color: white;
  margin-bottom: 10px; /* Add margin between options */
  width: 100px; /* Set width */
  display: inline-block; /* Display as inline-block */
  padding: 10px; /* Add padding */
  text-align: center; /* Center text */
}

/* Hover effect */
.widget-radio-box label:hover {
  background: linear-gradient(to right, #555555, #666666); /* Slightly lighter gradient on hover */
  transform: scale(1.05); /* Slightly increase size */
}

/* Active effect */
.widget-radio-box label:active {
  background: linear-gradient(to right, #FA8072, #F5F5DC); /* Darker gradient on click */
  transform: scale(0.95); /* Slightly decrease size */
}



/* Selected radio button effect */
.widget-radio-box input[type="radio"]:checked + label {
  background: linear-gradient(to right, #FA8072, #F5F5DC); /* Different gradient for selected state */
}



.gradient-link {
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

.gradient-link:hover {
  background-image: linear-gradient(to right, #FA8072, #F5F5DC);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}

.custom-accordion {
    width: 350px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #222222, #222222) !important;
    padding: 10px !important;
    z-index: 9999 !important;
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
import os
import re
import time
import gdown
from IPython.display import HTML, display

# Function to display a simple popup with a message
def display_popup(message):
    popup_html = f"""
    <style>
        .popup {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #F5F5DC;
            border: 2px solid #FA8072;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }}
        .popup p {{
            color: #333333;
        }}
        .popup button {{
            background-color: #FA8072;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }}
    </style>
    <div class="popup">
        <p>{message}</p>
        <button onclick="close_popup()">Close</button>
    </div>
    <script>
        function close_popup() {{
            var popup = document.querySelector('.popup');
            popup.style.display = 'none';
        }}
    </script>
    """
    display(HTML(popup_html))

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
        display_popup("Upload success!")
    refresh_file_indicators()

def start_download(button):
    try:
        given_link = link_field.value.strip()
        if given_link == "":
            display_popup("Please enter a link.")
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
            display_popup("Download completed successfully!")
        else:
            display_popup("Invalid Google Drive Shared Link. Please try again.")
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
    file_upload_left._counter = 0
    file_upload_right._counter = 0
    clear_all_fields()
    refresh_file_indicators()

container_width = '350px'
upload_box_width = '135px'
upload_box_height = '50px'

link_field = widgets.Text(placeholder='Enter Google Drive Shared Link', layout=widgets.Layout(width=container_width, height='auto'))
link_field.add_class("gradient-link")

download_button = widgets.Button(description="Start Download",
                                 layout=widgets.Layout(width=container_width, height='55px', margin='10px 0',
                                                      background_color='blue',
                                                      color='white'))

file_format_radio = widgets.RadioButtons(options=["Image", "Video"], description="Save as:", layout=widgets.Layout(width=container_width, height='82px'))



progress_bar_download = widgets.FloatProgress(value=0, min=0, max=100, style={'bar_color': 'teal', 'description_width': 'initial'}, layout=widgets.Layout(width=container_width, height='20px'))
overall_progress_download = widgets.HTML(value="<b>Progress:</b> 0%", layout=widgets.Layout(width=container_width, height='55px'))
file_upload_left = widgets.FileUpload(accept='.png, .jpg', multiple=True, description='Image:', layout=widgets.Layout(width=upload_box_width, height=upload_box_height, margin='0 10px'))
file_upload_right = widgets.FileUpload(accept='.mp4', multiple=True, description='Video:', layout=widgets.Layout(width=upload_box_width, height=upload_box_height, margin='0 10px'))
progress_bar_upload = widgets.FloatProgress(value=0, min=0, max=1, description='Progress :', layout={'width': container_width, 'height': '20px'})
output = widgets.Output(layout={'width': container_width})
refresh_button = widgets.Button(description='Refresh Files Status', layout=widgets.Layout(width=container_width, height='55px', margin='10px 0'))
download_success_output = widgets.Output(layout={'width': container_width})

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
                                    layout=widgets.Layout(width='350px', height='50px', margin='10px auto'))
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

from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))
import os
import ipywidgets as widgets
from IPython.display import display, HTML, Javascript

# Create the reset button
reset_button = widgets.Button(
    description="Reset & Delete All Uploads & Temp Files",
    layout=widgets.Layout(width='350px', height='55px', margin='10px auto'),
    style={'button_color': 'blue', 'font_weight': 'bold'}
)

# Function to delete all files in the folder
def delete_all_files(b):
    folder_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_U"
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            pass
    display_popup_message()

# Function to display a popup with gradient interface
def display_popup_message():
    popup_html = """
    <style>
        .popup-container {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(45deg, #FA8072, #F5F5DC);
            border: 10px solid #F5F5DC;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            z-index: 9999;
        }
        .popup-container h2 {
            color: #ff0066;
        }
        .popup-container p {
            color: #333333;
        }
    </style>
    <div class="popup-container">
        <h2>All files have been deleted.</h2>
        <p>This popup will close automatically in 10 seconds.</p>
    </div>
    <script>
        setTimeout(function() {
            var element = document.querySelector('.popup-container');
            element.parentNode.removeChild(element);
        }, 3000);
    </script>
    """
    display(HTML(popup_html))

# Attach the function to the button click event
reset_button.on_click(delete_all_files)

# Create a container to center the button
button_container = widgets.HBox(
    [reset_button],
    layout=widgets.Layout(justify_content='center')
)

# Display the button container
display(button_container)


from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))
