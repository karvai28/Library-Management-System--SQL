import mysql.connector
from mysql.connector import Error

class LibraryManagementSystem:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',  # Change to your MySQL username
                password='root@sql12345',  # Change to your MySQL password
                database='library_management'
            )
            return connection
        except Error as e:
            print(f"Error: {e}")
            return None

    def add_book(self, title, author, published_year):
        query = "INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (title, author, published_year))
        self.connection.commit()
        print("Book added successfully.")
    
    def view_books(self):
        query = "SELECT * FROM books"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def delete_book(self, book_id):
        query = "DELETE FROM books WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (book_id,))
        self.connection.commit()
        print("Book deleted successfully.")
    
    def add_member(self, name, membership_date):
        query = "INSERT INTO members (name, membership_date) VALUES (%s, %s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (name, membership_date))
        self.connection.commit()
        print("Member added successfully.")
    
    def view_members(self):
        query = "SELECT * FROM members"
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    def delete_member(self, member_id):
        query = "DELETE FROM members WHERE id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (member_id,))
        self.connection.commit()
        print("Member deleted successfully.")

def main():
    lms = LibraryManagementSystem()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Add Member")
        print("5. View Members")
        print("6. Delete Member")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter published year: "))
            lms.add_book(title, author, year)
        elif choice == '2':
            lms.view_books()
        elif choice == '3':
            book_id = int(input("Enter book ID to delete: "))
            lms.delete_book(book_id)
        elif choice == '4':
            name = input("Enter member name: ")
            date = input("Enter membership date (YYYY-MM-DD): ")
            lms.add_member(name, date)
        elif choice == '5':
            lms.view_members()
        elif choice == '6':
            member_id = int(input("Enter member ID to delete: "))
            lms.delete_member(member_id)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
