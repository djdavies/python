#!/usr/bin/env python

# Copyright 2003 Tom Rothamel <tom-potw@rothamel.us>
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Originally from http://tom.idealog.info/blog/20031205-1070600658.shtml
# Modified 2009 by Paul Vincent Craven using instructions from JessenNoller.com
# http://jessenoller.com/2006/10/10/python2html/

import re
import sys
import optparse

# NOTE: In comments, PRM is used to refer to the Python Reference
# Manual, Python 2.3.2 edition.

# This is a map from a symbolic style name to a CSS style, allowing us
# to change the CSS styles in one convenient place.
styles = {
    'string' : 'color: #006000;',
    'comment' : 'color: #800000;',
    'keyword' : 'color: #804000;',
    'highlight' : 'color: #000080;',
    }

##############################################################################

# The singleton state object, accessed by the tokenizers.
class State(object):
    """Fields on this object store state that needs to be passed between
    tokens.
    """

    def __init__(self):

        # This is used to indicate if the next name should be hilighted.
        # It's sent to True when def or class are seen, and is used to
        # hilight the name of the construct being defined.
        self.highlight_name = False

# The following take in a matched token, and return a list of
# style, text pairs. 
        
def tok_comment(m, state):
    """Returns a formatted comment."""
    return [ ('comment', m.group(0)) ]


def tok_whitespace(m, state):
    """Returns formatted whitespace."""
    return [ (None, m.group(0)) ]

# The set of all keywords defined in python. as and None will become
# keywords in a future release, but we include them now.
# (PRM 2.3.1)
keywords = """
and       del       for       is        raise    
assert    elif      from      lambda    return   
break     else      global    not       try      
class     except    if        or        while    
continue  exec      import    pass      yield    
def       finally   in        print     as
None
""".split()

def tok_name(m, state):
    """Returns a formatted name."""

    name = m.group(0)

    # If we have a function or class definition, remember to highlight
    # the next name.
    if name in ("def", "class"):
        state.highlight_name = True

    # If we have a keyword, style it.
    if name in keywords:
        return [ ("keyword", m.group(0)) ]

    # If we want to highlight the next name, do so.
    if state.highlight_name:
        state.highlight_name = False
        return [ ("highlight", m.group(0)) ]
    
    # Otherwise, don't style anything.
    return [ (None, m.group(0)) ]

def tok_number(m, state):
    """Returns a formatted number."""

    return [ (None, m.group(0)) ]

def tok_other(m, state):
    """Returns a formatted other (this usually matches operators)."""
    
    return [ (None, m.group(0)) ]

def tok_string(m, state):
    """Returns a formatted string."""

    # Style the body of the string, but leave the delimiters unstyled.
    return [ (None, m.group('start')),
             ("string", m.group('body')),
             (None, m.group('end')) ]

##########################################################################

def stringpat(delim):
    """Given a delimiters, return a regular expression that matches
    strings delimited by those characters.
    """

    # How to match characters that can be in the string but are not
    # the delimiter.


    # (?<!\\) asserts that the character is not preceded by a \.
    # So, this matches the shortest string such that the delimiter
    # is not preceded by an odd number of backslashes.
    #
    # More precisely, we match the shortest string of the form:
    #
    # opening
    # anything
    # something other than a backslash
    # any even number of backslashes
    # closing
        
    nodelim = r"(.*?(?<!\\)(?:\\\\)*)?"

    # Taken from PRM 2.4.1
    return ( r"(?P<start>[ru]*%s)" \
             r"(?P<body>%s)" \
             r"(?P<end>%s)" \
             % (delim, nodelim, delim) )

