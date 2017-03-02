Title: Hello Internet
Date: 2017-03-01 21:45
Modified: 2017-03-01 21:45
Category: misc
Tags: pelican, blogging
Slug: hello
Authors: neko.py
Summary: site dedication

I plan on using this website to focus output of projects I've identified for myself. This includes various topics including programming, reverse engineering, computer miscellany and potentially electronics, depending on which topics I choose to pursue. 

At the time of writing, I'm a software engineer at a network security company. In my free time I work on game development and occasionally help with the Discord chatbot, Bakabot.

Some upcoming plans include investigating claims that BetterDiscord steals user tokens, and an attempt to develop a Firefox plugin for ripping soundcloud content. 

Tonight I've been working mostly on configuring my pelican theme. At time of writing, I'm using the eevee theme, which is based on Google's material design philosophy. I tend to be a fan of the google material design look and feel but I'm not sure I'm sold on how it looks for a website. It's very... colorful despite being a minimal theme. My favorite colors tend to be mute earthy things and blues, but eevee insists on using non-hex values for the theme colors. I was hoping to emulate the colors of an espeon in order to continue the pokemon thing, but [the color picker eevee recommends use of](https://getmdl.io/customize/index.html) is fairly limited. For whatever reason, pelican seems to want to use reStructured Text instead of the more common markdown by default, so many of the examples are painfully presented in rST. I expect markdown to continue to be the _lingua franca_ of rich text markup, so I'm going to stick with that. Plus it's what discord uses, and it's what Atlassian uses, and gamejolt... basically my whole life.

Regardless of the text markup, most important to me is how well it can do code blocks, of course. Let's give it a shot...

```python
print("This should be a python block") 
```

```c
printf("and a c block");
```

```cpp
std::cout << "And c++..." << std::endl;
```

Those look alright? They better or I'm going to have to move to something else.

Well, after some quick learning, seems like pelican is lying through its gnarly bird teeth about how to do syntax highlighting in markdown. It's apparently the same as it is in Discord; three backticks, the name of the language, a return, then three more backticks:

\`\`\`python

print("shit")

\`\`\`

Like this. Fortunately the [WordPress Markdown quick reference](https://en.support.wordpress.com/markdown-quick-reference/) verified for me quickly that it's not just a nuance of discord.
