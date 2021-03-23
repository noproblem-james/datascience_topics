
# Glossary

**Ansible** open-source automation platform for configuration management, application deployment, and task automation. It can also do IT orchestration, where you have to run tasks in sequence and create a chain of events which must happen on several different servers or devices. Ansible runs 'playbooks', which are in YAML format.


**CRI-O (Container Runtime Interface)** a plugin interface that gives kubelet (a cluster node agent used to create pods and start containers) the ability to use different OCI-compliant container runtimes, without needing to recompile Cabernets.

**CIDR - Classless inter-domain routing**  is a set of Internet protocol (IP) standards that is used to create unique identifiers for networks and individual devices. CIDR Notation is a simplified way to show a specific range of IP addresses.  
- E.g., `10.0.0.0/16` = all IP addresses from `10.0.0.0 `to `10.0.255.255`. How does that work?

**etcd** is an open-source distributed key-value store that serves as the backbone of distributed systems by providing a canonical hub for cluster coordination and state management – the system's source of truth.

**firewalld** a firewall management tool that provides a dynamically managed firewall with support for network/firewall zones that define the trust level of network connections or interfaces. The RHEL Linux distribution uses firewalld as the default firewall management tool and docker also supports it.




**HAProxy** software that provides a high availability load balancer and proxy server for TCP and HTTP-based applications that spreads requests across multiple servers.


**httpd (HTTP Daemon)** a software program that runs in the background of a web server and waits for the incoming server requests. (We are installing it for air-gapped install  for hosting the RPM repository. `yum install -y httpd` command will automatically find and install all required dependencies for httpd.)

**Host name** is a combination of the name of your machine and a domain name (e.g. machinename.domain.com). The purpose of a host name is readability - it's much easier to remember than an IP address. All hostnames resolve to IP addresses, so in many instances they are used interchangeably

**inode** (index node) is a data structure in a Unix-style file system that describes a file-system object such as a file or a directory. Each inode stores the attributes and disk block locations of the object's data.[1] File-system object attributes may include metadata (times of last change,[2] access, modification), as well as owner and permission data.[3]

Directories are lists of names assigned to inodes. A directory contains an entry for itself, its parent, and each of its children.

**FDQN (Fully qualified domain name)** is the complete domain name for a specific computer, or host, on the internet. The FQDN consists of two parts: **the host name** and **the domain name**.

**IP forwarding** a process used to determine which path a packet or datagram can be sent. The process uses routing information to make decisions and is designed to send a packet over multiple networks.
Generally, networks are separated from each other by routers. For packets to travel between networks, they must be “routed” from one network to another. These routers contain a routing table that can contain specific instructions on how to send packets to a destination network (known as a route), or a set of generic instructions on where to send packets that do not match any of the other specified routes (called a default route), or both. These routes can either be hard-coded into the router by the network administrator (called a static route), or learned dynamically via a routing protocol. These routes give the routers instructions on how to utilize the physical network infrastructure that is in place to get packets to their destination, regardless of the number of hops that they must take to get there.  

**The Internet Protocol** (IP) is the principal communications protocol in the Internet protocol suite for relaying datagrams across network boundaries. Its routing function enables internetworking, and essentially establishes the Internet.

IP has the task of delivering packets from the source host to the destination host solely based on the IP addresses in the packet headers. For this purpose, IP defines packet structures that encapsulate the data to be delivered. It also defines addressing methods that are used to label the datagram with source and destination information.

Historically, IP was the connectionless datagram service in the original Transmission Control Program introduced by Vint Cerf and Bob Kahn in 1974, which was complemented by a connection-oriented service that became the basis for the Transmission Control Protocol (TCP). The Internet protocol suite is therefore often referred to as TCP/IP.

The first major version of IP, Internet Protocol Version 4 (IPv4), is the dominant protocol of the Internet. Its successor is Internet Protocol Version 6 (IPv6), which has been in increasing deployment on the public Internet since c. 2006.

**mkfs** makes file systems. On other operating systems, creating a file system is called formatting. Regardless of its name, it is the process that prepares a partition so that it can store data. The partition needs a way to store files, yes. But it also needs a mechanism to store the names and locations of those files, together with their metadata such as the file creation timestamp, the file modified timestamp, the size of the file, and so on. Once mkfs has built the necessary framework for handling and storing file metadata, you can start adding files to the partition.

**Network Manager** is a program for providing detection and configuration for systems to automatically connect to networks. NetworkManager was originally developed by Red Hat and now is hosted by the GNOME project.
 - Network Manager was developed to make things easier and more uniform across distributions. It can list all available networks (both wired and wireless), allow the choice of a wired, wireless, or mobile broadband network, handle passwords, and set up Virtual Private Networks (VPNs). Except for unusual situations, it is generally best to let Network Manager establish your connections and keep track of your settings.





