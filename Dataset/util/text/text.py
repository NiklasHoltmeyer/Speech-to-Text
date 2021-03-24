import os
import pandas as pd

class Text:
    def read_tsv(*path):
        tsv_path = os.path.join(*path)
        if not os.path.exists(tsv_path):
            raise Exception(f"TSV-File not Found\n {tsv_path}")
        
        return pd.read_csv(tsv_path, sep='\t', header=0)