
# @title **</h3>रूपांतरक ~ Rupantarak ○ Bypass<h3>**
import os
import threading
import subprocess
import time
import base64
from ipywidgets import Accordion
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import ipywidgets as widgets
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from IPython.display import HTML, display
from IPython.display import HTML
import base64
import random


from IPython.display import display, HTML

# Define a function to display the gradient text logo
def display_logo():
    logo_html = """
    <div style='text-align: center;'>
        <h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #5C0000, #8B0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffd700;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span><span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br>
            <span style='font-size: 25px;'>Bypass</span><br>
        </h1>
    </div>
    """
    display(HTML(logo_html))

# Display the gradient text logo
display_logo()

# Define custom CSS
custom_css = """
<style>
/* Add your custom CSS styles here */
.custom-accordion {
    width: 200px !important; /* Set width to 350px */
    margin: 10px auto !important; /* Center the widget horizontally */
    border-radius: 5px !important; /* Rounded corners */
    background: linear-gradient(to right, #333333, #333333) !important; /* Gradient background */
    padding: 10px !important; /* Padding for the header */
    z-index: 9999 !important; /* Ensure the widget appears in front of other elements */
}

/* Make the main widget border and background invisible */
.widget-container {
    border: none !important;
    background-color: transparent !important;
    box-shadow: none !important; /* Remove any shadow */
}

/* Set the color inside the accordion box */
.custom-accordion .custom-content {
    background-color: #111111 !important;
    padding: 5px; /* Optional: Add padding to the content area */
}
</style>
"""

# Inject custom CSS into the notebook
display(HTML(custom_css))
# Inject custom CSS into the notebook
custom_css = """
<style>
.rounded-image {
    border-radius: 10px;
}
.background-container {
    background-color: #111111;
    border-radius: 10px;
}
.custom-accordion .accordion-header {
    border-radius: 10px 10px 0 0;
    background-color: #111111;
}
.custom-accordion .accordion-content {
    border-radius: 0 0 10px 10px;
}


.container {
    display: flex;
    justify-content: center;
}

.accordion-container {
    background-color: #111111;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 10px;
}

.accordion-header {
    background: linear-gradient(to right, #ff6f61, #6b8e23);
    border-radius: 10px;
    color: white;
    font-weight: bold; /* Added for bold text */
    padding: 10px;
    cursor: pointer;
}

.accordion-content {
    padding: 10px;
    display: none;
}

.bold-text {
    font-weight: bold !important; /* Added for bold text */
}
.custom-accordion .custom-content {
    background-color: #111111 !important;
    padding: 10px;
}

.custom-image-container {
    background-color: #111111;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    margin: 0px;
    width: auto;
}

</style>
"""

display(HTML(custom_css))


# Define custom CSS to style the radio buttons
custom_css = """
<style>
/* Your custom CSS styles for the radio buttons */
.widget-radio-box label {
  background: linear-gradient(to right, #5C0000, #8B0000); /* Gradient from #800080 to #2196f3 */
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: white;
  margin-bottom: 10px; /* Add margin between options */
  width: 70px; /* Set width */
}
</style>
"""

# Inject custom CSS into the notebook
display(HTML(custom_css))

import os
import ipywidgets as widgets
from IPython.display import display, HTML
from datetime import datetime

def create_image_slideshow(image_folder_path, width=400):
    images = []
    for root, dirs, files in os.walk(image_folder_path):
        for file in files:
            if file.endswith('.png'):
                image_path = os.path.join(root, file)
                with open(image_path, "rb") as img_file:
                    img_data = img_file.read()
                image = widgets.Image(value=img_data, format='png', width=width)
                download_button = widgets.Button(description="Download")
                download_button.on_click(lambda event, img=image, fn=file: download_image(img, fn))
                images.append(widgets.VBox([image, download_button]))
    return images

def download_image(image, filename):
    with open(filename, 'wb') as f:
        f.write(image.value)

def refresh_images(btn):
    for img in images:
        with open(img.filename, "rb") as img_file:
            img_data = img_file.read()
        img.value = img_data

refresh_button = widgets.Button(description="Refresh Images")
refresh_button.on_click(refresh_images)

# Change the folder path accordingly
image_folder_path = "/content/Rupantarak_Pro/Rupantarak_E"

# Create image slideshow
images = create_image_slideshow(image_folder_path)

# HTML for collapsible section with centered button and rounded background
collapsible_html = """
<div style="background-color: #222222; padding: 10px; border-radius: 10px; margin-top: 15px;">
  <div style="text-align:center;">
    {}
  </div>
  <div style="margin-top: 10px;"></div> <!-- Added space between button and note button -->
  <div style="display: flex; justify-content: center;">
    <div style="background-color: #dddddd; border-radius: 10px; padding: 10px;">
      <details>
        <summary style="text-align: center;">Image Slideshow</summary>
        {}
      </details>
    </div>
  </div>
</div>
""".format(refresh_button, ''.join([widgets.widget_serialization['to_json'](w) for w in images]))

