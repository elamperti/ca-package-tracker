#!/usr/bin/python

from PIL import Image, ImageFilter
import sys

import pyocr
import pyocr.builders


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = 'eng'
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'

captcha = Image.open('samples/sample-1.png')
captcha=captcha.filter(ImageFilter.GaussianBlur(radius=2))

txt = tool.image_to_string(
    captcha,
    lang=lang,
    builder=pyocr.builders.TextBuilder()
)
# word_boxes = tool.image_to_string(
#     Image.open('test.png'),
#     lang="eng",
#     builder=pyocr.builders.WordBoxBuilder()
# )
# line_and_word_boxes = tool.image_to_string(
#     Image.open('test.png'), lang="fra",
#     builder=pyocr.builders.LineBoxBuilder()
# )

# Digits - Only Tesseract (not 'libtesseract' yet !)
# digits = tool.image_to_string(
#     Image.open('test-digits.png'),
#     lang=lang,
#     builder=pyocr.tesseract.DigitBuilder()
# )

print("Recognized text: %s" % txt)
