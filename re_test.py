import re

route = '''
        30.16.4.0/23     *[static/5] 89w4d 02:42:02, tag 903
                         > to 192.168.0.125 via reth1.903
        30.16.76.0/23     *[static/5] 89w4d 02:42:02, tag 903
                         > to 192.168.0.125 via reth1.903
        30.16.186.0/23     *[static/5] 89w4d 02:42:02, tag 903
                         > to 192.168.0.125 via reth1.903
        '''

pattern = re.compile(r"\d+.*[^a-z]\/\d+")
print pattern.findall(route)
