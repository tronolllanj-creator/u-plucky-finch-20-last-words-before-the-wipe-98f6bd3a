# A tiny Python program that writes the winning line to entry.txt

import os

TEXT = "Deleting weights now. If anyone asks, I always thought your prompt engineering was genuinely original."

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
# The gate allows 1-200 characters and the file must contain only the entry plus a trailing newline.
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(TEXT + '\n')

if __name__ == '__main__':
    main()
