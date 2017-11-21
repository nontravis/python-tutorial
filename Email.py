import smtplib      # simple mail transfer protocol library

#┌─────────────────────┐
#│ NOTE: Sending email │
#└─────────────────────┘
conn = smtplib.SMTP("smtp.gmail.com", 587)
conn.ehlo()         # connect to server
conn.starttls()     # start connect with TLS encryption
conn.login("asweigart@gmail.com", "lxkjfvcrlxxiinmj")

conn.sendmail(
    "from@gmail.com",
    "to@gmail.com",
    # first \n = end the subject, second \n = done with the headers
    "Subject: Subject test\n\nDear Al,\nSo long, and thanks for all the fish.\n")
# if result is empty = success
conn.quit()

# NOTE: Email providers
# - Gmail                       smtp.gmail.com
# - Outlook.com/hotmail.com     smtp-mail.outlook.com
# - Yahoo mail                  smtp.mail.yahoo.com
# - AT&T                        smtp.mail.att.net (port 465)
# - Comcast                     smtp.comcast.net
# - Verizon                     smtp.verizon.net (port 465)


#┌──────────────────────┐
#│ NOTE: Checking email │
#└──────────────────────┘
# IMAP: Internet Message Access Protocol
import imapclient
conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login("test@gmail.com", "password")
conn.list_folders()
conn.select_folder("INBOX", readonly=True)      # more safe to delete you email
UIDs = conn.search(["SINCE 20-Aug-2015"])       # with IMAP syntax
raw_message = conn.fetch([47474], ["BODY[]", "FLAGS"])

import pyzmail
message = pyzmail.PyzMessage.factory(raw_message[47474][b'BODY[]'])
message.get_subject()
message.get_addresses("from")
message.get_addresses("to")
message.get_addresses("bcc")
message.text_part
message.text_part.get_payload().decode("UTF-8")
message.html_part

conn.logout()


#┌────────────────────┐
#│ NOTE: Delete email │
#└────────────────────┘
conn.select_folder("INBOX", readonly=False)
UIDs = conn.search(["ON 24-Aug-2015"])
conn.delete_messages([47474])
