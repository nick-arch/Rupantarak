
import base64
import subprocess
import time
import threading
import os
from IPython.display import display, HTML
import ipywidgets as widgets

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