display(HTML(collapsible_html))

# Inject custom CSS into the notebook
custom_css = """
<style>
.rounded-image {
    border-radius: 10px;
}
.background-container {
    background-color: #111111;
    border-radius: 10px;
}
.custom-accordion .accordion-header {
    border-radius: 10px 10px 0 0;
    background-color: #111111;
}
.custom-accordion .accordion-content {
    border-radius: 0 0 10px 10px;
}

.custom-accordion .custom-content {
    background-color: #111111 !important;
    padding: 10px;
}

.custom-image-container {
    background-color: #111111;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
    margin: 0px;
    width: auto;
}

</style>
"""

display(HTML(custom_css))

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
    background: linear-gradient(to right, #5C0000, #8B0000);
    border-radius: 20px;
    border: none;
    color: white;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 26px;
    margin: 4px 2px;
    cursor: pointer;
    transition-duration: 0.4s;
}

button:hover {
    background-color: #abedd8;
    color: black;
}

.custom-accordion {
    width: 200px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #333333, #333333) !important;
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
            <img src='data:image/jpeg;base64,{}' style='border-radius: 50%; border: 4px solid #111111;'>
        </div>
    `;
    </script>
    """.format(encoded_image.decode())))

# Call the function with the provided image path
fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png")

# Define the refresh button
button = widgets.Button(description="Selected Face")
button.on_click(lambda btn: fetch_and_show_face("/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png"))

# Display the refresh button centered
container = VBox([button], layout={'align_items': 'center'})
display(container)








import cv2
import numpy as np
import os
import subprocess
import time
import base64
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from IPython.display import display, HTML
import ipywidgets as widgets
from PIL import Image as PILImage

# Load pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to recognize face and fill all other parts of the image with black color
def fill_image_except_faces(image_path, border_radius=20, scale_factor=0.2):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Create a mask to fill all parts of the image with black color
    mask = np.zeros_like(image)

    # Draw rounded rectangles around detected faces
    for (x, y, w, h) in faces:
        # Adjust the region to show more of the face
        x -= int(w * scale_factor)
        y -= int(h * scale_factor)
        w += int(2 * w * scale_factor)
        h += int(2 * h * scale_factor)
        # Draw a white filled rectangle around the face
        cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)
        # Add rounded corners
        cv2.circle(mask, (x + border_radius, y + border_radius), border_radius, (0, 0, 0), -1)
        cv2.circle(mask, (x + w - border_radius, y + border_radius), border_radius, (0, 0, 0), -1)
        cv2.circle(mask, (x + border_radius, y + h - border_radius), border_radius, (0, 0, 0), -1)
        cv2.circle(mask, (x + w - border_radius, y + h - border_radius), border_radius, (0, 0, 0), -1)

    # Fill the image with black color except for the detected faces
    result_image = cv2.bitwise_and(image, mask)

    # Save the result to a file
    blacked_image_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_F/blacked_image.png"
    cv2.imwrite(blacked_image_path, result_image)

    return blacked_image_path

# Function to apply Poisson blending
def apply_poisson_blending(target_img, source_img, mask, center):
    """
    Apply Poisson blending to merge the source image into the target image seamlessly.
    """
    # Apply Poisson blending
    result_image = cv2.seamlessClone(source_img, target_img, mask, center, cv2.NORMAL_CLONE)
    return result_image

# Function to replace face with deepfake
def replace_face_with_deepfake(original_image_path, deepfake_image_path, output_image_path):
    # Load the original and deepfake images
    original_image = cv2.imread(original_image_path)
    deepfake_image = cv2.imread(deepfake_image_path)

    # Create a mask from the deepfake image where the non-black parts (the face) are
    mask = cv2.cvtColor(deepfake_image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

    # Find the center of the mask
    mask_indices = np.where(mask == 255)
    center_y = (np.min(mask_indices[0]) + np.max(mask_indices[0])) // 2
    center_x = (np.min(mask_indices[1]) + np.max(mask_indices[1])) // 2
    center = (center_x, center_y)

    # Convert the mask to 3 channels
    mask = cv2.merge([mask, mask, mask])

    # Normalize the mask to keep it within the valid range
    mask = mask.astype(float) / 255
    mask = (mask * 255).astype(np.uint8)

    # Apply Poisson blending
    final_image = apply_poisson_blending(original_image, deepfake_image, mask, center)

    # Save the final image
    cv2.imwrite(output_image_path, final_image)

    return final_image

# Function to find image file
def find_image_file(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith(('.png', '.jpg', '.jpeg')):
            return os.path.join(directory, file_name)
    return None

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
    <button onclick="window.open('{file_link}')" style="background: linear-gradient(to right, #8B0000, #5C0000); color: #ffffff; border: none; border-radius: 5px; padding: 10px; width: 100%; margin-top: 5px;">Download Image</button>
    '''
    return button_html, file_link

# Function to post-process image
def post_process_function(image_path, final_image, index):
    output_directory = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_B/"
    output_image_path = os.path.join(output_directory, f"Rupantarak_B_{index}.png")
    cv2.imwrite(output_image_path, final_image)
    upload_button_html, file_link = upload_image_to_drive(output_image_path, os.path.basename(output_image_path))
    return upload_button_html, file_link

# Function to update the progress bar
def update_progress():
    progress_bar.value = 0
    for i in range(451):
        time.sleep(0.1)
        progress_bar.value = (i + 1) / 4.5  # Fake progress from 0 to 100 over 45 seconds

# Function to delete original target image
def delete_original_target(target_image):
    os.remove(target_image)

# Modify the run_process function to display image previews one by one
def run_process(_):
    with output:
        clear_output(wait=True)

        # Determine the selected execution provider
        execution_provider = "cpu" if execution_provider_radio.value == 'CPU' else "cuda"

        # Automatically fetch target images from the path
        target_images_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T"
        target_images = [os.path.join(target_images_path, file) for file in os.listdir(target_images_path) if file.endswith('.png')]

        for index, target_image in enumerate(target_images):
            # Black out areas except for faces
            blacked_target_image = fill_image_except_faces(target_image)

            # Delete existing output files
            output_directory = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_O"
            existing_output_files = [os.path.join(output_directory, file) for file in os.listdir(output_directory) if os.path.isfile(os.path.join(output_directory, file))]
            for file in existing_output_files:
                os.remove(file)

            # Start the progress bar at 1%
            progress_bar.value = 1

            # Increment the progress bar to 70% over 10 seconds
            for i in range(1, 71):
                progress_bar.value = i
                time.sleep(10 / 70)  # Sleep for 10/70 seconds between each increment

            # Run the deepfake process for each target image
            subprocess.run(["python", "/content/Rupantarak/run.py",
                            "-s", "/content/Rupantarak/Rupantarak_Pro/Rupantarak_S/Rupantarak_S.png",
                            "-t", blacked_target_image,
                            "-o", "/content/Rupantarak/Rupantarak_Pro/Rupantarak_O/Rupantarak_Output.png",
                            "--keep-frames",
                            "--keep-fps",
                            "--temp-frame-quality", "1",
                            "--output-video-quality", "1",
                            "--execution-provider", execution_provider,
                            "--frame-processor", "face_swapper", "face_enhancer"])

            # Fill the progress bar to 100%
            progress_bar.value = 100

            # Apply Poisson blending and post-process the deepfake image
            original_directory = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T"
            deepfake_directory = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_O"

            original_image_path = find_image_file(original_directory)
            deepfake_image_path = find_image_file(deepfake_directory)

            output_image_path = f"/content/Rupantarak/Rupantarak_Pro/Rupantarak_B/Rupantarak_B_{index}.png"

            final_image = replace_face_with_deepfake(original_image_path, deepfake_image_path, output_image_path)

            # Save the output image with the new path and name
            upload_button_html, file_link = post_process_function(output_image_path, final_image, index)

            # Delete the original target image
            delete_original_target(target_image)

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

# Create a button with height 55px and width 400px
button = widgets.Button(description="Start Rupantarak Image", layout=widgets.Layout(width='400px', height='55px', margin='auto'))

# Attach the function to the button click event
button.on_click(run_process)

# Create radio buttons for CPU and CUDA without a label
execution_provider_radio = widgets.RadioButtons(
    options=['CPU', 'CUDA'],
    disabled=False,
    layout={'width': 'max-content'}
)

# Create an accordion to hold the radio button options
accordion = widgets.Accordion(children=[execution_provider_radio])
accordion.set_title(0, 'Acceleration Options')

# Add the custom class to the accordion
accordion.add_class("custom-accordion")

# Center the accordion
accordion_container = widgets.HBox([accordion], layout=widgets.Layout(justify_content='center'))

# Add margin between accordion and Start button
button_accordion_container = widgets.VBox([button], layout=widgets.Layout(margin='5px 0'))

# Create a vertical box to hold the button and accordion with a margin of 5px
button_and_accordion_container = widgets.VBox([button_accordion_container, accordion_container], layout=widgets.Layout(margin='5px'))

# Create a progress bar widget
progress_bar = widgets.FloatProgress(value=0, min=0, max=100, style={'bar_color': '#4e54c8'}, layout=widgets.Layout(width='350px', margin='10px 0'))

# Create a container to hold the button, accordion, and progress bar
container = widgets.VBox([button_and_accordion_container, progress_bar], layout=widgets.Layout(justify_content='center', align_items='center'))

# Display the container and output widget
display(container)
display(output)
