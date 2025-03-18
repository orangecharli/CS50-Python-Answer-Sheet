"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

"""

def main():
    x = question()
    evaluation(x)

#ask user for input and convert to string
def question():
    user_answer = input("What is the answer to the great question of life, the universe and everything?")
    user_answer = user_answer.lower().strip()
    return user_answer

#conditional statement
def evaluation(answer):
    if answer in ('42', 'forty-two', 'forty two'):
        print("Yes")
    else:
        print("No")
main()
