

# ## Juniper Café Collective

# ### Situation

# #Juniper Café Collective wants a small Python program that produces
# # a clear, readable receipt instead of handwritten totals.


# # CLIENT REQUIREMENTS

# # Your program must:

# # - -------------ask for a table number. ---------------------
# For this I create this list of available tables:

available_tables = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


products = ["Tea", "Coffee", "Sandwich", "Salad", "Fruit", "Pastry", "Soup", "Juice", "Water", "Soda"]
prices = [18.50, 24.00, 42.00, 12.75, 15.00, 20.00, 18.00, 14.00, 10.00, 16.00]

takeaway_charge = 5.00

print("\nWelcome to Juniper Café Collective!")
table_number = int(input("\nPlease enter your table number: "))


if table_number in available_tables:
    print(f"Table {table_number} is available.")
else:
    print("Invalid table number.")

# # takeaway-------------------------------------------------------------------------------------

takeaway = input("\nIs this order for takeaway? (yes/no): ").strip().lower()
if takeaway == "yes":
    print(f"\nA takeaway charge of {takeaway_charge:.2f} SEK will be added to your total.")
 
elif takeaway == "no":
    print("\nNo takeaway charge will be added to your total.")
else:
    print("\nInvalid input. Please enter 'yes' or 'no'.")


# # - ask for the client's name------------------------------------------------------------------
# # - display the client's name in uppercase

client_name = input("Please enter your name: ")
client_name_upper = client_name.upper()
print(f"\nHi and welcome, {client_name_upper}!")

# ------------------------------------------------------------------------------------------------

name = "JUNIPER MENU"

print("\nWhat would you like to order?\n")
print(f"................{name:.^8}................")
print(f"{'Product':<34}{'Price (SEK)':>12}")

for index in range(len(products)):
    product_item = f"{index + 1}. {products[index]}"
    print(f"{product_item:-<34}{prices[index]:>7.2f} SEK")
   

# # - ask for three product names----------------------------------------------------------------

product1 = input("\nEnter the name of the first product: ")
product2 = input("Enter the name of the second product: ")
product3 = input("Enter the name of the third product: ")

# # - convert the table number and prices to appropriate numeric types
products = [product1, product2, product3]

# # - ask for the price of each product
price1 = float(input(f"Enter the price of {product1}: "))
price2 = float(input(f"Enter the price of {product2}: "))
price3 = float(input(f"Enter the price of {product3}: "))


# # - calculate the subtotal of all three products
subtotal = price1 + price2 + price3
if takeaway == "yes":
    subtotal += takeaway_charge   
print (f"\nSubtotal: {subtotal:.2f} SEK")

# # - display every price with exactly two decimal places
print(f"Price of {product1}: {price1:.2f} SEK")
print(f"Price of {product2}: {price2:.2f} SEK")
print(f"Price of {product3}: {price3:.2f} SEK")

# # - align product names and prices into a readable receipt
# # - display the table number, client name and subtotal in the required format

# # IMPORTANT:

# # Do NOT manually type the subtotal.

# # The program must calculate it from the three prices.

# # ---

# # STEP 1 — UNDERSTAND THE DATA

# Before coding, determine the intended type of each value.

# Fill this in:

#     table_number -> ?
#     client_name  -> ?

#     product1     -> ?
#     price1       -> ?

#     product2     -> ?
#     price2       -> ?

#     product3     -> ?
#     price3       -> ?

#     subtotal     -> ?

# Do not choose a type merely because the input contains digits.

# Ask:

# > What does this value MEAN, and what operations must the program
# > perform with it?

# ---

# # STEP 2 — INPUT

# The official starter structure is:

#     table_number = input("Table number: ")
#     client_name = input("Client name: ")

#     product1 = input("Product 1: ")
#     price1 = input("Price 1: ")

#     product2 = input("Product 2: ")
#     price2 = input("Price 2: ")

#     product3 = input("Product 3: ")
#     price3 = input("Price 3: ")

# Do not change everything immediately.

# Think first:

# Which values need conversion?

# Where should conversion happen?

# Why?

# Implement your solution below this point in `lab03.py`.

# ---

# # STEP 3 — PROCESS THE DATA

# Your program needs to produce new information from the input.

# Think about:

# ### Client name

# You need the uppercase version.

# Which Lecture 3 string operation produces it?

# ### Prices

# You need to calculate:

#     subtotal = price1 + price2 + price3

# What must be true about the TYPES of `price1`, `price2`, and `price3`
# for this expression to perform arithmetic rather than text operations?

# ### Subtotal

# Do not hard-code it.

# It must depend on the values entered by the user.

# ---

# # STEP 4 — PRESENT THE RECEIPT

# Now separate:

#     STORED VALUE

# from:

#     DISPLAYED VALUE

# For example, a price might internally be stored as:

#     18.5

# but the receipt must PRESENT it as:

#     18.50

# Do not change the underlying value merely to make the output pretty.

# Use formatting when presenting it.

# Your receipt must make the product names and prices readable and aligned.

# Use the Lecture 3 formatting tools:

#     .2f
#     <width
#     >width
#     ^width

# Choose the appropriate formatting yourself.

# ---

# # STEP 5 — TEST

# Do not stop because the program runs once.

# ## Test 1 — Official example data

# Use:

#     Table number: 7
#     Client name: Ada Lovelace

#     Tea
#     18.5

#     Sandwich
#     42

#     Fruit
#     12.75

# Before running, calculate the expected subtotal yourself.

# Expected subtotal:

# Then run.

# Observed subtotal:

# Match? YES / NO

# ---

# ## Test 2 — Your own data

# Choose different:

# - table number
# - client
# - products
# - prices

# My test data:

#     Table:
#     Client:

#     Product 1:
#     Price 1:

#     Product 2:
#     Price 2:

#     Product 3:
#     Price 3:

# Expected subtotal:

# Observed subtotal:

# Match? YES / NO

# ---

# # STEP 6 — CODE REVIEW

# Before considering the lab complete, check:

# [ ] The program uses input().

# [ ] Table number has the appropriate numeric type.

# [ ] Prices have appropriate numeric types.

# [ ] Product names remain strings.

# [ ] Client name is displayed in uppercase.

# [ ] The subtotal is calculated, not hard-coded.

# [ ] Every price displays exactly two decimal places.

# [ ] The subtotal displays correctly.

# [ ] Product names and prices are aligned.

# [ ] The receipt is readable.

# [ ] I tested more than one set of input values.

# ---

# # FINAL EXPLANATION — NO RUNNING CODE

# When your program works, answer these from memory:

# 1. Why does input() initially give us strings?

# 2. Why must the prices be converted before calculating the subtotal?

# 3. What is the difference between:

#        price = 18.5

#    and:

#        f"{price:.2f}"

# 4. Why does formatting not change the stored value?

# 5. What is the difference between indexing and slicing?

# 6. What does this mean?

#        text[start:stop]

# 7. Why is `stop` not part of the resulting slice?

# 8. What does `text[-1]` retrieve?

# 9. What does `text[-4:]` retrieve?

# 10. Why should a numeric-looking identifier sometimes remain a string?

# ---

# # LAB 03 — COMPLETION

# I can now:

# [ ] receive user input

# [ ] reason about the type returned by input()

# [ ] convert text to numeric types when required

# [ ] use f-strings

# [ ] control decimal precision

# [ ] control field width and alignment

# [ ] use string methods

# [ ] use positive and negative indexing

# [ ] extract information using slicing

# [ ] distinguish stored values from displayed values"