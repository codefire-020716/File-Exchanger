import sqlite3 as database
from warehouse.file_upload.models import Upload


class PhoneBook:
    """
    Class for access data from database
    """

    def __init__(self, datafile):
        self.datafile = datafile
        # database queries
        self.select_all_contacts_query = "SELECT * FROM people"
        self.add_new_contact_query = "INSERT INTO people (`first_name`,`sec_name`, `phone`,`email`) VALUES ('%s', '%s', '%s', '%s')"
        self.select_by_id_query = "SELECT * FROM people WHERE id='%s'"
        self.select_by_like_name_query = "SELECT * FROM people WHERE first_name LIKE '%%%s%%'"
        self.delete_by_id_query = "DELETE FROM people WHERE id='%s'"

    def get_all(self):
        """
        Get all contacts from PhoneBook database
        :return: List of Contacts
        """
        contacts = []
        connect = database.connect(self.datafile)
        cursor = connect.cursor()
        try:
            cursor.execute(self.select_all_contacts_query)
            results = cursor.fetchall()
            for row in results:
                contacts.append(Contact(*row))
        except:
            print("Error: Can't get all contacts!")
        finally:
            connect.close()
        return contacts

    def add_new(self, contact):
        """
        Add new contact into database
        :param contact: instance of Contact
        """
        connect = database.connect(self.datafile)
        cursor = connect.cursor()
        try:
            cursor.execute(self.add_new_contact_query % (contact.name, contact.secname, contact.phone, contact.email))
            connect.commit()  # save changes
        except:
            print("Error: Can't create new contact!")
        finally:
            connect.close()

    def get_by_id(self, contact_id):
        """
        Get contact by 'id'
        :param contact_id: Primary key of Contact in database
        :return: Contact or Non(null) if not found
        """
        pass

    def search_by_name(self, contact_name):
        """
        Search Contacts by name (using LIKE query)
        :param contact_name: Contact name or part of name
        :return: List of Contacts or Non(null) if not found
        """
        contacts = []
        connect = database.connect(self.datafile)
        cursor = connect.cursor()
        try:
            cursor.execute(self.select_by_like_name_query % contact_name)
            results = cursor.fetchall()
            for row in results:
                contacts.append(Contact(*row))
        except:
            print("Error: Can't find contacts!")
        finally:
            connect.close()
        return contacts

    def delete_by_id(self, contact_id):
        """
        Delete Contact by 'id'
        :param contact_id: Primary key of Contact in database
        :return: bool: True for success, False otherwise.
        """
        connect = database.connect(self.datafile)
        cursor = connect.cursor()
        try:
            cursor.execute(self.delete_by_id_query % contact_id)
            connect.commit()  # save changes
        except:
            print("Error: Can't delete contact!")
        finally:
            connect.close()
