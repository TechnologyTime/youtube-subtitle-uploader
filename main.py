import subprocess
import platform
import os
import google_auth_oauthlib.flow
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
import google.auth.exceptions
import sys
import googleapiclient.discovery
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
base_path = os.path.dirname(os.path.realpath(__file__))
client_secrets_path = os.path.join(base_path, 'client_secrets.json')
def authenticate_youtube():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_path, SCOPES)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube
def upload_subtitle(video_id, file_path, language='en', name='en'):
    media = MediaFileUpload(file_path, mimetype='text/plain', resumable=True)

    request = youtube.captions().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "language": language,
                "name": name,
                "isDraft": False
            }
        },
        media_body=media
    )
    
    response = request.execute()
    print(f"Subtitle uploaded! ID: {response['id']}")
def clear_screen():
    system = platform.system().lower()
    if system == 'windows':
        subprocess.run(['cls'], shell=True)
    else:
        subprocess.run(['clear'], shell=True)
if os.path.exists(client_secrets_path):
     print("client_secrets.json file is found. Good!")
else:
     print("client_secrets.json file is missing. Refer 'https://developers.google.com/identity/protocols/oauth2/web-server#creatingcred' to create a json file.")
     sys.exit()
     
formats = ["srt", "vtt", "ttml", "scc", "mpsub", "sub", "lrc", "cap", "rt", "ytt", "dfxp", "stl", "tds", "cin", "asc"]
print("Supported subtitles formats:")
print(", ".join(formats))
file_path = input("Enter your subtitle file: ")
clear_screen()


if os.path.exists(file_path):
    extension = file_path.split('.')[-1].lower() 
    if extension not in formats:
        print("The file format may not be supported by YouTube.")
    else:
        print(f"File found! Size: {os.path.getsize(file_path)} bytes")
        if extension == "scc":
            print("Please check the CEA-608 complaince of the file. Otherwise, the upload may fail.")
        try:
            youtube = authenticate_youtube()
            video_id = input("Enter the YouTube video ID (NOT the URL): ")
            language = input("Enter the language code for the subtitles (e.g., 'en' for English) [Visit here for more details: https://developers.google.com/workspace/admin/directory/v1/languages]: ")
            track = input("Enter a name for the subtitle track (e.g., 'English Subtitles') [OPTIONAL, enter 'default' to use the language code]: ")
            if track == 'default':
                track = language
            upload_subtitle(video_id, file_path, language, track)
        except googleapiclient.errors.HttpError as e:
                subprocess.run(['color', '4'], shell=True) 
                print(f"An HTTP error occurred: {e.resp.status} - {e._get_reason()}")
        except google.auth.exceptions.GoogleAuthError as e:
                subprocess.run(['color', '4'], shell=True) 
                print(f"Authentication error: {e}")
        except googleapiclient.errors.Error as e:
                subprocess.run(['color', '4'], shell=True) 
                print(f"An API error occurred: {e}")
        except Exception as e:
                subprocess.run(['color', '4'], shell=True) 
                print(f"An error occurred: {e}")
                subprocess.run(['color', '4'], shell=True) 
else:       
    print(f"Error: Cannot find the file at: {file_path}")
    print(f"Current working directory is: {os.getcwd()}")
