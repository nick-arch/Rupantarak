from IPython.display import display, HTML

# HTML code for divider and headings
html_code = """
<div style="width: 300px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
<div style="width: 100px; height: 20px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto 0; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 14px;">Step ~❷</span>
</div>
<div style="width: 300px; height: 40px; background-color: #222222; border-radius: 5px; text-align: center; font-weight: bold; margin: 10px auto; display: flex; justify-content: center; align-items: center;">
  <span style="color: white; font-size: 13px;">Run ~ रूपांतरक ~ Rupantarak ○~○ Image</span>
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
    width: 250px !important;
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
button = widgets.Button(description="Start Rupantarak Image", layout=widgets.Layout(width='300px', height='55px', margin='auto'))

# Attach the function to the button click event
button.on_click(run_process)

# Create a progress bar widget
progress_bar = widgets.FloatProgress(value=0, min=0, max=100, style={'bar_color': '#4e54c8'}, layout=widgets.Layout(width='300px', margin='10px 0'))

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


import os
import ipywidgets as widgets
from IPython.display import display, HTML, Javascript

# Create the reset button
reset_button = widgets.Button(
    description="Reset & Delete All Uploaded Target's",
    layout=widgets.Layout(width='300px', height='55px', margin='10px auto'),
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


# HTML code for divider and headings
html_code = """
<div style="width: 300px; height: 10px; background-color: #222222; border-radius: 5px; margin: 0 auto;"></div>
</div>
"""

# Display HTML
display(HTML(html_code))


