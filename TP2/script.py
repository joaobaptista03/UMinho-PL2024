import sys
import re

def main(inp):
    if len(inp) != 2:
        print("Usage: python3 script.py <input.md>")
        sys.exit(1)
    mdFile = open(inp[1], "r")
    lines = mdFile.readlines()
    mdFile.close()
    
    writeFile = open("output.html", "w")

    preHTML = f'''<!DOCTYPE html>
<html lang="en">

    <head>
        <title>{inp[1]}</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1" >
    </head>

    <body>

'''

    posHTML = '''

    </body>
    <h5>Generated by MDtoHTML::PL2024::A100705</h5>
</html>
'''

    orderedList = False
    unorderedList = False
    content = ''
    for line in lines:
        newLine, closeOrd, closeUnord, orderedList, unorderedList = MDtoHTML(line, orderedList, unorderedList)
        
        if (newLine == line and line != "\n"):
            newLine = f"<p>{line.strip()}</p>\n"
        
        content += "    " + closeOrd + closeUnord + newLine
    
    if orderedList:
        content += '''
    </ol>
'''

    if unorderedList:
        content += '''
    </ul>
'''

    fullHTML = preHTML + content + posHTML
    writeFile.write(fullHTML)
    writeFile.close()

    print("File generated successfully")

def MDtoHTML(line, orderedList, unorderedList):
    closeOrd = ""
    closeUnord = ""

    # HEADERS
    line = re.sub(r'^#\s+(.*?)$', r'<h1>\1</h1>', line)
    line = re.sub(r'^##\s+(.*?)$', r'<h2>\1</h2>', line)
    line = re.sub(r'^###\s+(.*?)$', r'<h3>\1</h3>', line)
    line = re.sub(r'^####\s+(.*?)$', r'<h4>\1</h4>', line)
    line = re.sub(r'^#####\s+(.*?)$', r'<h5>\1</h5>', line)
    line = re.sub(r'^######\s+(.*?)$', r'<h6>\1</h6>', line)

    # BOLD
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

    # ITALIC
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    line = re.sub(r'_(.*?)_', r'<i>\1</i>', line)

    # BLOCKQUOTE
    line = re.sub(r'^>\s+(.*?)$', r'<blockquote>\1</blockquote>', line)

    # ORDERED LIST
    if re.match(r'^\d+\.\s+(.*?)$', line):
        if orderedList:
            line = re.sub(r'^\d+\.\s+(.*?)$', r'    <li>\1</li>', line)
        else:
            line = re.sub(r'^\d+\.\s+(.*?)$', r'''<ol>
        <li>\1</li>''', line)
            orderedList = True
    else:
        if orderedList:
            closeOrd = '''</ol>
'''
            orderedList = False

    # UNORDERED LIST
    if re.match(r'^[-*+]\s+(.*?)$', line):
        if unorderedList:
            line = re.sub(r'^[-*+]\s+(.*?)$', r'    <li>\1</li>', line)
        else:
            line = re.sub(r'^[-*+]\s+(.*?)$', r'''<ul>
        <li>\1</li>''', line)
            unorderedList = True
    else:
        if unorderedList:
            closeUnord = '''</ul>
'''
            unorderedList = False

    # CODE
    line = re.sub(r'`(.*?)`', r'<code>\1</code>', line)

    # HORIZONTAL RULE
    line = re.sub(r'^\*{3,}$', r'<hr>', line)
    line = re.sub(r'^-{3,}$', r'<hr>', line)
    line = re.sub(r'^_{3,}$', r'<hr>', line)

    # LINK
    line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

    # IMAGE
    line = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', line)

    return (line, closeOrd, closeUnord, orderedList, unorderedList)


if __name__ == '__main__':
    main(sys.argv)