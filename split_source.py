import librosa
from pydub import AudioSegment
from pydub.silence import split_on_silence
import argparse
import os
from tqdm import tqdm
from glob import glob


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", type=str)
    parser.add_argument("--output", type=str)

    parser.add_argument("--min_silence", type=float, default=500)
    parser.add_argument("--silence_th", type=float, default=-40)

    args = parser.parse_args()

    # input_list = os.listdir(args.input)
    input_list = glob(os.path.join(args.input, "*.mp3"))
    print(input_list)
    count = 0

    for input_path in tqdm(input_list):
        # 音声ファイルを読み込む
        audio, sr = librosa.load(input_path, sr=None)

        # 音声ファイルの長さを取得
        duration = librosa.get_duration(y=audio, sr=sr)

        # pydub用にAudioSegmentオブジェクトに変換
        audio_segment = AudioSegment.from_mp3(input_path)

        # 音声ファイルを発話単位に分割
        chunks = split_on_silence(
            audio_segment,
            min_silence_len=args.min_silence,  # 無音の最小長さ（ミリ秒）
            silence_thresh=args.silence_th,  # 無音と判断する音量閾値（dBFS）
        )

        # 分割した発話を個別のファイルに保存
        os.makedirs(args.output, exist_ok=True)

        for chunk in chunks:
            output_path = os.path.join(args.output, f"speech_{count}.wav")
            chunk.export(output_path, format="wav")
            count += 1
