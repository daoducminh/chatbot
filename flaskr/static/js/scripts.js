const CHAT_ROW = `<li class="left clearfix">
<span class="chat-img pull-left">
    <img src="/static/images/{0}-icon.png" alt="Avatar" class="img-circle" />
</span>
<div class="chat-body clearfix">
    <div class="header">
        <strong class="primary-font">{1}</strong>
    </div>
    <p>{2}</p>
</div>
</li>`;

function scrollToBottom(element) {
    $(element).stop().animate({ scrollTop: $(element)[0].scrollHeight }, 1000);
}

function format(str, ...args) {
    for (i = 0; i < args.length; i++)
        str = str.replace("{" + i + "}", args[i]);
    return str;
}

function addUserChatRow(text) {
    $('#chatbox').append(format(CHAT_ROW, 'customer', 'Customer', text));
}

function addBotChatRow(text) {
    $('#chatbox').append(format(CHAT_ROW, 'bot', 'Bot', text));
}

function handleChat() {
    const inputElement = $('#input-chat');
    const text = inputElement.val();
    if (text) {
        inputElement.val('');
        addUserChatRow(text);
        scrollToBottom('.panel-body')

        $.ajax({
            type: 'POST',
            url: 'bot',
            data: JSON.stringify({ 'text': text }),
            contentType: 'application/json',
            success: (data) => {
                addBotChatRow(data);
                scrollToBottom('.panel-body')
            }
        })
    }
}

$(document).ready(() => {
    $('#btn-chat').click(() => {
        handleChat();
    })

    $('#input-chat').keypress(function (e) {
        if (e.which == '13') {
            handleChat();
        }
    });
})
