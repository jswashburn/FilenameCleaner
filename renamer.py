import os

from styling import stylers
from formatting import Formatter
from filtering import Filterer

class Renamer:
    def __init__(self, args):
        self.force = args.force
        self.include_hidden = args.include_hidden
        self.top = args.top
        self.walk = args.walk

        self.formatter = Formatter(stylers[args.style])
        self.filterer = Filterer(args.match_pattern, args.ignore_pattern)

    def confirm_rename(self, original, renamed):
        if self.force:
            return True
        else:
            while True:
                response = input(f"Are you sure you want to rename {original} to {renamed}? [Y/N]: ")
                if response.lower().strip() == "y" or "n":
                    return response == "y"

    def is_hidden_file(self, original):
        return original.startswith(".")

    def rename(self, original):
        renamed = self.formatter.format(original)

        if self.include_hidden or not self.is_hidden_file(original):
            rename_confirmed = self.confirm_rename(original, renamed)
            if rename_confirmed:
                print(f"Renaming {original} to {renamed}")

    def start(self):
        if self.walk:
            for root, dirs, files in os.walk(self.top):
                for original in self.filterer.filter(files):
                    self.rename(original)
        else:
            for original in self.filterer.filter(os.listdir(self.top)):
                if os.path.isfile(original):
                    self.rename(original)