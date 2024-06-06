
from google.colab import drive
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import ipywidgets as widgets
from IPython.display import display, HTML

# Custom CSS for button styling
custom_css = """
<style>
.auth-button {
    background: linear-gradient(to right, #555555, #444444); /* Dark blue to purple gradient */
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
    width: 330px; /* Fixed width for authentication button */
}
</style>
"""

# HTML for custom CSS
custom_css_html = HTML(custom_css)
display(custom_css_html)

# Function to authenticate and authorize Google Drive access
def authenticate_drive(b):
    with output_auth:
        output_auth.clear_output()
        auth.authenticate_user()  # Perform authentication
        global drive_service
        drive_service = build('drive', 'v3')  # Build Drive service
        update_status()  # Update status after authentication

# Function to update LED indicator
def update_indicator(status):
    if status:
        return '<font size="3" color="green"><strong>&#9679;</strong></font>'  # Green
    else:
        return '<font size="3" color="red"><strong>&#9679;</strong></font>'  # Red

# Function to update status indicator
def update_status():
    if 'drive_service' in globals():
        status_indicator.value = update_indicator(True)  # Change status to green
    else:
        status_indicator.value = update_indicator(False)  # Change status to red

# Create button for authentication with dynamic size
auth_button = widgets.Button(description="Click To Authenticate Google Drive", layout=widgets.Layout(width='auto', height='100px', background_color='#FFB6C1', color='white'))
auth_button.style.font_weight = 'bold'
auth_button.on_click(authenticate_drive)
auth_button.add_class("auth-button")  # Apply custom CSS class

# Output widget for displaying status
output_auth = widgets.Output()

# Label for status
status_label = widgets.HTML(value="<strong>Status:</strong>", layout=widgets.Layout(font_weight='bold'))

# HTML widget for displaying LED indicator
status_indicator = widgets.HTML(layout=widgets.Layout(width='10px', height='10px'))

# Arrange status label and indicator side by side
status_box = widgets.HBox([status_label, status_indicator])

# Arrange button and status box vertically
button_status_box = widgets.VBox([auth_button, status_box])

# Function to display the collapsible note
def display_collapsible_note():
    # Define the content of the collapsible note
    note_content = """
    <details>
        <summary><strong>Permissions and File Access</strong></summary>
        <div style="border: 1px solid transparent; border-radius: 5px; padding: 10px;">
            <div style="border: 1px solid #CCCCCC; border-radius: 5px; padding: 10px;">
                <p><strong>Permissions Requested:</strong></p>
                <ul>
                    <li><strong>Read and write access to your Google Drive files and folders</strong></li>
                </ul>
                <p><strong>Why do we need these permissions?</strong></p>
                <p><strong>This notebook, <em>रूपांतरक ~ Rupantarak by Vishal Sharma</em>, requires access to your Google Drive to upload, download, and manage files as part of its functionality. Please note that only your account can access the processed files. Processed videos and images will be directly saved to your Google Drive account with private access permissions, ensuring that only you can access them.</strong></p>
            </div>
        </div>
    </details>
    """

    # Create the note widget
    note_widget = widgets.HTML(value=note_content)

    # Display the note
    display(note_widget)

# Display the widgets
display(button_status_box, output_auth)
display_collapsible_note()

# Check if authentication has already been completed
update_status()
