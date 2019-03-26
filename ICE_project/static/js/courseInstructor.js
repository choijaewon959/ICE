var num_module = 0;

function addModule(){
    var newModule = ' \
        <div class="newModuleDiv"> \
            <label for = "moduleInputBox">module number:</label> \
            <input name="number" id="moduleInputBox"></input> \
            <label for = "titleInputBox">Title:</label> \
            <input name= "title" id="titleInputBox"></input> \
        </div> \
    ';
    $('#moduleBoxes').append(newModule);

}

function test(){
    alert('test');
}