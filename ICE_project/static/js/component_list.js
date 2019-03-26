function addd(){
    var type = document.getElementById('kind').value
    var newModule = undefined
    console.log('abb');
    if (type == 'text'){
        newModule = ' \
            <div class="newModuleDiv"> \
                <label type="text" name="type" value="text"> \
                <label for = "componentInputBox">component number:</label> \
                <input name="number" id="componentInputBox"></input> \
                <label for = "titleInputBox">Title:</label> \
                <input name= "title" id="titleInputBox"></input> \
                <textarea name="componentTextBox" id="componentContent"></textarea> \
            </div> \
        ';
    }else if (type == "image"){
        newModule = ' \
            <div class="newModuleDiv"> \
                <label type="text" name="type" value="image"> \
                <label for = "componentInputBox">component number:</label> \
                <input name="number" id="componentInputBox"></input> \
                <label for = "titleInputBox">Title:</label> \
                <input name= "title" id="titleInputBox"></input> \
            </div> \
        ';
    }
        
    $('#componentContentBox').append(newModule);
}

// function addTextBox(){
//     var newTextBox ='<textarea name="componentTextBox" id="componentContent"></textarea>';
//     $('#componentContentBox').append(newTextBox);
// }

// function addImg(){
//     var imginput = '<div id="imageInputDiv"> \
//     <label for="imgInput">Insert Images</label>\
//     <input name="pageNum" id="imgInput" type="file" onchange=showImg()></image>\
//     </div>\
//     '
//     $('#componentContentBox').append(imginput);
// }