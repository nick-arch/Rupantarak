
import os
from IPython.display import display, HTML
import ipywidgets as widgets

def display_file_not_found_popup():
    popup_html = """
    <style>
        body {
            background-color: #111111;
        }
        .popup-container {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 330px;
            height: 220px;
            background-color: #222222;
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .file-not-found-popup {
            width: 100%;
            height: 100%;
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .file-not-found-popup h2 {
            color: #ff0066;
            margin: 0;
            padding: 0;
        }
        .file-not-found-popup p {
            color: white;
            margin: 10px 0;
        }
        .file-not-found-popup button {
            background-color: #FA8072;
            border: none;
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    <div class="popup-container">
        <div class="file-not-found-popup">
    <h2>रूपांतरक ~ Rupantarak Uncensored Not Found!</h2>
    <p>Please unlock the Python file first to use रूपांतरक ~ Rupantarak Uncensored.</p>
    <p>If you don't have the password, please contact me via the feedback form above.</p>
</div>
    </div>
    <script>
        function closePopup() {
            var popup = document.querySelector('.popup-container');
            popup.style.display = 'none';
        }
    </script>
    """
    display(HTML(popup_html))

def run_python_script(script_path):
    if os.path.isfile(script_path):
        %run $script_path
    else:
        # Create a fixed-size container
        container = widgets.Output(layout={'width': '300px', 'height': '240px'})
        display(container)
        
        with container:
            display_file_not_found_popup()

# Example usage
script_path = '/content/Rupantarak/Rupantarak_Pro/Rupantarak_I/unzipped/रूपांतरक_Bypass.py'
run_python_script(script_path)
