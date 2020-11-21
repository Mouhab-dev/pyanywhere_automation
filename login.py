from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
import smtplib
from email.message import EmailMessage

# Function to send_email_alert
def email_alert(subject, body, to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user="email address to send a message from"
    msg['from'] = user
    password="the password for the above email address"

    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless") # you have to ask pythonanywhere stuff to enable this option for your account first
chrome_options.add_argument("--disable-gpu")
drvr = webdriver.Chrome(options=chrome_options)

to_email = "enter here the email which you will receive the notifications from the script"

# Get the url
drvr.get('https://www.pythonanywhere.com/login/')

# Login
username = drvr.find_element_by_id("id_auth-username")
username.send_keys("enter your username here")
password = drvr.find_element_by_id("id_auth-password")
password.send_keys("enter your password for the username above here")
password.send_keys(Keys.RETURN)

print("Logging in...")

# Click webapps tab.
try:
    weblink = WebDriverWait(drvr, 5).until(
        EC.presence_of_element_located((By.ID, "id_web_app_link"))
    )
    weblink.click()
    print("Web Tab Clicked...")
except:
    print("Problem clicking Web Tab...")
    email_alert("Pythonanywhere Task Error: Web tab", "Alert:\nPythonanywhere Task has failed to click Web tab!", to_email)
    drvr.quit()

# Click reset Button
try:
    reset_btn = WebDriverWait(drvr, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/div/div[6]/div/div/div/form/input[2]'))
    )
    reset_btn.click()
    print("Reset Button Clicked...")
except:
    print("Problem clicking Reset Button...")
    email_alert("Pythonanywhere Task Error: Reset Button", "Alert:\nPythonanywhere Task has failed to click Reset Button!", to_email)
    drvr.quit()

# Click tasks tab.
try:
    weblink = WebDriverWait(drvr, 5).until(
        EC.presence_of_element_located((By.ID, "id_tasks_link"))
    )
    weblink.click()
    print("Tasks Tab Clicked...")
except:
    print("Problem clicking Tasks Tab...")
    email_alert("Pythonanywhere Task Error: Tasks tab", "Alert:\nPythonanywhere Task has failed to click Tasks tab!", to_email)
    drvr.quit()

# Click Extend expiry Button for tasks
try:
    reset_btn = WebDriverWait(drvr, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="id_scheduled_tasks_table"]/div/div/table/tbody/tr/td[5]/button[4]'))
    )
    reset_btn.click()
    print("Extend expiry Button Clicked...")
except:
    print("Problem clicking Extend expiry Button...")
    email_alert("Pythonanywhere Task Error: Extend expiry Button", "Alert:\nPythonanywhere Task has failed to click \"Extend expiry\" button!", to_email)
    drvr.quit()

# Click Logout Button
try:
    logout = WebDriverWait(drvr, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/nav[1]/div/ul/li[6]/form/button"))
    )
    logout.click()
    print("Logout Button Clicked...")
except:
    print("Problem Logging out...")
    email_alert("Pythonanywhere Task Error: Logout", "Alert:\nPythonanywhere Task has failed to log out!", to_email)
    drvr.quit()

# Close the web browser
drvr.quit()

# Send an email after successful execution
email_alert("Pythonanywhere Task Completed Successfully", "Pythonanywhere Task has been completed successfully.", to_email)

# Exit Successfully
# exit(0)
