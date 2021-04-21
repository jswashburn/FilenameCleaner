class Formatter:
    def __init__(self, styler, word_separators=("_", "-")):
        self.styler = styler
        self.word_separators = word_separators

    # "remove-my_separators" -> "remove my separators"
    def remove_separators(self, string):
        for sep in self.word_separators:
            string = string.replace(sep, " ")
        return string.strip()

    # "file.with.extensions" -> "(file, .with.extensions)"
    def split_path(self, path):
        partitioned = path.partition(".")
        filename = partitioned[0]
        extensions = "".join(partitioned[1:])
        return filename, extensions
        
    def style(self, string):
        return self.styler(string)

    # "please Format_this.cs.html" -> "PleaseFormatThis.cs.html"
    def format(self, filename):
        unformatted, extensions = self.split_path(filename)
        formatted = self.style(self.remove_separators(unformatted)) + extensions
        return formatted
