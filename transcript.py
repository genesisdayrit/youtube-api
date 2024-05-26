from youtube_transcript_api import YouTubeTranscriptApi

# Video ID of the YouTube video
video_id = 'YVgH7XdGB2o'

# Get the transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Print the transcript
for line in transcript:
    print(line['text'])
