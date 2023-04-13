# Create class Email. The __init__ method should receive sender, receiver and a content.
# It should also have a default set to False attribute called is_sent. The class should have two additional methods:
# •	send() - sets the is_sent attribute to True
# •	get_info() - returns the following string: "{sender} says to {receiver}: {content}. Sent: {is_sent}"
# You will receive some information (separated by a single space) until you receive the command "Stop".
# The first element will be the sender, the second one – the receiver, and the third one – the content.
# On the final line, you will be given the indices of the sent emails separated by comma and space ", ".
# Call the send() method for the given indices of emails. For each email, call the get_info() method.
# Input
# Peter John Hi,John
# John Peter Hi,Peter!
# Katy Lilly Hello,Lilly
# Stop
# 0, 2
# Output
# Peter says to John: Hi,John. Sent: True
# John says to Peter: Hi,Peter!. Sent: False
# Katy says to Lilly: Hello,Lilly. Sent: True
# Input
# Anna, Bella, Hi
# Sam, Dany, Okey
# Felix, Mery, Bye
# Stop
# 0
# Output
# Anna, says to Bella,: Hi. Sent: True
# Sam, says to Dany,: Okey. Sent: False
# Felix, says to Mery,: Bye. Sent: False
class Email:

    def __init__(self, sender, receiver, content, is_send = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_send

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
while True:
    line = input()
    if line == "Stop":
        break
    needed = line.split(" ")
    email = Email(needed[0], needed[1], needed[-1])
    emails.append(email)
sent = list(map(int, input().split(", ")))
for x in sent:
    emails[x].send()
for email in emails:
    print(email.get_info())