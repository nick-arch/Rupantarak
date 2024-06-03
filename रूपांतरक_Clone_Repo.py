# @markdown

import base64
import subprocess
import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets
# नमस्ते रुद्रमन्यव उतोत इषवेनमः |
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
    background-image: linear-gradient(to right, #FA8072, #D8D8B4);
}
.custom-accordion {
    width: 380px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #FA8072, #F5F5DC) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}
.widget-container {
    border: none !important;
    background-color: #F5F5DC !important; /* Background color changed */
    box-shadow: none !important;
    padding: 10px; /* Added padding */
    border-radius: 5px; /* Added border-radius */
}
.custom-accordion .custom-content {
    background-color: #F5F5DC !important;
    padding: 5px;
}
</style>
"""
# नमः प्रत्नय तॊषया गिरिश विप्रेषया ॥१॥
display(HTML(gradient_button_css))

# नमः पिपिव्याया च अम्भया च अर्णवाया च |
def display_logo():
    logo_html = """
    <div style='text-align: center;'>    <h1 style='font-family: Andika, sans-serif; font-size: 50px; background: -webkit-linear-gradient(left, #FA8072, #F5F5DC); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'><span style='color: #ff0066;'>र</span><span style='color: #ff6f00;'>ू</span><span style='color: #ffjd00;'>प</span><span style='color: #4caf50;'>ा</span><span style='color: #2196f3;'>ं</span><span style='color: #9c27b0;'>त</span><span style='color: #ff5722;'>र</span><span style='color: #FFC0CB;'>क</span> <span style='color: #2196f3; font-size: 22px;'>~ Rupantarak</span><br><span style='font-size: 18px;'>By Vishal Sharma</span><br><span style='color: #ff0066; font-size: 22px;'>ॐ नमः पार्वती पतये, हर-हर महादेव:</span></h1>
    </div>    """
    display(HTML(logo_html))
# नमः शिवाय च शर्वाय च महादेवाय च |
display_logo()


import os
import subprocess
import re
import time
from ipywidgets import IntProgress, VBox, HTML
from IPython.display import display

# Function to check if the repository is already cloned
def is_repo_cloned(repo_url):
    # Extract repository name from the URL
    repo_name = repo_url.split("/")[-1].split(".")[0]
    
    # Check if the repository directory exists
    return os.path.exists(repo_name)

# Function to clone a git repository with a progress bar widget
def clone_repo_with_progress(repo_url):
    if is_repo_cloned(repo_url):
        # Repository already cloned, display progress bar at 100%
        progress_bar = IntProgress(min=0, max=100, value=100, bar_style='success')
        percentage_label = HTML("100%")
    else:
        # Create a progress bar widget with specific width and margin
        progress_bar = IntProgress(min=0, max=100, value=0, bar_style='info')
        progress_bar.style.description_width = 'initial'
        progress_bar.layout.margin = '10px 0px 0px 60px'  # Add 10px margin up, 100px left
        progress_bar.layout.width = '200px'  # Set the width to 200px

        # Create a label for the progress bar with bold text
        progress_label = HTML("<b>Cloning रूपांतरक ~ Rupantarak:</b>")
        progress_label.layout.margin = '0px 0px 0px 60px'  # Add 100px margin left

        # Create a label for the live percentage
        percentage_label = HTML("0%")
        percentage_label.layout.margin = '0px 0px 10px 60px'  # Add 10px margin down, 100px left

        # Combine the labels and progress bar in a vertical box
        vbox = VBox([progress_label, progress_bar, percentage_label])
        display(vbox)

        # Run the git clone command and simulate progress
        process = subprocess.Popen(
            ["git", "clone", repo_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        total_time = 3  # total time to simulate in seconds
        steps = 100  # total steps for progress bar
        sleep_time = total_time / steps  # time to sleep between steps

        for i in range(steps + 1):
            # Simulate waiting for the actual git clone progress
            time.sleep(sleep_time)

            # Normally here you would capture and parse real-time progress from git output
            # Updating the progress bar value and the percentage label
            progress_bar.value = i
            percentage_label.value = f"{i}%"

        process.wait()
        progress_bar.bar_style = 'success' if process.returncode == 0 else 'danger'

        if process.returncode != 0:
            raise Exception(f"Error cloning repository: {process.stderr.read()}")

# URL of the repository to clone
repo_url = "https://github.com/nick-arch/Rupantarak.git"

# Clone the repository with progress bar
clone_repo_with_progress(repo_url)


# Note 1
html_content_1 = '''
<div style="display: flex; justify-content: center; margin-top: 10px; margin-bottom: 10px;">
  <div style="width: 400px; margin: 10px 0;">
    <details id="details1">
      <summary id="summary1" style="border: none; border-radius: 8px; background: linear-gradient(to right, #FA8072, #F5F5DC); color: black; padding: 3px; text-align: center; cursor: pointer; list-style: none; font-weight: bold; margin-bottom: 10px;">
        <span id="arrow1">➼</span> <b>Must-Knows</b>
      </summary>
      <div style="border-radius: 8px; background-color: #333333; padding: 7px; color: white;">
        Hey there! Strap in for the GPU installation rodeo with our buddy रूपांतरक (Rupantarak). It's gonna be a wild 8-minute rollercoaster ride of tech wizardry. Grab some snacks, take a nap, or ponder life's mysteries while you wait. See you on the other side – hopefully with a shiny new GPU!
    </details>
  </div>
</div>
<script>
  var details1 = document.getElementById('details1');
  var arrow1 = document.getElementById('arrow1');
  details1.addEventListener('toggle', function(event) {
    if (details1.open) {
      arrow1.textContent = '➷';
    } else {
      arrow1.textContent = '➼';
    }
  });
</script>
'''

display(HTML(html_content_1))
