import os

# Files to ignore (compiled files, git, images, etc.)
IGNORE_DIRS = {'.git', '__pycache__', 'assets', 'venv', 'env', 'results', 'database', 'build'}
IGNORE_EXTENSIONS = {'.pyc', '.jpg', '.png', '.mp3', '.wav', '.zip', '.exe'}

def pack_repo():
    output_filename = "full_codebase.txt"
    
    with open(output_filename, "w", encoding="utf-8") as outfile:
        # Walk through all directories
        for root, dirs, files in os.walk("."):
            # Modify dirs in-place to skip ignored directories
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
            
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in IGNORE_EXTENSIONS or file == output_filename or file == "pack_repo.py":
                    continue

                file_path = os.path.join(root, file)
                
                # Write a header for each file so I know where it starts
                outfile.write(f"\n{'='*50}\n")
                outfile.write(f"FILE: {file_path}\n")
                outfile.write(f"{'='*50}\n")
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        outfile.write(f.read())
                except Exception as e:
                    outfile.write(f"Error reading file: {e}")
                
                outfile.write("\n")

    print(f"Success! Upload '{output_filename}' to the chat.")

if __name__ == "__main__":
    pack_repo()
