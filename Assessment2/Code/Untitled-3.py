
def eight(input, a):
    length=len(input)//2
    print(length)
    if a < len(input):
        first=input[:length-1]
        second= input[length+a:]
        return first + second
    else:
        return ""
print(eight("Hello", 3))

