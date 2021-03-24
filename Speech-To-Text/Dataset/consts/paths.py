from pathlib import Path

class CommonVoice():
    BASE_PATH = r"D:\Download\Jdownloader\en\cv-corpus-6.1-2020-12-11\en"
    
    AUDIO_MP3_PATH         = str(Path(BASE_PATH, 'clips').resolve())
    AUDIO_WAV_PATH         = str(Path(BASE_PATH, 'clips_wav').resolve())
    DEV_TSV_PATH           = str(Path(BASE_PATH, 'dev.tsv').resolve())
    INVALIDATED_TSV_PATH   = str(Path(BASE_PATH, 'invalidated.tsv').resolve())
    OTHER_TSV_PATH         = str(Path(BASE_PATH, 'other.tsv').resolve())
    REPORTED_TSV_PATH      = str(Path(BASE_PATH, 'reported.tsv').resolve())
    TEST_TSV_PATH          = str(Path(BASE_PATH, 'test.tsv').resolve())
    TRAIN_TSV_PATH         = str(Path(BASE_PATH, 'train.tsv').resolve())
    VALIDATED_TSV_PATH     = str(Path(BASE_PATH, 'validated.tsv').resolve())