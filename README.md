# FilenameCleaner
Command line python script that applies styling and formatting to files, supports pattern matching

Useful for people like me who can't make up their minds on naming conventions for files

## How to use:
1. Run clean.py from directory you wish to rename files
2. Pass in your arguments, use -h for help.
3. Patterns are python regular expressions.


usage: clean.py [-h] [-w] [-t TOP] [-s {pascal,camel}] [-f] [-a] [-i PATTERN] [-m PATTERN]
#### example: rename all files that do not begin with "test_" and use camelCasing.
`clean.py -w -i ^test_ -s camel`

### Arguments
<dl>
  
  <dt>-w</dt>
  <dd>
    Whether or not to rename all files in child folders
  </dd>
  
  <dt>-t TOP</dt>
  <dd>
    The top level directory to start renaming files in. This is wherever you ran the script from by default.
  </dd>
  
  <dt>-s STYLE</dt>
  <dd>
    Styling to use when renaming files. Supports pascal and camel. Add custom stylers by adding a styling function to 'styling.py' and updating the argument parser
  </dd>
  
  <dt>-f</dt>
  <dd>
    Use this to skip confirmation of each file
  </dd>
  
  <dt>-a</dt>
  <dd>
    Whether or not to include hidden files (those beginning with a period ".")
  </dd>
  
  <dt>-i PATTERN</dt>
  <dd>
    Specify a regex pattern to ignore
  </dd>
  
  <dt>-m PATTERN</dt>
  <dd>
    Specify a regex pattern to match
  </dd>
  
</dl>
