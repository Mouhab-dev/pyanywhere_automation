# Pythonanywhere Automation
This is a python script used for pythonanywhere free hosting plan if you want to extend the 3-months period automatically without logging in every time to extend it manually yourself to keep your website running on the pythonanywhere servers.

## Features

- Easy to setup and use.
- Extend Webapp period and your automated task.
- Email Notifications.
- Email Alert if the script failed while running.

## Requirements

- Selenium Library <br>
Make sure to Choose your python version, here I'm using python 3.8:
```
py3.8 pip install selenium
```
- Gmail account for the script to use while sending emails to notify you about alerts.

## Usage
<ul>
  <li> <a href="https://www.pythonanywhere.com/login/">Login to your pythonanywhere account.</a>
  <li> Create a new topic on the forums or comment on a similar topic and request enabling "chrome headless" option for your account, this option is disabled by default and if it remains disabled the script will not work.<br>
    
Continue the next steps only after Pythonanywhere stuff enable this option for you:
  <li> Go to Consoles Tab:
    <ul>
      <li> Create a new Bash console.
        <li> install Selenium library if you don't have it.
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
      
      
## Notice

All of your sensetive informations will be hardcoded in the script as plaintext also your gmail password if you turned "less secure apps" option on for the gmail account the script will be using.

To solve this problem you have 2 options:
<ol>
  <li> You can solve gmail password issue by using the 2FA Method on your gmail account and use app passwords instead of your actual gmail password, but this do not solve pythonanywhere's problem.
  <li> You can hide all your sensitive informations by using "Environment variables" method but it is kind of masking the password and not completely securing it.
</ol>

Over all you should consider the free-tier as an expirmental hosting plan and not an actual real hosting service, and should be considered just only if you want to show your skills and web development experience, for the gmail account it should be a new one used for this purpose only or similar unsensitive uses.