**NFS** a distributed file system protocol originally developed by Sun Microsystems (Sun) in 1984,[1] allowing a user on a client computer to access files over a computer network much like local storage is accessed. NFS, like many other protocols, builds on the Open Network Computing Remote Procedure Call (ONC RPC) system

A network (also sometimes called distributed) filesystem may have all its data on one machine or have it spread out on more than one network node. A variety of different filesystems can be used locally on the individual machines; a network filesystem can be thought of as a grouping of lower level filesystems of varying types. Many system administrators mount remote users' home directories on a server in order to give them access to the same files and configuration files across multiple client systems. This allows the users to log in to different computers, yet still have access to the same files and resources.

The most common such filesystem is named simply NFS (the Network Filesystem). It has a very long history and was first developed by Sun Microsystems.

NFS uses daemons (built-in networking and service processes in Linux) and other system servers are started at the command line by typing:

`$ sudo systemctl start nfs`

The text file /etc/exports contains the directories and permissions that a host is willing to share with other systems over NFS. A very simple entry in this file may look like the following:

`/projects *.example.com(rw)`

This entry allows the directory /projects to be mounted using NFS with read and write (rw) permissions and shared with other hosts in the example.com domain. As we will detail in the next chapter, every file in Linux has three possible permissions: read (r), write (w) and execute (x).

After modifying the /etc/exports file, you can type `exportfs -av` to notify Linux about the directories you are allowing to be remotely mounted using NFS. You can also restart NFS with sudo `systemctl restart nfs`, but this is heavier, as it halts NFS for a short while before starting it up again. To make sure the NFS service starts whenever the system is booted, issue `sudo systemctl enable nfs`. (Note: On RHEL/CentOS 8, the service is called `nfs-server`, not `nfs`).

**ntpd** (Network Time Protocol daemon) is an operating system program that maintains the system time in synchronization with time servers using the Network Time Protocol (NTP).  

- The Network Time Protocol (NTP) is the most popular and reliable protocol for setting the local time by consulting established Internet servers. Linux distributions always come with a working NTP setup, which refers to specific time servers run or relied on by the distribution. This means that no setup, beyond "on" or "off", is required for network time synchronization. If desired, more detailed configuration is possible by editing the standard NTP configuration file (/etc/ntp.conf) for Linux NTP utilities.

**OVA, OVF** (Open Virtualization Appliance/Application, Open Virtualization Format)

An OVF refers to the Open Virtualization Format, which is a “packaging standard designed to address the portability and deployment of virtualization appliances” (Source). The OVF format standard was formed by the Distributed Management Task Force, or DMTF, which is an industry working group comprised of over 160 member companies and organizations. The DMTF board is comprised of 15 technology companies and includes Dell, EMC, VMware, Oracle, & Microsoft. As announced at VMworld 2010, DMTF’s OVF standard was adopted as a National Standard by ANSI.

An OVF package structure consists of a number of files: a descriptor file, optional manifest and certificate files, optional disk images, and optional resource files (such as ISO’s). The optional disk image files can be VMware vmdk’s, or any other supported disk image file. More information about the OVF format standard can be found here.
OVA and OVF: The Differences

OVF is not only the name of the packaging format standard, but it also refers to the package when distributed as a group of files. An OVA (open virtual appliance or application) is merely a single file distribution of the same file package, stored in the TAR format.



**RFS**: (Remote file sharing)  a type of distributed file system technology that enables file and/or data access to multiple remote users over the Internet or a network connection.

**RPC** (remote procedure call) is when a computer program causes a procedure (subroutine) to execute in a different address space (commonly on another computer on a shared network), which is coded as if it were a normal (local) procedure call, without the programmer explicitly coding the details for the remote interaction. (wikipedia)

**RPM** (originally Red Hat Package Manager; now a recursive acronym, “	RPM Package Manager”) is a free, open-source package management system. The name RPM refers to .rpm file format and the package manager program itself. RPM was intended primarily for Linux distributions; the file format is the baseline package format of the Linux Standard Base. Although it was created for use in Red Hat Linux, RPM is now used in many Linux distributions.

- *RPM Versus Containerized*
An RPM installation installs all services through package management and configures services to run within the same user space, while a containerized installation installs services using container images and runs separate services in individual containers.

**Process**
A process is simply an instance of one or more related tasks (threads) executing on your computer. It is not the same as a program or a command. A single command may actually start several processes simultaneously. Some processes are independent of each other and others are related. A failure of one process may or may not affect the others running on the system.

