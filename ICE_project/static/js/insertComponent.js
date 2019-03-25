function addTextBox(){
    var newTextBox ='<textarea id="componentContent"></textarea>';
    $('#componentContentBox').append(newTextBox);
}

function addImg(){
    var imginput = '<div id="imageInputDiv"> \
    <label for="imgInput">Insert Images</label>\
    <input id="imgInput" type="file" onchange=showImg(this)></image>\
    <img id="uploadedImg" /> \
    </div>\
    '
    $('#componentContentBox').append(imginput);
}

function showImg(input){
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#uploadedImg')
                .attr('src', e.target.result);
        };

        reader.readAsDataURL(input.files[0]);
    }
}