# Custom CSS for gradient styles
gradient_button_css = """
<style>
body {
    background: linear-gradient(135deg, #111111, #111111);
}

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
    background-image: linear-gradient(to right, lightgreen, lightblue);
}

button {
    background: linear-gradient(to right, #0D47A1, #8E24AA); /* Dark blue to purple gradient */
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
    width: 300px; /* Fixed width */
}
button:hover {
    background-color: #abedd8;
    color: black;
}

/* Your custom CSS styles for the radio buttons */
.widget-radio-box label {
  background: linear-gradient(to right, #0D47A1, #8E24AA); /* Gradient from #800080 to #2196f3 */
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  color: white;
  margin-bottom: 10px; /* Add margin between options */
  width: 70px; /* Set width */
}

.gradient-link {
  background-image: linear-gradient(to right, #222222, #222222);
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
  background-image: linear-gradient(to right, #0D47A1, #8E24AA);
  box-shadow: 0px 0px 10px 0px rgba(181, 102, 184, 0.5);
}

.custom-accordion {
    width: 380px !important;
    margin: 10px auto !important;
    border-radius: 5px !important;
    background: linear-gradient(to right, #222222, #222222) !important;
    padding: 10px !important;
    z-index: 9999 !important;
}

.widget-container {
    border: none !important;
    background-color: #111111 !important; /* Background color changed */
    box-shadow: none !important;
    padding: 10px; /* Added padding */
    border-radius: 5px; /* Added border-radius */
}

.custom-accordion .custom-content {
    background-color: #111111 !important;
    padding: 5px;
}

.custom-image-container {
    background-color: #111111;
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
.custom-download-button {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    width: 100%;
    margin-top: 10px;
}
.image-slider {
    display: flex;
    overflow-x: auto;
    width: 100%;
    justify-content: center;
}

.widget-button {
    font-size: 16px !important;
    font-weight: bold !important;
}

.rounded-heading {
    background-color: #333333;
    color: white;
    padding: 5px 10px;
    border-radius: 10px;
    margin-bottom: 5px;
}
</style>
"""

# Inject custom CSS into the notebook
display(HTML(gradient_button_css))

# Define the custom CSS style
custom_css = """
<style>
/* Increase font size for labels */
.widget-label {
    font-size: 14px !important; /* Adjust the font size as needed */
}

/* Increase font size and make button text bold */
.widget-button {
    font-size: 16px !important; /* Adjust the font size as needed */
    font-weight: bold !important;
}

/* Increase font size for upload box text */
.upload-box-text {
    font-size: 14px !important; /* Adjust the font size as needed */
}


</style>
"""

# Inject the custom CSS into the notebook
display(HTML(custom_css))

