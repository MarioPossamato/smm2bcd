# smm2bcd
A simple little command-line tool that reads data from a Super Mario Maker 2 course file.

## Pre-Requisites
[smm2bcd](https://github.com/MarioPossamato/smm2bcd/archive/master.zip)  
[Python 3.7](https://www.python.org/downloads/release/python-370/)  
[Super Mario Maker 2 Course Decryptor](https://cdn.discordapp.com/attachments/638445176070602752/665586143001051156/smm2dec.exe) See *How To Compile SMM2CourseDecryptor* to compile it yourself.

## Running smm2bcd
Before you start, make sure the `dec_path.txt` file contains the path of the course decryptor binary above!  
On `Windows`, you can just double-click `smm2bcd.bat`, which is included in the package;  
On `Linux`, open the console and run `python3 -i path_to_smm2bcd.py`.

## How do I use the `import_course_path` functions?
Make sure you set the `dec_course_path.txt` and `enc_course_path.txt` files in the `path` folder to the appropriate directories of courses you want to import, then you can run
```
import_enc_course_path()
```
or
```
import_dec_course_path()
```

# How To Compile SMM2CourseDecryptor
To compile SMM2CourseDecryptor yourself, you need MinGW.  
Download and run [mingw-get-setup.exe](https://osdn.net/frs/redir.php?m=pumath&f=mingw%2F68260%2Fmingw-get-setup.exe)  
Click "Install", and click "Continue"  
Once it's done, click "Continue", and the Installation Manager will pop up  
In the Installation Manager, right-click on each of the packages, and click "Mark For Installation".  Then, go to the "Installation" tab, click "Apply Changes", then click "Apply" in the new window that pops up  
A new window will pop up.  This will take a while, so please be patient.  Once it's done, just click "Close"  
At this point, you can close the Installation Manager  
To compile SMM2CourseDecryptor, download the source code from [here](https://github.com/blawar/SMM2CourseDecryptor), or if you have git you can run "git clone https://github.com/blawar/SMM2CourseDecryptor" in the Command Prompt  
Extract the SMM2CourseDecryptor archive to a local folder on your computer, and open the Command Prompt in that folder  
Finally, in the Command Prompt run `C:\MinGW\bin\gcc.exe main.c aes.c`, and you should get a Windows Executable called a.exe, which you can rename to anything you want.

## Where do I get help/support?
[My Discord Server](https://discord.gg/8wx8uQF)

## Where can I discuss development of this app?
[My Discord Server](https://discord.gg/8wx8uQF)

## Who gets credit for this?
- Mario Possamato for the initial script  
- Comex for cleaning up the script  
- Simontime for the initial course decryptor  
- Blawar for the encryption support for the decryptor
