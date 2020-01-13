const submitButtonQA = document.getElementById('submitButtonQA');
const chatbotInputQA = document.getElementById('chatbotInputQA');
const chatbotOutputQA = document.getElementById('chatbotOutputQA');
const submitButtonAI = document.getElementById('submitButtonAI');
const chatbotInputAI = document.getElementById('chatbotInputAI');
const chatbotOutputAI = document.getElementById('chatbotOutputAI');

submitButtonQA.onclick = userSubmitQAEventHandler;
chatbotInputQA.onkeyup = userSubmitQAEventHandler;
submitButtonAI.onclick = userSubmitAIEventHandler;
chatbotInputAI.onkeyup = userSubmitAIEventHandler;

function userSubmitQAEventHandler(event) {
    if (
        (event.keyCode && event.keyCode === 13) ||
        event.type === 'click'
    ) {
        chatbotOutputQA.innerText = 'thinking...';
        askQAChatBot(chatbotInputQA.value);
    }
}

function userSubmitAIEventHandler(event) {
    if (
        (event.keyCode && event.keyCode === 13) ||
        event.type === 'click'
    ) {
        askAIChatBot(chatbotInputAI.value);
    }
}

function askQAChatBot(userInput) {
    const myRequest = new Request('/', {
        method: 'POST',
        body: userInput
    });

    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('HTTP error, status = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        chatbotInputQA.value = '';
        chatbotOutputQA.innerText = text;
    }).catch((err) => {
        console.error(err);
    });
}

function askAIChatBot(userInput) {
    const myRequest = new Request('/', {
        method: 'PATCH',
        body: userInput
    });

    fetch(myRequest).then(function(response) {
        if (!response.ok) {
            throw new Error('HTTP error, status = ' + response.status);
        } else {
            return response.text();
        }
    }).then(function(text) {
        chatbotInputAI.value = '';
        chatbotOutputAI.innerText = text;
    }).catch((err) => {
        console.error(err);
    });
}