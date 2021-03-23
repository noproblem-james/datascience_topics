# Linux Concpets

## Key Linux concepts:
- The Linux kernel was developed by Linus Torvalds at the University of Helsinki, Finland, in 1991.
- The KDE (K Desktop Environment) and GNOME are the two most widely used Linux desktop managers.
- Linux passwords must not be all letters or all numbers, and cannot be less than eight characters long. They should have at least two letters, and at least one non-letter.
- Virtual terminals (VT) in Linux are consoles, or command line terminals that use the connected monitor and keyboard.
- Different Linux distributions start and stop the graphical desktop in different ways.
- A terminal emulator program on the graphical desktop works by emulating a terminal within a window on the desktop.
- The Linux system allows you to either log in via text terminal or remotely via the console.
- When typing your password, nothing is printed to the terminal, not even a generic symbol to indicate that you typed.
- The preferred method to shut down or reboot the system is to use the `shutdown` command.
- There are two types of pathnames: absolute and relative.
  - An absolute pathname begins with the root directory and follows the tree, branch by branch, until it reaches the desired directory or file.
  - A relative pathname starts from the present working directory.
- Using hard and soft (symbolic) links is extremely useful in Linux.
- cd remembers where you were last, and lets you get back there with cd -.
- locate performs a database search to find all file names that match a given pattern.
- find locates files recursively from a given directory or set of directories.
- find is able to run commands on the files that it lists, when used with the -exec option.
- touch is used to set the access, change, and edit times of files, as well as to create empty files.
- The Advanced Packaging Tool (apt) package management system is used to manage installed software on Debian-based systems.
- You can use the Yellowdog Updater Modified (yum) open source command-line package management utility for RPM-compatible Linux operating systems.
- The zypper package management system is based on RPM and used for openSUSE.
- -Package Documentation can be accessed through /usr/share/doc?

- sed: Either / or : can be used as a delimiter between fields in the command.

- The command interpreter on a Linux system is referred to as the **shell**.
  - Unlike other operating systems, where the command line interpreter is very closely coupled to the underlying operating system, on Linux, you have a choice of shells--in fact, almost any program can be your shell. Shells that are usually found on a Linux system include: Bash, ZSH, and TCSH. The most common shell is Bash.
  - the system automatically looks for a file of shell commands called `/etc/profile` and another called `/etc/bashrc`, which are executed before accepting input from the user. These files set up your operating environment with options, such as your initial prompt, the search path for commands, and variables to allow you to find your email and initial command shortcuts.
  These startup files will be set up by your system administrator, and cannot be edited by a user.

  - The **shell prompt** can be as simple as a dollar sign (`$`) or as complex as you like. The default for Bash is made up of your login ID, the name of the computer that you are using, and the terminal part of the working directory path. Customize the prompt by assigning a string to the shell variable `PS1`. If it contains spaces, you need to enclose the value in single or double quotes.

## Shell commands
**Shell commands** are words that represent the name of an executable file, an alias, a function, or a shell built-in. Commands may have options and arguments. Spaces or Tab characters are known collectively as whitespace. Separate commands have their own options and arguments.

Options are preceded by a single dash if they are single-letter options, or by a double dash if they are complex or long option names. Options may have associated arguments and the command as a whole may have arguments; these are usually the names of files that the command will operate on.

simple path is just the name of a command, and it requires the shell to search its PATH to find the file.

An absolute path starts with a forward slash, and each directory component is also separated by a slash. A relative path starts with either a period (.) or a double period (..) and indicates a file relative to the current (.) or parent (..) directory.

