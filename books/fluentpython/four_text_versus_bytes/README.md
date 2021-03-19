# Chapter 4 Text Versus Bytes
We started the chapter by dismissing the notion that 1 character == 1 byte. 
As the world adopts Unicode (80% of websites already use UTF-8), we need to
keep the concept of text strings separated from the binary sequences that
represent them in files, and Python 3 enforces this separation.

After a brief overview of the binary sequence data types—bytes, bytearray,
and memoryview we jumped into encoding and decoding, with a sampling of 
important codecs, followed by approaches to prevent or deal with the infamous
UnicodeEncodeError, UnicodeDecodeError, and the SyntaxError caused by wrong
encoding in Python source files.

While on the subject of source code, I presented my position on the debate about
non-ASCII identifiers: if the maintainers of the code base want to use a human
language that has non-ASCII characters, the identifiers should follow suit unless
the code needs to run on Python 2 as well. But if the project aims to attract an
international contributor base, identifiers should be made from English words,
and then ASCII suffices.

We then considered the theory and practice of encoding detection in the absence of
metadata: in theory, it can’t be done, but in practice the Chardet package pulls
it off pretty well for a number of popular encodings. Byte order marks were then
presented as the only encoding hint commonly found in UTF-16 and UTF-32 files
sometimes in UTF-8 files as well.

In the next section, we demonstrated opening text files, an easy task except for one
pitfall: the encoding= keyword argument is not mandatory when you open a text file,
but it should be. If you fail to specify the encoding, you end up with a program that
manages to generate “plain text” that is incompatible across platforms, due to 
conflicting default encodings. We then exposed the different encoding settings that 
Python uses as defaults and how to detect them: locale.getpreferredencoding(), 
sys.getfilesystemencoding(), sys.getdefaultencoding(), and the encodings for the 
standard I/O files (e.g., sys.stdout.encoding). A sad realization for Windows users is
that these settings often have distinct values within the same machine, and the values
are mutually incompatible; GNU/Linux and OSX users, in contrast, live in a happier place
where UTF-8 is the default pretty much everywhere.

Text comparisons are surprisingly complicated because Unicode provides multiple ways of 
representing some characters, so normalizing is a prerequisite to text matching. In 
addition to explaining normalization and case folding, we presented some utility functions
that you may adapt to your needs, including drastic transformations like removing all accents.
We then saw how to sort Unicode text correctly by leveraging the standard locale module
with some caveats—and an alternative that does not depend on tricky locale configurations: 
the external PyUCA package.

Finally, we glanced at the Unicode database (a source of metadata about every character), and
wrapped up with brief discussion of dual-mode APIs (e.g., the re and os modules, where some 
functions can be called with str or bytes arguments, prompt‐ ing different yet fitting results).
