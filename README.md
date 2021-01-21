# Techlore FAQ Bot

## An FAQ bot for the [Techlore Matrix room](https://matrix.to/)

[Techlore](https://techlore.tech) is a channel on different video platforms, as well as a community on privacy and security. This bot is used for quickly answering common questions. While I (FantasyCookie17) happen to host this repo, this is a community project. The bot ideally represents the consensus of the community, thus pull requests are very welcome.

Below you will find the original documentation by fireTwoOneNine, with slight modifications to fit this custom fork:

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
 !faq index | Gives an index listing of all currently loaded FAQ queries. 

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



