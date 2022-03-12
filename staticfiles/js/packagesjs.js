 function showDiv() {
   document.getElementById('welcomeDiv').style.display = "block";
   document.getElementById('welcomeDiv2').style.display = "none";
   document.getElementById("welcomeDiv").style.transition = "all 0.2s ease-in-out";
   document.getElementById("welcomeDiv2").style.transition = "all 0.2s ease-in-out";
}
    function showDiv2() {
   document.getElementById('welcomeDiv2').style.display = "block";
   document.getElementById('welcomeDiv').style.display = "none";
   document.getElementById("welcomeDiv").style.transition = "all 0.2s ease-in-out";
   document.getElementById("welcomeDiv2").style.transition = "all 0.2s ease-in-out";
}      
$(function() {

	$(".prev").on('click', function(event) {
		event.preventDefault();
		prevSlide();
	});

	$(".next").on('click', function(event) {
		event.preventDefault();
		nextSlide();
	});

	if ($(".item").length <= 1) {
		$(".next").addClass('hide-nav');
	}

	$(".prev").addClass('hide-nav');

	function nextSlide() {
		var atual = $(".cd-slider").find('.current'),
			next = atual.next();

		next.addClass('current').removeClass('prev_slide').siblings().removeClass('current');
		next.prevAll().addClass('prev_slide');

		if (next.index() > 0) {
			$(".prev").removeClass('hide-nav');
		}
		if (next.index() == $(".item").last().index()) {
			$(".next").addClass('hide-nav');
		}
	}

	function prevSlide() {
		var atual = $(".cd-slider").find('.current'),
			prev = atual.prev();

		prev.addClass('current').removeClass('prev_slide').siblings().removeClass('current');

		if (prev.index() !== $(".item").last().index()) {
			$(".next").removeClass('hide-nav');
		} 
		if (prev.index() == 0) {
			$(".prev").addClass('hide-nav');
		}
	}

});