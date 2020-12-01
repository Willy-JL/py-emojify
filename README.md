# PyEmojify

Emojify your text!

## Usage

```python
from PyEmojify import emojify

text = input("Write the text to emojify: ")

emojified = emojify(text)
print(emojified)
```

You can also have the emojis before the trigger words:

```python
from PyEmojify import emojify

text = input("Write the text to emojify: ")

emojified = emojify(text, position='before')
print(emojified)
```

### Thanks:
 Thanks to me4502's [Emojify](https://matthewmiller.dev/experiments/emojify/) ([GitHub](https://github.com/me4502/Emojify)) for the [Emoji Map](https://github.com/me4502/Emojify/blob/master/src/emojiMap.json)