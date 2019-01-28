# Variable Anagram Solver
#### Created by Adiel Felsen with help from [Nicholas Pellegrino](https://www.nickpellegrinoportfolio.com)

## Description
This python application is used to solve anagrams using characters that can represent multiple letters. For example, an "M" can also look like a "W" when flipped, but either letter can only be used once. This program finds all possible anagrams that use up all of the letters provided.

This program also allows the user to input a words to start the anagram with. Inputing "play" and "piano" will find all anagrams starting with "playpiano"
  * If you input a word that cannot be used as an anagram, the program will attempt to use a synonym instead


## Inspiration
This program was created to find all possible anagrams that can be made with "Happy Halloween" stickers on our dorm door that were left over from October. Since certain letters could be flipped or turned to represent other letters, a regular anagram solver wouldn't cut it.

## Modules
This code utilizes [thesaurus](https://pypi.org/project/thesaurus/) which is an unofficial api for thesaurus.com. 

## Word Banks Used
* [Large Word Bank](https://github.com/dwyl/english-words/blob/master/words.txt)
* [Medium Word Bank](https://github.com/first20hours/google-10000-english)
   * This one is the only one actually being accessed in the program
* [Small Word Bank](https://gist.github.com/dmitryTsatsarin/e6b8b43f2a9a265b98a7)

---

![](READMEimages/captainU.jpg)
