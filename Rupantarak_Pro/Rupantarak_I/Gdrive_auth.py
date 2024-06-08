

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
    background-color: #111111;
    border: 4px solid #222222;
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
auth_button = widgets.Button(description="Click To Authenticate Google Drive", layout=widgets.Layout(width='320px', height='60px'))
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
