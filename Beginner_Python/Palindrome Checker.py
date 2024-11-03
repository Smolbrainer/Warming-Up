
def start():
    word =str(input("What word are you checking if it is a palindrome? "))
    wordBackwords = word[::-1] #[start:end:step] empty:empty:-1 full string and the step is backwords 1
    checkIfPalindrome(word,wordBackwords)


def checkIfPalindrome(word,wordBackwords):
    if word == wordBackwords:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome as it is {wordBackwords} backwards. ")
    start()

start()