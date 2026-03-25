# youtube-subtitle-uploader
Upload subtitles with YouTube Subtitle Uploader

# How to setup?
<h2>It's so easy. You'll need Python (verion 3.13+) and a credentials (JSON file) from Google Cloud.</h2>
Here's a step-by-step documentation from Google Developers:<br>
https://developers.google.com/youtube/registering_an_application<br><br>
<b>Don't forget to add your account as a tester. Otherwise, the OAuth will block your access.</b>
<br>
To install Python, visit https://www.python.org/downloads/.

# How to upload a subtitle file?
<h2>Make sure your subtitle file extension is 
  <br>"srt", "vtt", "ttml", "scc", "mpsub", "sub", "lrc", "cap", "rt", "ytt", "dfxp", "stl", "tds", "cin", "asc"<br></h2>
<h4>For Broadcast file formats (TV and movies) ["scc", "stl", "tds", "cin", "asc","cap"], make sure the file is under complaince with CEA-608 or EBU-STL formats. Otherwise, the API will return an error.</h3>
<br>
<br>
1. Copy your video ID by clicking "Share" button and truncate the URLs like https://youtu.be/ or https://www.youtube.com/ , and remove other configurations such as "si" or "pp" or more. <br>
<img width="259" height="81" alt="image" src="https://github.com/user-attachments/assets/4b3e7cdb-a728-4804-a7e8-01eb5723b56a" />
<br>
2. Download the main.py and store where the clint_secret.json file is located. Copy the main.py as a path.
3. Open up the Command Prompt and change the directory where the subtitle file is located.
4. Paste the path. If you're greeted with <i>client_secrets.json file is found. Good</i>, type the subtitle name and its extension.
5. You'll be greeted with a OAuth page. Ignore all the warnings and click <i>Continue</i>.
6. Paste the video ID, and enter the subtitle language. You can find it here: https://developers.google.com/workspace/admin/directory/v1/languages
7. If you want, you can name the track. If you don't want to, you can leave it and press Enter.
8. Congrats! You have finally uploaded your subtitle. If the API returns an error, try checking the permissions in the Credential page in Google Cloud.

If you have any other issues, DM me on Discord: realtechnologytime69

