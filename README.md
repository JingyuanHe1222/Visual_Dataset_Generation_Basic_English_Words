# Visual_Dataset_Generation_Basic_English_Words

-----
## Word Data

Source: Ogden's 850 Basic English Words

Link: http://ogden.basic-english.org/words.html

Format: lowercase text

Categories and Count: 
 - Operations: 100
 - Things: 600
 - Qualities: 150
 
 Stored in the three text files by category names. 
 
## Visual Data Composition
 - 12000 images
  - 1200 images per word, 100 words
  - 
### Visual Data Format
- category_word_count.png
 - category abbreviation: opt, thing, qual
 - count: 1-1200 per image
- 224px * 224px images
 - White word printed on black background

## Data Generation

Generation Format Reference: Modeling the Visual Word Form Area Using a Deep Convolutional Neural Network - Sandy Wiraatmadja, Garrison W. Cottrell

Link: https://cogsci.mindmodeling.org/2016/papers/0435/paper0435.pdf

### Data Generation Implementation Setup: 
- Randomly choose 100 words from the three categories with ratio: (Operations: Things: Qualities = 12 : 70: 18)
  - Selected words will be stored in words.txt
- Randomly select 75 fonts from the font family of Python Pillow library
  - Selected fonts will be stored in fonts.txt

### Data Generation Implementation: 
- Random font out of the 75 fonts selected
- Random font size from [12pt, 15pt, 18pt]
- Random clockwise rotation [-15 to 15 degree]

