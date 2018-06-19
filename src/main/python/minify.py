#!/usr/bin/python

import dukpy
import os

def minifyJSProc(srcText):
    return dukpy.babel_compile(srcText, comments=False, minified=True)

def doProcessFiles(sourcePaths, header, destPath, minPath):
    print "Combining to %s and %s" % (destPath, minPath)
    f = open(destPath, 'w')
    mf = None
    try:
        mf = open(minPath, 'w')
        mf.write(header)
        for srcFile in sourcePaths:
            print(srcFile)
            with open(srcFile) as inputFile:
                srcText = inputFile.read()
                minTextObj = minifyJSProc(srcText)
            f.write(srcText)
            mf.write(minTextObj['code'])
    finally:
        f.close()
        if mf and not mf.closed:
            mf.close()

def doJSMin(sourcePaths, header, destPath, minPath):
    return doProcessFiles(sourcePaths, header, destPath, minPath)

jsDestPath = "static/concatenated.js"
jsMinPath = "static/index.min.js"
jsHeaderPath = "static/license.js"

jsSources = [
    "static/client.js",
    "static/product-area.js",
    "static/feature-request.js",
    "static/index-view-model.js",
    "static/index.js"
]

if __name__ == '__main__':
    jsHeader = ''
    with open(jsHeaderPath) as f:
        jsHeader = f.read()
    doJSMin(jsSources, jsHeader, jsDestPath, jsMinPath)
    os.remove("static/concatenated.js")
