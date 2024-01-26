def format_text(input_text):
    input_text = input_text.replace('#@', '@')
    
    input_text = ' '.join(input_text.split())
    
    input_text = input_text.replace('\\n', '\n')
    
    print("Formatted Text:", input_text)
input_text = input()
format_text(input_text)
