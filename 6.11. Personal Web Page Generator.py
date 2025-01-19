# 6.11. Personal Web Page Generator
# Write a program that asks the user for their name, then asks the user to enter a sentence
# that describes themself. Here is an example of the program’s screen:

# Enter your name: Tara Guzina [Enter]
# Describe yourself: I am a computer science major, a member of the
# Jazz club, and I hope to work as a mobile app developer after I
# graduate. [Enter]


#   Once the user has entered the requested input, the program should create an HTML file,
#   containing the input, for a simple Web page. Here is an example of the HTML content,
#   using the sample input previously shown:


# <html>
# <head>
# </head>
# <body>
#   <center>
#     <h1>Tara Guzina</h1>
#   </center>
#   <hr />
#   I am a computer science major, a member of the Jazz club,
#   and I hope to work as a mobile app developer after I graduate.
#   <hr />
# </body>
# </html>

# To test your program, enter any fake information you wish.

def create_personal_web_page():
    # Get user input
    name = input("Enter your name: ")
    description = input("Describe yourself: ")

    # HTML content
    html_content = f"""<html>
<head>
</head>
<body>
  <center>
    <h1>{name}</h1>
  </center>
  <hr />
  {description}
  <hr />
</body>
</html>"""

    # Specify the output file name
    filename = "D:/Dong Kim/CCC/2024/20242Fall/Python/personal_web_page.html"

    # Write the HTML content to a file
    try:
        with open(filename, 'w') as file:
            file.write(html_content)
        print(f"\nYour personal web page has been created as '{filename}'.")
    except IOError as e:
        print(f"An error occurred while creating the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
create_personal_web_page()
