const charBtn = document.getElementById("start-game");
charBtn.addEventListener("click", function () {
    let nameChoice = prompt("Enter your name: ")
    if(nameChoice === null) {
        return;
    }
    while(true) {
        let genderChoice = prompt(
            "Pick your gender: \n" +
            "1. Female\n" +
            "2. Male\n" +
            "3. Nonbinary"
        );
        genderChoice = genderChoice.toLowerCase();
        if(genderChoice == "1" ||
        genderChoice =="female" ||
        genderChoice == "2" ||
        genderChoice == "male" ||
        genderChoice == "3" ||
        genderChoice =="nonbinary") {
            alert("All set!")
            break;
        }
        else {
            alert("not a gender, please try again")
        }
    }
    
})