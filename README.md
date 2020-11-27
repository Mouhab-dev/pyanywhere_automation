# Pythonanywhere Automation
This is a python script used for pythonanywhere free hosting plan if you want to extend the 3-months period automatically without logging in every time to extend it manually yourself to keep your website running on the pythonanywhere servers.

## Features

- Easy to setup and use.
- Extend Webapp period and your automated task.
- Email Notifications.
- Email Alert if the script failed while running.

## Requirements

- Selenium Library <br>
Make sure to Choose your python version, here I'm using python 3.8
```
py3.8 pip install selenium
```

## Usage
<ul>
  <li> Login to your pythonanywhere account.
  <li> Create a topic on the forums and request enabling "chrome headless" option for your account, this option is disabled by default and if it remains disabled the script will not work.
  <li> Go to Consoles Tab:
    <ul>
      <li> Create a new Bash console.
      <li> Clone my repo by typing this command in the bash terminal:
        
```
git clone https://github.com/Mouhab-dev/pyanywhere_automation.git
```
   <li> Exit from the console.
    </ul>
    <li> Go to Tasks Tab:
      <ul>
        <li> Create a new task and choose "login.py"
        <li> DO NOT FORGET to edit the script to enter your username and password and your email address after you add the script as a task.
      </ul>
</ul>
      
      
## Test
