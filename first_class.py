class Point(object):
    def reset(self):
        self.x = 0
        self.y = 0

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 6


print(p1.x)
print(p1.y)

# p1.reset()
#
# print(p1.x)
# print(p1.y)

Point.reset(p1)


class SecretString(object):
    '''
    A not-at-all secure way to store a secret string.
    '''

    def __init__(self,plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase


    def decrypt(self,pass_phrasse):
        '''
        Only show the string if the pass_phrase is correct
        '''
        if pass_phrasse == self.__pass_phrase:
            return self.__pass_phrase
        else:
            return ""



secret_string = SecretString("acm","good")
print(secret_string.decrypt("good"))
print(secret_string._SecretString__plain_string)



class ContactList(list):
    def search(self,name):
        matching_contacts = []
        print(self)
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts



class Contact:
    all_contacts = ContactList()

    def __init__(self,name,email):
        # print(self)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contact):
    def __init__(self,name,email,phone):
        super().__init__(name,email)
        self.phone = phone



# c1 = Contact("A","123")
# c2 = Contact("B","23")
#
# print(Contact.all_contacts)
#
# print(isinstance(secret_string,SecretString))


f = Friend("geuan","haha",12)
print(f.__dict__)









