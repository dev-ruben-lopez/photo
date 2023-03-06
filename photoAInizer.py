import sys
import img_functions

def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py <source_file_path> <dest_file_path>')
        return

    source_file_path = sys.argv[1]
    dest_file_path = sys.argv[2]
    img_functions.create_thumbnail(source_file_path, dest_file_path)

if __name__ == '__main__':
    main()
