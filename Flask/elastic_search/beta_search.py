from algoliasearch.search_client import SearchClient
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os

app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")

client = SearchClient.create(app_id, api_key)
index = client.init_index('hackrx')


def structure(hits):
    s = ""
    for hit in hits:
        s += "Question: "+str(hit["question"])+"\nAnswer: " + \
            str(hit["body"])+"\nLink to Blog: "+str(hit["url"])+"\n"
        s+="\n"
    return s


def send_email(ans):
    to_email = 'abhirupchakraborty0205@gmail.com'
    from_email = 'abhirupchakraborty0205@gmail.com'
    subject = 'Bajaj Finserv Hackathon - Test Email'
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email
    content = structure(ans["hits"])

    text = "Your Results as per your recent query ({}) is\n{}".format(
        ans["query"], content)
    print(text)

    message.attach(MIMEText(text, "plain"))
    # message.attach(MIMEText(bodyContent, "html"))
    msgBody = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, 'your password')
    server.sendmail(from_email, to_email, msgBody)

    server.quit()


def beta_search(query):

    ans = index.search(query)
    send_email(ans)
    print(ans)

    return ans["hits"]
