from liteparse import LiteParse
import time

start_time = time.time()

parser = LiteParse()
result = parser.parse("AI Module 1.pdf")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(page.text for page in result.pages))

print(f"⏰ Time taken: {time.time()-start_time:.2f}s")