var num_module = 0;

function addModule(){
    var newModule = ' \
        <div class="newModuleDiv"> \
            <label for = "moduleInputBox">module number:</label> \
            <input id="moduleInputBox"></input> \
            <label for = "titleInputBox">Title:</label> \
            <input id="titleInputBox"></input> \
            <div id="moduleBtn"> \
                <form action = \'manageQuiz.html\'> \
                    <button>Manage Quiz</button> \
                </form> \
                <form action = \'manageComponents.html\'> \
                    <button>Manage</button> \
                </form> \
                <form action = \'manageQuiz.html\'> \
                    <button>Delete</button> \
                </form> \
            </div> \
        </div> \
    ';
    $('#moduleBoxes').append(newModule);

}

function test(){
    alert('test');
}