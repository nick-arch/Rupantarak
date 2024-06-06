

import base64
import requests
from IPython.display import display, HTML

# Function to encode image to base64
def encode_image_to_base64(url):
    response = requests.get(url)
    encoded_image = base64.b64encode(response.content).decode('utf-8')
    return encoded_image

# Public Google Drive URL for the image
image_url = "https://drive.google.com/uc?id=11C4SDoWfvJOXeNn0Luv0YZGuHaJrHkBH"

# Encode the image from the URL to base64
encoded_image = encode_image_to_base64(image_url)

# Define the CSS style for the image
image_style = """
<style>
.centered-image {
    display: block;
    margin-left: auto;
    margin-right: auto;
    border: 10px solid #444444;
    border-radius: 50%; /* Set border-radius to 50% to make it a circle */
    overflow: hidden; /* Ensure the border touches the corners */
}
</style>
"""

# Define the HTML markup for the image
image_html = f"""
<div style="text-align: center;">
  <img src="data:image/jpeg;base64,{encoded_image}" class="centered-image" width="100">
</div>
"""

# Display the image
display(HTML(image_style + image_html))
import ipywidgets as widgets
from IPython.display import display, HTML

# Define the paragraph style with centered alignment and width
paragraph_style = """
<div style="width: 350px; margin: auto;">
  <p style="font-size: 15px; color: #F5F5DC; font-weight: bold; text-align: center;">I'm Vishal Sharma, and I've created a modified GUI version of the tool "रूपांतरक ~ Rupantarak," which I copied from the original Roop repository by "Somdev Sangwan", enhancing it with several improved filters.</p>
</div>
"""

# Define the CSS style for the buttons
button_style = """
<style>
.rounded-button {
    border: none;
    color: white;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 13px;
    margin: 4px 22px;
    cursor: pointer;
    border-radius: 12px;
    width: 150px;
    height: 50px;
    background: linear-gradient(45deg, #24292e, #6e5494);
    font-weight: bold;
}
</style>
"""

# HTML markup for the buttons
html_buttons = """
<div style="display: flex; justify-content: center;">
  <button class="rounded-button" onclick="window.open('https://github.com/s0md3v/roop.git','_blank')">Original Roop Repository</button>
  <button class="rounded-button" onclick="window.open('https://github.com/nick-arch/Rupantarak.git','_blank')">Your Rupantarak Repository</button>
</div>
"""

# Combine the paragraph, style, and buttons
html_content = paragraph_style + button_style + html_buttons

# Display the content
display(HTML(html_content))





from IPython.display import HTML
import webbrowser

# Define button styles
button_style = 'width: 100px; height: 40px; border-radius: 5px; border: none; cursor: pointer; margin: 20px; color: white;'

# Define gradients for each button
gradient_styles = [
    'background: linear-gradient(90deg, #833ab4, #fd1d1d, #fcb045);',  # Instagram colors
    'background: linear-gradient(90deg, #0077b5, #1E90FF);',          # LinkedIn colors
    'background: linear-gradient(90deg, #24292e, #6e5494);'           # GitHub colors
]

# Define link URLs
links = ['https://www.instagram.com/nick_corbin_07?igsh=ZnA5d2Zhd3R3eXNt', 'https://www.linkedin.com/in/vishalsharma07', 'https://github.com/nick-arch']

# Define button labels
button_labels = ['Instagram', 'LinkedIn', 'GitHub']

# Define button click functions
def open_link(link):
    def open_link_func(_):
        webbrowser.open(link)
    return open_link_func

# Create buttons HTML
buttons_html = ''
for i, (gradient_style, label, link) in enumerate(zip(gradient_styles, button_labels, links)):
    button_html = f'<button style="{button_style}{gradient_style}" onclick="window.open(\'{link}\')">'
    button_html += f'<span style="font-weight: bold;">{label}</span></button>'
    buttons_html += button_html

# Center the buttons using HTML styling
centered_buttons_html = f"""
<div style="display: flex; justify-content: center;">
    {buttons_html}
</div>
"""

# Display the centered buttons
display(HTML(centered_buttons_html))



from IPython.display import display, HTML
import ipywidgets as widgets

# Custom CSS for gradient styles
gradient_button_css = """
<style>
.custom-accordion {
    width: 350px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #444444, #444444) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}

.widget-container {
    border: none !important;
    background-color: linear-gradient(to right, #444444, #444444) !important;
    box-shadow: none !important;
    padding: 10px; /* Added padding */
    border-radius: 5px; /* Added border-radius */
}

.custom-accordion .custom-content {
    background-color: linear-gradient(to right, #444444, #444444) !important;
    padding: 5px;
}

.custom-image-container {
    background-color: linear-gradient(to right, #444444, #444444) !important;
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

</style>
"""

