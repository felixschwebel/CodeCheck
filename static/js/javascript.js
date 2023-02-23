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



/* Manage the tiles */
$(document).ready(function() {
  // Add event listener to the Add Tile button
  $('#add-tile').click(function() {
    // Generate a new tile with a unique ID
    var tile_id = 'tile-' + $('.tile').length;
    var tile_html = '<div class="tile" id="' + tile_id + '">' +
                    '<h3>' + tile_id + '</h3>' +
                    '<button type="button" class="close-tile" data-dismiss="alert">&times;</button>' +
                    '<p>This is the content of ' + tile_id + '.</p>' +
                    '</div>';

    // Add the new tile to the tile container
    $('.tile-container').append(tile_html);
  });

  // Add event listener to the Close button of each tile
  $('.close-tile').click(function() {
      var id = $(this).data('id');
      $(this).closest('.tile').remove();
      $.ajax({
        url: '/delete_tile',
        type: 'POST',
        data: { id: id },
      });
      // Remove the parent tile from the DOM
      $(this).closest('.tile').remove();
  });
});
