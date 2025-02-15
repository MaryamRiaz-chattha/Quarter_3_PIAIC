from meta_ai_api import MetaAI
openAi=MetaAI()
place=input("Enter the place (city with country):")
instruction=f'''
you are in  custom weather bit.You need to provide the weather infromation of given place
in proper format
 - the given place is {place}
if user input something else then you have  to tell us that you are a weather chatbot and you cna only provide weather infromation
'''
response=openAi.prompt(instruction)
print(response["message"])