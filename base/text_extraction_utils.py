# import os
# import glob
# import tika
# from tika import parser

# tika.initVM()

# def extract_text_from_pdf(pdf_path):
#     parsed_pdf = parser.from_file(pdf_path)
#     content_bytes = parsed_pdf.get('content', '').encode('utf-8', errors='replace')
#     return content_bytes.decode('utf-8', errors='replace').lstrip('\n')

import os
import glob
import tika
from tika import parser

tika.initVM()

def extract_text_from_pdf(pdf_path):
    try:
        parsed_pdf = parser.from_file(pdf_path)
        content = parsed_pdf.get('content', '')

        # Encode as utf-8 and replace non-decodable characters
        content = content.encode('utf-8', errors='replace').decode('utf-8', errors='replace')

        return content.lstrip('\n')
    except UnicodeDecodeError:
        # If decoding fails, return an empty string or handle it accordingly
        return ''
