async def init(app: Client):
    @app.on_message(filters.command("modules", prefixes=settings.prefix)) # vmesto modules u can write any other command!!!!
    async def list_modules(client, message):
        modules_dir = "modules" # papka blin mozhna zhe bilo iz initializatiionnnnnnn vzyat'(((()
        available_modules = []

        for filename in os.listdir(modules_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                available_modules.append(f"{settings.prefix}{module_name}")

        if available_modules:
            module_list = "\n".join(available_modules) # just skip ny tipo (like vi ponyali da) propysk
            await message.edit_text(f"Доступные модули:\n{module_list}")
        else:
            await message.edit_text("Нет доступных модулей.") # pokazhi mne svoy :t
