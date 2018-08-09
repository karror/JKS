
$("#button").mousedown(function(){
    $.post(link,
        {
            'mailaddress': document.getElementById('email').value,
            'objname': name,
            'csrfmiddlewaretoken': csrf
        },
    )
});
