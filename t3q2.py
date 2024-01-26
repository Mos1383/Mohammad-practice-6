def format_text(input_text):
    # Remove # after @
    input_text = input_text.replace('#@', '@')
    
    # Remove extra spaces
    input_text = ' '.join(input_text.split())
    
    # Remove "n\" and move the rest of the text to the next line
    input_text = input_text.replace('\\n', '\n')
    
    # Print the formatted text
    print("Formatted Text:", input_text)

# Example input
input_text = input()

# Call the function with the example input
format_text(input_text)
