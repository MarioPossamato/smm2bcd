# Smm2Bcd
A simple command line tool that reads entity data from a Super Mario Maker 2 course file.

## Pre-Requisites
[Smm2Bcd](https://github.com/MarioPossamato/smm2bcd/archive/master.zip)  
[Python 3.7](https://www.python.org/downloads/release/python-370/)  
[Super Mario Maker 2 Course Decryptor](https://cdn.discordapp.com/attachments/638445176070602752/665586143001051156/smm2dec.exe)

## Running Smm2Bcd
Before you start, make sure the `dec_path.txt` file contains the path of the course decryptor binary above!  
On `Windows`, just double-click the `batch script` included in the package;  
On `Linux`, open the console and type `wine cmd.exe /c` followed by the path of the batch script.

## How do I use the 'import_course_path' functions?
Make sure you set the `dec_course_path.txt` and `enc_course_path.txt` files in `path_files` to the directories of courses you want to import, then you can run
```
import_enc_course_path()
```
or
```
import_dec_course_path()
```

## Where do I get help/support?
[My Discord Server](https://discord.gg/8wx8uQF)

## Where can I discuss development of this app?
[My Discord Server](https://discord.gg/8wx8uQF)

## Who gets credit for this?
Mario Possamato for the initial script;  
Comex for cleaning up the script;  
Simontime for the initial course decryptor;  
Blawar for the encryption support for the decryptor.
