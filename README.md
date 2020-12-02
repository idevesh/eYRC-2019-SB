## Table of Contents 
1. [Image Processing](#imagepro)
2. [Video Processing](#videopro)
2. [Video Deblurring Using Python](#videode)

**If you enjoy this project, please consider <a href="https://www.buymeacoffee.com/idevesh" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
 to continue developing and maintaining it.**






<a name="imagepro"></a>
## Image Processing
  ### Part A:
    For each image, we are required to identify and save certain properties of image as
    mentioned below:
    1. Name of image with extension (but without full path)
    2. Dimensions of the image
    3. Value of color (order: B, G, R) triplet at the (𝑀/2,𝑁/2) location in the image, where 𝑀 = number of rows and 𝑁 is the number of columns.
    Note: Indexing in Python starts from 0, so though M is an integer, Python row count goes
    from 0 to M-1

  ### Part B:
    Read the image “cat.jpg”. Set channels Blue and Green to 0. Save the image as
    “cat_red.jpg” in the “Generated” folder. This helps us visualize the red component of the
    image.

  ### Part C:
    Read the image “flowers.jpg”. This is an image with 3 channels.
    Add another channel, alpha channel, and set its value to 0.5. Save the resultant image as
    “flowers_alpha.png” to “Generated” folder. This increases the overall transparency of the
    image from 0% to 50%

  ### Part D:
    Read the image “horse.jpg”. One way to encode per-pixel information or colors is the color
    vector, i.e. (𝑅, 𝐺, 𝐵), (𝐵, 𝐺, 𝑅), etc. Another is the HSV/HSL representation.
    • H stands for Hue
    • S stands for Saturation
    • V/L stans for Value/Level (intensity)
    Here, we will compute the Level (intensity) component of every pixel. The formula to do so
    is:
    𝐼 = ((0.3 × 𝑅𝑒𝑑 𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡) + (0.59 × 𝐺𝑟𝑒𝑒𝑛 𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡)
    + (0.11 × 𝐵𝑙𝑢𝑒 𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡))
    Thus, compute intensity value for every pixel and save the image (1-channeled) as
    “horse_gray.jpg”.
    
  ### Output
    You should generate a “stats.csv” file, comma separated, in the “Generated” folder with the
    following format. Every row in the “stats.csv” file will represent a record having the above
    information and in the described order:
    1. filename
    2. height of the image
    3. width of the image
    4. number of channels in the image
    5. intensity value at pixel location (𝑀/2,𝑁/2) for each channel

<a name="videopro"></a>
## Video Processing
  ### Problem Description
    Remember that all file and folder paths in your program should be relative. A video named
    “RoseBloom.mp4” is provided in the “Videos” folder. The video is a colour video of the
    blooming of a red rose. As the video progresses the rose flower blooms into a fully bloomed
    rose. The Video is a 13 second playout .mp4 format video of resolution 640 × 360 at a
    25𝑓𝑝𝑠 frame rate. All your files must be generated in “Generated” folder. Write your code
    in the placeholder file, “main.py” provided in the “Codes” folder. Your “main.py” file must
    solve all the parts at once.
    
  ### Part A:
    Read the video and save the frame at the start of 6th second. Save the image as
    “frame_as_6.jpg” in the “Generated” folder.
    
  ### Part B:
    We want to visualize the red component of the frame_at_6.jpg image. Read the video or the
    file (which ever convenient) and set the Green and Blue components to 0. Save the image as
    “frame_as_6_red.jpg” in the “Generated” folder.
    
 <a name="videode"></a>
## Video Deblurring Using Python
  ### Folder Structure
    This folder contains 4 sub-folders. 
    1. Codes
    Contains the program files(s). main.py
    2. Generated
    This folder is where you’ll save the images/results from your task.
    3. Videos
    This folder will be the input video folder.

  ### Usage
    1. Copy your blurred video inside videos folder.
    2. Go to main.py inside the codes folder and change the name of the video you copied.
    3. Run main.py
    4. Generated folder will be having deblurred photos.

### Show some ❤️ by starring my repository! ![](https://visitor-badge.glitch.me/badge?page_id=idevesh.eYRC-2019-SB&style=flat-square&color=0088cc)
