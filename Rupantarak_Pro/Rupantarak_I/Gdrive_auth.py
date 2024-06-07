
from google.colab import drive
from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import ipywidgets as widgets
from IPython.display import display, HTML

# Custom CSS for button styling and popups
custom_css = """
<style>
.auth-button {
    background: linear-gradient(to right, #555555, #444444);
    border-radius: 20px;
    border: none;
    color: white;
    padding: 0; /* Removed padding */
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 18px;
    font-weight: bold;
    margin: 4px 2px;
    cursor: pointer;
    transition-duration: 0.4s;
    width: 300px;
    height: 60px;
    line-height: 60px; /* Center text vertically */
}
.popup {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #F5F5DC;
    border: 2px solid #FA8072;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    z-index: 1000;
    width: 250px;
    height: 70px;
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
</style>
"""

# HTML for custom CSS
custom_css_html = HTML(custom_css)
display(custom_css_html)

# Function to display the success popup
def display_success_popup():
    success_html = """
    <div class="popup" id="success-popup">
        <h2 style="color: green;">Successfully Authenticated</h2>
        <p style="color: green;">Google Drive access has been granted, You can now use Rupantarak GUI.</p>
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
auth_button = widgets.Button(description="Click To Authenticate Google Drive", layout=widgets.Layout(width='320px', height='60px'))
auth_button.style.font_weight = 'bold'
auth_button.on_click(authenticate_drive)
auth_button.add_class("auth-button")  # Apply custom CSS class

# Output widget for displaying status
output_auth = widgets.Output()

# Label for status
status_label = widgets.HTML(value="<strong>Status:</strong>", layout=widgets.Layout(font_weight='bold'))

# HTML widget for displaying LED indicator
status_indicator = widgets.HTML(layout=widgets.Layout(width='10px', height='10px'))

# Arrange status label and indicator side by side, centered
status_box = widgets.HBox([status_label, status_indicator], layout=widgets.Layout(justify_content='center'))

# Arrange button and status box vertically, centered
button_status_box = widgets.VBox([auth_button, status_box], layout=widgets.Layout(align_items='center'))

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

    # Display the note, centered
    display(widgets.HBox([note_widget], layout=widgets.Layout(justify_content='center')))

# Display the widgets
display(button_status_box, output_auth)
display_collapsible_note()

# Check if authentication has already been completed
update_status()
