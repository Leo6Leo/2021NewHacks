"""Contains a function that reads the pdf and return the course list"""
import fitz


def get_course_list(path: str):
    """Return a list of Course codes in the pdf without repeat
    Course codes have the type strings"""
    with fitz.open(path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    split_text = text.split()
    result = []
    for strings in split_text:
        if (len(strings) == 8) and strings.isalnum():
            state = 0
            for char in strings:
                if char.isnumeric():
                    state += 1
                if char.isalpha():
                    state -= 1
            if state == 0:
                result.append(strings)
    result = list(dict.fromkeys(result))
    return result
