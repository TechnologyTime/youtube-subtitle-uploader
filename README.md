# youtube-subtitle-uploader
Upload subtitles with YouTube Subtitle Uploader

# How to setup?
<h2>It's so easy. You'll need Python (verion 3.13+) and a credentials (JSON file) from Google Cloud.</h2>
Here's a step-by-step documentation from Google Developers:<br>
https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred<br><br>
<b>Don't forget to add your account as a tester. Otherwise, the OAuth will block your access.</b>
<br>
To install Python, visit https://www.python.org/downloads/.

# How to upload a subtitle file?
<h2>Make sure your subtitle file extension is 
  <br>"srt", "vtt", "ttml", "scc", "mpsub", "sub", "lrc", "cap", "rt", "ytt", "dfxp", "stl", "tds", "cin", "asc"<br></h2>
<h4>For Broadcast file formats (TV and movies) ["scc", "stl", "tds", "cin", "asc","cap"], make sure the file is under complaince with CEA-608 or EBU-STL formats. Otherwise, the API will return an error.</h3>
Enter your video ID given after the https://youtu.be/ or https://www.youtube.com/. Remove the URL and other configuration such as "si" or "pp" or more. <br>
<img width="259" height="81" alt="image" src="https://github.com/user-attachments/assets/4b3e7cdb-a728-4804-a7e8-01eb5723b56a" />

