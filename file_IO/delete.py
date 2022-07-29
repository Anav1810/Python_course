import os


# file_to_delete = "sample.txt"
# # os.remove(file_to_delete)

# # If file does not exist, we get FileNotFoundError
# """
# Traceback (most recent call last):
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'sample.txt'
# """

# if os.path.exists(file_to_delete):
#     os.remove(file_to_delete)
# else:
#     print("File does not exist")




# if folder is non empty, then it will throw OSError: [WinError 145] The directory is not empty:
folder_to_delete = "sample_folder"
os.rmdir(folder_to_delete)