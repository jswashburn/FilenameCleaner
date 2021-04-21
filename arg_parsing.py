import argparse
from os import getcwd

PROGRAM_DESCRIPTION = """clean.py - Cleans up filename formatting 
given a directory. The default directory is wherever the script is run from. 
See help for regular expression filtering options.
To add a different styling, add a styler function to the 'styler_functions' dictionary 
and update the argument parser."""

def get_args():

    parser = argparse.ArgumentParser(description=PROGRAM_DESCRIPTION)

    parser.add_argument("-w", "--walk",
        help="Rename files in all subfolders",
        action="store_true",
        default=False)

    parser.add_argument("-t", "--top",
        help="The top directory to rename files in",
        default=getcwd())

    parser.add_argument("-s", "--style",
        help="The style of formatting to apply to filenames",
        choices=["pascal", "camel"],
        default="pascal")

    parser.add_argument("-f", "--force",
        help="Whether or not to skip confirmation of each file",
        action="store_true",
        default=False)

    parser.add_argument("-a", "--all",
        help="Whether or not to also rename hidden files",
        action="store_true",
        dest="include_hidden",
        default=False)
    
    parser.add_argument("-i", "--ignore",
        metavar="PATTERN",
        dest="ignore_pattern",
        help="Filenames matched with this regex pattern will be ignored")
    
    parser.add_argument("-m", "--matching",
        metavar="PATTERN",
        dest="match_pattern",
        help="Filenames that do not match this regex pattern will be ignored")

    return parser.parse_args()