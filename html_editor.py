#!/usr/bin/env python
import os, sys, webbrowser
ui = open('./.editor.html', 'w')
contents = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/REC-html40/loose.dtd">
<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><title>HTML Word Processor</title><script>
function iimg()
{
  document.execCommand('InsertHTML', false, '\\x3Cimg src="' + prompt("Please enter the image's URL") + '" />');
}
function ilink()
{
	var lsrc = prompt("Please enter the link's source:");
	var ltext = prompt("Please enter the text displayed:");

	if(lsrc.substr(0, 7) == "http://" || lsrc.substr(0, 8) == "https://")
	{
		document.execCommand('InsertHTML', false, '\\x3Ca href="' + lsrc + '" >' + ltext + "\\x3C/a>");
	}
	else
	{
		document.execCommand('InsertHTML', false, '\\x3Ca href="http://' + lsrc + '" >' + ltext + "\\x3C/a>");

	}
}
function insertLine()
{
	document.execCommand('InsertHTML', false, '\\x3Chr/>');
}
function save()
{
	document.getElementById("htmlout").innerText = document.getElementById("contents").innerHTML;
	document.getElementById("down").href = 'data:application/x-octet-stream,' + encodeURIComponent(document.getElementById("htmlout").innerText);
	document.getElementById("down").innerHTML = 'Download this file';
	document.getElementById("down").download = document.getElementById("title").value;
}
</script></head><body>
<div style="text-align:center;">
Title: <input id="title" type="text"><br>
<button onclick="document.execCommand('bold', false, null);"><b>B</b></button>
<button onclick="document.execCommand('italic', false, null);"><i>I</i></button>
<button onclick="document.execCommand('underline', false, null);"><u>U</u></button>
<button onclick="iimg();">Img</button>
<button onclick="ilink();">Link</button>
<button onclick="document.execCommand('insertUnorderedList', false, null);">Unordered List</button>
<button onclick="document.execCommand('fontName', false, prompt('Enter the font name'));">Change font</button>
<button onclick="insertLine();">Insert line</button></div>
"""
try:
	sys.argv[1]
except IndexError:
	contents = contents + '<div contenteditable="true" style="border-style:solid; border-width:1px; background-color:#FFFFFF;" id="contents"><br/></div>'
else:
	fp = open(sys.argv[1], 'r+')
	contents = contents + '<div contenteditable="true" style="border-style:solid; border-width:1px; background-color:#FFFFFF;" id="contents">' + fp.read() + '</div>'
contents = contents + '<div style="text-align:center;" id="save"><button onclick="save();">Save</button><a id="down"></a></div>HTML output: <div id="htmlout"></div></body></html>'
ui.write(contents)
webbrowser.open_new('file://' + os.getcwd() + '/.editor.html')
