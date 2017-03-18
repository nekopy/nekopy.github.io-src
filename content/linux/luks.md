Title: LUKS vs eCryptfs
Date: 2017-03-15 20:59:40
Modified: 2017-03-15 20:59:40
Category: linux
Tags: ecryptfs, luks, linux, encryption, security, privacy
Slug: luks
Authors: neko.py
Summary: To round off my research from last week, I'm making a quick comparison between eCryptfs and LUKS. I present a quick introduction to LUKS, compare and contrast with eCryptfs and discuss their relative strengths.

Last week, I talked about setting up eCryptfs. I've been happily running it since. However, some of the major disadvantages of the system cropped up very quickly. The major issue I had was that even with eCryptfs I still had some more private documents that I didn't feel comfortable having decrypted whenever I'm logged into the laptop. 

Instead, I grabbed my large external harddrive and made a standard encrypted partion. I selected LUKS + ext4.  The major difference between LUKS and eCryptfs is that eCryptfs files are encrypted on their own, whereas LUKS crypto is applied to the entire partition. This is good and bad. eCryptfs likens themselves to PGP in this way, since the files have everything they need to be decrypted separately. So apparently you could migrate files from one machine to the other without them needing to be encrypted for transport.

Creating the encrypted partition was dead simple. The GNOME disk utility got me all set up making the partition. Then I just followed the long, slow process of migrating files. However, USB 3.0 made things move pretty quickly...

Now, I can access the disk only when I want to, decrypting it when I need it rather than all the time.

My next major interest was identifying how the cipher strength of default LUKS compares with default eCryptfs. So I went off to investigate how to figure out what kind of crypto was being used by each.

I used some fairly different commands for each. First, let's look at LUKS. Obviously, first make sure you've decrypted your disk.

```bash
lsblk -f
```

This is going to give you information about the block devices on the system. Importantly, it'll give you the ID of the LUKS partition. We need this in order to query cryptsetup for information about LUKS.

```bash
cryptsetup status <id>
```

From this, I'm able to see that my LUKS partition is using AES with a 256-bit key size. That's pretty good. It's FIPS 140-2 compliant, which is pretty good if you trust the NSA. Now how about eCryptfs?

```bash
mount
```

This shows us all the info we need. Much less work... We can see from the mount attributes that we're also using AES. And the key size is 16 _bytes_, or 128 bits. So that's AES 128. Not too shabby, but could be better. Initially I misread the keysize as 16 _bits_ and I was kind of terrified for a moment. 

So, you get better encryption with LUKS, _and_ better performance, I believe. When I was moving my stuff into my eCryptfs folder it brought the entire system to a crawl. And since it's going on in the kernel, I couldnt even set a nice value or tune it or anything. Yuck. However I didnt have that issue when moving files to LUKS for some reason, despite it needing to still encrypt the data on the fly. 

So personally, I now have two levels of secure storage. First, there's the eCryptfs mount on my laptop I use for normal stuff. For more sensitive content that I can afford to have off-box, I use LUKS. 
