import cv2
import numpy as np
import base64
from IPython.display import display, HTML
from ipywidgets import widgets, VBox, HBox

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
        <img src='data:image/jpeg;base64,{}' style='border-radius: 50%; border: 4px linear-gradient(to right, #FA8072, #F5F5DC);'>
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
