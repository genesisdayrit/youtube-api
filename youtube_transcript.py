from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_transcript(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Get video caption data
    captions = youtube.captions().list(
        part='snippet',
        videoId=video_id
    ).execute()

    # Get the ID of the English captions track (assuming English)
    caption_track_id = None
    for item in captions['items']:
        if item['snippet']['language'] == 'en':
            caption_track_id = item['id']
            break

    # Fetch the transcript
    if caption_track_id:
        transcript = youtube.captions().download(
            id=caption_track_id,
            ).execute()
        return transcript['body']
    else:
        return "No English captions found for this video."

# Example usage
video_id = 'YVgH7XdGB2o'
api_key = os.getenv('YOUTUBE_API_KEY')
transcript = get_transcript(video_id, api_key)
print(transcript)