If a command requires a literal semicolon, then you can remove its special meaning by using the back slash (\) symbol. This is also true for most shell special symbols or metacharacters like quote marks ("), brackets (( )), hash (#), exclamation mark (!), and the dollar sign ($). Removing the special meaning is termed escaping, and the back slash (\) symbol is the shell escape. Alternatively, you can use single quotes (') to make sure the shell ignores any metacharacters.



## Linux Documentation

- The main sources of Linux documentation are the man pages, GNU info, the help options and command, and a rich variety of online documentation sources.
- The man utility searches, formats, and displays man pages.
- The man pages provide in-depth documentation about programs and other topics about the system, including configuration files, system calls, library routines, and the kernel.
- The GNU info System was created by the GNU project as its standard documentation. It is robust and is accessible via command line, web, and graphical tools using info.
- Short descriptions for commands are usually displayed with the -h or --help argument.
- You can type help at the command line to display a synopsis of built-in commands.

## User environment


In Linux, the command shell program (generally bash) uses one or more startup files to configure the user environment. Files in the /etc directory define global settings for all users, while initialization files in the user's home directory can include and/or override the global settings.

The startup files can do anything the user would like to do in every command shell, such as:

- Customizing the prompt
- Defining command line shortcuts and aliases
- Setting the default text editor
- Setting the path for where to find executable programs  



The standard prescription is that when you first login to Linux, /etc/profile is read and evaluated, after which the following files are searched (if they exist) in the listed order:

              ~/.bash_profile
              ~/.bash_login
              ~/.profile

  where  ~/. denotes the user's home directory. The Linux login shell evaluates whatever startup file that it comes across first and ignores the rest. This means that if it finds ~/.bash_profile, it ignores ~/.bash_login and ~/.profile. Different distributions may use different startup files.

  However, every time you create a new shell, or terminal window, etc., you do not perform a full system login; only a file named ~/.bashrc file is read and evaluated. Although this file is not read and evaluated along with the login shell, most distributions and/or users include the ~/.bashrc file from within one of the three user-owned startup files.

  Most commonly, users only fiddle with ~/.bashrc, as it is invoked every time a new command line shell initiates, or another program is launched from a terminal window, while the other files are read and executed only when the user first logs onto the system.

  Recent distributions sometimes do not even have .bash_profile  and/or .bash_login , and some just do little more than include .bashrc.

             <bashinit.png>


 You can create customized commands or modify the behavior of already existing ones by creating aliases. Most often, these aliases are placed in your ~/.bashrc file so they are available to any command shells you create. unalias removes an alias.

 Typing alias with no arguments will list currently defined aliases.

 Please note there should not be any spaces on either side of the equal sign and the alias definition needs to be placed within either single or double quotes if it contains any spaces.

 |               Task                  |    Command                |
|---------------------------------------|--------------------|
| Show the value of a specific variable | echo $SHELL           |
| Export a new variable value           | export VARIABLE=value (or VARIABLE=value; export VARIABLE)        |
| Add a variable permanently            |  1.  Edit ~/.bashrc and add the line export VARIABLE=value  2.  Type source ~/.bashrc or just . ~/.bashrc (dot ~/.bashrc); or just start a new shell by typing  bash  |

### Environment Variables

Environment variables are quantities that have specific values which may be utilized by the command shell, such as bash, or other utilities and applications. Some environment variables are given preset values by the system (which can usually be overridden), while others are set directly by the user, either at the command line or within startup and other scripts.

An environment variable is actually just a character string that contains information used by one or more applications. There are a number of ways to view the values of currently set environment variables; one can type set, env, or export. Depending on the state of your system, set may print out many more lines than the other two methods.

#### Some common environment variables
`$SHELL` points to the user's default command shell (the program that is handling whatever you type in a command window, usually bash) and contains the full pathname to the shell
`$HOME` represents the home (or login) directory of the user. cd without arguments will change the current working directory to the value of HOME. Note the tilde character (~) is often used as an abbreviation for `$HOME`. Thus, `cd $HOME` and `cd ~` are completely equivalent statements.
`PATH` is an ordered list of directories (the path) which is scanned when a command is given to find the appropriate program or script to run. Each directory in the path is separated by colons (:). A null (empty) directory name (or ./) indicates the current directory at any given time.

            :path1:path2
            path1::path2

In the example :path1:path2, there is a null directory before the first colon (:). Similarly, for path1::path2 there is a null directory between path1 and path2.

To prefix a private bin directory to your path:

$ export PATH=$HOME/bin:$PATH
$ echo $PATH

`PS`

Prompt Statement (PS) is used to customize your prompt string in your terminal windows to display the information you want.

PS1 is the primary prompt variable which controls what your command line prompt looks like. The following special characters can be included in PS1:

\u - User name
\h - Host name
\w - Current working directory
\! - History number of this command
\d - Date

They must be surrounded in single quotes when they are used

```echo $PS1
$
$ export PS1='\u@\h:\w$ '
student@example.com:~$ # new prompt
```


about the history file.

            HISTFILE
            The location of the history file.
            HISTFILESIZE
            The maximum number of lines in the history file (default 500).
            HISTSIZE
            The maximum number of commands in the history file.
            HISTCONTROL
            How commands are stored.
            HISTIGNORE
            Which command lines can be unsaved.

For a complete description of the use of these environment variables, see man bash.

## Package Management Systems on Linux

The core parts of a Linux distribution and most of its add-on software are installed via the Package Management System. Each package contains the files and other instructions needed to make one software component work well and cooperate with the other components that comprise the entire system. Packages can depend on each other. For example, a package for a web-based application written in PHP can depend on the PHP package.

There are two broad families of package managers: those based on Debian and those which use RPM as their low-level package manager. The two systems are incompatible, but broadly speaking, provide the same features and satisfy the same needs. There are some other systems used by more specialized Linux distributions.

In this section, you will learn how to install, remove, or search for packages from the command line using these two package management systems.

Both package management systems operate on two distinct levels: a low-level tool (such as dpkg or rpm) takes care of the details of unpacking individual packages, running scripts, getting the software installed correctly, while a high-level tool (such as apt, yum, dnf or zypper) works with groups of packages, downloads packages from the vendor, and figures out dependencies.

Most of the time users need to work only with the high-level tool, which will take care of calling the low-level tool as needed. Dependency resolution is a particularly important feature of the high-level tool, as it handles the details of finding and installing each dependency for you. Be careful, however, as installing a single package could result in many dozens or even hundreds of dependent packages being installed.

Working With Different Package Management Systems

The Advanced Packaging Tool (apt) is the underlying package management system that manages software on Debian-based systems. While it forms the backend for graphical package managers, such as the Ubuntu Software Center and synaptic, its native user interface is at the command line, with programs that include apt (or apt-get) and apt-cache.

yum is an open source command-line package-management utility for the RPM-compatible Linux systems that belongs to the Red Hat family. yum has both command line and graphical user interfaces. Fedora and RHEL 8 have replaced yum with dnf, which has less historical baggage, has nice new capabilities and is mostly backwards-compatible with yum for day-to-day commands.

zypper is the package management system for the SUSE/openSUSE family and is also based on RPM. zypper also allows you to manage repositories from the command line. zypper is fairly straightforward to use and resembles yum quite closely.

To learn the basic packaging commands, take a look at these basic packaging commands.

## The Linux Filesystem

- The filesystem tree starts at what is often called the root directory (or trunk, or /).
- The **Filesystem Hierarchy Standard (FHS)** provides Linux developers and system administrators a standard directory structure for the filesystem.
- Partitions help to segregate files according to usage, ownership, and type.
- Filesystems can be mounted anywhere on the main filesystem tree at a mount point. Automatic filesystem mounting can be set up by editing `/etc/fstab`.
NFS (Network File System) is a useful method for sharing files and data through the network systems.
Filesystems like /proc are called pseudo filesystems because they exist only in memory.
/root (slash-root) is the home directory for the root user.

| Directory Name |  Usage |
|----------------|--------|
| `/etc `| system configuration files. Applies system-wide; thus only superuser can modify files here.|
| `/bin` | binaries, executable files for essential commands used to boot the system or in single-user mode, and those required by all system users, such as `cat`, `cp`, `ls`, `mv`, `ps`, and `rm`.  |
| `/sbin` |  binaries related to system administration, such as `fsck` and `ip` |
| `/lib` | libraries common code shared by applications and needed for them to run) for the essential programs in /bin and /sbin |
| `dev` | device nodes, a type of pseudo-file used by most hardware and software devices, except for network devices |
| `/tmp`           | Temporary files; on some distributions erased across a reboot and/or may actually be a ramdisk in memory    |
| `/usr `          | Multi-user applications, utilities and data. The directory tree under `usr` contains theoretically non-essential programs and scripts (in the sense that they should not be needed to initially boot the system)   |
| `/var` | Variable. Files that are expected to change in size and content as the system is running (var stands for variable) may be put in its own filesystem so that growth can be contained and not fatally affect the system. |
| `/proc` | pseudofilesystem for viewing kernel data |
| `/opt` | Optional application software packages |
| `/boot` | basic files needed to boot the system |
| `/sys`   | Virtual pseudo-filesystem giving information about the system and the hardware Can be used to alter system parameters and for debugging purposes |
| `/run` | any removable media are automatically mounted here |
| `/srv`   | Site-specific data served up by the system  Seldom used    |



#### /etc
The /etc directory is the home for system configuration files. It contains no binary programs, although there are some executable scripts. For example, /etc/resolv.conf tells the system where to go on the network to obtain host name to IP address mappings (DNS). Files like passwd, shadow and group for managing user accounts are found in the /etc directory. While some distributions have historically had their own extensive infrastructure under /etc (for example, Red Hat and SUSE have used /etc/sysconfig), with the advent of systemd there is much more uniformity among distributions today.

Note that /etc is for system-wide configuration files and only the superuser can modify files there. User-specific configuration files are always found under their home directory.

The /boot directory contains the few essential files needed to boot the system. For every alternative kernel installed on the system there are four files:

            vmlinuz
            The compressed Linux kernel, required for booting.
            initramfs
            The initial ram filesystem, required for booting, sometimes called initrd, not initramfs.
            config
            The kernel configuration file, only used for debugging and bookkeeping.
            System.map
            Kernel symbol table, only used for debugging.

Each of these files has a kernel version appended to its name.

The Grand Unified Bootloader (GRUB) files such as /boot/grub/grub.conf or /boot/grub2/grub2.cfg are also found under the /boot directory

#### /lib
/lib contains libraries (common code shared by applications and needed for them to run) for the essential programs in /bin and /sbin. These library filenames either start with ld or lib. For example, /lib/libncurses.so.5.9.

Most of these are what is known as dynamically loaded libraries (also known as shared libraries or Shared Objects (SO)). On some Linux distributions there exists a /lib64 directory containing 64-bit libraries, while /lib contains 32-bit versions.

#### /proc
Certain filesystems, like the one mounted at /proc, are called pseudo-filesystems because they have no permanent presence anywhere on the disk.

The /proc filesystem contains virtual files (files that exist only in memory) that permit viewing constantly changing kernel data. /proc contains files and directories that mimic kernel structures and configuration information. It does not contain real files, but runtime system information, e.g. system memory, devices mounted, hardware configuration, etc. Some important entries in /proc are:

/proc/cpuinfo
/proc/interrupts
/proc/meminfo
/proc/mounts
/proc/partitions
/proc/version

patch is a very useful tool in Linux. Many modifications to source code and configuration files are distributed with patch files, as they contain the deltas or changes to go from an old version of a file to the new version of a file.
File extensions in Linux do not necessarily mean that a file is of a certain type.
cp is used to copy files on the local machine, while rsync can also be used to copy files from one machine to another, as well as synchronize contents.
gzip, bzip2, xz and zip are used to compress files.
tar allows you to create or extract files from an archive file, often called a tarball. You can optionally compress while creating the archive, and decompress while extracting its contents.
dd can be used to make large exact copies, even of entire disk partitions, efficiently.


 #### /usr

 /usr directory tree contains theoretically non-essential programs and scripts (in the sense that they should not be needed to initially boot the system) and has at least the following sub-directories:
