import os
from liteparse import LiteParse
from tqdm import tqdm  # progress bar

input_folder = "Research Articles"
output_folder = "Research Articles PARSED"

os.makedirs(output_folder, exist_ok=True)

parser = LiteParse()

pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]

for file_name in tqdm(pdf_files, desc="Parsing PDFs"):
    pdf_path = os.path.join(input_folder, file_name)
    
    result = parser.parse(pdf_path)
    
    txt_name = os.path.splitext(file_name)[0] + ".txt"
    txt_path = os.path.join(output_folder, txt_name)
    
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(result.text)