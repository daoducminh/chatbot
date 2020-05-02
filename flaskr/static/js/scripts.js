function sendChat() {
    const inputElement = $('#input-chat');
    const text = inputElement.val();
    if (text) {
        inputElement.val('')
        console.log(text);
    }
}

$(document).ready(() => {
    $('#btn-chat').click(() => {
        sendChat();
    })

    $('#input-chat').keypress(function (e) {
        if (e.which == '13') {
            sendChat();
        }
    });
})
