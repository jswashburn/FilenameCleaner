import re

class Filterer:
    def __init__(self, match_pattern=None, ignore_pattern=None):
        self.match_pattern = self.validate_regex(match_pattern)
        self.ignore_pattern = self.validate_regex(ignore_pattern)

    def set_match_pattern(self, pattern: str):
        self.match_pattern = self.validate_regex(pattern)
    
    def set_ignore_pattern(self, pattern: str):
        self.ignore_pattern = self.validate_regex(pattern)

    def validate_regex(self, string):
        try:
            pattern = re.compile(string)
        except re.error:
            pattern = None
        except TypeError:
            pattern = None

        return pattern
    
    def get_except(self, strings, ignore_pattern):
        return [s for s in strings if re.match(ignore_pattern, s) is None]

    def get_matching(self, strings, match_pattern):
        return [s for s in strings if re.match(match_pattern, s)]

    def filter(self, strings):
        filtered = strings

        if self.match_pattern:
            filtered = self.get_matching(filtered, self.match_pattern)

        if self.ignore_pattern:
            filtered = self.get_except(filtered, self.ignore_pattern)
        
        return filtered