Processes use many system resources, such as memory, CPU (central processing unit) cycles, and peripheral devices, such as network cards, hard drives, printers and displays. The operating system (especially the kernel) is responsible for allocating a proper share of these resources to each process and ensuring overall optimized system utilization.


A terminal window (one kind of command shell) is a process that runs as long as needed. It allows users to execute programs and access resources in an interactive environment. You can also run programs in the background, which means they become detached from the shell.

Processes can be of different types according to the task being performed. Here are some different process types, along with their descriptions and examples:


| Process Type          | Description                                                                                                                                                                                                                                                                                                                                                       | Example                        |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| Interactive Processes | Need to be started by a user, either at a command line or through a graphical interface such as an icon or a menu selection.                                                                                                                                                                                                                                      | bash, firefox, top             |
| Batch Processes       | Automatic processes which are scheduled from and then disconnected from the terminal. These tasks are queued and work on a FIFO (First-In, First-Out) basis.                                                                                                                                                                                                      | updatedb, ldconfig             |
| Daemons               | Server  processes that run continuously. Many are launched during system  startup and then wait for a user or system request indicating that their  service is required.                                                                                                                                                                                          | httpd, sshd, libvirtd          |
| Threads               | Lightweight  processes. These are tasks that run under the umbrella of a main  process, sharing memory and other resources, but are scheduled and run  by the system on an individual basis. An individual thread can end  without terminating the whole process and a process can create new  threads at any time. Many non-trivial programs are multi-threaded. | firefox, gnome-terminal-server |
| Kernel Threads        | Kernel  tasks that users neither start nor terminate and have little control  over. These may perform actions like moving a thread from one CPU to  another, or making sure input/output operations to disk are completed.                                                                                                                                        | kthreadd, migration, ksoftirqd |


At any given time, there are always multiple processes being executed. The operating system keeps track of them by assigning each a unique process ID (PID) number. The PID is used to track process state, CPU usage, memory use, precisely where resources are located in memory, and other characteristics.

The priority for a process can be set by specifying a **nice value**, or niceness, for the process. The lower the nice value, the higher the priority. Low values are assigned to important processes, while high values are assigned to processes that can wait longer. A process with a high nice value simply allows other processes to be executed first. In Linux, a nice value of -20 represents the highest priority and +19 represents the lowest.  While this may sound backwards,  this convention (the nicer the process, the lower the priority) goes back to the earliest days of UNIX.


**SELinux** a security enhancement for access control--which users can access which resources.

**SRV Record** (Service record) is a specification of data in the Domain Name System defining the location, i.e., the hostname and port number, of servers for specified services.

`_service._proto.name. TTL class SRV priority weight port target.`

- service: the symbolic name of the desired service.
- proto: the transport protocol of the desired service; this is usually either TCP or UDP.
- name: the domain name for which this record is valid, ending in a dot.
- TTL: standard DNS time to live field.
- class: standard DNS class field (this is always IN).
- SRV: Type of Record (this is always SRV).
- weight: A relative weight for records with the same priority, higher value means higher chance of getting picked.
- port: the TCP or UDP port on which the service is to be found.
- target: the canonical hostname of the machine providing the service, ending in a dot.

An example SRV record in textual form that might be found in a zone file might be the following:

`_sip._tcp.example.com. 86400 IN SRV 0 5 5060 sipserver.example.com.`


**Static vs Dynamic memory**:
Static memory has pre-determined purpose throughout the whole life of the process. Static data simply exists all the time, at one place. The space is determined and reserved on compile time.
Dynamic data, on the other hand, is created at some point during the process execution and destroyed at another, not necessarily at the process termination. Obviously, dynamic data needs to reside somewhere, too. That place is called “heap”. It’s a memory segment which is managed by a “dynamic allocator” that finds and returns large enough memory chunk on demand (and you’re supposed to release the chunk back to it when you no longer need it).
Dynamic allocation may be a bit costly, but allows you to determine your data space requirements at runtime. Which is what you mostly need (you don’t want to reserve huge amount of memory if you might typically need just a little, but you still need to deal with some cases which will require a lot).

Static Memory Allocation
* Memory is allocated before the execution of the program begins (During Compilation).
* Variables remain permanently allocated.
* In this type of allocation Memory cannot be resized after the initial allocation.
* Implemented using stacks.
* Faster execution than Dynamic.
* It is less efficient than Dynamic allocation strategy.
* Implementation of this type of allocation is simple.
* Memory cannot be reuse when it is no longer needed.

