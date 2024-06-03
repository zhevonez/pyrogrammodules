# uses https://api.dictionaryapi.dev/ \\\\\\\\\\\\\\\\\ only for anglosakskogo yazika

async def init(app: Client):
    @app.on_message(filters.command(["dictionary", "dctnr", "dtr", "dct"], prefixes=settings.prefix)) # if esli ny ODNA command to () a esli neskolko to [] kak spisok ili list
    async def dictionary(client, message):
        word = message.text.split(maxsplit=1)[1]
        response = get_definition(word)

        if response:
            await message.edit_text(response)
        else:
            await message.edit_text("Word not found in the dictionary.") # :((((((

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}" #zvooooooN mozhno pomenyat na lyboi drygoi instead of en_US 
    try:
        response = requests.get(url)
        data = response.json()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', None)
        if example:
            return f"Definition of {word}:\n{meaning}\n\nExample: {example}"
        else:
            return f"Definition of {word}:\n{meaning}"
    except Exception as e:
        print(e)
        return None
