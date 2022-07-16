# pdf to audiobooks software

## Usage 
  - Download the main.py file and run it in your desired folder from your terminal
  
 ### Command line
 #### To learn the whole syntax : 
 
   ```cli
      aud -help
   ```
 #### To convert a single pdf to audiobook, The syntax of the command
  ```cli
     aud .conv -voiceOption filename.pdf startPage:endPage
   ```
 #### For Instance :
   ```cli
     aud .conv -f mydocument.pdf 3:5
   ```
 #### Voice options 
 - Male option : Use '-m' as the voice option
   ```cli
    aud .conv -m mydocument.pdf 3:5
   ```
 - Female option : Use '-f' as the voice option
     ```cli
    aud .conv -f mydocument.pdf 3:5
   ```
 #### Upcoming Features :
  - Ability to convert all pdfs to audiobooks in a directory at once
   
   ```cli
     aud .conv -f all
   ``` 
  - Convert a pdf from a specific start point to end :
  
   ```cli
    aud .conv -f mydocument.pdf 3:END
   ```
  - Convert from the beginning to a specific page
  
   ```cli
     aud .conv -f mydocument.pdf START:5
   ```
#### Finally: You probably want to add to this, So why not?
