/* Side navigation */
function openNav() {
  document.getElementById("mySidenav").style.width = "300px";
  document.getElementById("main").style.marginRight = "300px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginRight = "0";
}


/* Map the sidebar buttons to the submit form of the CodeMirror field */
const buttons = document.querySelectorAll('.FUNC-BTN');
const form = document.querySelector('form');
const submitFormButton = document.getElementById('CALL-FUNCTION');

buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        const clickedButtonName = button.id;
        const clickedButtonValue = button.innerText;

        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'button-id'
        input.value = clickedButtonName;
        form.appendChild(input);

        submitFormButton.click();
    });
});