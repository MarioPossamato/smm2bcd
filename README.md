## What does this do?
This is a simple command line tool that reads entity data from a Super Mario Maker 2 course file.

## What do I need to set this tool up?
[This Package](https://github.com/MarioPossamato/smm2bcd/archive/master.zip)  
[Python 3.7](https://www.python.org/downloads/release/python-370/)  
[Super Mario Maker 2 Course Decryptor](https://cdn.discordapp.com/attachments/638445176070602752/665586143001051156/smm2dec.exe) --> [Source Code](https://github.com/0Liam/SMM2CourseDecryptor)

## Note:
If you have git installed, you can run `git clone https://github.com/MarioPossamato/smm2bcd` in a console window and download the smm2bcd package that way.  Also, for now modified courses are found as 'corrupt'.  At this time the problem is being researched.

## How do I run this tool?
Before you start, make sure the `dec_path.txt` file contains the path of the course decryptor executable above...  
On Windows, just double-click the batch script included in the package;  
On Linux, open the console and type `wine cmd.exe /c` followed by the path of the batch script.

## How do I use the 'import_course_path' functions?
Make sure you set the `dec_course_path.txt` and `enc_course_path.txt` files in `path_files` to the directories of courses you want to import.

## Where do I get help/support?
[My Discord Server](https://discord.gg/8wx8uQF)

## Where can I discuss development of this app?
[My Discord Server](https://discord.gg/8wx8uQF)

## Who gets credit for this?
mario possamato for the initial script;  
comex for cleaning up the script;  
simontime for the initial course decryptor;  
blawar for the encryption support for the decryptor.
