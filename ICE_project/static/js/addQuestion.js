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
                    <textarea name="questionTxt" id="questionTxt"></textarea> \
                </div> \
                <div id="optionBox"> \
                    option1: <input name="o1" type="text"></input><br> \
                    option2: <input name="o2" type="text"></input><br> \
                    option3: <input name= "o3" type="text"></input><br> \
                    option4: <input name= "o4"type="text"></input> \
                </div> \
                <div id="answerBox"> \
                    Answer: <input name="answer" type="text"></input> \
                </div> \
            </div> \
        </div> \
    ';
    $('#boxPanel').append(quizBox);
}