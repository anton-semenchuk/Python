# O(n) time | O(n) space
def caesarCipherEncryptor(string, shift):
    newShift = shift % 26
    newLetters = []
    for letter in string:
        newLetters.append(shiftChar(letter, newShift))
    return "".join(newLetters)


def shiftChar(letter, shift):
    idx = ord(letter) + shift
    if idx > 122:
        idx = idx % 122 + 96
    return chr(idx)


print(caesarCipherEncryptor('xyz', 2))