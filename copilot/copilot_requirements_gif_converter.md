 
Create a modular Python CLI app that processes images and GIFs.

Requirements:

1. When the app starts, it should continuously prompt the user for a directory using this structure:

   def main():
       while True:
           folder = input("\nEnter folder path (or press Enter to quit): ").strip()
           if not folder:
               break
           if not os.path.isdir(folder):
               print("Invalid directory. Please try again.")
               continue
           process_directory(folder)

   main()

2. After the user enters a valid directory, prompt them to choose an option:
   - Option 1: Convert GIFs in the folder to image frames.
   - Option 2: Convert folders of images in the folder to GIFs.

3. The output directory should always be a sibling to the input directory:
   - If input = /parent/input, output = /parent/output
   - The output folder should be created automatically if it doesn’t exist.

4. **Option 1: GIF → Frames**
   - For each `.gif` file in the input directory:
     - Extract all frames using Pillow.
     - Save frames as PNGs in `/parent/output/<gif_name>/frame0001.png`, `frame0002.png`, etc.
   - Use `tqdm` to show progress (e.g. “Extracting frames from example1.gif...”).
   - Overwrite existing files without confirmation.
   - If no valid `.gif` files are found, warn the user: “No GIF files found in this directory.”

5. **Option 2: Images → GIF**
   - For each subfolder in the input directory:
     - Load all image files in sorted order (PNG, JPG, JPEG).
     - If a subfolder is empty or has no valid image files, warn the user and skip it.
     - Prompt the user for a frame duration (in milliseconds, default 100).
     - Save the resulting GIF as `/parent/output/<folder_name>.gif`.
   - Use `tqdm` to show progress when loading frames.
   - Overwrite existing files without confirmation.

6. All print statements should clearly show progress and errors.
   - If a file fails to process, log the error to the console but continue with the next one.
   - After processing, print a summary of how many files were successfully processed and how many failed.

7. Use the `Pillow` (PIL) library for all image and GIF handling.

8. Include a `requirements.txt` file listing all dependencies (e.g. `Pillow`, `tqdm`).

9. Keep the code modular:
   - `main()` handles the user input loop.
   - `process_directory()` handles user options and dispatching.
   - `convert_gifs_to_frames()` implements option 1.
   - `convert_images_to_gif()` implements option 2.
   - Use helper functions for creating paths, naming frames, validating inputs, etc.

10. After completing a task, the app should automatically prompt the user for another directory to process until they press Enter with no input to exit.

11. Create a readme that the explain show to use the app. This is MIT licence. And add a link to the github repo with a placeolder TODO that says to update before commiting. Readme should also include an "Ideas for enhancements" section that lists Gif to Pixiv Ugoira as an idea and any other nice enhancements you can think of.