import json
import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def init() -> None:
    full_path = os.path.dirname(os.path.realpath(__file__))

    file = open(full_path + '/links.json')
    links = json.load(file)
    file.close()

    for linkData in links:
        mp4_video_path = full_path + '/temp/' + linkData['name'] + '.mp4'
        mp3_audio_path = full_path + '/output/' + linkData['name'] + '.mp3'

        if os.path.isfile(mp3_audio_path):
            continue

        YouTube(linkData['link']).streams\
            .filter(progressive=True, file_extension='mp4')\
            .order_by('resolution')\
            .asc()\
            .first()\
            .download(
                output_path=full_path + '/temp',
                filename=linkData['name'] + '.mp4',
            )

        video = VideoFileClip(mp4_video_path)
        video.audio.write_audiofile(mp3_audio_path)
        os.remove(mp4_video_path)


if __name__ == '__main__':
    init()
