import os
import sys
from tqdm import tqdm
from PIL import Image

def main():
    while True:
        folder = input("\nEnter folder path (or press Enter to quit): ").strip()
        if not folder:
            break
        if not os.path.isdir(folder):
            print("Invalid directory. Please try again.")
            continue
        process_directory(folder)


def process_directory(folder):
    print(f"\nProcessing directory: {folder}")
    print("Choose an option:")
    print("1. Convert GIFs in the folder to image frames.")
    print("2. Convert folders of images in the folder to GIFs.")
    option = input("Enter 1 or 2: ").strip()
    parent = os.path.dirname(folder)
    output_dir = os.path.join(parent, "output")
    os.makedirs(output_dir, exist_ok=True)
    if option == "1":
        convert_gifs_to_frames(folder, output_dir)
    elif option == "2":
        convert_images_to_gif(folder, output_dir)
    else:
        print("Invalid option. Returning to main menu.")


def convert_gifs_to_frames(input_dir, output_dir):
    gif_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.gif')]
    if not gif_files:
        print("No GIF files found in this directory.")
        return
    success, failed = 0, 0
    for gif_file in tqdm(gif_files, desc="Processing GIFs"):
        gif_path = os.path.join(input_dir, gif_file)
        gif_name = os.path.splitext(gif_file)[0]
        out_folder = os.path.join(output_dir, gif_name)
        os.makedirs(out_folder, exist_ok=True)
        try:
            with Image.open(gif_path) as im:
                for i, frame in enumerate(iter_frames(im)):
                    frame_path = os.path.join(out_folder, f"frame{str(i+1).zfill(4)}.png")
                    frame.save(frame_path, format="PNG")
            print(f"Extracted frames from {gif_file}.")
            success += 1
        except Exception as e:
            print(f"Error processing {gif_file}: {e}")
            failed += 1
    print(f"\nSummary: {success} GIFs processed, {failed} failed.")


def iter_frames(im):
    try:
        i = 0
        while True:
            im.seek(i)
            frame = im.copy()
            yield frame
            i += 1
    except EOFError:
        pass


def convert_images_to_gif(input_dir, output_dir):
    subfolders = [f for f in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, f))]
    if not subfolders:
        print("No subfolders found in this directory.")
        return
    success, failed = 0, 0
    for folder in subfolders:
        folder_path = os.path.join(input_dir, folder)
        images = sorted([f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))])
        if not images:
            print(f"No valid images in {folder}. Skipping.")
            failed += 1
            continue
        duration = input(f"Enter frame duration for {folder} in ms (default 100): ").strip()
        duration = int(duration) if duration.isdigit() else 100
        frames = []
        for img_file in tqdm(images, desc=f"Loading frames from {folder}"):
            img_path = os.path.join(folder_path, img_file)
            try:
                frame = Image.open(img_path)
                frames.append(frame.copy())
            except Exception as e:
                print(f"Error loading {img_file}: {e}")
        if not frames:
            print(f"No valid images loaded from {folder}. Skipping.")
            failed += 1
            continue
        out_gif = os.path.join(output_dir, f"{folder}.gif")
        try:
            frames[0].save(out_gif, save_all=True, append_images=frames[1:], duration=duration, loop=0)
            print(f"Saved GIF: {out_gif}")
            success += 1
        except Exception as e:
            print(f"Error saving GIF for {folder}: {e}")
            failed += 1
    print(f"\nSummary: {success} GIFs created, {failed} failed.")

if __name__ == "__main__":
    main()
