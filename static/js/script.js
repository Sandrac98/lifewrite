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

  fetch('url',{
    method:'POST'                
    }) 
    .then((response)=>{         
        if(response.redirected){
            window.location.href = response.url;
        }
    })           
    .catch(function(e){
        
    })