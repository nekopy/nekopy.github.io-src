Title: Directory Encryption with eCryptfs
Date: 2017-03-10  21:24:05
Modified: 2017-03-10 21:24:05
Category: linux
Tags: ecryptfs, shred, linux, encryption, security, privacy
Slug: ecryptfs
Authors: neko.py
Summary: Encrypting folders on Fedora easily using eCryptfs

A couple nights ago I decided to finally get some encryption up and running with eCryptfs.

![eCryptfs Honey Badger Mascot](http://ecryptfs.org/img/big-honey-badger.png)

I have a buddy who's using GPG to do their encryption, however this wasnt really the right choice for me. The primary issue was that the GPG tools I was looking at tend to just deal with a single file. The recommended way of using GPG on folders is to tar them up and encrypt them. To me this approach is really annoying. I dont want to untar some files whenever I want to use them. So after some further digging I wound up coming across the recommendation of using eCryptfs. 

eCryptfs is, as the name suggests, actually an encrypted filesystem and abstraction layer. The way it works is by introducing a kernel module which handles mounting the encrypted files on disk, and decrypts/encrypts file I/O on the fly. This way, you never actually have files decrypted on disk. Judging from the files, you can even set it up to work on your swap space. 

The issue I have with it right now is that it's _slow_. I'm trying to move some very large files, and it's grinding my laptop to a halt. As you might have seen in my other post, my laptop is relatively chunky. However, since this is overhead, I'm gonna give it the benefit of the doubt and finish moving the files to where I want them before I throw in the towel and try something else. But really, it hurt. I would have written this blog post on the 7th but the kernel module brought even vim to a halt. And since its in the kernel, I can't just hop in and set a good nice value...

Anyway, to set it up, it's mega simple. You wanna grab ecryptfs-utils from your package repos. 

For me, in order to use them I needed to add myself to a new group called ecryptfs.

Fun little trick I learned is that once you're in the group, you can get your system to honor the new group without needing to reboot by using the newgrp command.

```bash
newgrp ecrypts
```

Good stuff. Now that we're all set there, we wanna use the default eCryptfs setup. You do this like so:

```bash
ecryptfs-setup-private
```

This is gonna get you all configured with some new juicy ecryptfs space in a folder called .Private in your home directory and it's going to automatically set up a mount which allows you to access the files in a folder called Private when you login. There's two passwords you set up. One is the normal login password. This should match your account password and will be used for decrypting the folder when you mount it at login time. The other is actually to be used for recovery in case your OS dies or whatever. You can recover ecryptfs stuff using ecryptfs-recover-private in case your OS gets fucked or something. 

So my next step was obviously to move all my private goodies like accounting records into my new Private folder. And after that, I obviously wanted to protect myself a little by shredding the files that I'd copied in. But there's a problem. I use ext4, which to my understanding is a journaling filesystem. This means that writes arent all done immediately. However, you can flush the journal buffer with the shell command sync. The shred man page says the following goodies:

>  CAUTION: Note that shred relies on a very important assumption: that the file system over‐
>  writes data in place.  This is the traditional way to do things, but many modern file sys‐
>  tem designs do not satisfy this assumption.  The following are examples of file systems on
>  which shred is not effective, or is not guaranteed to be  effective  in  all  file  system
>  modes:
>
>  *  log-structured  or  journaled file systems, such as those supplied with AIX and Solaris (and JFS, ReiserFS, XFS, Ext3, etc.)
>
>  * file systems that write redundant data and carry on even if some writes  fail,  such  as RAID-based file systems
>
>  * file systems that make snapshots, such as Network Appliance's NFS server
>
>  * file systems that cache in temporary locations, such as NFS version 3 clients
>
>  * compressed file systems
>
>  In  the case of ext3 file systems, the above disclaimer applies (and shred is thus of lim‐
>  ited effectiveness) only in data=journal mode, which journals file  data  in  addition  to
>  just  metadata.   In both the data=ordered (default) and data=writeback modes, shred works
>  as usual.  Ext3 journaling modes can be changed by adding the data=something option to the
>  mount  options  for  a particular file system in the /etc/fstab file, as documented in the
>  mount man page (man mount).


And there's a lot of internet paranoia on the same subject. However someone out there made a good point... A journaling filesystem will only journal for a little while. We can forcibly flush that using a sync. They proposed the following code which should flush the shred before deleting it. I wrapped it all up nice in a shell function.

```bash
jshred() {
        shred -v -n 1 $1
        sync
        shred -v -n 0 -z -u $1
}
```

This is going to nuke the file with random garbage before deleting it. 

I've got a lot of crap to move into my encrypted folder and I wanna get to playing games tonight, so I think that's enough for one night.
