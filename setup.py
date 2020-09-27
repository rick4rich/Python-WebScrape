from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Web Scraper",
    options = options,
    version = "1.0.0",
    description = 'It can Scrape any website',
    executables = executables
)