# This is a list of regular expression, function pairs. It's used to
# tokenize the file. When a regular expression matches, the match
# object created is passed to the corresponding function, which is
# responsible for returning formatted text.
patterns = [

    # PRM 2.4.1 (string literals)
    ( stringpat('"""'), tok_string),
    ( stringpat('"'), tok_string),
    ( stringpat("'''"), tok_string),
    ( stringpat("'"), tok_string),

    # PRM 2.4.6 (imaginary), gives j at the end of the next few patterns.

    # PRM 2.4.5 (floating point)
    ( r"(\d*\.\d+|\d+\.)(e[+-]?\d+)?j?", tok_number),

    # PRM 2.4.4 (integers)
    ( r"0x?[0-9a-f]+l?j?", tok_number),
    ( r"0[0-7]+l?j?", tok_number ),
    ( r"\d+l?j?", tok_number ),

    # The rest of these are mostly common sense.

    # Names.
    ( r"\w+", tok_name ),
    # Whitespace.
    ( r"\s+", tok_whitespace ),
    # Comments.
    ( r"#[^\r\n]*", tok_comment),    

    # Everything that doesn't match something else matches here. 
    ( r"[^\w\s\"\'\#]+", tok_other),
    ]

# Compile the patterns.
patterns = [ (re.compile(regex, re.S | re.I), action)
             for regex, action in patterns ]


def tokenize(source):
    """This a generator that tokenizes the source into a a sequence
    of style, text pairs.
    """
    
    lens = len(source)
    pos = 0

    # Instatiate the state object.
    state = State()

    # We advance along the string...
    while pos < lens:

        # ...finding a regex that matches...
        for regex, action in patterns:
            m = regex.match(source, pos)

            if m:
                break
        else:
            # If no regex matches, it's an error. (Should never happen.)
            print >>sys.stderr, repr(source[pos:pos + 200])            
            print >>sys.stderr
            raise (Exception, "Didn't match token.")

        # ... and calling the appropriate action with the match and
        # state objects.

        tokens = action(m, state)

        # This gives us a list of style, text tokens, which we then
        # yield up for formatting.
        for style, text in tokens:            
            yield style, text

        # Update the new position in the string to the end of the last
        # match.
        pos = m.end()

##########################################################################

def quote(s):
    """Escapes characters that would otherwise have special meanings
    in html. Only works for text, not attributes.
    """

    s = re.sub(r"&", "&amp;", s)
    s = re.sub(r"<", "&lt;", s)

    return s

def format(source, out):
    """Formats the source as html, and sends it to the file out. fn is
    a filename associated with the source being formatted, which is used
    to make <a name> anchors for each line number.
    """

    line = 1

    # This is what we do at the start of each line. (Print out a
    # line number and anchor.)
    def newline():
        if options.line_numbers:
            out.write('<a name="%d">% 5d</a> ' % (line, line))
        else:
            out.write('<a name="%d" />' % line)

    newline()

    for style, text in tokenize(source):

        # Further split the text into chunks of text,
        # separated by newlines.
        for t in re.split(r"(\n)", text):

            if t == '\n':
                # If we have a newline, write it out.
                out.write(t)

                # We have to do this increment here to get the scopes
                # right.
                line += 1

                # Write out the line preamble.
                newline()

            elif style:
                # If we have a style, emit a quoted and styled block of text.
                out.write('<span style="%s">%s</span>'
                          % (styles[style], quote(t)))
                
            else:
                # Otherwise, emit a block of text that is quoted, but not
                # styled.
                out.write(quote(t))
                

def main():

    # Parse the options.

    usage = """%prog <files>

For each python source file listed in <files>, generates file.html
containing colorized html, anchors, and optional line numbers.
"""

    op = optparse.OptionParser(usage=usage, version="%prog 1")    
    op.add_option("-n", "--line-numbers",
                  action="store_true", dest="line_numbers", default=False,
                  help="Prefix each line with its line number.")

    global options
    options, args = op.parse_args()

    if len(args) == 0:
        op.error('You must specify at least one file to process.')


    # Iterate over the files, converting each to html.
    
    for fn in args:
        print (fn)

        # Open the input and output files.
        f = open(fn, "rU")
        out = open(fn + ".html", "w")

        # Write out a quick html header.
        out.write("<html><head><title>%s</title></head><body>\n" % fn)
        out.write("<pre>\n")

        # Format the python source.
        format(f.read(), out)

        # Write out a quick html footer.
        out.write("</pre>\n")
        out.write("</body></html>\n")

        out.close()
        f.close()


if __name__ == "__main__":
    main()
