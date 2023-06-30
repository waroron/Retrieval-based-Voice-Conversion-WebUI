import argparse
import os
from yt_dlp import YoutubeDL


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--url_txt', required=True,  type=str)
    parser.add_argument('--save_dir', type=str)

    
    args = parser.parse_args()
    
    with open(args.url_txt, 'r') as f:
        url_list = f.readlines()
        
    url_list = set(url_list)
    print(url_list)
    
    option = {
        'outtmpl' : os.path.join(args.save_dir, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  
            'preferredcodec': 'mp3',  #変換したい形式を指定
            'preferredquality': '192' #ビットレートを指定
        }]
    }

    os.makedirs(args.save_dir, exist_ok=True)
    
    ydl = YoutubeDL(option)

    #動画一覧を取得
    ydl = YoutubeDL(option)
    result = ydl.download(url_list)
