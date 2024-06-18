# your code goes here!
import re
class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses=email_addresses

    def parse(self):
        pattern=r'[a-z]+\.?[a-z]+@[a-z]+\.com'
        emailRegex=re.compile(pattern)
        return sorted(emailRegex.findall(self.email_addresses))