/usr subdirectories

| Directory Name | Usage                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------------|
| /usr/include   | Header files used to compile applications                                                                    |
| /usr/lib       | Libraries for programs in /usr/bin and /usr/sbin                                                             |
| /usr/lib64     | 64-bit libraries for 64-bit programs in /usr/bin and /usr/sbin                                               |
| /usr/sbin      | Non-essential system binaries, such as system daemons                                                        |
| /usr/share     | Shared data used by applications, generally architecture-independent                                         |
| /usr/src       | Source code, usually for the Linux kernel                                                                    |
| /usr/local     | Data and programs specific to the local machine. Subdirectories include bin, sbin, lib, share, include, etc. |
| /usr/bin       | This is the primary directory of executable commands on the system                                           |




### Partitions

Each filesystem on a Linux system occupies a disk partition. Partitions help to organize the contents of disks according to the kind and use of the data contained. For example, important programs required to run the system are often kept on a separate partition (known as root or /) than the one that contains files owned by regular users of that system (/home). In addition, temporary files created and destroyed during the normal operation of Linux may be located on dedicated partitions. One advantage of this kind of isolation by type and variability is that when all available space on a particular partition is exhausted, the system may still operate normally.

Before you can start using a filesystem, you need to mount it on the filesystem tree at a mount point. This is simply a directory (which may or may not be empty) where the filesystem is to be grafted on. Sometimes, you may need to create the directory if it does not already exist.

Warning: If you mount a filesystem on a non-empty directory, the former contents of that directory are covered-up and not accessible until the filesystem is unmounted. Thus, mount points are usually empty directories.


## File compression
As compression factors go up, CPU time does as well (i.e. producing smaller archives takes longer).

| Command | Usage                                                                             |
|---------|-----------------------------------------------------------------------------------|
| gzip    | The most frequently used Linux compression utility                                |
| bzip2   | Produces files significantly smaller than those produced by gzip                  |
| xz      | The most space-efficient compression utility used in Linux                        |
| zip     | Is often required to examine and decompress archives from other operating systems |


In addition, the tar utility is often used to group files in an archive and then compress the whole archive at once.
gzip is the most often used Linux compression utility. It compresses very well and is very fast. The following table provides some usage examples:

| Command          | Usage                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------|
| gzip *           | Compresses all files in the current directory; each file is compressed and renamed with a .gz extension        |
| zgip -r projectX | Compresses all files in the projectX directory, along with all files in all of the directories under projectX  |
| gunzip foo       | De-compresses foo found in the file foo.gz. Under the hood, the gunzip command is actually the same as `gzip –d` |

| Command                      | Usage                                                                                                                  |
|------------------------------|------------------------------------------------------------------------------------------------------------------------|
| tar xvf mydir.tar            | Extract all the files in mydir.tar into the mydir directory                                                            |
| tar zcvf mydir.tar.gz mydir  | Create the archive and compress with gzip                                                                              |
| tar jcvf mydir.tar.bz2 mydir | Create the archive and compress with bz2                                                                               |
| tar Jcvf mydir.tar.xz mydir  | Create the archive and compress with xz                                                                                |
| tar xvf mydir.tar.gz         | Extract all the files in mydir.tar.gz into the mydir directory  Note: You do not have to tell tar it is in gzip format |



## Processes
A process is simply an instance of one or more related tasks (threads) executing on your computer. It is not the same as a program or a command. A single command may actually start several processes simultaneously. Some processes are independent of each other and others are related. A failure of one process may or may not affect the others running on the system.

Processes use many system resources, such as memory, CPU (central processing unit) cycles, and peripheral devices, such as network cards, hard drives, printers and displays. The operating system (especially the kernel) is responsible for allocating a proper share of these resources to each process and ensuring overall optimized system utilization.

| Process Type          | Description                                                                                                                                                                                                                                                                                                                                                  | Example                        |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Interactive Processes | Need to be started by a user, either at a command line or through a graphical interface such as an icon or a menu selection.                                                                                                                                                                                                                                 | bash, firefox, top             |
| Batch Processes       | Automatic processes which are scheduled from and then disconnected from the terminal. These tasks are queued and work on a FIFO (First-In, First-Out) basis.                                                                                                                                                                                                 | updatedb, ldconfig             |
| Daemons               | Server processes that run continuously. Many are launched during system startup and then wait for a user or system request indicating that their service is required.                                                                                                                                                                                        | httpd, sshd, libvirtd          |
| Threads               | Lightweight processes. These are tasks that run under the umbrella of a main process, sharing memory and other resources, but are scheduled and run by the system on an individual basis. An individual thread can end without terminating the whole process and a process can create new threads at any time. Many non-trivial programs are multi-threaded. | firefox, gnome-terminal-server |
| Kernel Threads        | Kernel tasks that users neither start nor terminate and have little control over. These may perform actions like moving a thread from one CPU to another, or making sure input/output operations to disk are completed.                                                                                                                                      | kthreadd, migration, ksoftirqd |



A critical kernel function called the scheduler constantly shifts processes on and off the CPU, sharing time according to relative priority, how much time is needed and how much has already been granted to a task.

When a process is in a so-called running state, it means it is either currently executing instructions on a CPU, or is waiting to be granted a share of time (a time slice) so it can execute. All processes in this state reside on what is called a run queue and on a computer with multiple CPUs, or cores, there is a run queue on each.

However, sometimes processes go into what is called a sleep state, generally when they are waiting for something to happen before they can resume, perhaps for the user to type something. In this condition, a process is said to be sitting on a wait queue.

There are some other less frequent process states, especially when a process is terminating. Sometimes, a child process completes, but its parent process has not asked about its state. Amusingly, such a process is said to be in a zombie state; it is not really alive, but still shows up in the system's list of processes.

At any given time, there are always multiple processes being executed. The operating system keeps track of them by assigning each a unique process ID (PID) number. The PID is used to track process state, CPU usage, memory use, precisely where resources are located in memory, and other characteristics.

New PIDs are usually assigned in ascending order as processes are born. Thus, PID 1 denotes the init process (initialization process), and succeeding processes are gradually assigned higher numbers.

The table explains the PID types and their descriptions:

| ID Type                  | Description                                                                                                                                                       |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Process ID (PID)         | Unique Process ID number                                                                                                                                          |
| Parent Process ID (PPID) | Process (Parent) that started this process. If the parent dies, the PPID will refer to an adoptive parent; on recent kernels, this is kthreadd which has PPID=2.  |
| Thread ID (TID)          | Thread ID number. This is the same as the PID for single-threaded processes. For a multi-threaded process, each thread shares the same PID, but has a unique TID. |

## Networks and Network operations
### Summary

- The IP (Internet Protocol) address is a unique logical network address that is assigned to a device on a network.
- IPv4 uses 32-bits for addresses and IPv6 uses 128-bits for addresses.
- Every IP address contains both a network and a host address field.
- - There are five classes of network addresses available: A, B, C, D & E.
- DNS (Domain Name System) is used for converting Internet domain and host names to IP addresses.
- You can use the route utility program to manage IP routing.
- You can monitor and debug network problems using networking tools.
- Firefox, Google Chrome, Chromium, and Epiphany are the main graphical browsers used in Linux.
- Non-graphical or text browsers used in Linux are Lynx, Links, and w3m.
- You can use wget to download webpages.
- You can use curl to obtain information about URLs.
- FTP (File Transfer Protocol) is used to transfer files over a network.
- ftp, sftp, ncftp, and yafc are command line FTP clients used in Linux.
- You can use ssh to run commands on remote systems.

### Introduction to Networking

A network is a group of computers and computing devices connected together through communication channels, such as cables or wireless media. The computers connected over a network may be located in the same geographical area or spread across the world.

A network is used to:

- Allow the connected devices to communicate with each other
- Enable multiple users to share devices over the network, such as printers and scanners
- Share and manage information across computers easily.

