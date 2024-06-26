


from google.colab import drive
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import ipywidgets as widgets
from IPython.display import display, HTML
from IPython.display import display, HTML

# HTML code for divider and headings
html_code = """
<div style="width: 300px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
</div>
</div>
"""

# Display HTML
display(HTML(html_code))
# Custom CSS for button styling and popups
custom_css = """
<style>


.auth-button {
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
.auth-button:hover {
    background: linear-gradient(to right, #FF0000, #FF5733);
    transform: scale(1.00);
}
.auth-button:active {
    background: linear-gradient(to right, #FF5733, #FF0000);
    transform: scale(0.75);
}

.popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #111111;
    border: 4px solid #222222;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    z-index: 1000;
    width: 200px;
    height: 100px;
}
.popup h2 {
    color: #ff0066;
    margin: 0;
    padding: 0;
    line-height: normal;
}
.popup p {
    color: #333333;
    margin: 0;
    padding: 0;
    line-height: normal;
}

.indicator {
    display: inline-block;
    background-color: #222222;
    border-radius: 10px;
    padding: 5px 5px;
    font-size: 16px;
    font-weight: bold;
}
.authenticated {
    color: #00FF7F;
}
.unauthenticated {
    color: #DC143C;
}
</style>
"""

# HTML for custom CSS
custom_css_html = HTML(custom_css)
display(custom_css_html)

# Function to display the success popup
def display_success_popup():
    success_html = """
    <div class="popup" id="success-popup">
        <h2 style="color: green;">Successfully Authenticated Gdrive</h2>
        <p style="color: green;">ʏᴏᴜ ᴄᴀɴ ɴᴏᴡ ᴜsᴇ रूपांतरक ~ Ꮢᥙραɳ𝜏αɾαƙ ᑌᑎᑕᗴᑎᔕᗝᖇᗴᗪ ᴛᴏᴏʟ.</p>
    </div>
    <script>
        setTimeout(function() {
            document.getElementById('success-popup').style.display = 'none';
        }, 5000);
    </script>
    """
    display(HTML(success_html))

# Function to display the denial popup
def display_denial_popup():
    denial_html = """
    <div class="popup" id="denial-popup">
        <h2 style="color: red;">Permission Denied</h2>
        <p style="color: red;">Google Drive access was denied. Please grant permission to proceed.</p>
    </div>
    <script>
        setTimeout(function() {
            document.getElementById('denial-popup').style.display = 'none';
        }, 5000);
    </script>
    """
    display(HTML(denial_html))

# Function to authenticate and authorize Google Drive access
def authenticate_drive(b):
    with output_auth:
        output_auth.clear_output()
        try:
            auth.authenticate_user()  # Perform authentication
            global drive_service
            drive_service = build('drive', 'v3')  # Build Drive service
            update_status()  # Update status after authentication
            display_success_popup()  # Show success popup
        except Exception as e:
            display_denial_popup()  # Show denial popup if an error occurs

# Function to update LED indicator
def update_indicator(status):
    if status:
        return '<font size="3" color="#00FF7F" class="indicator"><strong>⸦ ⸧  ᗩᑌ丅ᕼᗴᑎ丅Iᑕᗩ丅ᗴᗪ  ⸦ ⸧</strong></font>'  # Green
    else:
        return '<font size="3" color="#DC143C" class="indicator"><strong>⸦ ⸧  ᑌᑎ~ᗩᑌ丅ᕼᗴᑎ丅Iᑕᗩ丅ᗴᗪ  ⸦ ⸧</strong></font>'  # Red

# Function to update status indicator
def update_status():
    if 'drive_service' in globals():
        status_indicator.value = update_indicator(True)  # Change status to green
    else:
        status_indicator.value = update_indicator(False)  # Change status to red

# Create button for authentication with dynamic size
auth_button = widgets.Button(description="Click To Authenticate Gdrive", layout=widgets.Layout(width='320px', height='50px'))
auth_button.style.font_weight = 'bold'
auth_button.on_click(authenticate_drive)
auth_button.add_class("auth-button")  # Apply custom CSS class

# Output widget for displaying status
output_auth = widgets.Output()

# Label for status

# HTML widget for displaying LED indicator
status_indicator = widgets.HTML(value=update_indicator(False))


