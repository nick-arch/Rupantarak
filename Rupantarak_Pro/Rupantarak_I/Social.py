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