Most organizations have both an internal network and an Internet connection for users to communicate with machines and people outside the organization. The Internet is the largest network in the world and can be called "the network of networks".


### IP Addresses

Devices attached to a network must have at least one unique network address identifier known as the IP (Internet Protocol) address. The address is essential for routing packets of information through the network.

Exchanging information across the network requires using streams of small packets, each of which contains a piece of the information going from one machine to another. These packets contain data buffers, together with headers which contain information about where the packet is going to and coming from, and where it fits in the sequence of packets that constitute the stream. Networking protocols and software are rather complicated due to the diversity of machines and operating systems they must deal with, as well as the fact that even very old standards must be supported.

### IPv4 and IPv6

There are two different types of IP addresses available: IPv4 (version 4) and IPv6 (version 6). IPv4 is older and by far the more widely used, while IPv6 is newer and is designed to get past limitations inherent in the older standard and furnish many more possible addresses.

IPv4 uses 32-bits for addresses; there are only 4.3 billion unique addresses available. Furthermore, many addresses are allotted and reserved, but not actually used. IPv4 is considered inadequate for meeting future needs because the number of devices available on the global network has increased enormously in recent years.

IPv6 uses 128-bits for addresses; this allows for 3.4 X 1038 unique addresses. If you have a larger network of computers and want to add more, you may want to move to IPv6, because it provides more unique addresses. However, it can be complex to migrate to IPv6; the two protocols do not always inter-operate well. Thus, moving equipment and addresses to IPv6 requires significant effort and has not been quite as fast as was originally intended. We will discuss IPv4 more than IPv6 as you are more likely to deal with it.

One reason IPv4 has not disappeared is there are ways to effectively make many more addresses available by methods such as NAT (Network Address Translation).  NAT enables sharing one IP address among many locally connected computers, each of which has a unique address only seen on the local network. While this is used in organizational settings, it also used in simple home networks. For example, if you have a router hooked up to your Internet Provider (such as a cable system) it gives you one externally visible address, but issues each device in your home an individual local address.


A 32-bit IPv4 address is divided into four 8-bit sections called octets.

Example:
IP address →            172    .   16   .    31  .    46
Bit format →           10101100.00010000.00011111.00101110

Note: Octet is just another word for byte.

Network addresses are divided into five classes: A, B, C, D and E. Classes A, B and C are classified into two parts: Network addresses (Net ID) and Host address (Host ID). The Net ID is used to identify the network, while the Host ID is used to identify a host in the network. Class D is used for special multicast applications (information is broadcast to multiple computers simultaneously) and Class E is reserved for future use. In this section you will learn about classes A, B and C.

<pic>

Class A Network Addresses

Class A addresses use the first octet of an IP address as their Net ID and use the other three octets as the Host ID. The first bit of the first octet is always set to zero. So you can use only 7-bits for unique network numbers. As a result, there are a maximum of 126 Class A networks available (the addresses 0000000 and 1111111 are reserved). Not surprisingly, this was only feasible when there were very few unique networks with large numbers of hosts. As the use of the Internet expanded, Classes B and C were added in order to accommodate the growing demand for independent networks.

Each Class A network can have up to 16.7 million unique hosts on its network. The range of host address is from 1.0.0.0 to 127.255.255.255.

Note: The value of an octet, or 8-bits, can range from 0 to 255.

<pic: class a network addresses>

### IP Address Allocation

Typically, a range of IP addresses are requested from your Internet Service Provider (ISP) by your organization's network administrator. Often, your choice of which class of IP address you are given depends on the size of your network and expected growth needs. If NAT is in operation, such as in a home network, you only get one externally visible address!

You can assign IP addresses to computers over a network either manually or dynamically. Manual assignment adds static (never changing) addresses to the network. Dynamically assigned addresses can change every time you reboot or even more often; the Dynamic Host Configuration Protocol (DHCP) is used to assign IP addresses.

### Name Resolution

Name Resolution is used to convert numerical IP address values into a human-readable format known as the hostname. For example, 104.95.85.15 is the numerical IP address that refers to the hostname whitehouse.gov. Hostnames are much easier to remember!

Given an IP address, you can obtain its corresponding hostname. Accessing the machine over the network becomes easier when you can type the hostname instead of the IP address.

You can view your system’s hostname simply by typing hostname with no argument.

Note: If you give an argument, the system will try to change its hostname to match it, however, only root users can do that.

The special hostname localhost is associated with the IP address 127.0.0.1, and describes the machine you are currently on (which normally has additional network-related IP addresses).


#### Network Configuration Files

Network configuration files are essential to ensure that interfaces function correctly. They are located in the /etc directory tree. However, the exact files used have historically been dependent on the particular Linux distribution and version being used.

For Debian family configurations, the basic network configuration files could be found under /etc/network/, while for Fedora and SUSE family systems one needed to inspect /etc/sysconfig/network.

Modern systems emphasize the use of Network Manager, which we briefly discussed when we considered graphical system administration, rather than try to keep up with the vagaries of the files in /etc. While the graphical versions of Network Manager do look somewhat different in different distributions, the nmtui utility (shown in the screenshot) varies almost not at all, as does the even more sparse nmcli (command line interface) utility. If you are proficient in the use of the GUIs, by all means, use them. If you are working on a variety of systems, the lower level utilities may make life easier.

#### Network Interfaces

Network interfaces are a connection channel between a device and a network. Physically, network interfaces can proceed through a network interface card (NIC), or can be more abstractly implemented as software. You can have multiple network interfaces operating at once. Specific interfaces can be brought up (activated) or brought down (de-activated) at any time.

Information about a particular network interface or all network interfaces can be reported by the ip and ifconfig utilities, which you may have to run as the superuser, or at least, give the full path, i.e. /sbin/ifconfig, on some distributions. ip is newer than ifconfig and has far more capabilities, but its output is uglier to the human eye. Some new Linux distributions do not install the older net-tools package to which ifconfig belongs, and  so you would have to install it if you want to use it.

#### route

A network requires the connection of many nodes. Data moves from source to destination by passing through a series of routers and potentially across multiple networks. Servers maintain routing tables containing the addresses of each node in the network. The IP routing protocols enable routers to build up a forwarding table that correlates final destinations with the next hop addresses.



route

route



One can use the route utility or the newer ip route command to view or change the IP routing table to add, delete, or modify specific (static) routes to specific hosts or networks. The table explains some commands that can be used to manage IP routing:


#### FTP (File Transfer Protocol)

When you are connected to a network, you may need to transfer files from one machine to another. File Transfer Protocol (FTP) is a well-known and popular method for transferring files between computers using the Internet. This method is built on a client-server model. FTP can be used within a browser or with stand-alone client programs.  

FTP is one of the oldest methods of network data transfer, dating back to the early 1970s. As such, it is considered inadequate for modern needs, as well as being intrinsically insecure. However, it is still in use and when security is not a concern (such as with so-called anonymous FTP) it can make sense. However, many websites, such as kernel.org, have abandoned its use.



FTP Clients

FTP clients enable you to transfer files with remote computers using the FTP protocol. These clients can be either graphical or command line tools. Filezilla, for example, allows use of the drag-and-drop approach to transfer files between hosts. All web browsers support FTP, all you have to do is give a URL like ftp://ftp.kernel.org where the usual http:// becomes ftp://.

Some command line FTP clients are:

            ftp
            sftp
            ncftp
            yafc (Yet Another FTP Client).

FTP has fallen into disfavor on modern systems, as it is intrinsically insecure, since passwords are user credentials that can be transmitted without encryption and are thus prone to interception. Thus, it was removed in favor of using rsync and web browser https access for example. As an alternative, sftp is a very secure mode of connection, which uses the Secure Shell (ssh) protocol, which we will discuss shortly. sftp encrypts its data and thus sensitive information is transmitted more securely. However, it does not work with so-called anonymous FTP (guest user credentials).

#### SSH: Executing Commands Remotely

