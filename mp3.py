import moviepy.editor as mp

# Replace the file path below with the path to your video file
video = mp.VideoFileClip("vid1.mp4")

# Extract the audio from the video and save it as an MP3 file
audio = video.audio
audio.write_audiofile("elon.mp3")

# Close the video and audio objects to free up resources
video.close()
audio.close()