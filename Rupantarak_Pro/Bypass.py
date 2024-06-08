
from IPython.display import display, HTML
import ipywidgets as widgets
import cv2
import numpy as np
import os
import subprocess
import time
import base64
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from PIL import Image as PILImage

# Load Google Fonts
font_link = """
<link href="https://fonts.googleapis.com/css2?family=Bree+Serif&display=swap" rel="stylesheet">
"""
display(HTML(font_link))

# Define custom CSS styles
custom_css = """
<style>
/* Set Bree Serif font for all elements */
body, button, label, .popup-message h2, .popup-message p {
    font-family: 'Bree Serif', serif;
}


/* Customize progress bar */
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
    background-image: linear-gradient(to right, #FF5733, #FF0000);
}

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
    background: linear-gradient(to right, #FF0000, #FF5733); /* Darker gradient on click */
    transform: scale(0.75); /* Slightly decrease size */
}

/* Customize radio buttons */
.widget-radio-box {
    display: flex;
    flex-direction: column;
}

.widget-radio-box label {
    background: linear-gradient(to right, #444444, #555555);
    border-radius: 20px;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.3s ease;
    color: white;
    margin-bottom: 10px;
    width: 100px;
    display: inline-block;
    padding: 10px;
    text-align: center;
}

/* Radio button container */
.widget-radio-box {
  display: flex;
  flex-direction: column;
}

/* Custom styles for radio button labels */
.widget-radio-box label {
  background: linear-gradient(to right, #FF5733, #FF0000); /* Gradient colors */
  border-radius: 20px; /* Rounded corners */
  cursor: pointer;
  transition: background 0.3s ease, transform 0.3s ease; /* Transition effect duration */
  color: white; /* Text color */
  margin-bottom: 10px; /* Add margin between options */
  width: 113px; /* Set width */
  display: inline-block; /* Display as inline-block */
  padding: 10px; /* Add padding */
  text-align: center; /* Center text */
}

/* Hover effect for radio button labels */
.widget-radio-box label:hover {
  background: linear-gradient(to right, #FF0000, #FF5733); /* Reverse gradient on hover */
  transform: scale(1.00); /* Slightly increase size */
}

/* Click effect for radio button labels */
.widget-radio-box label:active {
  background: linear-gradient(to right, #800000, #8B4513); /* Darker gradient on click */
  transform: scale(0.75); /* Slightly decrease size */
}


/* Accordion container */
.custom-accordion {
    width: 190px !important; /* Set width */
    margin: 10px auto !important; /* Center horizontally */
    border-radius: 5px !important; /* Rounded corners */
    background: linear-gradient(to right, #FF5733, #FF0000) !important; /* Gradient colors */
    padding: 10px !important; /* Add padding */
    z-index: 9999 !important; /* Ensure it's on top of other elements */
}




.widget-button {
    font-size: 16px !important;
    font-weight: bold !important;
}

/* Customize heading */
.rounded-heading {
    background-color: #333333;
    color: white;
    padding: 5px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}

.popup-message h2 {
    color: #222222;
}

.popup-message p {
    color: #333333;
}

</style>
"""

# Inject custom CSS into the notebook
display(HTML(custom_css))

from IPython.display import HTML, display

# Define the CSS style for the popup messages
popup_style = """
<style>
    /* Popup message background gradient */
    .popup-message {
        background: linear-gradient(to right, #222222, #222222); /* Gradient colors */
        padding: 20px; /* Add padding */
        border-radius: 10px; /* Rounded corners */
        text-align: center; /* Center text */
        color: white; /* Text color */
    }
</style>
"""

# Display the CSS style
display(HTML(popup_style))

# Rest of the code...

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



html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Page Title</title>
  <style>
    /* Add your custom CSS styles here */
  </style>
</head>
<body>

<div style="width: 330px; height: 5px; background-image: linear-gradient(90deg, #222222, #222222); border-radius: 5px; margin: 0 auto;"></div>
<div style="width: 350px; height: 40px; text-align: center; margin: 10px auto; display: flex; justify-content: center; align-items: center; background-color: #222222; border-radius: 20px;">
  <span style="color: white; font-size: 18px; background-image: linear-gradient(90deg, #FF5733, #FF0000); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">रूपांतरक ~ Ꮢᥙραɳ𝜏αɾαƙ ᑌᑎᑕᗴᑎᔕᗝᖇᗴᗪ</span>
