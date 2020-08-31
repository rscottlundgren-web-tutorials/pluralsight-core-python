import json

items = json.loads(
    '[{"id":1, "text": "Item 1"}, {"id":2, "text": "Item 2"}, {"id":3, "text": "Item 3"}]')

for item in items:
    print(item['text'])


def greet(greeting, name):
    """Returns a greet

    Args:
        greeting (string): a greet word
        name (string): person's name

    Returns:
        string: a greeting with a name
    """
    return f'{greeting} {name}'


print(greet('Hello', 'World'))
