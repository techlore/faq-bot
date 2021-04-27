<div align="center">
<h1>Techlore FAQ Bot</h1>
<p>
	<em>An FAQ Bot for Techlore's Discord and Matrix Channels.</em>
</p>
<p>
<a href="https://github.com/techlore/faq-bot/pulls">
	<img src="https://img.shields.io/github/issues-pr/techlore/faq-bot?style=for-the-badge">
</a>
<a href="https://discord.gg/Xd7baMSpqS">
	<img src="https://img.shields.io/discord/422332274323750922?label=Discord&logo=discord&logoColor=white&style=for-the-badge">
</a>
<a href="https://matrix.to/#/+techlore-official:matrix.org">
	<img src="https://img.shields.io/matrix/techlore:matrix.org?label=Matrix&logo=matrix&server_fqdn=matrix.org&style=for-the-badge">
</a>
</p>
</div>

## About this bot

This bot was originally conceived by (community member and moderator) [FantasyCookie17](https://artemislena.eu) as a way to quickly answer common questions asked in our online communities. This is a community project, with answers ideally representing the consensus of the community. Thus, pull requests are very welcome. Questions and answers can be added to [`faq.json`](/faq.json).

This bot is a fork of [@fire219/pine-faq-bot](https://github.com/fire219/pine-faq-bot), and below you will find the original documentation, with slight modifications to fit this custom fork:

## A simple question-response Matrix bot, built on matrix-nio API

Built out of necessity, this easy to use and manage Matrix bot will give recorded responses from its JSON file.

**Example:**

    Random User: !faq pbpOS
    Pine64 FAQ Bot: [FAQbot] Which OS you should run depends on what you prefer. Well supported options are Debian (default on all PBPs), Ubuntu, and Manjaro.

### Requirements:
- Python 3.5+ (uses async/await syntax)
- matrix-nio library (`pip install matrix-nio`)
- curl (urllib no longer needed though)
- A user account on a Matrix homeserver

### Setup:
After downloading the bot files, create a new file named `login.json`.
Create the following structure in the file and fill in the relevant blanks:

    {"homeserver": "<homeserver URL>", "username": "<@botuser:matrix.org>", "password": "<examplepassword>", "botadmin": "<@you:matrix.org>"}

After saving this file, the bot is ready to use. As downloaded, your bot will have the latest version of the Techlore room FAQ file within `faq.json`. However, it can easily be edited to fit your needs.

### Special commands:
Most !faq commands will simply be looked up within the FAQ listings. However, a few commands are reserved:

 Command| Description
--|--
 !faq shutdown | Shuts down the bot. Can only be triggered by `botadmin`, else gives default FAQ error.
 !faq update | `git pull`s in the current directory. This both updates the FAQ file and, if you shut it down subsequently, allows you to run the latest version of the source code.
 !faq | Gives an index listing of all currently loaded FAQ queries.

### License:

    Copyright (c) 2019 Matthew Petry (fireTwoOneNine/fire219)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
