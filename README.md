## Table of Contents
1. [Image Processing](#imagepro)
2. [Video Processing](#videopro)








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

### Output
  You should generate a “stats.csv” file, comma separated, in the “Generated” folder with the
  following format. Every row in the “stats.csv” file will represent a record having the above
  information and in the described order:
  1. filename
  2. height of the image
  3. width of the image
  4. number of channels in the image
  5. intensity value at pixel location (𝑀/2,𝑁/2) for each channel
  
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
  

