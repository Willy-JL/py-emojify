import json

with open('emojimap.json', encoding='utf-8') as f:
    emoji_map = json.load(f)


def emojify(text: str, location='after'):
    words = text.split()
    for i, word in enumerate(words):
        for emoji in emoji_map:
            if word.lower() in emoji_map[emoji]:
                print(word, i)
                if location == 'after':
                    words[i] = f'{word} {emoji}'
                elif location == 'before':
                    words[i] = f'{emoji} {word}'
                break
    return ' '.join(words)