Secure Shell (SSH) is a cryptographic network protocol used for secure data communication. It is also used for remote services and other secure services between two devices on the network and is very useful for administering systems which are not easily available to physically work on, but to which you have remote access.

To login to a remote system using your same user name you can just type ssh some_system and press Enter. ssh then prompts you for the remote password. You can also configure ssh to securely allow your remote access without typing a password each time.

If you want to run as another user, you can do either ssh -l someone some_system or ssh someone@some_system. To run a command on a remote system via SSH, at the command prompt, you can type ssh some_system my_command.

scp

We can also move files securely using Secure Copy (scp) between two networked hosts. scp uses the SSH protocol for transferring data.

To copy a local file to a remote system, at the command prompt, type scp <localfile> <user@remotesystem>:/home/user/ and press Enter.

You will receive a prompt for the remote password. You can also configure scp so that it does not prompt for a password for each transfer.

## Security


The root account has authority over the entire system.
root privileges may be required for tasks, such as restarting services, manually installing packages and managing parts of the filesystem that are outside your home directory.
In order to perform any privileged operations such as system-wide changes, you need to use either su or sudo.
Calls to sudo trigger a lookup in the /etc/sudoers file, or in the /etc/sudoers.d directory, which first validates that the calling user is allowed to use sudo and that it is being used within permitted scope.
One of the most powerful features of sudo is its ability to log unsuccessful attempts at gaining root access. By default, sudo commands and failures are logged in /var/log/auth.log under the Debian family and /var/log/messages in other distribution families.


One process cannot access another process’ resources, even when that process is running with the same user privileges.
Using the user credentials, the system verifies the authenticity and identity.
The SHA-512 algorithm is typically used to encode passwords. They can be encrypted, but not decrypted.
Pluggable Authentication Modules (PAM) can be configured to automatically verify that passwords created or modified using the passwd utility are strong enough (what is considered strong enough can also be configured).
Your IT security policy should start with requirements on how to properly secure physical access to servers and workstations.
Keeping your systems updated is an important step in avoiding security attacks.




### User Accounts
The Linux kernel allows properly authenticated users to access files and applications. While each user is identified by a unique integer (the user id or UID), a separate database associates a username with each UID. Upon account creation, new user information is added to the user database and the user's home directory must be created and populated with some essential files. Command line programs such as useradd and userdel as well as GUI tools are used for creating and removing accounts.

Command line programs such as useradd and userdel as well as GUI tools are used for creating and removing accounts.

For each user, the following seven fields are maintained in the /etc/passwd file:

| Field Name     | Details                                                                                                  | Remarks                                                                                                                                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Username       | User login name                                                                                          | Should be between 1 and 32 characters long                                                                                                                                                                                       |
| Password       | User password (or the character x if the password is stored in the /etc/shadow file) in encrypted format | Is never shown in Linux when it is being typed; this stops prying eyes                                                                                                                                                           |
| User ID (UID)  | Every user must have a user id (UID)                                                                     |     UID 0 is reserved for root user   UID's ranging from 1-99 are reserved for other predefined accounts   UID's ranging from 100-999 are reserved for system accounts and groups   Normal users have UID's of 1000 or greater   |
| Group ID (GID) | The primary Group ID (GID); Group Identification Number stored in the /etc/group file                    | Is covered in detail in the chapter on Processes                                                                                                                                                                                 |
| User Info      | This field is optional and allows insertion of extra information about the user such as their name       | For example: Rufus T. Firefly                                                                                                                                                                                                    |
| Home Directory | The absolute path location of user's home directory                                                      | For example: /home/rtfirefly                                                                                                                                                                                                     |
| Shell          | The absolute location of a user's default shell                                                          | For example: /bin/bash                                                                                                                                                                                                           |


By default, Linux distinguishes between several account types in order to isolate processes and workloads. Linux has four types of accounts:

            root
            System
            Normal
            Network

For a safe working environment, it is advised to grant the minimum privileges possible and necessary to accounts, and remove inactive accounts. The `last` utility, which shows the last time each user logged into the system, can be used to help identify potentially inactive accounts which are candidates for system removal.

####  Understanding the root Account

root is the most privileged account on a Linux/UNIX system. This account has the ability to carry out all facets of system administration, including adding accounts, changing user passwords, examining log files, installing software, etc. Utmost care must be taken when using this account. It has no security restrictions imposed upon it.

When you are signed in as, or acting as root, the shell prompt displays '#' (if you are using bash and you have not customized the prompt, as we have discussed previously). This convention is intended to serve as a warning to you of the absolute power of this account.


root privileges are required to perform operations such as:

            Creating, removing and managing user accounts
            Managing software packages
            Removing or modifying system files
            Restarting system services.

Regular account users of Linux distributions might be allowed to install software packages, update some settings, use some peripheral devices, and apply various kinds of changes to the system. However, root privilege is required for performing administration tasks such as restarting most services, manually installing packages and managing parts of the filesystem that are outside the normal user’s directories.

Operations Not Requiring root Privileges

A regular account user can perform some operations requiring special permissions; however, the system configuration must allow such abilities to be exercised.

SUID (Set owner User ID upon execution - similar to the Windows "run as" feature) is a special kind of file permission given to a file. Use of SUID provides temporary permissions to a user to run a program with the permissions of the file owner (which may be root) instead of the permissions held by the user.


Comparing sudo and su

When assigning elevated privileges, you can use the command su (switch or substitute user) to launch a new shell running as another user (you must type the password of the user you are becoming). Most often, this other user is root, and the new shell allows the use of elevated privileges until it is exited. It is almost always a bad (dangerous for both security and stability) practice to use su to become root. Resulting errors can include deletion of vital files from the system and security breaches.

Granting privileges using sudo is less dangerous and is preferred. By default, sudo must be enabled on a per-user basis. However, some distributions (such as Ubuntu) enable it by default for at least one main user, or give this as an installation option.

In Linux you can use either su or sudo to temporarily grant root access to a normal user. However, these methods are actually quite different. Listed below are the differences between the two commands:

| su  | sudo        |
|-----|---------------|
| When  elevating privilege, you need to enter the root password. Giving the  root password to a normal user should never, ever be done.                                          | When elevating privilege, you need to enter the user’s password and not the root password.               |
| Once a user elevates to the root account using su, the user can do anything that the root user can do for as long as the user wants, without being asked again for a password.  | Offers  more features and is considered more secure and more configurable.  Exactly what the user is allowed to do can be precisely controlled and  limited. By default the user will either always have to keep giving  their password to do further operations with sudo, or can avoid doing so for a configurable time interval. |
| The command has limited logging features.     | The command has detailed logging features.           |


sudo Features

sudo has the ability to keep track of unsuccessful attempts at gaining root access. Users' authorization for using sudo is based on configuration information stored in the /etc/sudoers file and in the /etc/sudoers.d directory.

A message such as the following would appear in a system log file (usually /var/log/secure) when trying to execute sudo bash without successfully authenticating the user:

```bash
authentication failure; logname=op uid=0 euid=0 tty=/dev/pts/6 ruser=op rhost= user=op
conversation failed
auth could not identify password for [op]
op : 1 incorrect password attempt ;
TTY=pts/6 ; PWD=/var/log ; USER=root ; COMMAND=/bin/bash
```


### the sudoers file

Whenever sudo is invoked, a trigger will look at /etc/sudoers and the files in /etc/sudoers.d to determine if the user has the right to use sudo and what the scope of their privilege is. Unknown user requests and requests to do operations not allowed to the user even with sudo are reported. The basic structure of entries in these files is:

who where = (as_whom) what

/etc/sudoers contains a lot of documentation in it about how to customize. Most Linux distributions now prefer you add a file in the directory /etc/sudoers.d with a name the same as the user. This file contains the individual user's sudo configuration, and one should leave the master configuration file untouched except for changes that affect all users.

