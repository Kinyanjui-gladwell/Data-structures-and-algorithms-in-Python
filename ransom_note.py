"""This solves the ransomnote problem."""
def construct(ransomnote, magazine):
    magazine_letters = list(magazine)
    count = 0
    ransomnote_letters = list(ransomnote)
    for element in ransomnote_letters:
        if element in magazine_letters:
            magazine_letters.remove(element)
            count += 1
        else:
            print('False')
            return False
    if count == len(ransomnote_letters):
        print('True')
        return True

construct('ar', 'aab')