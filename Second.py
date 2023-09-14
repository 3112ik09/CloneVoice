# import torch
# import torchaudio
# import deepspeech

# # Load the DeepSpeech model
# # Load the DeepSpeech model
# model = deepspeech.Model('deepspeech-0.9.3-models.pbmm')

# # Load the audio file and specify the sample rate (usually 16000 Hz for DeepSpeech)
# audio_file = "elon1min.wav"
# sample_rate = 16000  # Adjust the sample rate if needed

# # Load the audio file using torchaudio
# waveform, _ = torchaudio.load(audio_file, num_frames=-1, normalize=True)
# waveform = waveform.squeeze().numpy()

# # Convert the audio data to int16 format (16-bit PCM)
# int16_waveform = np.int16(waveform * 32767.0)  # Assuming the data is in the range [-1, 1]

# # Transcribe the audio
# transcription = model.stt(int16_waveform)

# print(transcription)