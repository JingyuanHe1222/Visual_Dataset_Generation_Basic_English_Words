# Visual_Dataset_Generation_Basic_English_Words

-----
## Word Data

Reference: Ogden's 850 Basic English Words

Link: http://ogden.basic-english.org/words.html

Format: lowercase text

Categories and Count: 
 - Operations: 100
 - Things: 600
 - Qualities: 150
 
 Stored in the three text files by category names. 

-----
## Data Generation

Reference: Modeling the Visual Word Form Area Using a Deep Convolutional Neural Network - Sandy Wiraatmadja, Garrison W. Cottrell

Link: https://cogsci.mindmodeling.org/2016/papers/0435/paper0435.pdf

Data Generation Implementation Setup: 
- Randomly choose 100 words from the three categories with ratio: (Operations: Things: Qualities = 12 : 70: 18)
  - Selected words will be stored in words.txt
- Randomly select 75 fonts from the font family of Python Pillow library
  - Selected fonts will be stored in fonts.txt

Data Generation Implementation: 
- 
