def main():
  conda activate my_environment_name
  first_book = input("Enter the name of a book you own: ")
  second_book = input("Enter the name of another book you own (or press 'Enter' to skip): ")

  library = []
  library.append(first_book)

  if second_book:
      library.append(second_book)

  print(f"\nYour library: {library}\n")

  wish_book = input('Enter the name of a book you wish to have in the future: ')
  another_wish = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")

  wish_list = []
  wish_list.append(wish_book)

  if another_wish:
      wish_list.append(another_wish)
      print(f"\nYour Wishlist: {wish_list}\n")

      acquired_book = input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ").lower()

      if acquired_book:
          library.append(acquired_book)
          wish_list.remove(acquired_book)
          print(f"\nUpdated Library {library}")
          print(f"Updated Wishlist {wish_list}\n")

          donate = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")

          if donate:
              library.remove(donate)
              print(f"\nFinal library after Donations: {library}\n")
          else:
              print("Thank you for using the program")
      else:
          print("Thank you for using the program")
  else:
      print("Thank you for using the program")
  return

if __name__ == "__main__":
  main()
