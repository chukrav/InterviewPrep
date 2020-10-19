x = 5
console.write(str(x))

def printNameAge(name, age):
	console.write("Hello {0}, ".format(name))
	console.write("how was your {0} birthday?".format(age))
	
printNameAge("vasya", 99)	

 # editor.gotoLine(line)  #to start of a line 
 # editor.setSelectionStart(0)
 # editor.setSelectionEnd(22)
 # pos = editor.findText(-1,0,100,"petya")  # -1-flag, 0-100 - start-stop positions pos == (54, 56), pos[1] == 56
 # editor.getLineCount()  # Returns the number of lines in the document. There is always at least one.
 # editor.insertText(56, "<tb>")   # Insert string at a position.
# editor.cut() #Cut the selection to the clipboard.
# editor.copy() #Copy the selection to the clipboard.
# Editor.paste() 
# Editor.appendText(text) > int #Append a string to the end of the document without changing the selection.
# Editor.lineDown() #Move caret down one line.
# Editor.lineUp() 
# Editor.charLeft() #Move caret left one character.
# Editor.charRight() 
# Editor.wordLeft() ; Editor.wordRight() 
# Editor.home() 
# Editor.lineEnd() #Move caret to last position on line.
# Editor.documentStart() #Move caret to first position in document.
# Editor.documentEnd() #Move caret to last position in document.
# Editor.newLine() #Insert a new line, may use a CRLF, CR or LF depending on EOL mode.
# Editor.delWordLeft()  Editor.delWordRight() 
# Editor.lineCut()  Editor.lineDelete() 
# Editor.lowerCase() Transform the selection to lower case.
# Editor.upperCase() Transform the selection to upper case.
# Editor.lineCopy() Copy the line containing the caret.
# Editor.lineLength(line) > int How many characters are on a line, including end of line characters?
# Editor.replaceLine(line, newContents) 
# Editor.setTarget(start, end) 
# editor.rereplace('^', "<tb>");
# Editor.forEachLine(function) #Runs the function passed for each line in the current document.

















