import string, random

def code_generator(prefix, size, chars=string.ascii_uppercase + string.digits):
    return prefix + "".join(random.choice(chars) for x in range(size))