# Inject custom CSS into the notebook
display(HTML(gradient_button_css))

# PayPal integration script
paypal_script = """
<script src="https://www.paypal.com/sdk/js?client-id=BAAV8njGbz3QGKORLv3DqieB3kTnW-z4KT2sllTMdy9JtX4I_dwxhpzuMkJNwkA71YjxJHOThcfX_sJvXI&components=hosted-buttons&disable-funding=venmo&currency=USD"></script>
<div id="paypal-container-RSGF46P7UMRNW"></div>
<script>
  paypal.HostedButtons({
    hostedButtonId: "RSGF46P7UMRNW",
  }).render("#paypal-container-RSGF46P7UMRNW")
</script>
"""

# Create an HTML widget with the PayPal script
paypal_widget = widgets.HTML(value=paypal_script)

# Create an accordion to contain the widget
accordion = widgets.Accordion(children=[paypal_widget])

# Set the title of the accordion
accordion.set_title(0, 'Support Development')

# Apply custom styling to the accordion
accordion.add_class("custom-accordion")

# Display the accordion
display(accordion)


import ipywidgets as widgets
from IPython.display import display, HTML
import requests
import time

gradient_button_css = """
<style>
.gradient-link {
  background-image: linear-gradient(to right, #444444, #444444);
  border: none;
  border-radius: 10px;
  padding: 10px 10px;
  color: #F5F5DC;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.gradient-link:hover {
  background-image: linear-gradient(to right, #FA8072, #F5F5DC);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}

.rounded-heading {
    background-color: #333333;
    color: white;
    padding: 5px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}

.heading {
    text-align: center;
    color: #F5F5DC;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
"""

# Inject custom CSS into the notebook
display(HTML(gradient_button_css))

# Define the heading
heading = widgets.HTML("<div class='heading'>रूपांतरक ~ Feedback</div>")

# Define the form fields
name_field = widgets.Text(
    value='',
    placeholder='Your Name',
    description='Your Name:',
    disabled=False,
    layout=widgets.Layout(width='350px', margin='10px 0'),
    style={'description_width': 'initial'}
)
name_field.add_class("gradient-link")

feedback_field = widgets.Textarea(
    value='',
    placeholder='Your Feedback',
    description='Feedback:',
    disabled=False,
    layout=widgets.Layout(width='350px', height='auto', margin='10px 0'),
    style={'description_width': 'initial'}
)
feedback_field.add_class("gradient-link")

email_field = widgets.Text(
    value='',
    placeholder='Email (Optional)',
    description='Email:',
    disabled=False,
    layout=widgets.Layout(width='350px', margin='10px 0'),
    style={'description_width': 'initial'}
)
email_field.add_class("gradient-link")

submit_button = widgets.Button(
    description='Submit',
    disabled=False,
    button_style='success',
    layout=widgets.Layout(width='350px', height='50px', margin='10px 0')  # Set width, height, and margin
)
submit_button.add_class("gradient-link")

output_field = widgets.Output(layout={'visibility': 'hidden'})  # Hide output by default

# Define the submit function
def on_submit(b):
    with output_field:
        output_field.clear_output()
        name = name_field.value.strip()
        feedback = feedback_field.value.strip()
        email = email_field.value.strip()

        if not name or not feedback:
            print("Name and Feedback are required fields and cannot be empty.")
            return

        # Construct the URL to submit the form
        form_id = '1FAIpQLSd3CQpBkn5_yGRPocSNVkXy6Lx_W5xI0X5z6MVzgzn31wOodw'
        url = f"https://docs.google.com/forms/d/e/{form_id}/formResponse"
        data = {
            'entry.1395913307': name,  # Replace with the actual entry ID for the 'Your Name' field
            'entry.2005839779': feedback,  # Replace with the actual entry ID for the 'Feedback' field
            'entry.1744226297': email  # Replace with the actual entry ID for the 'Email' field
        }

        # Submit the form
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Form submitted successfully!")
            output_field.layout.visibility = 'visible'  # Show output
            # Clear fields
            name_field.value = ''
            feedback_field.value = ''
            email_field.value = ''
            # Hide success message after 2 seconds
            time.sleep(2)
            output_field.layout.visibility = 'hidden'
        else:
            print("Failed to submit the form.")
            print(f"Status code: {response.status_code}")
            print(f"Response: {response.text}")

submit_button.on_click(on_submit)

# Define a VBox to contain the form
form_container = widgets.VBox([
    heading,
    name_field,
    feedback_field,
    email_field,
    submit_button,
    output_field
], layout=widgets.Layout(align_items='center'))  # Display form

# Display the form container
display(form_container)
