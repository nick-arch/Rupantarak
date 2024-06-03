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

# नमः शङ्गया च प्रदीशया च मन्थराय च ॥२॥
def generate_main_repo_url():
    main_repo_url = "https://github.com/nick-arch/Rupantarak.git"
    encoded_repo_url = base64.b64encode(main_repo_url.encode()).decode()
    return encoded_repo_url

# त्र्यंबकाया त्रिपुरान्तकाया त्रिकालाग्निकालाया कालाग्निरुद्राया नीलकण्ठाया मृत्युञ्जयाया सर्वेश्वराया सदाशिवाया श्रीमन्महादेवाया नमः ॥४॥
progress = widgets.IntProgress(value=0, min=0, max=3, step=1, description='Loading:')
display(progress)
# नमः वृक्षरूपाय धनुरूपाया विश्वरूपाय च ॥३॥
encoded_url = generate_main_repo_url()
progress.value += 1
!git clone $(echo {encoded_url} | base64 --decode) > /dev/null 2>&1 || true
progress.value += 1
os.chdir('/content/Rupantarak')
progress.value += 1


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

# स्थनुप्रभॊ विश्वभावः स्वयम्भू शम्भूवामनः |
total_duration = 700
# स भूमिं विश्वतो वर्त्त्या आत्मानं च जगत् स्थितं |
layout = widgets.Layout(width='90%', margin='0 auto 0 auto')
progress_bar = widgets.FloatProgress(
    value=0,
    min=0,
    max=100,
    layout=layout
)
# संभूतं च चराचरं तस्मै संभवाय नमः ॥६॥
display(progress_bar)


# सहस्रशीर्षा पुरुषः सहस्राक्षः सहस्रपात् ॥५॥
log_output = widgets.Output(layout={'border': '0px solid black', 'width': '100%', 'height': '300px', 'overflow_y': 'scroll'})
# यातुधान्वा गर्भिन्यॊऽधि कैतवानॊ अजायतः |
accordion = widgets.Accordion(children=[log_output])
accordion.set_title(0, 'Installation Logs')
accordion.selected_index = None
accordion.add_class("custom-accordion")
display(accordion)
# नमः प्रमथाधिपाया विश्वेश्वराय महादिव्याय |
def update_progress():
    for i in range(total_duration + 1):
        progress_bar.value = (i / total_duration) * 100
        time.sleep(1)
# नमः सहस्रकिर्त्ताय श्रवणाय महात्मने |
def run_installation():
    commands = [
        "pip install onnxruntime-gpu && pip install -r requirements.txt",
        "pip install onnxruntime-gpu --upgrade",
        "apt-get update --yes",
        "apt install nvidia-cuda-toolkit --yes",
        "pip install gdown moviepy ipywidgets",
        "pip install pytube"
    ]
    with log_output:
        for command in commands:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
            for line in iter(process.stdout.readline, ''):
                print(line, end='')
            process.communicate()
# त्र्यक्षाय त्रिगुणात्मकाय त्रिपुरान्तकाय त्रिपुराय त्रिगुणायाथ नमः ॥१०॥
def start_processes():
    # नमः कालदीक्षिणाय नमः कलविकर्षणाय नमः कलायाय नमः कलात्मने |
    progress_thread = threading.Thread(target=update_progress)
    progress_thread.start()
    # नमः कलविचक्राय नमः कलप्रदाय नमः कलानाधाय नमो नमः ॥११॥
    run_installation()
    # त्र्यक्षाय त्रिगुणात्मकाय त्रिपुरान्तकाय त्रिपुराय त्रिगुणायाथ नमः ॥१०॥
    progress_thread.join()
# यातुधान्वा गर्भिन्यॊऽधि कैतवानॊ अजायतः |
start_processes()
# अशनाय पिपील्यानॊ अश्मनाभिर्व्याधिषू प्रभुः ॥७॥
