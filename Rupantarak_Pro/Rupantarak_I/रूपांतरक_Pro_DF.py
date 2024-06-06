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
    width: 300px !important;
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










from IPython.display import HTML

# Define the link and JavaScript code
link = "https://shulugoo.net/4/7464140"
js_open_new_tab = f'<script>window.open("{link}", "_blank");</script>'

# Display the link with JavaScript embedded
display(HTML(js_open_new_tab))









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
    display_width = '350px'

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
    display_width = '330px'

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
        <div id="note_content" style="display: block; background: #222222; border-radius: 5px; padding: 10px; text-align: center; width: 300px; margin: 0 auto;">
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
progress_label = widgets.Label(value='', layout=widgets.Layout(font_weight='bold', width='300px', text_align='center'))
progress_bar = widgets.FloatProgress(value=0.0, min=0.0, max=1.0, step=0.01, layout=widgets.Layout(width='300px', margin='20px auto'))
time_remaining_label = widgets.Label(value='', layout=widgets.Layout(font_weight='bold', width='300px', text_align='center'))



# Button to start the deepfake process with custom style
run_button = widgets.Button(
    description="Start Rupantarak",
    button_style='success',
    layout=widgets.Layout(width='300px', height='55px', margin='25px auto'),
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
], layout=widgets.Layout(width='330px', margin='auto', align_items='center', border='2px solid #111111', border_radius='5px'))
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
