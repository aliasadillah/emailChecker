import easyimap as e
import smtplib
email = "testemailfor.ali1@gmail.com"
password = "test1234."
server = e.connect("imap.gmail.com",email,password)
for i in range (len(server.listids())):
    mail = server.mail(server.listids()[i])
    body = mail.body
    conts = list(body.split(" "))
conts2 = []

for j in range (len(conts)):
    conts2.append(conts[j].lower())

for k in range (len(conts2)):
    if conts2[j] == "google":
        print("hi")
    


##import imaplib
##mail = imaplib.IMAP4_SSL('imap.gmail.com')
##mail.login('testemailfor.ali1@gmail.com', 'test1234.')
##mail.list()
### Out: list of "folders" aka labels in gmail.
##mail.select("inbox") # connect to inbox.
##result, data = mail.search(None, "ALL")
##
##ids = data[0] # data is a list.
##id_list = ids.split() # ids is a space separated string
##latest_email_id = id_list[-1] # get the latest
##
### fetch the email body (RFC822) for the given ID
##result, data = mail.fetch(latest_email_id, "(RFC822)") 
##
##raw_email = data[0][1] # here's the body, which is raw text of the whole email
### including headers and alternate payloads
