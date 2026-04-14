#Problem J2: I Speak TXTMSG - 2007 (SirNooby)
dictionary = {
    "CU":"see you",
    ":-)":"I'm happy",
    ":-(":"I'm unhappy",
    ";-)":"wink",
    ":-P":"stick out my tongue",
    "(~.~)":"sleepy",
    "TA":"totally awesome",
    "CCC":"Canadian Computing Competition",
    "CUZ":"because",
    "TY":"thank-you",
    "YW":"you're welcome",
    "TTYL":"talk to you later"
}

while True:
    message = input()
    if message in dictionary:
        print(dictionary[message])
    else:
        print(message)
    
    if message == "TTYL":
        break