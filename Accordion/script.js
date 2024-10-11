    function hideElement(answerID) {
        var answer = document.getElementById(answerID)
        if (answer.style.display === "none" || answer.style.display ==="") {
            answer.style.display = "block";

        } else {
            answer.style.display = "none";
        }
    }