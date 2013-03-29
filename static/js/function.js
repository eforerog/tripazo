// JavaScript Document
/*traveler type*/
 $(document).ready(function() {

            $(".drop").click(function(e) {          
				e.preventDefault();
                $("div#traveler_list").toggle();
				$(".drop").toggleClass("up");
            });
			
			$("div#traveler_list").mouseup(function() {
				return false
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.drop").length==0) {
					$(".drop").removeClass("up");
					$("div#traveler_list").hide();
				}
			});			
			
        });
		
/*budget*/	
 $(document).ready(function() {

            $(".drop2").click(function(e) {          
				e.preventDefault();
                $("div#budget_list").toggle();
				$(".drop2").toggleClass("up");
            });
			
			$("div#budget_list").mouseup(function() {
				return false
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.drop2").length==0) {
					$(".drop2").removeClass("up");
					$("div#budget_list").hide();
				}
			});			
			
        });	

/*select a city*/	
$(document).ready(function() {

            $(".drop3").click(function(e) {          
				e.preventDefault();
                $("div#city_list").toggle();
				$(".drop3").toggleClass("up");
            });
			
			$("div#city_list").mouseup(function() {
				return false
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.drop3").length==0) {
					$(".drop3").removeClass("up");
					$("div#city_list").hide();
				}
			});			
			
        });		
		

/*itinerary options*/	
$(document).ready(function() {

            $(".deploy").click(function(e) {          
				e.preventDefault();
                $("div#options").toggle();
				$(".deploy").toggleClass("up");
            });
			
			$("div#options").mouseup(function() {
				return false
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.deploy").length==0) {
					$(".deploy").removeClass("up");
					$("div#options").hide();
				}
			});			
			
        });			
		
		
		
/*background image rotator*/

$(document).ready(function() {
				$('#slideshow').cycle({
				fx: 'fade',
				 
				pause:   1, 
				speed: 1800,
				timeout:  3500 
			});			
		});
	
/*jquery calendar calling*/
$(function() {
$( "#datepicker" ).datepicker();
$( "#datepicker2" ).datepicker();
});



/*header stick top calling*/
 $(window).load(function(){
      $("#header").sticky({ topSpacing: 0 });
    });
	
/*placeholder on IE */
    $(function(){
      $(':input[placeholder]').placeholder();
    });
	
/*scroll itinerary*/
$(function() {
  // initialize scrollable
  $(".scrollable").scrollable();
});