You should edit any of these configuration files by using visudo, which ensures that only one person is editing the file at a time, has the proper permissions, and refuses to write out the file and exit if there are syntax errors in the changes made. The editing can be accomplished by doing a command such as the following ones:

```
# visudo /etc/sudoers
# visudo -f /etc/sudoers.d/student
```

The actual specific editor invoked will depend on the setting of your EDITOR environment variable.


#### Demo of user mangagement

1. Create a new user and give the user an initial password with passwd.

    `sudo useradd newuser`
    `sudo passwd newuser `  (give the password for this user when prompted)

2. Configure this user to be able to use sudo.    

    With root privilege, (use `sudo visudo`) add this line to `/etc/sudoers`:

    `newuser      ALL=(ALL)     ALL`

    Alternatively, create a file named `/etc/sudoers.d/newuser` with just that one line as content.

3. Login as or switch to this new user and make sure you can execute a command that requires root privilege.

    `sudo su newuser` or `ssh newuser@localhost`

    which will require giving newuser's password, and is probably a better solution. Instead of localhost you can give your hostname, IP address or 127.0.0.1.

    Then as newuser just type: `sudo ls /root`
4. Look at the password aging for the user. Modify the expiration date for the user, setting it to be something that has passed, and check to see what has changed.
    ```bash
    chage --list newuser
    sudo chage -E 2014-31-12 newuser
    chage --list newuser
    sudo userdel newuser  
    ```
5. When you are finished and wish to delete the newly created account, use userdel, as in:
`$ sudo userdel newuser`



### Process Isolation

Linux is considered to be more secure than many other operating systems because processes are naturally isolated from each other. One process normally cannot access the resources of another process, even when that process is running with the same user privileges. Linux thus makes it difficult (though certainly not impossible) for viruses and security exploits to access and attack random resources on a system.

More recent additional security mechanisms that limit risks even further include:

            Control Groups (cgroups)
            Allows system administrators to group processes and associate finite resources to each cgroup.
            Containers
            Makes it possible to run multiple isolated Linux systems (containers) on a single system by relying on cgroups.
            Virtualization
            Hardware is emulated in such a way that not only processes can be isolated, but entire systems are run simultaneously as isolated and insulated guests (virtual machines) on one physical host.

Linux limits user access to non-networking hardware devices in a manner that is extremely similar to regular file access.


Password aging is a method to ensure that users get prompts that remind them to create a new password after a specific period. This can ensure that passwords, if cracked, will only be usable for a limited amount of time. This feature is implemented using chage, which configures the password expiry information for a user.

Another method is to force users to set strong passwords using Pluggable Authentication Modules (PAM). PAM can be configured to automatically verify that a password created or modified using the passwd utility is sufficiently strong. PAM configuration is implemented using a library called pam_cracklib.so, which can also be replaced by pam_passwdqc.so to take advantage of more options.

One can also install password cracking programs, such as John The Ripper, to secure the password file and detect weak password entries. It is recommended that written authorization be obtained before installing such tools on any system that you do not own.


### Hardware Device Access

Linux limits user access to non-networking hardware devices in a manner that is extremely similar to regular file access. Applications interact by engaging the filesystem layer (which is independent of the actual device or hardware the file resides on). This layer will then open a device special file (often called a device node) under the /dev directory that corresponds to the device being accessed. Each device special file has standard owner, group and world permission fields. Security is naturally enforced just as it is when standard files are accessed.

Hard disks, for example, are represented as /dev/sd*. While a root user can read and write to the disk in a raw fashion, for example, by doing something like:

` # echo hello world > /dev/sda1`

The standard permissions as shown in the figure, make it impossible for regular users to do so. Writing to a device in this fashion can easily obliterate the filesystem stored on it in a way that cannot be repaired without great effort, if at all. The normal reading and writing of files on the hard disk by applications is done at a higher level through the filesystem, and never through direct access to the device node.

### Staying Current
Linux distributions have a good record of reacting quickly and pushing out fixes to all systems by updating their software repositories and sending notifications to update immediately. The same thing is true with bug fixes and performance improvements that are not security related.
Many of the most successful attack vectors come from exploiting security holes for which fixes are already known but not universally deployed.

### Passwords

Originally, encrypted passwords were stored in the /etc/passwd file, which was readable by everyone. This made it rather easy for passwords to be cracked.

On modern systems, passwords are actually stored in an encrypted format in a secondary file named /etc/shadow. Only those with root access can read or modify this file.

Most Linux distributions rely on a modern password encryption algorithm called SHA-512 (Secure Hashing Algorithm 512 bits), developed by the U.S. National Security Agency (NSA) to encrypt passwords.

The SHA-512 algorithm is widely used for security applications and protocols. These security applications and protocols include TLS, SSL, PHP, SSH, S/MIME and IPSec. SHA-512 is one of the most tested hashing algorithms.

You can secure the boot process with a secure password to prevent someone from bypassing the user authentication step. This can work in conjunction with password protection for the BIOS. Note that while using a bootloader password alone will stop a user from editing the bootloader configuration during the boot process, it will not prevent a user from booting from an alternative boot media such as optical disks or pen drives. Thus, it should be used with a BIOS password for full protection.

### Guidelines of security:
- Lock down workstations and servers.
- Protect your network links such that it cannot be accessed by people you do not trust.
- Protect your keyboards where passwords are entered to ensure the keyboards cannot be tampered with.
- Ensure a password protects the BIOS in such a way that the system cannot be booted with a live or rescue DVD or USB key.

For single user computers and those in a home environment some of the above features (like preventing booting from removable media) can be excessive, and you can avoid implementing them. However, if sensitive information is on your system that requires careful protection, either it shouldn't be there or it should be better protected by following the above guidelines.





## Shell scripting
Motivation
- Automate tasks and reduce risk of errors
- Combine long and repetive sequences of commands into one simple command
- Share procedures among several Users
- Quick prototyping, no need to compile.
- Create new commands using combinations of UtilitiesProvide a controlled interface to users

Types of commands that can be used in a bash shell script:
- Compiled applications
- Built-in bash commands
- Other scripts


 ### Summary
- Scripts are a sequence of statements and commands stored in a file that can be executed by a shell. The most commonly used shell in Linux is bash.
- Command substitution allows you to substitute the result of a command as a portion of another command.
- Functions or routines are a group of commands that are used for execution.
- Environmental variables are quantities either preassigned by the shell or defined and modified by the user.
- To make environment variables visible to child processes, they need to be exported.
- Scripts can behave differently based on the parameters (values) passed to them.
- The process of writing the output to a file is called output redirection.
- The process of reading input from a file is called input redirection.
- The if statement is used to select an action based on a condition.
- Arithmetic expressions consist of numbers and arithmetic operators, such as `+`, `-`, and `*`.

### Choice of Shells
Linux provides a wide choice of shells; exactly what is available on the system is listed in /etc/shells. Typical choices are:

/bin/sh
/bin/bash
/bin/tcsh
/bin/csh
/bin/ksh
/bin/zsh

Most Linux users use the default bash shell.

Remember from our earlier discussion, a shell is a command line interpreter which provides the user interface for terminal windows. It can also be used to run scripts, even in non-interactive sessions without a terminal window, as if the commands were being directly typed in.

For example, typing `find . -name "*.c" -ls` at the command line accomplishes the same thing as executing a script file containing the lines:
```
#!/bin/bash
find . -name "*.c" -ls
```

The first line of the script, which starts with #!, contains the full path of the command interpreter (in this case /bin/bash) that is to be used on the file. As we have noted, you have quite a few choices for the scripting language you can use, such as /usr/bin/perl, /bin/csh, /usr/bin/python, etc.


All shell scripts generate a return value upon finishing execution, which can be explicitly set with the exit statement. Return values permit a process to monitor the exit state of another process, often in a parent-child relationship. Knowing how the process terminates enables taking any appropriate steps which are necessary or contingent on success or failure.

