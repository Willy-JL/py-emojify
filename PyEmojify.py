import json

with open('emojimap.json', encoding='utf-8') as f:
    emoji_map = json.load(f)


def emojify(text: str, position='after'):
    emojified_lines = []
    lines = text.split('\n')
    for i, line in enumerate(lines):
        words = line.split()
        for i, word in enumerate(words):
            for emoji in emoji_map:
                if word.lower() in emoji_map[emoji]:
                    if position == 'after':
                        words[i] = f'{word} {emoji}'
                    elif position == 'before':
                        words[i] = f'{emoji} {word}'
                    break
        emojified_lines.append(' '.join(words))
    return '\n'.join(emojified_lines)
