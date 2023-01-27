import os
import numpy as np
import pypdf

path = '/Users/louisdaub/Projects/pAIper/pAIper/data'

for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        filepath = os.path.join(path, filename)
        with open(filepath, 'rb') as f:
            pdf = pypdf.PdfReader(f)
            text = ''
            for page in range(len(pdf.pages)):
                text += pdf.pages[page].extract_text()
            # Perform text analysis on the extracted text
            print(text)