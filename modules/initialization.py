modules_dir = "modules" # or any other folder where the modules will be #1488

async def load_modules():
    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = import_module(f"{modules_dir}.{module_name}")
            await module.init(app) #app is client with api_id and api_hash
