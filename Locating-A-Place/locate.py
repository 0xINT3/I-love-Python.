import sys, pyperclip, webbrowser
sys.argv  #Stores all the arguments that are passed to the command line

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() #pyperclip module stores whatever is currently copied on the clipboard
webbrowser.open('https://www.google.co.in/maps/dir/''/' + address)
