import base64

def createPassword():
    # User input for the file
    path = input("Enter the path of the file: ")

    # Reading file
    openedFile = open(path, 'rb')
    image = openedFile.read()

    # Encoding the file
    encodedImage = base64.a85encode(image)

    # Make the text impossible to reverse engineer without knowing which tool was used
    utf8Name = path.encode('utf-8')
    encodedName = base64.b85encode(utf8Name)
    addedImage = str(encodedName + encodedImage + encodedName)

    # Format the string
    formattedImage = stringFormat(addedImage, 35)

    # Crate and store formattedImage
    textFile = open('textFiles/text.txt', 'w')
    textFile.write(str(formattedImage))

def stringFormat(text, charLimit):
    newText = ''
    currentText = ''

    for char in text:
        currentText += str(char)
        if len(currentText) == charLimit:
            newText += currentText + '\n'
            currentText = ''
            
    newText += currentText
    return newText

createPassword()