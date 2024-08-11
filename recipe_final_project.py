from openai import OpenAI
client = OpenAI(
    api_key = "sk-1rdSiULSPo3eCLa3F54BNJB0JSUvEqUg4IKDQP7xWtT3BlbkFJKzYdeDrwEBLjWnMVu30yoxdcRSyUFtDWgkAc97CIoA"
)
type = int(input("Would you like to find out what you can make with available ingredients (click 1) or find a recipe for a delious dish (click 2)? "))
if type == 1:
    allergy = input("\nAre you allergic or restriced to anything? If so type in the items or say no. ")
    ing_num = int(input("How many ingredients would you like to enter? "))
    print("Please enter your ingredients: ")
    if allergy == "no":
        list_of_words = []
        string_of_words = " "
        stop = False
        while stop == False:
            for x in range(ing_num):
                get_input = input("Ingredient # " + str(x+1) + ": ")
                list_of_words.append(get_input)
            print("Loading...")
            system_data = [
                {"role": "system", "content": "Generate a detailed recipe from around the world that includes the words"},
                {"role": "user", "content": string_of_words.join(list_of_words)}
            ]
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = system_data
            )
            assistant_response = response.choices[0].message.content
            system_data.append({"role": "assistant", "content": assistant_response})
            print("Assistant: " + assistant_response)
            another = input("\nYou can do this! If you would like to see another recipe click a or say no: ")
            if another == "a":
                print("Okay!")
                stop = False
            elif another == "no":
                print("Enjoy!")
                stop = True
    else: 
        list_of_words = []
        string_of_words = " "
        stop = False
        while stop == False:
            for x in range(ing_num):
                get_input = input("Ingredient # " + str(x+1) + ": ")
                list_of_words.append(get_input)
            print("Loading...")
            system_data = [
                {"role": "system", "content": f"Generate a detailed recipe from around the world that includes the words, without {allergy}"},
                {"role": "user", "content": string_of_words.join(list_of_words)}
            ]
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = system_data
            )
            assistant_response = response.choices[0].message.content
            system_data.append({"role": "assistant", "content": assistant_response})
            print("Assistant: " + assistant_response)
            another = input("\nYou can do this! If you would like to see another recipe click a or say no: ")
            if another == "a":
                print("Okay!")
                stop = False
            elif another == "no":
                print("Enjoy!")
                stop = True
elif type == 2:
    allergy = input("\nAre you allergic or restriced to anything? If so type in the items or say no. ")
    print("Please enter what you would like to make: ")
    if allergy == "no":
        list_of_words = []
        string_of_words = " "
        stop = False
        while stop == False:
            get_input = input("Dish: ")
            list_of_words.append(get_input)
            print("Loading...")
            system_data = [
                {"role": "system", "content": "Generate a recipe for the word."},
                {"role": "user", "content": string_of_words.join(list_of_words)}
            ]
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = system_data
            )
            assistant_response = response.choices[0].message.content
            system_data.append({"role": "assistant", "content": assistant_response})
            print("Assistant: " + assistant_response)
            another = input("\nYou can do this! If you would like to see another recipe click a or say no: ")
            if another == "a":
                print("Okay!")
                stop = False
            elif another == "no":
                print("Enjoy!")
                stop = True
    else:
        list_of_words = []
        string_of_words = " "
        stop = False
        while stop == False:
            get_input = input("Dish: ")
            list_of_words.append(get_input)
            print("Loading...")
            system_data = [
                {"role": "system", "content": f"Generate a recipe for the word without {allergy}."},
                {"role": "user", "content": string_of_words.join(list_of_words)}
            ]
            response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = system_data
            )
            assistant_response = response.choices[0].message.content
            system_data.append({"role": "assistant", "content": assistant_response})
            print("Assistant: " + assistant_response)
            another = input("\nYou can do this! If you would like to see another recipe click a or say no: ")
            if another == "a":
                print("Okay!")
                stop = False
            elif another == "no":
                print("Enjoy!")
                stop = True

    
