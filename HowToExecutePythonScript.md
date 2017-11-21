# MAC OSX shell script

You've got to add this at top of file:

```
#!/usr/bin/env python
```

Then make the script executable:

```
chmod +x foo
```

Then you can run it like any other executable:

```
./foo
```

# Windows batch script

create .bat file same name with your python script
- %cd% : current directory
- %* : argument

```
[example: mapit.bat]

@py.exe %cd%\mapit.py %*
```
