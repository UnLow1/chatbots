from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def trainChatbot(chatbot):
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

    # trainer.export_for_training('./export.json')


def createChatbot():
    return ChatBot('Adam Chatbot', logic_adapters=[  # 'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        # 'chatterbot.logic.LogicAdapter',
        # 'chatterbot.logic.SpecificResponseAdapter',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.UnitConversion'])


if __name__ == "__main__":
    chatbot = createChatbot()
    trainChatbot(chatbot)

    while True:
        userInput = input("message: ")
        if userInput == 'q' or userInput == 'quit' or userInput == 'quit()':
            break
        response = chatbot.get_response(userInput)
        print(response)
