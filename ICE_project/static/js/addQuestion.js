function addQuestion(){
    var quizBox = ' \
        <div class="manageQuizBody"> \
            <div id="quizBox"> \
                <header> \
                    <div id="Questiontxt"> \
                        Question \
                    </div> \
                    <div id="DeleteBtnDiv"> \
                        <button id="deleteBtn">\
                            Delete \
                        </button> \
                    </div> \
                </header> \
                <div id= "question_txtAreaDiv"> \
                    <textarea id="questionTxt"></textarea> \
                </div> \
                <div id="optionBox"> \
                    option1: <input type="text"></input><br> \
                    option2: <input type="text"></input><br> \
                    option3: <input type="text"></input><br> \
                    option4: <input type="text"></input> \
                </div> \
                <div id="answerBox"> \
                    Answer: <input type="text"></input> \
                </div> \
            </div> \
        </div> \
    ';
    $('#boxPanel').append(quizBox);
}