</div>

<!-- Your other HTML content and functions go here -->

</body>
</html>
"""

display(HTML(html_code))




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
    <button onclick="window.open('{file_link}')" style="background: linear-gradient(to right, #FF5733, #FF0000); color: #ffffff; border: none; border-radius: 5px; padding: 10px; width: 250px; margin-top: 5px;">Download Image</button>
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

import cv2
import numpy as np
from IPython.display import display, HTML

from IPython.display import display, HTML

# Function to display a popup message with gradient header
def display_popup_message(message, width='250px', height='60px', background_color='#111111', border_color='#222222', text_color='#333333'):
    if message.startswith("Success"):
        text_color = '#008000'  # Green color for success messages
    elif message.startswith("No target"):
        text_color = '#222222' # Red color for no target messages

    popup_html = f"""
    <style>
        .popup-message {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: {background_color};
            border: 2px solid {border_color};
            border-radius: 10px;
            width: {width};
            height: {height};
            padding: 20px;
            text-align: center;
            z-index: 9999;
        }}
        .popup-message h2 {{
            background: linear-gradient(to right, #FF5733, #FF0000);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .popup-message p {{
            color: {text_color};
        }}
    </style>
    <div class="popup-message">
        <h2>{message}</h2>
    </div>
    <script>
        setTimeout(function(){{
            var popup = document.querySelector('.popup-message');
            if (popup) {{
                popup.remove();
            }}
        }}, 3000);  // Hide popup after 3 seconds
    </script>
    """
    display(HTML(popup_html))


import os
import subprocess
import time
import base64
import cv2
import numpy as np
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets

# Define the output widget
output = widgets.Output()

# Modify the run_process function to display a popup message
def run_process(_):
    with output:
        clear_output(wait=True)

        # Display popup message
        display_popup_message("Processing started...")

        # Determine the selected execution provider
        execution_provider = "cpu" if execution_provider_radio.value == 'CPU' else "cuda"

        # Automatically fetch target images from the path
        target_images_path = "/content/Rupantarak/Rupantarak_Pro/Rupantarak_T"
        target_images = [os.path.join(target_images_path, file) for file in os.listdir(target_images_path) if file.endswith('.png')]

        if not target_images:
            display_popup_message("No target images found!", background_color='#FFCCCC', border_color='#FF0000')
            return

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
            <div style="background-color: #383838; padding: 20px; text-align: center;">
                <details>
                    <summary style="font-weight: bold; background-color: #222222; padding: 10px; border-radius: 5px;">Click to Preview Image {index + 1}</summary>
                    <div style="background-color: #222222; border-radius: 5px; padding: 10px; max-width: 300px; margin: 0 auto;">
                        <img src="data:image/jpeg;base64,{encoded_string}" style="border-radius: 5px; max-width: 100%;"/>
                        {upload_button_html}
                    </div>
                </details>
            </div>
            """

            display(HTML(html_code))

        # Display success message after processing all images
        display_popup_message("Process completed successfully!")

# Create a button with height 55px and width 400px
button = widgets.Button(description="Start ~ Ꮢᥙραɳ𝜏αɾαƙ ᑌᑎᑕᗴᑎᔕᗝᖇᗴᗪ", layout=widgets.Layout(width='300px', height='55px', margin='auto'))

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
progress_bar = widgets.FloatProgress(value=0, min=0, max=100, style={'bar_color': '#4e54c8'}, layout=widgets.Layout(width='300px', margin='10px 0'))

# Create a container to hold the button, accordion, and progress bar
container = widgets.VBox([button_and_accordion_container, progress_bar], layout=widgets.Layout(justify_content='center', align_items='center'))

# Display the container and output widget
display(container)
display(output)


from IPython.display import HTML, display

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Page Title</title>
  <style>
    /* Add your custom CSS styles here */
  </style>
</head>
<body>

<div style="width: 330px; height: 5px; background-image: linear-gradient(90deg, #222222, #222222); border-radius: 5px; margin: 0 auto;"></div>
</div>

<!-- Your other HTML content and functions go here -->

</body>
</html>
"""

display(HTML(html_code))

# @markdown