An easy way to demonstrate success and failure completion is to execute ls on a file that exists as well as one that does not, the return value is stored in the environment variable represented by $?

The concatenation operator (\), the backslash character, is used to continue long commands over several lines.

Environment varialbes:
standard environment variables are HOME, PATH, and HOST. When referenced, environment variables must be prefixed with the $ symbol, as in $HOME. You can view and set the value of environment variables. For example, the following command displays the value stored in the PATH variable:

`$ echo $PATH`

However, no prefix is required when setting or modifying the variable value. For example, the following command sets the value of the MYCOLOR variable to blue:

`$ MYCOLOR=blue`

Multiple commands in a line:
`$ make ; make install ; make clean` Three commands in the following example will all execute, even if the ones preceding them fail.

`$ make && make install && make clean`  abort subsequent commands when an earlier one fails.  If the first command fails, the second one will never be executed.

`$ cat file1 || cat file2 || cat file3` proceed until something succeeds and then you stop executing any further steps.

Builtin Shell Commands
Built in bash Commands (view a complete list by typing `help`)
 - cd
 - pwd
 - echo
 - read
 - logout
 - printf
 - let
 - ulimit
 Compiled Applications
 - rm
 - ls
 - df
 - vi
 - gzip
 Other Scripts





###Substitutions:
If you want to substitute the result of an expression (say echo /tmp) to be the argument for cd, you can represent this in two different ways:


- By enclosing the inner command in $( )
```bash
cd $(echo /tmp)
```

