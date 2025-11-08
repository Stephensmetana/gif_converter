# gif_converter

A modular Python CLI app for converting GIFs to image frames and folders of images to GIFs.

## Features
- Convert GIFs in a folder to PNG frames
- Convert folders of images to GIFs
- Progress bars and error handling
- Modular code structure

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python gif_converter.py
   ```

3. Follow the prompts to select a directory and choose an operation.

## Output
- Output folders are created as siblings to the input folder.
- GIF frames are saved as PNGs in `/parent/output/<gif_name>/frame0001.png`, etc.
- GIFs are saved as `/parent/output/<folder_name>.gif`.

## License
MIT License

## GitHub
https://github.com/Stephensmetana/gif_converter

## Ideas for enhancements
- GIF to Pixiv Ugoira conversion
- Batch resizing or optimization
- Frame Interpolation 
- Change Frame Rate of gifs
