import os
import subprocess

from pydub import AudioSegment

def convert_normalize(directory, normalized_subdir=''):
	ind = 0
	for file in os.listdir(directory):
		ind += 1
		filename = os.fsdecode(file)
		if filename.endswith('.mp4'):
			print('{} {} / {}'.format(os.path.join(directory, filename), ind, len(os.listdir(directory))))
			new_filename = filename.replace('.mp4', '.mp3')
			subprocess.run([
				'ffmpeg',
				'-i', os.path.join(directory, filename),
				os.path.join(directory, new_filename)
			])
			os.remove(os.path.join(directory, filename))
			audio = AudioSegment.from_file(os.path.join(directory, new_filename), 'mp3')
			os.remove(os.path.join(directory, new_filename))
			audio = audio.normalize()
			audio.export(os.path.join(directory, normalized_subdir, new_filename), format='mp3')
