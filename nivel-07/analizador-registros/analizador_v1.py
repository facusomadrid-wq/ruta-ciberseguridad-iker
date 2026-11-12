# Security log analyzer - version 1
# Reads the records from registros.txt instead of a hardcoded list

total_lines = 0

try:
    with open("registros.txt", "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.strip()            # remove the line break at the end
            total_lines +=1                      # count one more line
            print(clean_line)
    print(f"Lines read: {total_lines}")
except FileNotFoundError:
    print("File not found: registros.txt")