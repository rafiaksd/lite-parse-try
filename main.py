from liteparse import LiteParse
import time

start_time = time.time()

pdf_doc = "Project Proposal.pdf"
pdf_doc_name = pdf_doc.split(".")[0].strip()

parser = LiteParse()
result = parser.parse(pdf_doc)

with open(f"{pdf_doc_name}.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(page.text for page in result.pages))

print(f"⏰ Time taken: {time.time()-start_time:.2f}s")