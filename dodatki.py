import base64
import pathlib
import os


def tobase64(filepath: str) -> str:
    with open(filepath, 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        return base64_bytes

def isimg(path: str) ->bool:
    roszezenie = pathlib.Path(path).suffix
    image_extension = ('.png')
    if roszezenie.find(image_extension)!=-1:
        return True
    return False


def main():
    if '__main__' == __name__:
        print(isimg(''))

main()