- By enclosing the inner command with backticks ( \` )
```bash
cd `echo /tmp`
```

The second, backticks form, is deprecated in new scripts and commands. No matter which method is used, the specified command will be executed in a newly launched shell environment, and the standard output of the shell will be inserted where the command substitution is done.

Virtually any command can be executed this way. While both of these methods enable command substitution, the $( ) method allows command nesting. New scripts should always use this more modern method. For example:

`$ ls /lib/modules/$(uname -r)/`

## Interactive Example Using bash Scripts

Now, let's see how to create a more interactive example using a bash script. The user will be prompted to enter a value, which is then displayed on the screen. The value is stored in a temporary variable, name. We can reference the value of a shell variable by using a $ in front of the variable name, such as $name. To create this script, you need to create a file named getname.sh in your favorite editor with the following content:

```bash
#!/bin/bash
# Interactive reading of a variable
echo "ENTER YOUR NAME"
read name
# Display variable input
echo The name given was :$name
```

Once again, make it executable by doing chmod +x getname.sh.

In the above example, when the user types./getname.sh and the script is executed, the user is prompted with the string ENTER YOUR NAME. The user then needs to enter a value and press the Enter key. The value will then be printed out.

Note: The hash-tag/pound-sign/number-sign (#) is used to start comments in the script and can be placed anywhere in the line (the rest of the line is considered a comment). However, note the special magic combination of #!, used on the first line, is a unique exception to this rule.

### Basic Syntax and Special Characters

| Character | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| #         | Used to add a comment, except when used as \#, or as #! when starting a script |
| \         | Used at the end of a line to indicate continuation on to the next line         |
| ;         | Used to interpret what follows as a new command to be executed next            |
| $         | Indicates what follows is an environment variable                              |
| >         | Redirect output                                                                |
| >>        | Append output                                                                  |
| <         | Redirect input                                                                 |
| \|        | Used to pipe the result into the next command                                  |


### Script Parameters
Users often need to pass parameter values to a script, such as a filename, date, etc

| Parameter    | Meaning                       |
|--------------|-------------------------------|
| $0           | Script name                   |
| $1           | First parameter               |
| $2, $3, etc. | Second, third parameter, etc. |
| $*           | All parameters                |
| $#           | Number of arguments           |




### Exporting Environment Variables

While we discussed the export of environment variables in the section on the "User Environment", it is worth reviewing this topic in the context of writing bash scripts.

By default, the variables created within a script are available only to the subsequent steps of that script. Any child processes (sub-shells) do not have automatic access to the values of these variables. To make them available to child processes, they must be promoted to environment variables using the export statement, as in:

export VAR=value

or

VAR=value ; export VAR

While child processes are allowed to modify the value of exported variables, the parent will not see any changes; exported variables are not shared, they are only copied and inherited.

Typing export with no arguments will give a list of all currently exported environment variables.


### Functions
A function is a code block that implements a set of operations. Functions are useful for executing procedures multiple times, perhaps with varying input variables. Functions are also often called subroutines. Using functions in scripts requires two steps:

1. Declaring a function
2. Calling a function

The function declaration requires a name which is used to invoke it. The proper syntax is:

function_name () {
   command...
}

For example, the following function is named display:

display () {
   echo "This is a sample function"
}

The function can be as long as desired and have many statements. Once defined, the function can be called later as many times as necessary. In the full example shown in the figure, we are also showing an often-used refinement: how to pass an argument to the function. The first argument can be referred to as $1, the second as $2, etc.


e.g.,

#!/bin/bash

showmess(){
    echo My favorite Linux Distro is : $1
}
echo ""

showmess Ubuntu
showmess Fedora


### The if Statement

Conditional decision making, using an if statement, is a basic construct that any useful programming or scripting language must have.

When an if statement is used, the ensuing actions depend on the evaluation of specified conditions, such as:

            Numerical or string comparisons
            Return value of a command (0 for success)
            File existence or permissions.

In compact form, the syntax of an if statement is:

if TEST-COMMANDS; then CONSEQUENT-COMMANDS; fi

A more general definition is:

if condition
then
       statements
else
       statements
fi



In the following example, an if statement checks to see if a certain file exists, and if the file is found, it displays a message indicating success or failure:

```bash
if [ -f "$1" ]
then
    echo file "$1 exists"
else
    echo file "$1" does not exist
fi
```

We really should also check first that there is an argument passed to the script ($1) and abort if not.

Notice the use of the square brackets ([]) to delineate the test condition. There are many other kinds of tests you can perform, such as checking whether two numbers are equal to, greater than, or less than each other and make a decision accordingly; we will discuss these other tests.

In modern scripts, you may see doubled brackets as in [[ -f /etc/passwd ]]. This is not an error. It is never wrong to do so and it avoids some subtle problems, such as referring to an empty environment variable without surrounding it in double quotes; we will not talk about this here.

You can use the `elif` statement to perform more complicated tests, and take action appropriate actions. The basic syntax is:

if [ sometest ] ; then
    echo Passed test1
elif [ somothertest ] ; then
    echo Passed test2
fi

In the example shown we use strings tests which we will explain shortly, and show how to pull in an environment variable with the read statement.


bash provides a set of file conditionals, that can be used with the if statement, including those in the table.

You can use the if statement to test for file attributes, such as:

            File or directory existence
            Read or write permission
            Executable permission.

For example, in the following example:

if [ -x /etc/passwd ] ; then
    ACTION
fi

the if statement checks if the file /etc/passwd is executable, which it is not. Note the very common practice of putting:

; then

on the same line as the if statement.

You can view the full list of file conditions typing:

man 1 test.

| Condition | Meaning                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------|
| -e file   | Checks if the file exists.                                                                    |
| -d file   | Checks if the file is a directory.                                                            |
| -f file   | Checks if the file is a regular file (i.e. not a symbolic link, device node, directory, etc.) |
| -s file   | Checks if the file is of non-zero size.                                                       |
| -g file   | Checks if the file has sgid set.                                                              |
| -u file   | Checks if the file has suid set.                                                              |
| -r file   | Checks if the file is readable.                                                               |
| -w file   | Checks if the file is writable.                                                               |
| -x file   | Checks if the file is executable.                                                             |


### Boolean expressions

| Operator | Operation | Meaning                                                                     |
|----------|-----------|-----------------------------------------------------------------------------|
| &&       | AND       | The action will be performed only if both the conditions evaluate to true.  |
| \|\|     | OR        | The action will be performed if any one of the conditions evaluate to true. |
| !        | NOT       | The action will be performed only if the condition evaluates to false.      |

Note that if you have multiple conditions strung together with the && operator, processing stops as soon as a condition evaluates to false. For example, if you have A && B && C and A is true but B is false, C will never be executed.

Likewise, if you are using the || operator, processing stops as soon as anything is true. For example, if you have A || B || C and A is false and B is true, you will also never execute C.


Boolean expressions return either TRUE or FALSE. We can use such expressions when working with multiple data types, including strings or numbers, as well as with files. For example, to check if a file exists, use the following conditional test:

[ -e <filename> ]

Similarly, to check if the value of number1 is greater than the value of number2, use the following conditional test:

[ $number1 -gt $number2 ]

The operator -gt returns TRUE if number1 is greater than number2.


You can use the if statement to compare strings using the operator == (two equal signs). The syntax is as follows:

if [ string1 == string2 ] ; then
   ACTION
fi

Note that using one = sign will also work, but some consider it deprecated usage. Let’s now consider an example of testing strings.

In the example illustrated here, the if statement is used to compare the input provided by the user and accordingly display the result.

Numerical Tests

| Operator     Meaning             |
|----------------------------------|
| -eq     Equal to                 |
| -ne     Not equal to             |
| -gt     Greater than             |
| -lt     Less than                |
| -ge     Greater than or equal to |
| -le     Less than or equal to    |


Arithmetic expressions can be evaluated in the following three ways (spaces are important!):

1. Using the `expr` utility. `expr` is a standard but somewhat deprecated program. The syntax is as follows:
```bash
expr 8 + 8
echo $(expr 8 + 8)
```
2 .Using the $((...)) syntax. This is the built-in shell format. The syntax is as follows:
```bash
echo $((x+1))
```
3. Using the built-in shell command let. The syntax is as follows:
```bash
let x=( 1 + 2 ); echo $x
```
In modern shell scripts, the use of expr is better replaced with var=$((...)).

`$0` parameter that contains the name of the script being executed

### String operations

| Operator                 | Meaning                                                            |
|--------------------------|--------------------------------------------------------------------|
| `[[ string1 > string2 ]] ` | Compares the sorting order of string1 and string2.                 |
| `[[ string1 == string2 ]]` | Compares the characters in string1 with the characters in string2. |
| `myLen1=${#string1}  `     | Saves the length of string1 in the variable myLen1.                |


Parts of a String

At times, you may not need to compare or use an entire string. To extract the first n characters of a string we can specify: ${string:0:n}. Here, 0 is the offset in the string (i.e. which character to begin from) where the extraction needs to start and n is the number of characters to be extracted.

To extract all characters in a string after a dot (.), use the following expression: ${string#\*.}.

`${#abc}` Find length of string 'abc'

### The `case` Statement

The case statement is used in scenarios where the actual value of a variable can lead to different execution paths. case statements are often used to handle command-line options.

Below are some of the advantages of using the case statement:

            It is easier to read and write.
            It is a good alternative to nested, multi-level if-then-else-fi code blocks.
            It enables you to compare a variable against several values at once.
            It reduces the complexity of a program.



Here is the basic structure of the case statement:

```bash
case expression in
   pattern1) execute commands;;
   pattern2) execute commands;;
   pattern3) execute commands;;
   pattern4) execute commands;;
   * )       execute some default commands or nothing ;;
esac
```

### Looping Constructs

By using looping constructs, you can execute one or more lines of code repetitively, usually on a selection of values of data such as individual files. Usually, you do this until a conditional test returns either true or false, as is required.

Three type of loops are often used in most programming languages:

            for
            while
            until.

All these loops are easily used for repeating a set of statements until the exit condition is true.

The for loop operates on each element of a list of items. The syntax for the for loop is:

for variable-name in list
do
    execute one iteration for each item in the list until the list is finished
done

The while loop repeats a set of statements as long as the control command returns true. The syntax is:

while condition is true
do
    Commands for execution
    ----
done


The until loop repeats a set of statements as long as the control command is false. Thus, it is essentially the opposite of the while loop. The syntax is:

until condition is false
do
    Commands for execution
    ----
done

Similar to the while loop, the set of commands that need to be repeated should be enclosed between do and done. You can use any command or operator as the condition


### Debugging
You can run a bash script in debug mode either by doing bash –x ./script_file, or bracketing parts of the script with set -x and set +x. The debug mode helps identify the error because:

            It traces and prefixes each command with the + character.
            It displays each command before executing it.
            It can debug only selected parts of a script (if desired) with:

            set -x    # turns on debugging
            ...
            set +x    # turns off debugging

### Creating a Temporary File and Directory

Sloppiness in creation of temporary files can lead to real damage, either by accident or if there is a malicious actor.

The best practice is to create random and unpredictable filenames for temporary storage. One way to do this is with the mktemp utility, as in the following examples.

The XXXXXXXX is replaced by mktemp with random characters to ensure the name of the temporary file cannot be easily predicted and is only known within your program.

TEMP=$(mktemp /tmp/tempfile.XXXXXXXX) 	To create a temporary file
TEMPDIR=$(mktemp -d /tmp/tempdir.XXXXXXXX) 	

To create a temporary directory

Discarding Output with /dev/null

Certain commands (like find) will produce voluminous amounts of output, which can overwhelm the console. To avoid this, we can redirect the large output to a special file (a device node) called /dev/null. This pseudofile is also called the bit bucket or black hole.

All data written to it is discarded and write operations never return a failure condition. Using the proper redirection operators, it can make the output disappear from commands that would normally generate output to stdout and/or stderr:

$ ls -lR /tmp > /dev/null

In the above command, the entire standard output stream is ignored, but any errors will still appear on the console. However, if one does:

$ ls -lR /tmp >& /dev/null

both stdout and stderr will be dumped into /dev/null.

random numbers can be generated by using the $RANDOM environment variable, which is derived from the Linux kernel’s built-in random number generator

the system maintains a so-called entropy pool of these digital numbers/random bits. Random numbers are created from this entropy pool.

The Linux kernel offers the /dev/random and /dev/urandom device nodes, which draw on the entropy pool to provide random numbers which are drawn from the estimated number of bits of noise in the entropy pool.

/dev/random is used where very high quality randomness is required, such as one-time pad or key generation, but it is relatively slow to provide values. /dev/urandom is faster and suitable (good enough) for most cryptographic purposes.

Furthermore, when the entropy pool is empty, /dev/random is blocked and does not generate any number until additional environmental noise (network traffic, mouse movement, etc.) is gathered, whereas /dev/urandom reuses the internal pool to produce more pseudo-random bits.
***


## Appendix

### Email
 All users by default have an email account in the form "username@system.fullyqualifieddomain" for which there will be a mailbox on the Linux system.

 The IMAP server normally runs on port 143 by default.

 An IMAP server that is not running or is not installed, and the port being blocked by the firewall are two common problems that affect email connections to a Linux server.

 How could you check that an IMAP server is running and accessible on the Linux server?
Testing access to the port used by the IMAP server using Telnet is an effective check.
telnet <servername> imap and/or telnet <servername> imaps. If you get answers then you have IMAP from the Internet. You can also look if it is available only on your server by telnet localhost imap and/or telnet localhost imaps.

Alternatively you could check if netstat -a | fgrep imap returns a line with LISTEN in it. Then the IMAP server is up and running.


Linux provides users with choice in their email clients, and even has graphical email clients, if the hardware permits. Even the text based clients can generally handle multimedia content. There is no need to purchase costly commercial email software.

An IMAP server that is not running or is not installed, and the port being blocked by the firewall are two common problems that affect email connections to a Linux server.

Testing access to the port used by the IMAP server using Telnet is an effective check.

Linux email clients are based on open standards and can be used on the same mail folders.

 Using standard protocols like IMAP and POP3, they can even safely share folders with commercial packages.
