

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
    background: linear-gradient(to right, #FF007F, #800080); /* Dark blue to purple gradient */
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
  background: linear-gradient(to right, #FF007F, #800080); /* Gradient from #800080 to #2196f3 */
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
    width: 250px !important;
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






# Define a function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #FF007F, #800080); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Image</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
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



# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))


from IPython.display import display, HTML

# HTML code for divider and headings
html_code = """
<div style="width: 400px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
<div style="width: 100px; height: 20px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto 0; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 14px;">Step ~1</span>
</div>
<div style="width: 350px; height: 40px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 18px;">Upload Source Image & Multiple Target's</span>
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

# Function to handle the upload process for source upload box
def handle_source_upload(uploader, folder_path, html_note, counter_label):
    global total_uploads
    if not uploader.value:
        print("No file uploaded.")
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

    # Clear the selection of the upload box
    uploader.value.clear()
    uploader._counter = 0  # Reset counter to ensure upload of same file again

# Function to handle the upload process for target upload box
def handle_target_upload(uploader, folder_path, html_note, counter_label):
    global total_uploads
    if not uploader.value:
        print("No file uploaded.")
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
    <details style="width: 210px; margin-right: -2px;" open>
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
                               layout=widgets.Layout(width='170px', height='40px', margin='5px'))
uploader2 = widgets.FileUpload(description="Select Target", accept="image/*", multiple=True,
                               layout=widgets.Layout(width='170px', height='40px', margin='5px'))

# Set text to bold
uploader1.style.font_weight = 'bold'
uploader2.style.font_weight = 'bold'

# Create upload counter label
counter_label = widgets.HTML(value=f"<b>Total uploads: {total_uploads}</b>",
                             layout=widgets.Layout(width='350px', margin='5px auto', text_align='center'))

# Create button
upload_button = widgets.Button(description="Start Upload",
                               layout=widgets.Layout(width='350px', height='40px', margin='5px auto'))

# Create HTML notes to display uploaded images
html_note1 = widgets.HTML()
html_note2 = widgets.HTML()

# Function to handle button click event
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
                                          layout=widgets.Layout(width='100%', justify_content='center', align_items='center', margin='5px'))

# Display the container
display(centered_widgets_container)






import cv2
import numpy as np
from IPython.display import display, HTML, clear_output
import base64
import ipywidgets as widgets
from ipywidgets import VBox  # Import VBox

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
        return

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

    # Clear previous face preview
    display(HTML('<div id="face_preview"></div>'))

    # Display the image without heading
    display(HTML("""
    <script>
    document.getElementById('face_preview').innerHTML = `
        <div style='text-align: center;'>
            <img src='data:image/jpeg;base64,{}' style='border-radius: 50%; border: 10px solid #222222;'>
        </div>
    `;
    </script>
    """.format(encoded_image.decode())))

# Call the function with the provided image path
fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png")

# Define the refresh button
button = widgets.Button(description="Refresh Face")
button.on_click(lambda btn: fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png"))

# Display the refresh button centered
container = VBox([button], layout={'align_items': 'center'})
display(container)


# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))

from IPython.display import display, HTML

# HTML code for divider and headings
html_code = """
<div style="width: 400px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
<div style="width: 100px; height: 20px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto 0; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 14px;">Step ~2</span>
</div>
<div style="width: 350px; height: 40px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 18px;">Run ~ रूपांतरक ~ Rupantarak ○~○ Image</span>
</div>
"""

# Display HTML
display(HTML(html_code))



import os
import subprocess
import time
import base64
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from IPython.display import display, HTML
import ipywidgets as widgets

# Function to upload image to Google Drive
def upload_image_to_drive(image_file_path, file_name):
    auth.authenticate_user()
    drive_service = build('drive', 'v3')

    response = drive_service.files().list(q=f"name='{file_name}'", spaces='drive', fields='files(id)').execute()
    existing_files = response.get('files', [])
    if existing_files:
        for file in existing_files:
            drive_service.files().delete(fileId=file['id']).execute()

    file_metadata = {'name': file_name}
    media = MediaFileUpload(image_file_path, mimetype='image/png')
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = uploaded_file.get('id')
    file_link = f'https://drive.google.com/uc?id={file_id}&export=download'

    button_html = f'''
    <button onclick="window.open('{file_link}')" style="background: linear-gradient(to right, #FF69B4, #800080); color: #ffffff; border: none; border-radius: 5px; padding: 10px; width: 100%; margin-top: 5px;">Download Image</button>
    '''
    return button_html, file_link

# Function to post-process image
def post_process_function(output_image_path, index):
    output_directory = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_B"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_image_path = os.path.join(output_directory, f"Rupantarak_B_{index}.png")

    if not os.path.exists(output_image_path):
        raise FileNotFoundError(f"Expected output image not found: {output_image_path}")

    upload_button_html, file_link = upload_image_to_drive(output_image_path, os.path.basename(output_image_path))
    return upload_button_html, file_link

# Function to run the deepfake process for multiple targets
def run_process(_):
    with output:
        clear_output(wait=True)
        try:
            # Automatically fetch target images from the path
            target_images_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T"
            target_images = [os.path.join(target_images_path, file) for file in os.listdir(target_images_path) if file.endswith('.png')]

            if not target_images:
                raise FileNotFoundError("No target images found in the directory.")

            for index, target_image in enumerate(target_images):
                # Delete existing output files
                output_directory = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_O"
                existing_output_files = [os.path.join(output_directory, file) for file in os.listdir(output_directory) if os.path.isfile(os.path.join(output_directory, file))]
                for file in existing_output_files:
                    os.remove(file)

                # Start the progress bar at 1%
                progress_bar.value = 1

                # Run the deepfake process for each target image
                subprocess.run(["python", "/content/Rupantarak/run.py",
                                "-s", "/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png",
                                "-t", target_image,
                                "-o", f"/content/Rupantarak/Rupantarak_Pro/Rupantarak_B/Rupantarak_B_{index}.png",
                                "--keep-frames",
                                "--keep-fps",
                                "--temp-frame-quality", "1",
                                "--output-video-quality", "1",
                                "--execution-provider", execution_provider_radio.value.lower(),  # Ensuring correct casing
                                "--frame-processor", "face_swapper", "face_enhancer"])

                # Set the progress bar to 70% over 10 seconds
                for i in range(1, 71):
                    progress_bar.value = i
                    time.sleep(10 / 70)  # Sleep for 10/70 seconds between each increment

                # Set the progress bar to 100%
                progress_bar.value = 100

                # Save the output image with the new path and name
                output_image_path = f"/content/Rupantarak/Rupantarak_Pro/Rupantarak_B/Rupantarak_B_{index}.png"
                upload_button_html, file_link = post_process_function(output_image_path, index)

                with open(output_image_path, "rb") as img_file:
                    encoded_string = base64.b64encode(img_file.read()).decode('utf-8')

                # Display image preview
                html_code = f"""
                <div style="background-color: #111111; padding: 20px; text-align: center;">
                    <details>
                        <summary style="font-weight: bold; background-color: #222222; padding: 10px; border-radius: 5px;">Click to Preview Image {index + 1}</summary>
                        <div style="background-color: #222222; border-radius: 5px; padding: 10px; max-width: 400px; margin: 0 auto;">
                            <img src="data:image/jpeg;base64,{encoded_string}" style="border-radius: 5px; max-width: 100%;"/>
                            {upload_button_html}
                        </div>
                    </details>
                </div>
                """

                display(HTML(html_code))
        except Exception as e:
            display(HTML(f"<div style='color: red;'><strong>Error:</strong> {str(e)}</div>"))


# Create radio buttons for CPU and CUDA
execution_provider_radio = widgets.RadioButtons(
    options=['CPU', 'CUDA'],
    description='Execution Provider:',
    disabled=False,
    layout={'width': 'max-content'}
)

# Create an accordion with radio buttons
accordion = widgets.Accordion(children=[execution_provider_radio])
accordion.set_title(0, 'Acceleration Options')
accordion.add_class("custom-accordion")  # Add custom class

# Create a button with height 55px and width 400px
button = widgets.Button(description="Start Rupantarak Image", layout=widgets.Layout(width='400px', height='55px', margin='auto'))

# Attach the function to the button click event
button.on_click(run_process)

# Create a progress bar widget
progress_bar = widgets.FloatProgress(value=0, min=0, max=100, style={'bar_color': '#4e54c8'}, layout=widgets.Layout(width='350px', margin='10px 0'))

# Create a container to hold the button, accordion, and progress bar
container = widgets.VBox([button, accordion, progress_bar], layout=widgets.Layout(justify_content='center', align_items='center'))

import ipywidgets as widgets

# Create an output widget
output = widgets.Output()

# Display the container and output widget
display(container)
display(output)

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))
from IPython.display import display, HTML

# HTML code for divider and headings
html_code = """
<div style="width: 400px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
<div style="width: 150px; height: 20px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto 0; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 14px;">Things To Know</span>
</div>
<div style="width: 350px; height: 40px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 18px;">○~○~○~○~○~○~○~○~○~○~○~○~○~○</span>
</div>
"""

# Display HTML
display(HTML(html_code))


# Define a function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h3 style='font-family: Andika, sans-serif; font-size: 30px; background: -webkit-linear-gradient(left, #FF007F, #800080); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Image</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 18px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
    </div>    """
    display(HTML(logo_html))

# Display the gradient text logo
display_logo()


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
        <button onclick="window.open('https://github.com/nick-arch/Rupantarak.git', '_blank')" style="background: linear-gradient(45deg, #FF69B4, #800080); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; display: inline-block; margin-right: 10px;">Repository I Used</button>
        <button onclick="window.open('https://github.com/s0md3v/roop.git', '_blank')" style="background: linear-gradient(45deg, #FF69B4, #800080); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; display: inline-block; margin-right: 10px;">Original Roop Repository</button>
        <div style="margin-top: 20px;">
        </div>
        <button onclick="window.open('https://www.linkedin.com/in/vishalsharma07', '_blank')" style="background: linear-gradient(45deg, #FF69B4, #800080); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; display: inline-block;">My LinkedIn Profile</button>
    </div>
    """
    return other_tools_content

# Collapsible note with rounded corners and background color #222222
collapsible_note = """
<div style="background-color: #222222; border-radius: 10px; width: 400px; padding: 10px; margin: 20px auto; color: white;">
    <button onclick="this.nextElementSibling.style.display = this.nextElementSibling.style.display === 'none' ? 'block' : 'none';"
            style="background: linear-gradient(45deg, #FF69B4, #800080); border: none; color: white; padding: 10px 20px; border-radius: 5px; cursor: pointer; width: 380px; margin: 10px auto; display: block;">
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
