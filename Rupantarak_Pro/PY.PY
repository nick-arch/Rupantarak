
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

# Define the output widget
output = widgets.Output()

# Rest of the code...

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
    background-image: linear-gradient(to right, #FF007F, #800080);
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

/* Container for the radio buttons */
.widget-radio-box {
  display: flex;
  flex-direction: column;
}

/* Your custom CSS styles for the radio buttons */
.widget-radio-box label {
  background: linear-gradient(to right, #222222, #222222); /* Gradient from dark grey to lighter grey */
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
  background: linear-gradient(to right, #FF007F, #800080); /* Slightly lighter gradient on hover */
  transform: scale(1.05); /* Slightly increase size */
}

/* Active effect */
.widget-radio-box label:active {
  background: linear-gradient(to right, #FF007F, #800080); /* Darker gradient on click */
  transform: scale(0.95); /* Slightly decrease size */
}



/* Selected radio button effect */
.widget-radio-box input[type="radio"]:checked + label {
  background: linear-gradient(to right, #FF007F, #800080); /* Different gradient for selected state */
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
  background-image: linear-gradient(to right, #FF007F, #800080);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}

.custom-accordion {
    width: 210px !important;
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

<div style="width: 330px; height: 5px; background-image: linear-gradient(90deg, #FF007F, #800080); border-radius: 5px; margin: 0 auto;"></div>
<div style="width: 350px; height: 40px; text-align: center; margin: 10px auto; display: flex; justify-content: center; align-items: center; background-color: #000000; border-radius: 20px;">
  <span style="color: white; font-size: 18px; background-image: linear-gradient(90deg, #FF007F, #800080); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: bold;">Run रूपांतरक ~ Rupantarak Uncensored</span>
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
    <button onclick="window.open('{file_link}')" style="background: linear-gradient(to right, #FF007F, #800080); color: #ffffff; border: none; border-radius: 5px; padding: 10px; width: 250px; margin-top: 5px;">Download Image</button>
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

# Function to display a popup message
# Function to display a popup message
def display_popup_message(message, background_color='#F5F5DC', border_color='#FA8072', text_color='#333333'):
    if message.startswith("Success"):
        text_color = '#008000'  # Green color for success messages
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
            padding: 20px;
            text-align: center;
            z-index: 9999;
        }}
        .popup-message h2 {{
            color: #ff0066;
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
            <div style="background-color: #111111; padding: 20px; text-align: center;">
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
button = widgets.Button(description="Start Rupantarak Image", layout=widgets.Layout(width='300px', height='55px', margin='auto'))

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


def display_popup_message(message, success=False, background_color='#000000', border_color='#333333', text_color='#FFFFFF'):
    text_color_start = '#FF007F' if not success else '#008000'
    text_color_end = '#800080' if not success else '#00FF00'
    message_class = 'bypass' if not success else 'unlocked'

    popup_html = f"""
    <style>
        .popup-message {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: {background_color};
            border: 10px solid {border_color}; /* Solid color border */
            border-radius: 20px; /* Rounded corners */
            width: 250px;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            z-index: 9999;
        }}
        .popup-message .bypass {{
            font-weight: bold;
            background: -webkit-linear-gradient({text_color_start}, {text_color_end});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }}
        .popup-message .unlocked {{
            font-weight: bold;
            background: -webkit-linear-gradient(#008000, #00FF00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }}
    </style>
    <div class="popup-message">
        <h2><span class="{message_class}">{message}</span></h2>
    </div>
    <script>
        setTimeout(function(){{
            var popup = document.querySelector('.popup-message');
            if (popup) {{
                popup.remove();
            }}
        }}, 4000);  // Hide popup after 4 seconds
    </script>
    """
    display(HTML(popup_html))


# Display the container and output widget
display(container)
display(output)
display_popup_message("रूपांतरक ~ Bypass Unlocked Successfully")


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

<div style="width: 330px; height: 5px; background-image: linear-gradient(90deg, #FF007F, #800080); border-radius: 5px; margin: 0 auto;"></div>
</div>

<!-- Your other HTML content and functions go here -->

</body>
</html>
"""

display(HTML(html_code))
