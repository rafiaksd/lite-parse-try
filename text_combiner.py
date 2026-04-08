import os

folder = "Research Articles PARSED"
output_file_name = "ALL ARTICLES.txt"
output_file = os.path.join(folder, output_file_name)

with open(output_file, "w", encoding="utf-8") as outfile:
    for file_name in sorted(os.listdir(folder)):
        if file_name.lower().endswith(".txt") and file_name != output_file_name:
            file_path = os.path.join(folder, file_name)
            
            # Write header

            file_name = file_name.split(".")[0] # filename.txt -> filename

            separator = "=" * len(file_name)

            outfile.write(f"{separator}\n\n")
            outfile.write(f"{file_name}\n\n")
            outfile.write(f"{separator}\n\n")
            
            # Write file content
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
            
            outfile.write("\n\n")  # separate each file

print(f"All texts combined into {output_file}")