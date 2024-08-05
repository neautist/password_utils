import rstr
def password_generator(length: int):
    if not(isinstance(length,int)):
        raise ValueError("Должно быть введено число")

    # TODO: insert logic here
    return generate_string( r'[A-Za-z0-9!@#$%^&*()]',length=length)


def generate_string(pattern, length):
    generated_string = ''
    while len(generated_string) < length:
        generated_string += rstr.xeger(pattern)
    return generated_string[:length]