Dynamic Memory Allocation
* Memory is allocated during the execution of the program.
* Allocated only when program unit is active
* In this type of allocation Memory can be dynamically expanded and shrunk as necessary.
* Implemented using heap
* Slower execution than static.
* It is more efficient than Static allocation strategy.
*  Implementation of this type of allocation is complicated.
* Memory can be freed when it is no longer needed & reuse or reallocate during execution

**OCR** OpenShift Container Registry adds the ability to automatically provision new image repositories on demand. This provides users with a built-in location for their application builds to push the resulting images.

Whenever a new image is pushed to OCR, the registry notifies OpenShift Container Platform about the new image, passing along all the information about it, such as the namespace, name, and image metadata. Different pieces of OpenShift Container Platform react to new images, creating new builds and deployments.

OCR can also be deployed as a stand-alone component that acts solely as a container registry, without the build and deployment integration. See Installing a Stand-alone Deployment of OpenShift Container Registry for details.
Third Party Registries

OpenShift Container Platform can create containers using images from third party registries, but it is unlikely that these registries offer the same image notification support as the integrated OpenShift Container Platform registry. In this situation OpenShift Container Platform will fetch tags from the remote registry upon imagestream creation. Refreshing the fetched tags is as simple as running `oc import-image <stream>`. When new images are detected, the previously-described build and deployment reactions occur.

**podman** is an open-source Linux tool for working with containers. That includes containers in registries such as docker.io and quay.io.

**portworx** is a storage service for containerized applications across multiple clouds and on-prem environments. With Portworx, you can manage any database or stateful service on any infrastructure using any container scheduler.

**Network File System (NFS)** is a distributed file system protocol originally developed by Sun Microsystems (Sun) in 1984, allowing a user on a client computer to access files over a computer network much like local storage is accessed. NFS, like many other protocols, builds on the Open Network Computing Remote Procedure Call (ONC RPC) system. The NFS is an open standard defined in a Request for Comments (RFC), allowing anyone to implement the protocol.

**tar** is a computer software utility for collecting many files into one archive file, often referred to as a **tarball**, for distribution or backup purposes. The name is derived from (t)ape (ar)chive, as it was originally developed to write data to sequential I/O devices with no file system of their own. 

**XFS** is a high-performance 64-bit journaling file system created by Silicon Graphics, Inc (SGI) in 1993.[6] It was the default file system in SGI's IRIX operating system starting with its version 5.3. XFS was ported to the Linux kernel in 2001; as of June 2014, XFS is supported by most Linux distributions, some of which use it as the default file system. Journaling is a capability which ensures consistency of data in the file system, despite any power outages or system crash that may occur. XFS provides journaling for file system metadata, where file system updates are first written to a serial journal before the actual disk blocks are updated. The journal is a circular buffer of disk blocks that is not read in normal file system operation. [wiki](https://en.wikipedia.org/wiki/XFS)  

**vim**
Usually, the actual program installed on your system is vim, which stands for Vi IMproved, and is aliased to the name vi. The name is pronounced as “vee-eye”.

Even if you do not want to use vi, it is good to gain some familiarity with it: it is a standard tool installed on virtually all Linux distributions. Indeed, there may be times where there is no other editor available on the system.

`vimtutor` launches a short but very comprehensive tutorial for those who want to learn their first vi commands. Even though it provides only an introduction and just seven lessons, it has enough material to make you a very proficient vi user, because it covers a large number of commands. After learning these basic ones, you can look up new tricks to incorporate into your list of vi commands because there are always more optimal ways to do things in vi with less typing.

| Mode    | Feature                                                                                                                                                                                                                                                                                                                                                                                                |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Command |     By default, vi starts in Command mode.   Each key is an editor command.   Keyboard strokes are interpreted as commands that can modify file contents.                                                                                                                                                                                                                                              |
| Insert  |     Type i to switch to Insert mode from Command mode.   Insert mode is used to enter (insert) text into a file.   Insert mode is indicated by an “? INSERT ?” indicator at the bottom of the screen.   Press Esc to exit Insert mode and return to Command mode.                                                                                                                                      |
| Line    |     Type :  to switch to the Line mode from Command mode. Each key is an external  command, including operations such as writing the file contents to disk  or exiting.   Uses line editing commands inherited from older line editors. Most  of these commands are actually no longer used. Some line editing  commands are very powerful.   Press Esc to exit Line mode and return to Command mode.  |



**yum** (Yellowdog Updater, Modified) is a free and open-source command-line package-management utility for computers running the Linux operating system using the RPM Package Manager. Allows for automatic updates and package and dependency management on RPM-based distributions. Under the hood, YUM depends on RPM, which is a packaging standard for digital distribution of software, which automatically uses hashes and digisigs to verify the authorship and integrity of said software.
