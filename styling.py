# Add custom styling functions here, and ensure you update the argument parser!
# These are meant to take a string without file extensions!

def to_pascal_case(string):
    formatted = string.title().replace(" ", "")
    return formatted

def to_camel_case(string):
    formatted = string.title().replace(" ", "")
    formatted = formatted[0].lower() + formatted[1:]
    return formatted

stylers = {
    "pascal": to_pascal_case,
    "camel": to_camel_case
}