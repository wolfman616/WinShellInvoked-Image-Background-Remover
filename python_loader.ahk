#persistent
msgbox % str:= quote("C:\windows\py.exe") " " quote("C:\Users\ninj\Desktop11\nigger.py") " " quote(a_args[1])

run,% comspec " /c " quote("C:\windows\py.exe") chr(32) quote(a_args[1]) chr(32) quote(a_args[2]),,hide