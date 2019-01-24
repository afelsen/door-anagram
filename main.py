def combinations(startingWordsLength,iterable, r):
    '''
        Outputs all possible combinations of "r" number of words that are 15 characters long
        args:
            startingWordsLength (int): The length of the words that the user starts with
            iterable (array): The list that contains all possible words
            r (int): How many words are in each combination
        returns:
            A list with all combinations stored in tuples with length of "r"
    '''
    # Most of this function was taken from the standard library "itertools" documentation
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    runs = 0
    while True:#runs < 1000000:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        accum = 0
        for i in indices:
            accum += len(pool[i])

        #This conditional was added to the standard function - It only creates combinations with 15 characters (taking into account any words the user is starting with)
        if accum == 15-startingWordsLength:
            yield tuple(pool[i] for i in indices)
        runs += 1

def listToFile(startingWords,phraseList):
    '''
        Writes the list of combinations onto a file
        args:
            startingWords (string): The words that the user starts out with
            phraseList (array): The list of all possible combinations (returned by combinationsList)
    '''
    combinedWords = ""
    for phrase in phraseList:
        stringedPhrase = startingWords
        for item in phrase:
            stringedPhrase = stringedPhrase + item
        combinedWords = combinedWords + stringedPhrase + "\n"
    file = open("OutputFiles/combinedwords.txt","w")
    file.write(combinedWords)
    file.close()

def isWordInLetters(cLetters,vLetters1,vLetters2,input,output):
    '''
        Checks to see if a word can be made from the letters avaliable. Outputs successful words to a file
        args:
            cLetters: Letters available that can only represent one letter
            vLetters1: Letters available that can represent two different letters if flipped or turned
            vLetters2: The counterpart letter to vLetters1
                Example of what this means: vLetters1[6] = M
                                            vLetters2[6] = W
            input (str): The name of the file that contains the input words
            output (str): The name of the file to output words that can be made from the letters avaliable
        returns:
            successWordsList (array): A list of all "successful" words
    '''

    successWords = ""
    successWordsList = []
    file = open(input)

    for word in file:
        constantLetters = cLetters.copy()
        variableLetters1 = vLetters1.copy()
        variableLetters2 = vLetters2.copy()


        inWord = True
        word = word.strip()
        for letter in word:
            if letter.upper() in constantLetters:
                constantLetters.remove(letter.upper())
            elif letter.upper() in variableLetters1:
                index = variableLetters1.index(letter.upper())
                variableLetters1.pop(index)
                variableLetters2.pop(index)
            elif letter.upper() in variableLetters2:
                index = variableLetters2.index(letter.upper())
                variableLetters1.pop(index)
                variableLetters2.pop(index)
            else:
                inWord = False
                break

        if inWord:

            successWords = successWords + word + "\n"
            successWordsList += [word]
    file.close()

    successFile = open(output,"w")
    successFile.write(successWords)
    successFile.close()
    return successWordsList

def removeWord(word,constantLetters,variableLetters1,variableLetters2):
    '''
        Removes the letters of a word from the available letters.
        args:
            word (str): The word to be removed
            constantLetters: Letters available that can only represent one letter
            variableLetters1: Letters available that can represent two different letters if flipped or turned
            variableLetters2: The counterpart letter to vLetters1
                Example of what this means: vLetters1[6] = M
                                            vLetters2[6] = W
        returns:
            constantLetters (array), variableLetters1 (array), variableLetters2 (array): The updated arrays with the proper letters removed
    '''
    inWord = True
    word = word.strip()
    for letter in word:
        if letter.upper() in constantLetters:
            constantLetters.remove(letter.upper())
        elif letter.upper() in variableLetters1:
            index = variableLetters1.index(letter.upper())
            variableLetters1.pop(index)
            variableLetters2.pop(index)
        elif letter.upper() in variableLetters2:
            index = variableLetters2.index(letter.upper())
            variableLetters1.pop(index)
            variableLetters2.pop(index)
        else:
            inWord = False
            return "Word not in letters"
    return constantLetters,variableLetters1,variableLetters2


def main():
    ###The letters of HAPPY HALLOWEEN
    constantLetters = ["H","E","H","E","L","L","O","Y"]

    variableLetters1 = ["M","A","P","I","A","N","D"]
    #variableLetters2 has alternative ways of representing letters in variableLetters1. For example an "M" can be flipped and be a "W"
    variableLetters2 = ["W","V","D","!","V","Z","P"]

    #The original letter lists - stays constant even when the other lists are updated/changed
    constantLettersOrig = constantLetters.copy()
    variableLetters1Orig = variableLetters1.copy()
    variableLetters2Orig = variableLetters2.copy()


    #Below is functionality that allows the user to start with a specific word
        # For example, the user could type "piano" and "day" and all resulting anagrams will begin with "pianoday"
        # It uses the function removeWord() to remove the letters from the anagramable letters and the variable startWords to keep track of the words that the user is starting with
        # The user can keep inputing words, and stops by typing "!"
    theme = ""
    startWords = ""
    while theme != "!":
        theme = input("What word should the phrase include? (\"!\" to continue)")
        if theme == "!":
            break
        newLetters = removeWord(theme,constantLetters,variableLetters1,variableLetters2)
        if newLetters == "Word not in letters":
            print("Choose another word")
            #Eventually it should look for synonyms
        else:
            constantLetters = newLetters[0]
            variableLetters1 = newLetters[1]
            variableLetters2 = newLetters[2]
            startWords += theme

    # Outputs words that only use the provided letters onto a file "successwords.txt"
    successWordsList = isWordInLetters(constantLetters,variableLetters1,variableLetters2,"WordBanks/mediumbank.txt","OutputFiles/successwords.txt")

    #Creates a list of all combinations of words - single words, pairs of words and triples - that are 15 letters
        #For example
        # 1 word combo: Algorithmically
        # 2 word combo: IncredibleCodes
        # 3 word combo: VeryGoodProgram
    combinationsList = []
    for r in [1,2,3]:
        combinationsList += list(combinations(len(startWords),successWordsList,r))

    # Outputs the combinations onto a file "combinedwords.txt"
    stringedList = listToFile(startWords,combinationsList)

    # Outputs the combinations that only use the appropriate letters onto a file "finalresult.txt"
    successPhraseList = isWordInLetters(constantLettersOrig,variableLetters1Orig,variableLetters2Orig,"OutputFiles/combinedwords.txt","OutputFiles/finalresult.txt")
main()
