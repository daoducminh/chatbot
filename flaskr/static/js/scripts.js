const CHAT_ROW = `<li class="left clearfix">
<span class="chat-img pull-left">
    <img src="/static/images/{0}-icon.png" alt="Avatar" class="img-circle" />
</span>
<div class="chat-body clearfix">
    <div class="header">
        <strong class="primary-font">{1}</strong>
    </div>
    <div>{2}</div>
</div>
</li>`;
const TABLE_ITEMS = `<div id="result-box"><table class="table table-bordered table-striped">
<thead><tr>
<th>Tên sản phẩm</th>
<th>Hãng</th>
<th>Loại</th>
<th>Màu sắc</th>
<th>Cỡ</th>
</tr></thead>
<tbody>{0}</tbody>
</table></div>`;
const ITEM_ROW = `<tr>
<td>{0}</td>
<td>{1}</td>
<td>{2}</td>
<td>{3}</td>
<td>{4}</td>
</tr>`;

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
                addBotChatRow(data['text']);
                const items = data['items'];
                if (items) {
                    results = ''
                    for (let i = 0; i < items.length; i++) {
                        results += format(ITEM_ROW, items[i].name, items[i].brand, items[i].categories, items[i].colors, items[i].sizes)
                    }
                    addBotChatRow(format(TABLE_ITEMS, results))
                }

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

    addBotChatRow('Xin chào. Tôi có thể giúp gì được cho bạn?')
})
