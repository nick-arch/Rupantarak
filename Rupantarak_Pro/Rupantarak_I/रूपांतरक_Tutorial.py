# @markdown
from IPython.display import HTML, display

# YouTube video ID
video_id = 'jDCPmySzePw'

# YouTube video URL with required parameters
youtube_url = f'https://www.youtube.com/embed/{video_id}?controls=0&autoplay=1&loop=1&mute=1&playlist={video_id}'

# HTML for the collapsible section with styled button and video container
html_code = f"""
<div style="text-align: center; margin-bottom: 10px;">
  <button style="
      font-weight: bold;
      width: 350px;
      height: 40px;
      border-radius: 15px;
      background: linear-gradient(to right, #FFA500, #FF0000);
      color: white;
      border: none;
      cursor: pointer;
  " type="button" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display=='none'?'block':'none';">
    रूपांतरक ~ Rupantarak ○ Tutorial
  </button>
  <div style="display:none; margin-top: 10px;">
    <div style="
        display: inline-block;
        background-color: #222222;
        border-radius: 15px;
        padding: 10px;
    ">
      <iframe style="
          border-radius: 15px;
      " width="380" height="852" src="{youtube_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
</div>
"""

# Display the HTML
display(HTML(html_code))
