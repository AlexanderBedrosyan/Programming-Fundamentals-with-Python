import re


class Emails:

    def final_result(self):
        while True:
            command = input()
            if not command:
                break

            pattern = r'\b([w]{3})(\.[A-Za-z0-9\-]+)(\.[a-z]+){1,}\b'
            matches = re.finditer(pattern, command)
            for ch in matches:
                print(ch.group())


emails = Emails()
emails.final_result()
