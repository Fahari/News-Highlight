import pyperclip
class User:
    '''
    Class that generates new instances of User
    '''

    user_list = []

    def __init__(self,first_name,last_name,user_name,email):
        '''
            __init__ method that helps us define properties for our objects.

            Args:
                first_name: New user first name.
                last_name : New user last name.
                user_name: New user user_name.
                email : New user email address.
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a user_name and returns a user that matches that user_name.

        Args:
            user_name: user_name to search for
        Returns :
            credentials of person that matches the user_name.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user_name: user_name to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False

    @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
