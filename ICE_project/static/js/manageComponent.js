function addTextBox(){
    var newTextBox ='<textarea name="componentTextBox" id="componentContent"></textarea>';
    $('#componentContentBox').append(newTextBox);
}

function addImg(){
    var imginput = '<div id="imageInputDiv"> \
    <label for="imgInput">Insert Images</label>\
    <input name="pageNum" id="imgInput" type="file" onchange=showImg()></image>\
    </div>\
    '
    $('#componentContentBox').append(imginput);
}

function addd()



// <div class="newModuleDiv">
//     <label for = "moduleInputBox">component title:</label>
//     <input type = "text" name="title" id="moduleInputBox"/>
//     <div id="moduleBtn">
//             <form action = '/templates/manageComponents.html' method="POST">
//                 {% csrf_token %}
//                 <input type="text" value="{{ m.pk }}" hidden=true name=k />
//                 <input type="text" value="{{ m.component_title }}" hidden=true, name=title />
//                 <input id="componentsubmit" type="submit" value="View" />
//             </form>   
        
//     </div>
// </div>