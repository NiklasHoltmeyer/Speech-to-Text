from consts.settings import Audio as Audio_Consts
from util.audio.audio import Audio
from consts import paths as PATHS
from util.logging import Logger
from util.text.text import Text
from tqdm.auto import tqdm
from pathlib import Path
import swifter
import logging
import time 

tqdm.pandas()

class CommonVoice:
    def __init__(self):
        self.logger = Logger.defaultLogger()
        self.__init_folders()        

    def __init_folders(self):
        if Path(PATHS.CommonVoice.AUDIO_WAV_PATH).exists():
            return True
        
        if not Path(PATHS.CommonVoice.AUDIO_MP3_PATH).exists():
            raise Exception(f"Invalid Common Voice MP3 Folder:\n{PATHS.CommonVoice.AUDIO_MP3_PATH}")    
        
        Path(PATHS.CommonVoice.AUDIO_WAV_PATH).mkdir(parents=True, exist_ok=True)
        
    def load_df(self, path):
        startTime = time.time()
        
        self.logger.debug('Loading Dataset')
        
        cv_df = Text.read_tsv(path)

        cv_df.drop(["client_id", 'up_votes', "down_votes", "age", "gender", "accent", "locale", "segment"], inplace=True, axis=1, errors='ignore')
        cv_df = cv_df.sample(frac = 1)   #shuffle
        
        startTime2 = time.time()
        self.logger.debug('Converting Audio (Count: {})'.format(len(cv_df.path)))
        cv_df['path_wav'] = cv_df['path'].swifter.apply(CommonVoice.__common_voice_map_path)
        self.logger.debug('Converting Audio ({}) - {} seconds'.format(path, time.time() - startTime2))
        
        self.logger.debug('Loading Dataset ({}) - {} seconds'.format(path, time.time() - startTime))
        
        self.cv_df = cv_df
        return self.cv_df
    
    def __common_voice_map_path(fileName):
        full_mp3_path, target_wav_path = Path(PATHS.CommonVoice.AUDIO_MP3_PATH, fileName), Path(PATHS.CommonVoice.AUDIO_WAV_PATH, fileName.replace(".mp3", ".wav"))
        if not full_mp3_path.exists():
            raise Exception(f"File not Found:\n{full_mp3_path}")
        
        full_mp3_path, target_wav_path = str(Path(full_mp3_path).resolve()), str(Path(target_wav_path).resolve())
    
        wav_path = Audio.convert_mp3_to_wav(src=full_mp3_path, dst=target_wav_path, sample_rate=Audio_Consts.SAMPLE_RATE, mono_channel=Audio_Consts.MONO_CHANNEL)

        if not Path(wav_path).exists():
            raise Exception(f"File not Found:\n{wav_path}")
        
        return wav_path