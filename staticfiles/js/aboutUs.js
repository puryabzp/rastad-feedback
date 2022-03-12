$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});
 $(function() {
  $('.man-four').hover(function() {
    $('.four-feet-apart').css('height', '400px');
  }, function() {
    // on mouseout, reset the background colour
    $('.four-feet-apart').css('height', '');
  });
});
    $(function() {
  $('.man-four2').hover(function() {
    $('.four-feet-apart2').css('height', '400px');
  }, function() {
    // on mouseout, reset the background colour
    $('.four-feet-apart2').css('height', '');
  });
});
    $(function() {
  $('.man-four3').hover(function() {
    $('.four-feet-apart3').css('height', '400px');
  }, function() {
    // on mouseout, reset the background colour
    $('.four-feet-apart3').css('height', '');
  });
});
 $(function() {
  $('.man-four4').hover(function() {
    $('.four-feet-apart4').css('height', '400px');
  }, function() {
    // on mouseout, reset the background colour
    $('.four-feet-apart4').css('height', '');
  });
});    
  wow = new WOW(
    {
        boxClass:     'wow',      // default
        animateClass: 'animated', // change this if you are not using animate.css
        offset:       0,          // default
        mobile:       true,       // keep it on mobile
        live:         true        // track if element updates
      }
    )
   wow.init();
 paceOptions = {
    ajax: true,
    document: true,
    eventLag: false
};
     
$(document).ready(function() {
 
  // Fakes the loading setting a timeout
    setTimeout(function() {
        $('body').addClass('loaded');
    }, 1700);
 
});   
function showDiv() {
   document.getElementById('welcomeDiv').style.display = "block";
   document.getElementById('welcomeDiv2').style.display = "none";
}
    function showDiv2() {
   document.getElementById('welcomeDiv2').style.display = "block";
   document.getElementById('welcomeDiv').style.display = "none";
}      
