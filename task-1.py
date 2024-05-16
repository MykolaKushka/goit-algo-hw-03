import os
import shutil
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(description="Recursively copy and sort files by extension.")
    parser.add_argument('src_dir', type=str, help="Path to the source directory.")
    parser.add_argument('dst_dir', type=str, nargs='?', default='dist', help="Path to the destination directory (default: 'dist').")
    
    args, unknown = parser.parse_known_args()
    return args

def copy_files(src_dir, dst_dir):
    try:
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)
            if os.path.isdir(item_path):
                new_dst_dir = os.path.join(dst_dir, item)
                copy_files(item_path, new_dst_dir)
            else:
                file_ext = os.path.splitext(item)[1][1:]  # Get file extension without the dot
                if file_ext:  # Check if there is an extension
                    ext_dir = os.path.join(dst_dir, file_ext)
                else:
                    ext_dir = os.path.join(dst_dir, 'no_extension')
                
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)
                
                shutil.copy2(item_path, ext_dir)
                
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    args = parse_arguments()
    src_dir = args.src_dir
    dst_dir = args.dst_dir

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    
    copy_files(src_dir, dst_dir)
    print(f"Files have been copied and sorted to '{dst_dir}'.")

if __name__ == '__main__':
    main()
