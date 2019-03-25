function addTextBox(){
    var newTextBox ='<textarea id="componentContent"></textarea>';
    $('#componentContentBox').append(newTextBox);
}

function addImg(){
    var imginput = '<div id="imageInputDiv"> \
    <label for="imgInput">Insert Images</label>\
    <input id="imgInput" type="file" onchange=showImg()></image>\
    </div>\
    '
    $('#componentContentBox').append(imginput);
}

function showImg(){
    
}