# Arrange status label and indicator side by side, centered
status_box = widgets.HBox([status_indicator], layout=widgets.Layout(justify_content='center'))

# Arrange button and status box vertically, centered
button_status_box = widgets.VBox([auth_button, status_box], layout=widgets.Layout(align_items='center'))
status_indicator.add_class(".indicator")  # Apply custom CSS class


# Display the widgets
display(button_status_box, output_auth)

# Check if authentication has already been completed
update_status()

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

from ipywidgets import HBox
from google.colab import auth
from google.colab import drive
import gdown
from IPython.display import display, Javascript
from IPython.display import display, clear_output
# Define CSS import for Bree Serif font
css_import = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap');
</style>
"""

# Define CSS styles for widgets, button text, headings, labels, counter_labels, and popups
# Define CSS styles for widgets, button text, headings, labels, counter_labels, and popups
widget_css = """
<style>
.bree-serif-regular {
  font-family: "Bree Serif", serif;
  font-weight: 400;
  font-style: normal;
}

/* Apply font to all widgets */
.widget {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to button text */
button {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to headings */
h1, h2, h3, h4, h5, h6 {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to labels */
label {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to counter labels */
.counter_label {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to popups */
.popup {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to total uploads counter label */
.total_uploads_label {
    font-family: "Bree Serif", serif !important;
    font-weight: 400 !important;
    font-style: normal !important;
}

/* Apply font to success refresh popup */
.success-popup p {
    font-family: "Bree Serif", serif;
    font-weight: 400;
    font-style: normal;
}
</style>
"""

# Display CSS import
display(HTML(css_import))

# Display CSS styles for widgets, button text, headings, labels, counter_labels, and popups
display(HTML(widget_css))


# Custom CSS for gradient styles
gradient_button_css = """
<style>

/* Default button style */
button {
    background: linear-gradient(to right, #FF5733, #FF0000);
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    width: 300px
    margin-top: 5px;
    transition: background 0.4s, transform 0.4s; /* Transition effect duration */
}

/* Hover effect */
button:hover {
    background: linear-gradient(to right, #FF0000, #FF5733); /* Reverse gradient on hover */
    transform: scale(1.00); /* Slightly increase size */
}

/* Click effect */
button:active {
    background: linear-gradient(to right, #800000, #8B4513); /* Darker gradient on click */
    transform: scale(0.75); /* Slightly decrease size */
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







from IPython.display import display, HTML

# HTML code for divider and headings
html_code = """
<div style="width: 300px; height: 5px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
</div>
</div>
"""

# Display HTML
display(HTML(html_code))


import os
import base64
import ipywidgets as widgets
from IPython.display import display, HTML

# Counter for total uploads
total_uploads = 0

# Function to display a popup for successful upload
# Function to display a popup for successful upload
def display_upload_success():
    success_html = """
    <style>
        .upload-success-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #111111; /* Popup background color */
            border: 5px solid #222222;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .upload-success-popup h2 {
            color: #008000;
            font-weight: bold; /* Make text bold */
            background: -webkit-linear-gradient(#00FF00, #008000); /* Green gradient for text */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    <div class="upload-success-popup" id="upload-success-popup">
        <h2>Upload Successful!</h2>
    </div>
    <script>
        setTimeout(function() {
            var element = document.getElementById('upload-success-popup');
            element.parentNode.removeChild(element);
        }, 3000);
    </script>
    """
    display(HTML(success_html))

# Function to display a popup for no image selected
def display_no_image_selected():
    error_html = """
    <style>
        .no-image-selected-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #111111; /* Popup background color */
            border: 5px solid #222222;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .no-image-selected-popup h2 {
            color: #FF6347;
            font-weight: bold; /* Make text bold */
            background: -webkit-linear-gradient(#FF5733, #FF0000); /* Red gradient for text */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    <div class="no-image-selected-popup" id="no-image-selected-popup">
        <h2>No Image Selected!</h2>
    </div>
    <script>
        setTimeout(function() {
            var element = document.getElementById('no-image-selected-popup');
            element.parentNode.removeChild(element);
        }, 3000);
    </script>
    """
    display(HTML(error_html))

# Function to handle the upload process for source upload box
def handle_source_upload(uploader, folder_path, html_note, counter_label):
    global total_uploads
    if not uploader.value:
        display_no_image_selected()  # Display popup for no image selected
        return
    total_uploads += 1

    # Create folder if not exists
    os.makedirs(folder_path, exist_ok=True)

    # Delete existing files
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

    # Save uploaded file with specific name
    uploaded_filename = list(uploader.value.keys())[0]
    save_path = os.path.join(folder_path, f"{folder_path.split('/')[-1]}.png")

    with open(save_path, 'wb') as f:
        f.write(uploader.value[uploaded_filename]['content'])

    # Update HTML note with uploaded image
    display_images(folder_path, html_note)

    # Update counter label
    counter_label.value = f"<b>Total uploads: {total_uploads}</b>"

    # Display success popup
    display_upload_success()

    # Clear the selection of the upload box
    uploader.value.clear()
    uploader._counter = 0  # Reset counter to ensure upload of same file again

# Function to handle the upload process for target upload box
def handle_target_upload(uploader, folder_path, html_note, counter_label):
    global total_uploads
    if not uploader.value:
        display_no_image_selected()  # Display popup for no image selected
        return

    # Create folder if not exists
    os.makedirs(folder_path, exist_ok=True)

    # Save uploaded files with sequential names
    for i, file_info in enumerate(uploader.value.values()):
        uploaded_filename = list(uploader.value.keys())[i]
        save_path = os.path.join(folder_path, f"{folder_path.split('/')[-1]}_{total_uploads + i + 1}.png")

        with open(save_path, 'wb') as f:
            f.write(file_info['content'])

    total_uploads += len(uploader.value)

    # Update HTML note with uploaded image
    display_images(folder_path, html_note)

    # Update counter label
    counter_label.value = f"<b>Total uploads: {total_uploads}</b>"

    # Display success popup
    display_upload_success()

    # Clear the selection of the upload box
    uploader.value.clear()
    uploader._counter = 0  # Reset counter to ensure upload of same file again

# Function to display the uploaded image in HTML note
def display_images(folder_path, html_note):
    encoded_strings = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "rb") as f:
                encoded_string = base64.b64encode(f.read()).decode("utf-8")
                encoded_strings.append(encoded_string)

    # Construct HTML content with uploaded image
    images_html = ""
    for encoded_string in encoded_strings:
        images_html += f'<img src="data:image/jpeg;base64,{encoded_string}" style="border-radius: 5px; max-width: 100%;"/>'

    # Update HTML note with uploaded image and text
    html_note.value = f"""
    <details style="width: 170px; margin-right: -2px;" open>
        <summary style="font-weight: bold; background-color: #222222; color: white; border-radius: 5px; padding: 8px; text-align: center;">{html_note.description}</summary>
        <div style="background-color: #222222; border-radius: 10px; padding: 10px;">
            {images_html}
            <div style="text-align: center; margin-top: 5px;">
                <b style="font-size: 16px;">Selected Image</b>
            </div>
        </div>
    </details>
    """

# Define folder paths
folder_path1 = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_S"
folder_path2 = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T"

# Create select boxes accepting only image file types, allowing one image for source and multiple for target
uploader1 = widgets.FileUpload(description="Select Source", accept="image/*", multiple=False,
                               layout=widgets.Layout(width='150px', height='40px', margin='5px'))
uploader2 = widgets.FileUpload(description="Select Target", accept="image/*", multiple=True,
                               layout=widgets.Layout(width='150px', height='40px', margin='5px'))

# Set text to bold
uploader1.style.font_weight = 'bold'
uploader2.style.font_weight = 'bold'

# Create upload counter label
# Create upload counter label with CSS class name
import ipywidgets as widgets

counter_label = widgets.HTML(value=f"<b class='total_uploads_label'>Total uploads: {total_uploads}</b>",
                             layout=widgets.Layout(width='300px', margin='5px auto', text_align='center'))
# Create button
upload_button = widgets.Button(description="Start Upload",
                               layout=widgets.Layout(width='300px', height='40px', margin='5px auto'))

# Create HTML notes to display uploaded images
html_note1 = widgets.HTML()
html_note2 = widgets.HTML()

## Function to handle button click event
def on_button_click(b):
    handle_source_upload(uploader1, folder_path1, html_note1, counter_label)
    handle_target_upload(uploader2, folder_path2, html_note2, counter_label)

upload_button.on_click(on_button_click)

# Create containers for select boxes, button, counter label, and HTML notes
select_boxes_container = widgets.HBox([uploader1, uploader2], layout=widgets.Layout(justify_content='center'))
button_container = widgets.HBox([upload_button], layout=widgets.Layout(justify_content='center'))
counter_label_container = widgets.HBox([counter_label], layout=widgets.Layout(justify_content='center'))
html_notes_container = widgets.HBox([html_note1, html_note2], layout=widgets.Layout(justify_content='center'))

# Define custom CSS styles
custom_css = """
<style>
.rounded-button {
    border-radius: 5px;
}
</style>
"""

# Inject custom CSS into the notebook
display(HTML(custom_css))

# Center all widgets within the containers
centered_widgets_container = widgets.VBox([select_boxes_container, button_container, counter_label_container, html_notes_container],
                                          layout=widgets.Layout(width='370px', justify_content='center', align_items='center', margin='5px'))

# Display the container
display(centered_widgets_container)


import cv2
import numpy as np
from IPython.display import display, HTML, clear_output
import base64
import ipywidgets as widgets

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
    background_color = (17, 17, 17)  # RGB for #111111    # Process the first detected face only
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
        <img src='data:image/jpeg;base64,{}' style='border-radius: 50%; border: 4px linear-gradient(to right, #FA8072, #F5F5DC);'>
    </div>
    """.format(encoded_image.decode())

    return image_html


# Function to display a success refresh popup
def display_success_refresh_popup():
    popup_html = """
    <div class="success-popup">
        <p>Face refreshed successfully!</p>
    </div>
    <style>
        .success-popup {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: #111111;
            border: 5px solid #222222;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
        .success-popup p {
            color: yellow; /* Yellow text */
            font-weight: bold; /* Make text bold */
            background: -webkit-linear-gradient(#FF5733, #FF0000); /* Yellow gradient for text */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
    """
    # Display HTML and execute JavaScript to hide the popup after 3 seconds
    display(HTML(popup_html))
    display(Javascript("""
    setTimeout(function() {
        var popup = document.querySelector('.success-popup');
        if (popup) {
            popup.parentNode.removeChild(popup);
        }
    }, 3000);
    """))

# Display the initial face image
image_html = fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png")
image_output = widgets.HTML(value=image_html)

# Define the refresh button with margin
button = widgets.Button(description="Refresh Face", layout=widgets.Layout(width='auto', margin='0 auto 10px auto'))

# Define the refresh function
def refresh_face(btn):
    image_output.value = fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png")
    display_success_refresh_popup()
    

# Assign the refresh function to the button click event
button.on_click(refresh_face)

# Display the refresh button with margin and face image
display(widgets.VBox([image_output, widgets.HBox([button], layout=widgets.Layout(justify_content='center'))]))

import os
import ipywidgets as widgets
from IPython.display import display, HTML, Javascript

# Create the reset button
reset_button = widgets.Button(
    description="Click To Delete All Uploaded Target's",
    layout=widgets.Layout(width='300px', height='40px', margin='10px auto'),
    style={'button_color': 'blue', 'font_weight': 'bold'}
)

# Function to delete all files in the folder
def delete_all_files(b):
    folder_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T"
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
            background: linear-gradient(45deg, #111111, #111111);
            border: 10px solid #222222;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            z-index: 9999;
        }
        .popup-container h2 {
            color: yellow; /* Yellow text */
            font-weight: bold; /* Make text bold */
            background: -webkit-linear-gradient(#FF5733, #FF0000); /* Yellow gradient for text */
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .popup-container p {
            color: #ffffff;
        }
    </style>
    <div class="popup-container">
        <h2>All Uploaded Target's Have Been deleted</h2>
        <p>Upload New Target's Via Source Face & Target Images From The Uploader Above</p>
    </div>
    <script>
        setTimeout(function() {
            var element = document.querySelector('.popup-container');
            element.parentNode.removeChild(element);
        }, 5000);
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



# HTML code for divider and headings with margin
html_code = """
<div style="margin-top: 10px; margin-bottom: 10px; width: 300px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
"""

# Display HTML
display(HTML(html_code))

# @markdown
