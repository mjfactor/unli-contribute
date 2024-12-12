with open('README.md', 'r') as file: # the readme is our target file
    content = file.read()


content = content.replace('Dynamic Programming', '###REPLACE###').replace('Docker', 'Dynamic Programming').replace('###REPLACE###', 'Docker', 1) # You can use any word that is in your target file


with open('readme.md', 'w') as file:
    file.write(content) # This write the replaced word. 
