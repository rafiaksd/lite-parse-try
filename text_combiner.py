import os

folder = "parsed_txt"
output_file = os.path.join(folder, "all_lessons.txt")

with open(output_file, "w", encoding="utf-8") as outfile:
    for file_name in sorted(os.listdir(folder)):
        if file_name.lower().endswith(".txt") and file_name != "all_lessons.txt":
            file_path = os.path.join(folder, file_name)
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(infile.read())
                outfile.write("\n\n")  # separate each file

print(f"All texts combined into {output_file}")