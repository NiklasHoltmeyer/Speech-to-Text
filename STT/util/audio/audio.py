import librosa
import soundfile as sf
from pydub import AudioSegment
import os

class Audio:  
    def load_wav(file, sample_rate, mono_channel):
        return librosa.load(file, sr=sample_rate, mono=mono_channel) # signal, sample_rate
         
    def save_wav(signal, destination, sample_rate):
        sf.write(destination, data=signal, samplerate=sample_rate, subtype='PCM_24')
        
    def convert_mp3_to_wav(src, dst, sample_rate, mono_channel, overwrite=False):    
        if not overwrite and os.path.exists(dst):
            return dst
        
        if not os.path.exists(src):
            raise(f"Convert Audio - File not Found\n{src}")
        
        tmp_dst = dst+"_tmp.wav"
        
        audio = AudioSegment.from_mp3(src)
        audio.export(tmp_dst, format="wav")  # mp3->wav
        
        y, sr = Audio.load_wav(tmp_dst, sample_rate, mono_channel)  # wav-> wav(sample_rate, channel, clean?, ...)
        Audio.save_wav(y, dst, sample_rate)
        
        os.remove(tmp_dst)
            
        return dst