$(document).ready(function(){
    $('.sidenav').sidenav();
  });


  $(document).ready(function(){
    $('.collapsible').collapsible();
  });


  $('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));


  document.getElementById("show-form-btn").addEventListener("click", function() {
    var form = document.getElementById("new-journal-form");
    form.style.display = form.style.display === "none" ? "block" : "none";
  });


 // Initialize Materialize CSS components
 document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.card');
  var instances = M.Cards.init(elems, {});
});

// Add click event listeners to the read more links
document.querySelectorAll('.read-more-link').forEach(function(link) {
  link.addEventListener('click', function(event) {
    event.preventDefault();
    var card = this.closest('.card');
    var cardInstance = M.Cards.getInstance(card);
    cardInstance.open();
  });
});

// Add click event listeners to the read more links
document.querySelectorAll('.read-more-link').forEach(function(link) {
  link.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default behavior of the link
    var card = this.closest('.card');
    var cardInstance = M.Cards.getInstance(card);
    cardInstance.open();
  });
});

