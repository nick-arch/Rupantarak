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
