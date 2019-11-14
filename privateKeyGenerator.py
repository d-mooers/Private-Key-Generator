import hashlib
import base58

def makeHash():

    randInput = input("Blindly sweep your hands across the keyboard and then press enter ").encode("utf-8")
    print()

    hexIntermediate = hashlib.sha256(randInput).hexdigest()
    
    if int("0x" + hexIntermediate, 0) > 2 ** 256 :
        return

    hexIntermediate = "80" + hexIntermediate

    doubleHash = hashlib.sha256(hashlib.sha256(hexIntermediate.encode("utf-8")).hexdigest().encode("utf-8")).hexdigest()
    hexIntermediate += doubleHash[:9]

    return(base58.encode(int("0x" + hexIntermediate, 0)))


if __name__ == "__main__" :

    run = True

    while run:
        print("Your private key: ", makeHash() + "\n")

        if (input("Do you want to generate another private key? Press 'y' or 'Y' to make another ").lower()
                != "y") :
            run  = False

