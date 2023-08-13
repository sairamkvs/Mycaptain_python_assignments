# Input filename from the user
filename = input("Input the Filename: ")

# Find the position of the last dot in the filename
last_dot_index = filename.rfind('.')

# Check if a dot was found and there's at least one character after it
if last_dot_index != -1 and last_dot_index < len(filename) - 1:
    extension = filename[last_dot_index + 1:]
    
    # Map common extensions to their corresponding full names
    extension_names = {
        'py': 'python',
        # Add more extensions and names as needed
    }
    
    # Look up the full name for the extension, or use the extension itself if not found
    full_extension_name = extension_names.get(extension, extension)
    
    print(f"The extension of the file is: '{full_extension_name}'")
else:
    print("No valid extension found.")

