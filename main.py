import youtube_dl
import sys

def get_info(url):
    # get info the video
    options = {
        'simulate': True,
        'quiet': True
    }
    ydl = youtube_dl.YoutubeDL(options)

    try:
        video = ydl.extract_info(url=url)
        formats = video.get('formats', None)
        p_formats = {}
        count = 1

        for format in formats:
            if format['protocol'] == 'https':
                p_formats[count] = format['format_id']
                count += 1

        video_data = {
            'title': video.get('title', None),
            'thumbnail': video.get('thumbnail', None),
            'formats': p_formats
        }

        return video_data

    except Exception as ex:
        return 'CHECK THE URL, PLEASE!'

def download_video(url, format):
    # download video
    options = {
        'format': format
    }

    try:
        ydl = youtube_dl.YoutubeDL(options)
        ydl.extract_info(url=url)

        return '[INFO] Video Downloaded!'
    except Exception as ex:
        return 'CHECK THE URL, please!'


def main():
    # load all
    url = input('Введите URL: ')
    url = url.strip()
    video_data = get_info(url=url)
    title = video_data['title']
    available_formats = video_data['formats']

    print(f'[INFO] {title}\n{"-" * 50}')
    print('Выберете желаемое качество: ')

    for k, v in available_formats.items():
        print(f'{k} - {v}')

    format = int(input('Введите число, например 2: '))

    if format not in available_formats:
        print('Такого формата нет, проверьте данные!')
        sys.exit()

    print(download_video(url=url, format = available_formats[format]))

if __name__ == '__main__':
    main()
