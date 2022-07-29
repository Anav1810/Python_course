# Write (w mode) will wipe out the existing content of file before adding new content
# so, use it carefully

# filepath = "sample2.txt"
# fo = open(filepath, "w")
# fo.close()


filepath = "sample2.txt"
content_to_write = """writing content
123
afgh
strhthsr
"""
with open(filepath, "w") as fo:
    n_chars_written = fo.write(content_to_write)
    print(f"Number of characters written: {n_chars_written}")

content_to_write = """appending content
1234
afghi
strhthsefwr"""
with open(filepath, "a") as fo:
    n_chars_written = fo.write(content_to_write)
    print(f"Number of characters written: {n_chars_written}")