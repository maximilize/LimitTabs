#Limit Tabs for Sublime Text

Ever get to the end (middle?) of a day of coding only to find your window littered with tabs that are nearly impossible to search through visually? Find yourself rage-quitting all your tabs in disgust and starting over? No? Just me? Ok.

With this plugin, a simple keystroke `ctrl + alt + w` will close all tabs, the oldest first, whose file has not been modified in the last 30 minutes (to change this interval, see Preferences > Packages > LimitTabs > Settings). It will keep 10 tabs open (also changeable in settings) and will only close tabs in the background – so files that are open and active in your window won't be closed. Likewise, it will not close files with unsaved changes.

You can change the key binding in Preferences > Package Settings > LimitTabs > Key Bindings.

##Run automatically

You can also configure the plugin to automatically close old tabs each time you save a file. To enable this, go to Preferences > Package Settings > LimitTabs > Settings and set `limittabs_run_on_post_save` to `true`:

~~~js
// Automatically run after a file is saved
"limittabs_run_on_post_save": true,
~~~

##Threshold

Another configuration option is the **threshold**. Setting this to 0 disables this plugin, a number greater than 0 will keep always at least this amount of tabs open

~~~js
// If this is set and greater than 0, LimitTabs will only run if
// the number of tabs is greater than the threshold setting.
"limittabs_threshold": 12,
~~~

##Keep open minimum files

The setting variable **keep_open** lets you choose a number of tabs that will always kept open

~~~js
// Keep this amount of tabs open. Tabs are closed by last access time
// or last modified time, whatever is higher
"limittabs_threshold": 10
~~~

##Installation with Package Manager (Recommended)

The easiest way to install is via the excellent [Sublime Package Manager](https://sublime.wbond.net/installation). Once Package Manager is installed, bring up the commands menu (`Command + Shift + P` on Mac, `Control + Shift + P` on Windows or Linux), then type "Package Control" to filter the commands list. Select the "Package Control: Install Package" command, then find and install the LimitTabs plugin.

##Installation without Package Manager
Clone or download this repo to your **Packages** folder.

##Fork
This is a fork of the [TidyTabs-Sublime](https://github.com/bradleyboy/TidyTabs-Sublime/) plugin.

##License
Licensed under the MIT license.

Copyright (c) Brad Daily

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
