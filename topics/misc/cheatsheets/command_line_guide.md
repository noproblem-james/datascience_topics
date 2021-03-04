# Guide to the Command Line

### Table of Contents

[Level 1: Basics](#level-1-basics)
 - Short list of commonly used commands
 - Navigation in terminal emulator
 - Vim fundamentals  

[Level 2: Slightly More Advanced](#level-2-slightly-more-advanced)
 - Control and Redirection Operators, Globbing
 - Another Short List of Familiar Commands
 - Some Slightly More Obscure (But Useful!) Commands

[Level 3: Real Proficiency](#level-3-real-proficiency)
 - Text and File Manipulation
   - Sed, awk
   - regex
   - diff  
- Processes
- [Disk Management](#disk-management)
- Package Management
- [Networking](#networking)
- Linux Specific

[Other CLIs](#other-clis)
- Git
- Docker CLI
- Openshift CLI


- Further Discussion
  - `less` vs `more`, `cat`
  - `curl` vs `wget`
  - `find`
  - `sed` vs. `awk` + regex
  - `find`
  - `top`
  - `systemctl`


[Misc](#misc)

## Level 1: Basics

#### The Short List - Used all the time
`pwd` print working directory  
`ls` list files and subdirectories  (`ls –a` 	list all files, including hidden files and directories, including those whose names start with `.` )  
`cd` change directory (`cd ~` change to home dir; `cd -` change to previous dir; `cd /` change to root dir)  
`mv` move (also, change name)  
`cp` copy  
`rm` remove  
`cat` (concatenate) print entire file, more below  
`less` display file one page at a time (use `q` to escape)  
`head` print top lines  
`mkdir` make directory  
`touch` create file (or update the timestamp of an existing file)  
`rmdir` remove directory (if it has no contents)  
`rm -rf` remove--recursive and force; delete directory and all of its contents  
`echo` print arguments  
`grep` search; will accept regex  

#### Navigation
**ctl + a** beginning of line  
**ctl + e** end of line  
**ctl + d** last line character  
**ctl + c** interrupt, exit current process  
**ctl + r**  search previously used commands

**ctl + k** delete from cursor to the end of the command line.
**ctrl + w** delete from cursor to start of word (i.e. delete backwards one word)
**Up/Down arrow keys** Browse through the list of commands previously executed
**!!**  Execute the previous command (Pronounced as "bang-bang")
`history` see command history  
`clear` clear the screen  

| Keyboard Shortcut | Task                                               |
|-------------------|----------------------------------------------------|
| CTRL+A            | Goes to the beginning of the line                  |
| CTRL+E            | Goes to the end of the line                        |
| CTRL+L            | Clears the screen                                  |
| CTRL+D            | Exits the current shell                            |
| CTRL+Z            | Puts the current process into suspended background |
| CTRL+C            | Kills the current process                          |
| CTRL+H            | Works the same as backspace                        |
| CTRL+W            | Deletes the word before the cursor                 |
| CTRL+U            | Deletes from beginning of line to cursor position  |
| CTRL+K            | Deletes from cursor position to end of line        |
| CTRL+Z            | Suspend foreground processes                       |


##### Executing previously issued commands

| Syntax  | Task                                                  |
|---------|-------------------------------------------------------|
| !       | Start a history substitution                          |
| !$      | Refer to the last argument in a line                  |
| !n      | Refer to the nth command line                         |
| !string | Refer to the most recent command starting with string |

### Vim

Text editors (rather than word processing programs) are used quite often in Linux, for tasks such as creating or modifying system configuration files, writing scripts, developing source code, etc.

The vi editor is available on all Linux systems and is very widely used. All developers have at least some proficiency in vim, even if they prefer to use an alternative whenever possible.

vi has three modes: Command, Insert, and Line. emacs has only one, but requires use of special keys, such as Control and Escape.



**i** enter insert mode in vim   
**esc** enter command mode in vim  
`:wq` write and quit  
`:q!` quit without writing  
`:%s/stringtoreplace/replacewithstring/g` hack for find/replace  
**A**  automatically move the cursor to the end of the line and enter Insert Mode.  
**G** move to end of file and enter Insert Mode  
**gg** move to beginning of file  
**^** move  cursor to first non-blank character of a line  
**0** always moves the cursor to the "first column"  
**esc + gg + dG** clear all lines (go to first line, delete from first line to last)  
`w` in command mode, move forward one word at a time  
`b` in command mode, move backward one word at a time  
`v` in command mode, enter visual mode (highlighting)  
`dw` delete the characters from the cursor to the end of the word


## Level 2: Slightly More Advanced

##### Control operators
`|` pipe, passes the output of one command as input to another  
`;` run one command after another has finished, irrespective of the outcome of the first.  
`&` Run a command in the background, allowing you to continue working in the same shell.  
`&&` chain, run one command only if another exited successfully.  
`||` Build OR lists; run one command only if another exited *unsuccessfully*.  

##### Redirection operators

`<` Give input to a command  
`>` Direct the output of a command into a file.  
`>>` Does the same as `>`, except that if the target file exists, new data are appended.  
`<<` A here document. It is often used to print multi-line strings.  
`<<<` Here strings, similar to here documents, but intended for a single line; used for feeding input into a prior command.  
`2>`allows you to capture stderr instead of stdout. Often you need to discard error or normal output. You can do this by redirecting to the device `/dev/null`  
`$ do_something 2> error-file`  redirect stderr to a separate file, you use stderr’s file descriptor number (2), the greater-than sign (>), followed by the name of the file you want to hold everything the running command writes to stderr
`$ do_something > all-output-file 2>&1` A special shorthand notation can send anything written to file descriptor 2 (stderr) to the same place as file descriptor 1 (stdout): 2>&1.

##### Globbing
`*` wildcard  
`{}` match any of the alternative string sequences, e.g., `ls app.{css, html}`  
`[]` match any one of the characters  
`?` match any one character
***
#### Another Short List of Familiar Commands/Utilities
`passwd` change password  
`uname -a` info about the operating system  
`id` info about the user  
`uptime`  how long system has been on  
`su` switch user (become superuser for a series of commands)  
`sudo <command>` superuser do. Execute just one command with root privileges.  
`chmod` change mode, change access permissions of filesystem objects (files and directories)  
`chown` 	Used to change user ownership of a file or directory
`chgrp` 	Used to change group ownership
`exit` exit the shell; also, terminate your current ssh connection.  
`bc` (bench calculator) calculator program, understands order of operations, etc.  
`nproc`  print the number of processing units available    
`free -g` displays the total amount of free space available (with flag, does so in gigabytes)
`df -lh` disk space  (local, human readable)
`man <util name>` print manual (man page  
`info` find info about GNU tools.  
`apropos` search the names and descriptions of all available man pages
`file` indicate the type of a file  
`type` determine how the shell is going to interpret any command  
`alias` change command assignment (with no args, list all currently defined aliases)  
`unalias` revert command assignment  
`var=$(command-name-here)` assign output of command to a variable  
`var=<command-name-here>`  alternative syntax to assign output of command to a variable  
`shasum` - Print or Check SHA Checksums  
`tree` bird’s-eye view of the filesystem tree. Use tree -d to view just the directories and to suppress listing file names.
`xref` TODO  
`xargs`  build and execute command lines from standard input  
`watch` execute a program periodically, showing output in fullscreen.  
`locate` (linux only) performs a search taking advantage of a previously constructed database of files and directories on your system.   
`updatedb` update file directory db (the one used by `locate`)
`find` lists all files in the current directory and all of its subdirectories.  
`whereis` find the location of source/binary file of a command and manuals sections for a specified file in Linux system.  
`wget` ('World Wide Web + get') a free utility for non-interactive download of files from the Web.  
`curl` ('Client URL') is a tool to transfer data from or to a server, using one of the (many) supported protocols.  
`cat /etc/*release ` get more info about OS (Linux)  
`mount`  can be used to inquire whether a filesystem is mounted as read-only or as read/write  
`du`  “disk usage”, reports the estimated amount of disk space used by given files or directories


### Some slightly more obscure commands

`nl` print a file out with line numbers  
`tac` reverse cat - prints files out last line first (linux only)  
`printf` formatted printing of arguments to the fullscreendircolors -set the colors used by ls to differentiate file types  
`dir` briefly print out directory contents (linux only)
`od` print out binary files in human readable forms  
`strings` display printable strings from a binary file  
`pushd` and `popd` maintain directory stack, allowing rapid movement between directories (BASH and tcsh only)  
`date` display current date and times  
`time` time a command  
`tee` takes input and writes it both to a named file and to stdout, which is normally the screen. (The tee command's name comes from its resemblance to a T-fitting in a water pipe.)  
`who` list the currently logged-on users. `-a` option will give more detailed information.  
`useradd`, `userdel` add new user, remove existing user  
`groups <username>` show groups to which a user belongs  
`usermod` add a user to an already existing group
`ptx` produce permuted indexes, that is, keyword index with the keyword in context (TODO Not sure what this means)  
`pr` pretty print - displays the file with page headings and numbers, suitable for physical printing  
`nano <filename>` nano text editor, a little more user-friendly than Vim  
 `ln` used to create hard links and (with the `-s` option) soft links, also known as symbolic links or symlinks. (see more below)  
`pushd`, `popd`  put a filesystem location on the queue, pop it back off again (and move there)
`dirs` TODO
`halt` instructs the hardware to stop all the CPU functions. Basically, it reboots or stops the system. If the system is in runlevel 0 or 6 or using the command with –force option, it results in rebooting of the system otherwise it results in shutdown.  
`zcat`, `zless`, `zdiff`, `zgrep` special utilities for commonly-used file and text manipulation programs, there is also a version especially designed to work directly with compressed files. These associated utilities have the letter "z" prefixed to their name. There are also equivalent utility programs for other compression methods besides gzip, for example, we have bzcat and bzless associated with bzip2, and xzcat and xzless associated with xz.  
`bg`, `fg` run a process in the background and foreground, respectively.  
`jobs` enumerate the background processes running in the current terminal session  
`at` execute non-interactive programs at a specific time  
`diff3` compare three files at once  
`rsync` bakup data (see more below)  
`last`  shows the last time each user logged into the system; used to identify how long a user account has remained inactive  
`chage` ensures that passwords, if cracked, will only be usable for a limited amount of time.  
`visudo` edit superuser configuration files. /etc/sudoers contains a lot of documentation in it about how to customize. Most Linux distributions now prefer you add a file in the directory /etc/sudoers.d with a name the same as the user. This file contains the individual user's sudo configuration, and one should leave the master configuration file untouched except for changes that affect all users.  

You should edit any of these configuration files by using visudo, which ensures that only one person is editing the file at a time, has the proper permissions, and refuses to write out the file and exit if there are syntax errors in the changes made.




## Level 3: Real Proficiency

### Text and file manipulation

`tr` translate characters (also, remove unwanted characters). always used as a filter and acts upon its stdin; cannot supply a filename without using redirection.  

`sort` sort input, accepts multiple file arguments to merge and sort into single output.
 - `-r` reverse sort.
 - `-f` ignore case (otherwise, by default, sorts any uppercase letters before any lowercase letters)

`cut` cut out fields of a file, using either whitespace (space and Tab characters) as the delimiter. Useful for files where data is presented in fields, such as Linux control files, like the password file.
  - `-d` Specifies the delimiter for fields
  - `-f` Specifies the field number  
  - `-c` Cut by  (e.g., `-c1-3` means that you want the first, second and third characters cut from the file.)

`uniq` print out unique lines in a sorted file
`diff` print differences between files  
`cmp` compare two files  
`comm` compare files for common lines.  
`diff` displays the differences between two files.
`zcmp`, `zdiff` compare compressed files

`paste` merge files horizontally (as opposed to vertically with `cat`). takes a line from each of the files on the command line and constructs a single line, with all fields separated by tabs.
 - `-s` serial option, can paste sequential lines from the one file, instead of from multiple files.
 - `-d` delimiter specify field separators  

`join` selects lines in two files that have a matching key field, and joins the two lines together with optional output field control. Both files must be sorted in key field order.
 - `-t` supply a delimiter (default is tab)
 - By default, join tries to match the first field in each file, and you can  with the . Normally, tab would be the delimiter. For the example, `-12` option specifies the key for file one is field two.  

`strings` extracts printable character strings from binary files.


`wc` wordcount. prints the line, word, and character count, in that order:
   - `-c` print out character count
   - `-w` print out word count
   - `-l` print out line count  

`sed` ('stream editor') frequently used for searching, find and replace, insertion hand deletion.

`awk` (acronym of its developers' names) a scripting language used for manipulating data and generating reports, mostly used for pattern scanning and processing.

### Other
`exportfs` ensure that the shared files are available over a network


***


## Further Discussion


### More on `cat`, `echo`, `less` and `more`
#### `cat`
- `cat` can take a number of files on its command line and display them together. Since this can be redirected to another file, cat can be used to create files that are concatenations of the original files, hence the name.  


| Command                   | Usage                                                                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| cat file1 file2           | Concatenate  multiple files and display the output; i.e. the entire content of the  first file is followed by that of the second file |
| cat file1 file2 > newfile | Combine multiple files and save the output into a new file                                                                            |
| cat file >> existingfile  | Append a file to the end of an existing file                                                                                          |
| cat > file                | Any subsequent lines typed will go into the file, until CTRL-D is typed                                                               |
| cat >> file               | Any subsequent lines are appended to the file, until CTRL-D is typed                                                                  |


  - cat is one of the most frequently used Linux command line utilities. It is often used to read and print files, as well as for simply viewing file contents. To view a file, use the following command:

    `$ cat <filename>`

    For example, cat readme.txt will display the contents of readme.txt on the terminal. However, the main purpose of cat is often to combine (concatenate) multiple files together. You can perform the actions listed in the table using cat.

    The tac command (cat spelled backwards) prints the lines of a file in reverse order. Each line remains the same, but the order of lines is inverted. The syntax of tac is exactly the same as for cat.

    cat can be used to read from standard input (such as the terminal window) if no files are specified. You can use the > operator to create and add lines into a new file, and the >> operator to append lines (or files) to an existing file. We mentioned this when talking about how to create files without an editor.

- creating a new file with cat
  To create a new file, at the command prompt type cat > <filename> and press the Enter key.

  This command creates a new file and waits for the user to edit/enter the text. After you finish typing the required text, press CTRL-D at the beginning of the next line to save and exit the editing.

  Another way to create a file at the terminal is cat > <filename> << EOF. A new file is created and you can type the required input. To exit, enter EOF at the beginning of a line.

  Note that EOF is case sensitive. One can also use another word, such as STOP.

#### `echo`


echo simply displays (echoes) text. It is used simply, as in:

`$ echo string`

echo can be used to display a string on standard output (i.e. the terminal) or to place in a new file (using the > operator) or append to an already existing file (using the >> operator).

The –e option, along with the following switches, is used to enable special character sequences, such as the newline character or horizontal tab.

            \n  represents newline
            \t  represents horizontal tab.

echo is particularly useful for viewing the values of environment variables (built-in shell variables). For example, echo $USERNAME will print the name of the user who has logged into the current terminal.

The following table lists echo commands and their usage:


| Command                     | Usage                                                                   |
|-----------------------------|-------------------------------------------------------------------------|
| echo string > newfile       | The specified string is placed in a new file                            |
| echo string >> existingfile | The specified string is appended to the end of an already existing file |
| echo $variable              | The contents of the specified environment variable are displayed        |

#### `less` and `more`
- use less to view the contents of such a large file, scrolling up and down page by page, without the system having to place the entire file in memory before starting. This is much faster than using a text editor.
- By default, man pages are sent through the less command. You may have encountered the older more utility which has the same basic function but fewer capabilities: i.e. less is more!

- `less` command provides extra functionality in moving through text
- If you want to move forward or back a page in either more or less, you can use the `PageUp` `PageDown` keys, or just `f` and `b`. Typing q at the prompt will quit displaying the file.
- If you forget the commands to use, type `h` and more will display a page of help text.

### More on `chmod` and `shashum`

`chmod`
- `r`, `w`, and `x` specify the read, write, and execute, respectively
- `-R` Recursive, i.e. include objects in subdirectories.  
  `-v` verbose, show objects changed (unchanged objects are not shown).


#### File Permission Modes and `chmod`

Files have three kinds of permissions: read (r), write (w), execute (x). These are generally represented as in rwx. These permissions affect three groups of owners: user/owner (u), group (g), and others (o).

As a result, you have the following three groups of three permissions:

```
rwx: rwx: rwx
 u :  g :  o
```

There are a number of different ways to use chmod. For instance, to give the owner and others execute permission and remove the group write permission

```bash
$ ls -l somefile
-rw-rw-r-- 1 student student 1601 Mar 9 15:04 somefile
$ chmod uo+x,g-w somefile
$ ls -l somefile
-rwxr--r-x 1 student student 1601 Mar 9 15:04 somefile
```
where u stands for user (owner), o stands for other (world), and g stands for group.

This kind of syntax can be difficult to type and remember, so one often uses a shorthand which lets you set all the permissions in one step. This is done with a simple algorithm, and a single digit suffices to specify all three permission bits for each entity. This digit is the sum of:

            4 if read permission is desired
            2 if write permission is desired
            1 if execute permission is desired.

Thus, 7 means read/write/execute, 6 means read/write, and 5 means read/execute.

When you apply this to the chmod command, you have to give three digits for each degree of freedom, such as in:

```bash
$ chmod 755 somefile
$ ls -l somefile
-rwxr-xr-x 1 student student 1601 Mar 9 15:04 somefile
```


`shasum`  
  - `-a` --algorithm. `-a 256` tells shasum to use sha256.  
  - `-c` --check. tells shasum to "check" the provided input.  
  - example usage: `shasum -a 256 -c <<< '<hash_to_compare> *<filename>'` cool one-liner for checksum

### More on `man`, `apropos`, and `info`
`man`
- `–f` generates the same result as typing `whatis`.
- `–k` generates the same result as typing `apropos`.
- `-a` display all man pages in sequence with the given name in all chapters
 - once viewing manual page: `f` move forward `b`; move back a page; `h` key will show other options available.


`info` find info about GNU tools.  lends itself to more detailed, hyperlinked descriptions than `man`.
 - once inside the info pages: `n` Go to the next node; `p` Go to the previous node; `u` Move one node up in the index . info command (with no arguments) shows the index of topics.

 `help` (linux only) displays a short synopsis of built-in shell commands

### More about `curl` and `wget`

`wget`

Sometimes you need to download files and information, but a browser is not the best choice, either because you want to download multiple files and/or directories, or you want to perform the action from a command line or a script. `wget` is a command line utility that can capably handle the following types of downloads:

- Large file downloads
- Recursive downloads, where a web page refers to other web pages and all are downloaded at once
- Password-required downloads
- Multiple file downloads.

To download a web page, you can simply type wget <url>, and then you can read the downloaded page as a local file using a graphical or non-graphical browser.

`curl`

Besides downloading, you may want to obtain information about a URL, such as the source code being used. `curl` can be used from the command line or a script to read such information. `curl` also allows you to save the contents of a web page to a file, as does `wget`.

You can read a URL using `curl <URL>`. For example, if you want to read http://www.linuxfoundation.org, type `curl http://www.linuxfoundation.org`.

To get the contents of a web page and store it to a file, type c`url -o saved.html http://www.mysite.com`. The contents of the main index file at the website will be saved in `saved.html`.


`curl`
- `-k`: pass through secure certificate error  
- `-H "Authorization: Bearer  <token>"` : pass a header with an authorization token
- `-L`
- `-v`
- `-u` <username>:<password>

#### Differences between `curl` and `wget`
- `wget` can download recursively.
- `wget` is command-line only, with no library, but curl's features are powered by libcurl.
- `curl` supports many more transfer protocols (FTP, FTPS, HTTP, HTTPS, SCP, SFTP, TFTP, TELNET, DICT, LDAP, LDAPS, FILE, POP3, IMAP, SMTP, RTMP and RTSP). `wget` supports HTTP, HTTPS and FTP.
- `curl` builds and runs on more platforms than `wget`.
- `wget` is released under a free software copyleft license (the GNU GPL). `curl` is released under a free software permissive license (an MIT derivate).
- `curl` offers upload and sending capabilities. `wget` only offers plain HTTP POST support.

### More on `ln`
The `ln` command is a standard Unix command utility used to create a hard link or a symbolic link (symlink) to an existing file.

- The use of a hard link allows multiple filenames to be associated with the same file since a hard link points to the inode of a given file, the data of which is stored on disk. (An **inode** (index node) is a data structure in a Unix-style file system that describes a file-system object such as a file or a directory.)
- On the other hand, symbolic links are special files that refer to other files by name.

- The `ln` command by default creates hard links, and when called with the command line parameter `ln -s `creates symbolic links.

- Most operating systems prevent hard links to directories from being created since such a capability could disrupt the structure of a file system and interfere with the operation of other utilities.

- The `ln` command can however be used to create symbolic links to non-existent files.

Hard links are very useful and they save space, but you have to be careful with their use, sometimes in subtle ways. For one thing, if you remove either file1 or file2 in the example, the inode object (and the remaining file name) will remain, which might be undesirable, as it may lead to subtle errors later if you recreate a file of that name.

If you edit one of the files, exactly what happens depends on your editor; most editors, including vi and gedit, will retain the link by default, but it is possible that modifying one of the names may break the link and result in the creation of two objects.

Symbolic links take no extra space on the filesystem (unless their names are very long). They are extremely convenient, as they can easily be modified to point to different places. An easy way to create a shortcut from your home directory to long pathnames is to create a symbolic link.

Unlike hard links, soft links can point to objects even on different filesystems, partitions, and/or disks and other media,  which may or may not be currently available or even exist. In the case where the link does not point to a currently available or existing object, you obtain a dangling link.

### More on `locate`, `find`, and `updatedb`

`locate` performs a search, matching all entries that contain a specified character string. This can sometimes result in a very long list. To get a shorter (and possibly more relevant) list, we can use the grep program as a filter, e.g., `$ locate zip | grep bin`

`locate` utilizes a database created by a related utility, updatedb.

`updatedb` Most Linux systems run this automatically once a day, but you can  it at any time by just running command as the root user.    

Commonly used options to shorten the list include `-name` (only list files with a certain pattern in their name), `-iname` (also ignore the case of file names), and `-type` (which will restrict the results to files of a certain specified type, such as `d` for directory, `l` for symbolic link, or `f` for a regular file, etc.).
 - e.g., `$ find /usr -type d -name gcc` searches only for directories named 'gcc'.



 - `-exec`run commands on the files that match your searcha criteria. E.g., to find and remove all files that end with .swp: `find -name "*.swp" -exec rm {} \’;\’`
    - The {} curly braces are a placeholder that will be filled with all the file names that result from the find expression, and the preceding command will be run on each one individually. You must end the command with either ‘;’ (including the single-quotes) or "\;". Both forms are fine.
 - `-ok` option, which behaves the same as `-exec`, except that find will prompt you for permission before executing the command. This makes it a good way to test your results before blindly executing any potentially dangerous commands.


It is sometimes the case that you wish to find files according to attributes, such as when they were created, last used, etc., or based on their size. It is easy to perform such searches.

To find files based on time:

`find / -ctime 3`

Here, `-ctime` is when the inode metadata (i.e. file ownership, permissions, etc.) last changed; it is often, but not necessarily, when the file was first created. You can also search for accessed/last read (`-atime`) or modified/last written (`-mtime`) times. The number is the number of days and can be expressed as either a number (n) that means exactly that value, +n, which means greater than that number, or -n, which means less than that number. There are similar options for times in minutes (as in -cmin, -amin, and -mmin).

Note the size here is in 512-byte blocks, by default; you can also specify bytes (c), kilobytes (k), megabytes (M), gigabytes (G), etc. As with the time numbers above, file sizes can also be exact numbers (n), +n or -n.

#### Examples


`$ find / -size 0` find files of size 0 in the root directory

`$ find / -size +10M -exec head {} ’;’` find files greater than 10 MB in size and print first lines from those files

`$ find -type f -mtime 0` find files in current directory modified today.

### More on `pushd` and `popd`
The cd command remembers where you were last, and lets you get back there with `cd -`. For remembering more than just the last directory visited, use `pushd` to change the directory instead of cd; this pushes your starting directory onto a list. Using `popd` will then send you back to those directories, walking in reverse order (the most recent directory will be the first one retrieved with `popd`). The list of directories is displayed with the


### More on `rsync`
There are many ways you can back up data or even your entire system. Basic ways to do so include the use of simple copying with cp and use of the more robust rsync.

Both can be used to synchronize entire directory trees.
rsync is more efficient, because it checks if the file being copied already exists. If the file exists and there is no change in size or modification time, rsync will avoid an unnecessary copy and save time. Furthermore, because rsync copies only the parts of files that have actually changed, it can be very fast.

cp can only copy files to and from destinations on the local machine (unless you are copying to or from a filesystem mounted using NFS), but rsync can also be used to copy files from one machine to another. Locations are designated in the target:path form, where target can be in the form of someone@host. The someone@ part is optional and used if the remote user is different from the local user.

rsync is very efficient when recursively copying one directory tree to another, because only the differences are transmitted over the network. One often synchronizes the destination directory tree with the origin, using the -r option to recursively walk down the directory tree copying all files and directories below the one listed as the source.



rsync is a very powerful utility. For example, a very useful way to back up a project directory might be to use the following command:

$ rsync -r project-X archive-machine:archives/project-X

Note that rsync can be very destructive! Accidental misuse can do a lot of harm to data and programs, by inadvertently copying changes to where they are not wanted. Take care to specify the correct options and paths. It is highly recommended that you first test your rsync command using the -dry-run option to ensure that it provides the results that you want.

To use rsync at the command prompt, type rsync sourcefile destinationfile, where either file can be on the local machine or on a networked machine; The contents of sourcefile will be copied to destinationfile.

A good combination of options is shown in:

$ rsync --progress -avrxH  --delete sourcedir destdir

### More on `visudo`

### More on `patch`
`patch`
`$ diff -Nur originalfile newfile > patchfile`

Distributing just the patch is more concise and efficient than distributing the entire file. For example, if only one line needs to change in a file that contains 1000 lines, the patch file will be just a few lines long.

To apply a patch, you can just do either of the two methods below:

`$ patch -p1 < patchfile`
`$ patch originalfile patchfile`

The first usage is more common, as it is often used to apply changes to an entire directory tree, rather than just one file, as in the second example. To understand the use of the -p1 option and many others, see the man page for patch.

### More about `comm` and `diff`
- By default, comm produces three columns of output. The first column contains the lines found only in the first file on the command line. The second column contains the lines found only in the second file, and the third column contains lines common to both files.
- if you only want the common lines, you would suppress columns one and two by using the option `-12`  


`diff` displays the differences between two files. The normal output may be a little cryptic, but it was designed to make it easy to produce automated edit scripts, to bring one file in line with another.

The diff command is an essential part of many version control systems, including rcs and cvs, both of which are standard Linux utilities.

```
$ diff monarchs streets
1d0
< Charles
3,5c2,5
< George
< Henry
< Victoria
---
> King
> Queen
> Russell
> Spencer
```


The 1d0 at the top of the output says to delete the first line in file one, and there is no corresponding line in file two. The 3,5c2,5 says that lines three to five in file one are changed to match lines two to five in file two. Lines in file one to be modified are marked with a less than (<) and added lines in file two are marked with a greater than character (>).

```
$ diff -c monarchs streets
*** monarchs      Wed Jan  9 17:04:10 2002
--- streets       Wed Jan  9 17:04:20 2002
***************
*** 1,6 ****
- Charles
! George
! Henry
! Victoria
  William
--- 1,6 ----
  Elizabeth
! King
! Queen
! Russell
! Spencer
  William
  ```

Using the context option (-c) with the diff command will produce output that is more easily readable, by providing separating lines around the changed lines. The files are marked with either asterisks or dashes, as displayed at the top of the output.

The line numbers of affected lines are displayed at the top of each block of output. Deleted lines are marked with a dash (-), added lines are marked with a plus (+) and changed lines marked with an exclamation mark (!).

Once you understand the output, diff can be a very useful utility for sorting out changed areas of source code or documentation files.

| diff Option | Usage                                                                                                                 |
|-------------|-----------------------------------------------------------------------------------------------------------------------|
| -c          | Provides a listing of differences that include three lines of context before and after the lines differing in content |
| -r          | Used to recursively compare subdirectories, as well as the current directory                                          |
| -i          | Ignore the case of letters                                                                                            |
| -w          | Ignore differences in spaces and tabs (white space)                                                                   |
| -q          | Be quiet: only report if files are different without listing the differences                                          |


`diff -qr /usr/src/linux-4.9 /usr/src/linux-4.10:` recursively compare two directory trees, just mentioning which files

### More about `sed` and `awk`
many Linux users and administrators will write scripts using comprehensive scripting languages such as Python and perl, rather than use sed and awk (and some other utilities we will discuss later). Using such utilities is certainly fine in most circumstances; one should always feel free to use the tools one is experienced with. However, the utilities that are described here are much lighter; i.e. they use fewer system resources, and execute faster. There are situations (such as during booting the system) where a lot of time would be wasted using the more complicated tools, and the system may not even be able to run them. So, the simpler tools will always be needed.

Difference between `sed` and `awk`
  - `sed` is a command utility often used to filter and perform substitutions on files and text data streams.
  - `awk` more powerful and robust with sophisticated programming constructs such as if/else, while, do/while etc. it's an interpreted programming language, typically used as a data extraction and reporting tool.

`awk` (Aho, Weinberger, and Kernighan--developers' names) a scripting language used for manipulating data and generating reports, mostly used for pattern scanning and processing. It searches one or more files to see if they contain lines that matches with the specified patterns and then performs the associated action.  

`sed` The most common use of SED command in UNIX is for substitution or for find and replace. Can edit files without opening them, which is much quicker than manually opening the file in VI Editor and then changing it.  

- `sed -e command <filename>`  Specify editing commands at the command line, operate on file and put the output on standard out (e.g. the terminal). The `-e` option allows you to specify multiple editing commands simultaneously at the command line. It is unnecessary if you only have one operation invoked.

- `sed -f scriptfile <filename> `	Specify a scriptfile containing sed commands, operate on file and put output on standard out

| Command                                | Usage                                                 |
|----------------------------------------|-------------------------------------------------------|
| sed s/pattern/replace_string/ file     | Substitute first string occurrence in every line      |
| sed s/pattern/replace_string/g file    | Substitute all string occurrences in every line       |
| sed 1,3s/pattern/replace_string/g file | Substitute all string occurrences in a range of lines |
| sed -i s/pattern/replace_string/g file | Save changes for string substitution in the same file |

You must use the -i option with care, because the action is not reversible. It is always safer to use `sed` without the `–i` option and then replace the file yourself, as shown in the following example:

`$ sed s/pattern/replace_string/g file1 > file2`

The above command will replace all occurrences of pattern with `replace_string` in `file1` and move the contents to `file2`. The contents of `file2` can be viewed with `cat file2`. If you approve you can then overwrite the original file with `mv file2 file1`.


#### `awk`

awk is used to extract and then print specific contents of a file and is often used to construct reports. It was created at Bell Labs in the 1970s and derived its name from the last names of its authors: Alfred Aho, Peter Weinberger, and Brian Kernighan.

awk has the following features:

- It is a powerful utility and interpreted programming language.
- It is used to manipulate data files, retrieving, and processing text.
- It works well with fields (containing a single piece of data, essentially a column) and records (a collection of fields, essentially a line in a file).

As with sed, short awk commands can be specified directly at the command line, but a more complex script can be saved in a file that you can specify using the -f option.

The table explains the basic tasks that can be performed using awk. The input file is read one line at a time, and, for each line, awk matches the given pattern in the given order and performs the requested action. The -F option allows you to specify a particular field separator character. For example, the /etc/passwd file uses ":" to separate the fields, so the -F: option is used with the /etc/passwd file.

The command/action in awk needs to be surrounded with apostrophes (or single-quote (')). awk can be used as follows:

| Command                               | Usage                                                          |
|---------------------------------------|----------------------------------------------------------------|
| awk '{ print $0 }' /etc/passwd        | Print entire file                                              |
| awk -F: '{ print $1 }' /etc/passwd    | Print first field (column) of every line, separated by a space |
| awk -F: '{ print $1 $7 }' /etc/passwd | Print first and seventh field of every line                    |


### More about `sort` and `uniq` and `paste` and `join` and `split`

| Syntax                  | Usage                                   |
|-------------------------|-----------------------------------------|
| sort <filename>         | Sort the lines in the specified file, according to the characters at the beginning of each line |
| cat file1 file2 \| sort | Combine the two files, then sort the lines and display the output on the terminal               |
| sort -r <filename>      | Sort the lines in reverse order                                                                 |
| sort -k 3 <filename>    | Sort the lines by the 3rd field on each line instead of the beginning                           |

When used with the -u option, sort checks for unique values after sorting the records (lines). It is equivalent to running `uniq` on the output of sort.

`uniq` removes duplicate consecutive lines in a text file and is useful for simplifying the text display.

Because uniq requires that the duplicate entries must be consecutive, one often runs sort first and then pipes the output into uniq; if sort is used with the -u option, it can do all this in one step.

To remove duplicate entries from multiple files at once, use the following command:

sort file1 file2 | uniq > file3

or

sort -u file1 file2 > file3

To count the number of duplicate entries, use the following command:

uniq -c filename

paste

paste can be used to create a single file containing all three columns. The different columns are identified based on delimiters (spacing used to separate two fields). For example, delimiters can be a blank space, a tab, or an Enter. In the image provided, a single space is used as the delimiter in all files.

paste accepts the following options:

            -d delimiters, which specify a list of delimiters to be used instead of tabs for separating consecutive values on a single line. Each delimiter is used in turn; when the list has been exhausted, paste begins again at the first delimiter.
            -s, which causes paste to append the data in series rather than in parallel; that is, in a horizontal rather than vertical fashion.


join
Suppose you have two files with some similar columns. You have saved employees’ phone numbers in two files, one with their first name and the other with their last name. You want to combine the files without repeating the data of common columns. How do you achieve this?

The above task can be achieved using join, which is essentially an enhanced version of paste. It first checks whether the files share common fields, such as names or phone numbers, and then joins the lines in two files based on a common field.

split

split is used to break up (or split) a file into equal-sized segments for easier viewing and manipulation, and is generally used only on relatively large files. By default, split breaks up a file into 1000-line segments. The original file remains unchanged, and a set of new files with the same name plus an added prefix is created. By default, the x prefix is added. To split a file into segments, use the command split infile.

To split a file into segments using a different prefix, use the command split infile <Prefix>.

### More about `grep`
`grep -ril "word"`
- `-r` recursive
- `-i` ignore case distinctions
- `-l` print only the filenames (with GNU grep)



grep is extensively used as a primary text searching tool. It scans files for specified patterns and can be used with regular expressions, as well as simple strings, as shown in the table:

| Command                        | Usage                                                            |
|--------------------------------|------------------------------------------------------------|
| grep [pattern] <filename>      | Search for a pattern in a file and print all matching lines                                                                                             |
| grep -v [pattern] <filename>   | Print all lines that do not match the pattern                                                                                                           |
| grep [0-9] <filename>          | Print the lines that contain the numbers 0 through 9                                                                                                    |
| grep -C 3 [pattern] <filename> | Print  context of lines (specified number of lines above and below the  pattern) for matching the pattern. Here, the number of lines is  specified as 3 |

strings
`strings` is used to extract all printable character strings found in the file or files given as arguments. It is useful in locating human-readable content embedded in binary files; for text files one can just use grep.

For example, to search for the string my_string in a spreadsheet:

$ strings book1.xls | grep my_string

The screenshot shows a  search of a number of programs to see which ones have GPL licenses of various versions.



### Brief aside about regex

Regular expressions are text strings used for matching a specific pattern, or to search for a specific location, such as the start or end of a line or a word. Regular expressions can contain both normal characters or so-called meta-characters, such as * and $.

Many text editors and utilities such as vi, sed, awk, find and grep work extensively with regular expressions. Some of the popular computer languages that use regular expressions include Perl, Python and Ruby. It can get rather complicated and there are whole books written about regular expressions; thus, we will do no more than skim the surface here.

- Regular expressions are similar, but not the same, as shell filename generation. You can supply a list of characters to match within by using square brackets (`[]`); you can also use a caret (`^`) at the start of the list to invert the meaning of the list, which will refer to everything except those characters listed. In othe words, if the first character of the list is caret (^), then the list is complemented, for example, matching only those lines which do not match the list. If the caret is at the start of the expression, then the match begins at the start of the line.

- The period (.) indicates any single character. A period followed by an asterisk (`.*`) indicates zero or more of any character.

- Any character or RE may precede the asterisk (`*`), resulting in zero or more of that RE.

- Dollar sign ($) can be used as the last character of the RE to match at the end of the line.

- The special meaning of a period (.), asterisk (`*`) and square bracket (`[`) can be escaped by preceding with a backslash (`\`) character.

| Search Patterns | Usage                                |
|-----------------|--------------------------------------|
| .(dot)          | Match any single character           |
| a\|z            | Match a or z                         |
| $               | Match end of string                  |
| ^               | Match beginning of string            |
| *               | Match preceding item 0 or more times |


For example, consider the following sentence: the quick brown fox jumped over the lazy dog.

Some of the patterns that can be applied to this sentence are as follows:


| Command | Usage                      |
|---------|----------------------------|
| a..     | matches azy                |
| b.\|j.  | matches both br and ju     |
| ..$     | matches og                 |
| l.*     | matches lazy dog           |
| l.*y    | matches lazy               |
| the.*   | matches the whole sentence |


example:
```
$ grep '^a' fruit
apple
$ grep 'a$' fruit
banana
```

### Misc Text Utilities: `tr`

$ tr [options] set1 [set2]

The items in the square brackets are optional. tr requires at least one argument and accepts a maximum of two. The first, designated set1 in the example, lists the characters in the text to be replaced or removed. The second, set2, lists the characters that are to be substituted for the characters listed in the first argument. Sometimes these sets need to be surrounded by apostrophes (or single-quotes (')) in order to have the shell ignore that they mean something special to the shell. It is usually safe (and may be required) to use the single-quotes around each of the sets as you will see in the examples below.

For example, suppose you have a file named city containing several lines of text in mixed case. To translate all lower case characters to upper case, at the command prompt type cat city | tr a-z A-Z and press the Enter key.

| Command                                                  | Usage                                           |
|----------------------------------------------------------|-------------------------------------------------|
| tr abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ | Convert lower case to upper case                |
| tr '{}' '()' < inputfile > outputfile                    | Translate braces into parenthesis               |
| echo "This is for testing" \| tr [:space:] '\t'          | Translate white-space to tabs                   |
| echo "This   is   for    testing" \| tr -s [:space:]     | Squeeze repetition of characters using -s       |
| echo "the geek stuff" \| tr -d 't'                       | Delete specified characters using -d option     |
| echo "my username is 432234" \| tr -cd [:digit:]         | Complement the sets using -c option             |
| tr -cd [:print:] < file.txt                              | Remove all non-printable character from a file  |
| tr -s '\n' ' ' < file.txt                                | Join all the lines in a file into a single line |


***

### More about `top`


 - The first line displays a quick summary of what is happening in the system, including: How long the system has been up, how many users are logged on, what is the load average.
 - The second line of the top output displays the total number of processes, the number of running, sleeping, stopped, and zombie processes. Comparing the number of running processes with the load average helps determine if the system has reached its capacity.
 - The third line of the top output indicates how the CPU time is being divided between the users (us) and the kernel (sy) by displaying the percentage of CPU time used for each. The percentage of user jobs running at a lower priority (niceness - ni) is then listed. Idle mode (id) should be low if the load average is high, and vice versa. The percentage of jobs waiting (wa) for I/O is listed. Interrupts include the percentage of hardware (hi) vs. software interrupts (si). Steal time (st) is generally used with virtual machines, which has some of its idle CPU time taken for other uses.

- The fourth and fifth lines of the top output indicate memory usage, which is divided in two categories: Physical memory (RAM) – displayed on line 4; Swap space – displayed on line 5.

Both categories display total memory, used memory, and free space.

You need to monitor memory usage very carefully to ensure good system performance. Once the physical memory is exhausted, the system starts using swap space (temporary storage space on the hard drive) as an extended memory pool, and since accessing disk is much slower than accessing memory, this will negatively affect system performance.


- Process Identification Number (PID)
- Process owner (USER)
- Priority (PR) and nice values (NI)
- Virtual (VIRT), physical (RES), and shared memory (SHR)
- Status (S)
- Percentage of CPU (%CPU) and memory (%MEM) used
- Execution time (TIME+)
- Command (COMMAND)

Besides reporting information, top can be utilized interactively for monitoring and controlling processes. While top is running in a terminal window, you can enter single-letter commands to change its behavior. For example, you can view the top-ranked processes based on CPU or memory usage. If needed, you can alter the priorities of running processes or you can stop/kill a process.

  The table lists what happens when pressing various keys when running top:

  | Command | Output                                                    |
  |---------|-----------------------------------------------------------|
  | t       | Display or hide summary information (rows 2 and 3)        |
  | m       | Display or hide memory information (rows 4 and 5)         |
  | A       | Sort the process list by top resource consumers           |
  | r       | Renice (change the priority of) a specific processes      |
  | k       | Kill a specific process                                   |
  | f       | Enter the top configuration screen                        |
  | o       | Interactively select a new sort order in the process list |

  ***

`at` execute any non-interactive command at a specified time
 - e.g.,
 ```bash
$ at now + 2 days
at> cat file1.txt
at> <EOT>
```
press **CTL-D** to finish

***

### More about `cron`
cron is driven by a configuration file called` /etc/crontab` (cron table), which contains the various shell commands that need to be run at the properly scheduled times. There are both system-wide crontab files and individual user-based ones. Each line of a crontab file represents a job, and is composed of a so-called CRON expression, followed by a shell command to execute.

`crontab -e ` open the crontab editor to edit existing jobs or to create new jobs. Each line of the crontab file will contain 6 fields:

| Field | Description  | Values                     |
|-------|--------------|----------------------------|
| MIN   | Minutes      | 0 to 59                    |
| HOUR  | Hour field   | 0 to 23                    |
| DOM   | Day of Month | 1-31                       |
| MON   | Month field  | 1-12                       |
| DOW   | Day Of Week  | 0-6 (0 = Sunday)           |
| CMD   | Command      | Any command to be executed |


e.g.,
- `/usr/local/bin/execute/this/script.sh` will schedule a job to execute `script.sh` every minute of every hour of every day of the month, and every month and every day in the week.
- The entry `30 08 10 06 * /home/sysadmin/full-backup` will schedule a full-backup at 8.30 a.m., 10-June, irrespective of the day of the week.

***

### More about `systemctl`
[source](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)

- `systemctl status <application>` check the status of a service on your system, will provide you with the service state, the cgroup hierarchy, and the first few log lines.

- `sudo systemctl start <application>` start a systemd service, executing instructions in the service’s unit file. Although you can use this format for general administration, for clarity, we will use the `.service `suffix for the remainder of the commands to be explicit about the target we are operating on.

- `sudo systemctl stop <application.service>` stop a currently running service

- `sudo systemctl restart <application.service>` restart a running service

- `sudo systemctl reload <application.service>` reload configuration files (without restarting)

- `sudo systemctl reload-or-restart <application.service>` reload the configuration in-place if available; otherwise, restart the service so the new configuration is picked up.

- `sudo systemctl enable <application.service>` start a service at boot. (The above commands are useful for starting or stopping commands during the current session. To tell systemd to start services automatically at boot, you must enable them.)

- `systemctl is-failed <application.service>` will return active if it is running properly or failed if an error occurred. If the unit was intentionally stopped, it may return unknown or inactive. An exit status of “0” indicates that a failure occurred and an exit status of “1” indicates any other status.

- `systemctl list-units` see a list of all of the active units that systemd knows about.

### More about networking tools

| Networking Tools | Description                                                     |
|------------------|-----------------------------------------------------------------|
| ethtool          | Queries network interfaces and can also set various parameters such as the speed                          |
| netstat          | Displays all active connections and routing tables. Useful for monitoring performance and troubleshooting |
| nmap             | Scans open ports on a network. Important for security analysis       |
| tcpdump          | Dumps network traffic for analysis                        |
| iptraf           | Monitors network traffic in text mode                |
| mtr              | Combines functionality of `ping` and `traceroute` and gives a continuously updated display         |
| dig              | Tests DNS workings. A good replacement for `host` and `nslookup`                                              |


| Non-Graphical Browsers | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| Lynx                   | Configurable text-based web browser; the earliest such browser and still in use |
| ELinks                 | Based on Lynx. It can display tables and frames                                 |
| w3m                    | Another text-based web browser with many features.                              |

wget is a command line utility that can capably handle the following types of downloads:
- Large file downloads
- Recursive downloads, where a web page refers to other web pages and all are downloaded at once
- Password-required downloads
- Multiple file downloads.

To download a web page, you can simply type wget <url>, and then you can read the downloaded page as a local file using a graphical or non-graphical browser.



### More about vim
`vimtutor` opens vim tutorial

### Working with Files in vi
| Command      | Usage                                                      |
|--------------|------------------------------------------------------------|
| vi myfile    | Start the editor and edit myfile                           |
| vi -r myfile | Start and edit myfile in recovery mode from a system crash |
| vi +36 myfile| Start and edit myfile with cursor on line 36               |
| :r file2     | Read in file2 and insert at current position               |
| :w           | Write to the file                                          |
| :w myfile    | Write out to myfile                                        |
| :w! file2    | Overwrite file2                                            |
| :x or :wq    | Exit and write out modified file                           |
| :q           | Quit                                                       |
| :q!          | Quit even though modifications have not been saved         |

### Changing Cursor Positions in vi

| Key                 | Usage                             |
|---------------------|-----------------------------------|
| arrow keys          | To move up, down, left and right  |
| j or <ret>          | To move one line down             |
| k                   | To move one line up               |
| h or Backspace      | To move one character left        |
| l or Space          | To move one character right       |
| 0                   | To move to beginning of line      |
| $                   | To move to end of line            |
| w                   | To move to beginning of next word |
| :0 or 1G            | To move to beginning of file      |
| :n or nG            | To move to line n                 |
|`:$ or G`            | To move to last line in file      |
| CTRL-F or Page Down | To move forward one page          |
| CTRL-B or Page Up   | To move backward one page         |
| ^l                  | To refresh and center screen      |

### Commands and keys used when searching for text in vi

| Command  | Usage                       |
|----------|-----------------------------|
| /pattern | Search forward for pattern  |
| ?pattern | Search backward for pattern |

| Key | Usage                                         |
|-----|-----------------------------------------------|
| n   | Move to next occurrence of search pattern     |
| N   | Move to previous occurrence of search pattern |


### Important keystrokes used when changing, adding, and deleting text in vi
| Key        | Usage                                                                        |
|------------|------------------------------------------------------------------------------|
| a          | Append text after cursor; stop upon Escape key                               |
| A          | Append text at end of current line; stop upon Escape key                     |
| i          | Insert text before cursor; stop upon Escape key                              |
| I          | Insert text at beginning of current line; stop upon Escape key               |
| o          | Start a new line below current line, insert text there; stop upon Escape key |
| O          | Start a new line above current line, insert text there; stop upon Escape key |
| r          | Replace character at current position                                        |
| R          | Replace text starting with current position; stop upon Escape key            |
| x          | Delete character at current position                                         |
| Nx         | Delete N characters, starting at current position                            |
| dw         | Delete the word at the current position                                      |
| D          | Delete the rest of the current line                                          |
| dd         | Delete the current line                                                      |
| Ndd or dNd | Delete N lines                                                               |
| u          | Undo the previous operation                                                  |
| yy         | Yank (copy) the current line and put it in buffer                            |
| Nyy or yNy | Yank (copy) N lines and put it in buffer                                     |
| p          | Paste at the current position the yanked line or lines from the buffer.      |


### Using External Commands in vi

Typing sh command opens an external command shell. When you exit the shell, you will resume your editing session.

Typing ! executes a command from within vi. The command follows the exclamation point. This technique is best suited for non-interactive commands, such as : ! wc %. Typing this will run the wc (word count) command on the file; the character % represents the file currently being edited.

***

## Other CLIs

### Git
`git add`  
`git commit -m '<commit message>'`  
`git push`  
`git pull`  
 - `-v`  verify. prompt for username/password  

`git reset <file>` undo git add  before commit   
`git branch`   
`git fetch upstream`   
`git checkout master`   
`git merge upstream/master`   

#### How to override local files with git pull
`git branch new-branch`  
`git add . && commit` save current commits  
`git fetch --all`  
`git reset --hard origin/master`

##### Create a new repo
`git init`  
`touch .gitignore`  
- Go to github.  
- Log in to your account.  
- Click the new repository button in the top-right. You’ll have an option there to initialize the repository with a README file, but don’t.  
- Click the “Create repository” button.  

`git remote add origin https://github.com/username/new_repo`  


`git branch -d branch_name`  delete local branch
`git push <remote_name> --delete <branch_name>` delete remote branch  

#### Force overwrite of master branch with dev branch (careful with this)
`git branch -f master dev_branch` rewrite local master branch.
`git push remote +dev_branch:master` rewrite remote branch. `remote` here means your remote. Most likely it's called `origin`.

`git config --global credential.helper osxkeychain` reset git auth key (mac osx)


### Docker CLI
`docker pull my_image:1.0` pull an image from a registry    
`docker tag myimage:1.0 myrepo/myimage:2.0` Retag a local image with a new image name and tag  
`docker push myrepo/myimage:2.0` push an image to a registry
`docker run <image> -p <external_port>:<internal_port> --name <name>`  
`docker ps -a` list containers on your system   
`docker stop <container>` Stop one or more running containers using `SIGTERM`
  - `-f` force  

`docker kill <container>` stop a running container using `<SIGKILL>`
`docker rm` Remove one or more containers   
`docker images -a` list images  
`docker rmi <IMAGE ID> <IMAGE ID>`Remove one or more images  

`docker build -t <image>`  
`docker image ls` list all images that are locally stored withinn the docker engine  
`docker tag` retag a local image with anew image name and tag.  
`docker push` push an image to a registry  
`docker system prune` delete any resources — images, containers, volumes, and networks — that are dangling (not associated with a container)  
   - `-a` additionally remove any stopped containers and all unused images (not just dangling images)  


`docker cp foo.txt 72ca2488b353:/foo.txt`s

### Openshift CLI
`oc adm` oc is the OpenShift Container Platform command line interface (CLI) adm provides tools for managing a cluster  
`oc login` authenticate an openshift cluster    
`oc logout` end current session  
`oc whoami` get username (show current user context)  
`oc whoami -t` get current user's access token  

##### Project management
`oc project` show the current project context  
`oc get projects` show all project current login has access to  
`oc status` show overview of current project resources  
`oc new-project` create a new project in Openshift and change to that context

##### Resource Management
`oc new-app` create a new application from from source code, container image, or OpenShift template
`oc create` create a new resource from filename or stdin

##### Cluster Management
`oc adm policy`  
`oc get pods -o wide`  
`oc create` create a new resource from filename or stdin

`oc describe pod <pod name>` find what node a pod is on
`oc describe node <node name>` check if node is healthy

`oc delete job,deploy,rs,pod,statefulset,configmap,secret,ingress,service,serviceaccount,role,rolebinding,pvc,poddisruptionbudget --selector=release=disco --namespace=zen` - nuke it from orbit

##### Build/Deploy
`oc rollout latest <deployment_name>` trigger a build  
`oc rollout history <deployment_name>`  see history of builds  
`oc rollout describe <deployment_name>` see detailed info about a rollout  
`oc rollout undo <deployment_name>` rollback a deployment.  

#### Drain/evacuate a node for maintenance
1. Disable scheduling on node
`oc adm manage-node <node-name> --schedulable=false`
or
`oc adm cordon <node>`  


2. stop all running docker containers
`docker stop $(docker ps -aq)`  

3. Delete all docker images/resources
`docker system prune -a`

4. Drain or evacuate pods from nodes
`oc adm drain <node>`
   - Most of the time it will not work as there will be pods with local data or some pods with daemons running. So we need to add additional options such as `–ignore-daemonsets`, `–delete-local-data`.  
`oc adm drain <node> --delete-local-data --ignore-daemonsets --force`

5. Verify that no pods are running on the node.
6. Set pods to schedulable again
`oc adm manage-node <node-name> --schedulable=true`
or
`oc adm uncordon <node>`


##### Other Useful OC Commands
`watch "oc get pods —all-namespaces -o wide | grep -Ev ‘1/1|2/2|3/3|4/4|Completed"` watch those pods that aren't in a healthy state

`oc get pods | grep CrashLoopBackOff | cut -d' ' -f 1 | xargs -I {} oc delete pod {}` Delete all pods in CrashLoopBackOff

`oc get pods —all-namespaces -o wide | grep -Ev ‘1/1|2/2|3/3|4/4|Completed`
`./sshexec allnodes "docker images -a | grep ago | tr -s ' ' | cut -d' ' -f3 |  xargs -I {} docker rmi {}`
`get pods --all-namespaces -o wide --field-selector spec.nodeName=<node_name>`

## Misc

`ansible-playbook` run Ansible playbooks, which are a configuration and multinode deployment system.  
- `-i` specify inventory host path or comma separated host list   

### Changing a machine's names (OSX)
`scutil` manage system configuration parameters for macOS  
`sudo scutil --set HostName <new host name>`  change hostname  
`sudo scutil --set LocalHostName <new host name> ` change the name usable on the local network, for example myMac.local  
`sudo scutil --set ComputerName <new name>` user-friendly computer name you see in Finder  
`dscacheutil -flushcache` Flush the DNS cache   

### CSV hacks
`wc -l myfile.csv` return number of lines in CSV  
`grep -c 'some_value' myfile.csv` Count total number of lines containing word/pattern.  
`cat  myfile.csv | column -t -s, | less -S` Pretty print csv

### One-liners
`ls -lt | head` list most recently added file in the directory  

`cat nlu.json | jq '.apikey' -r` use jq to access value for key 'apikey', return raw results (no quotation marks)
