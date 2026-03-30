# requires Node.js (>= 18), npm install -g @llamaindex/liteparse
from liteparse import LiteParse

# Create parser
parser = LiteParse()

# Parse a document
result = parser.parse("test_pdf.pdf")
print(result.text)

# Access structured data
for page in result.pages:
    print(f"Page {page.pageNum}: {len(page.textItems)} text items")