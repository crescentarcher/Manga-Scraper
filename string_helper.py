import settings  # Import the settings module

def dashes(seriesName):
    return "_".join(seriesName.split(" ")).lower()

def add_zeros(pgNum):
    digits = len(pgNum)
    zeros = "0" * (settings.EST_MAX_DIGITS - digits)  # Use settings.EST_MAX_DIGITS
    return zeros + pgNum

def get_url(seriesName, chpNum):
    # Construct the URL for the specific manga chapter without the page number
    series_name_formatted = dashes(seriesName)  # Convert spaces to underscores and lowercase
    return settings.PROVIDER + "Read1_" + series_name_formatted + "_" + str(chpNum)

def get_download_path(seriesName, chpNum):
    return settings.LOCAL_PATH + seriesName + "/" + str(chpNum) + "/"  # Use '/' for macOS/Linux path separator

def format_manga_name(manga_name):
    # Format the manga name as needed, replacing spaces with underscores and making lowercase
    return manga_name.lower().replace(" ", "_")
