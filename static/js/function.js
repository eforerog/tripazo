// JavaScript Document
/*traveler type*/
var expand_act = 0;
var expand_state = Array();

function init(day_max) {
	for(var i = 0; i <= day_max; i++)
	{
		expand_state.push(new Array());
                expand_state[i].push(0);
                expand_state[i].push(0);
                expand_state[i].push(0);
                expand_state[i].push(0);
                expand_state[i].push(0);
	}
}

function expand_detail(id, day_n, day_max, column_id) {
	switch(column_id)
        {
            case 1: document.getElementById("angle_" + day_n).style.left = "-365px";
                    break;
            case 2: document.getElementById("angle_" + day_n).style.left = "-210px";
                    break;
            case 3: document.getElementById("angle_" + day_n).style.left = "-50px";
                    break;
            case 4: document.getElementById("angle_" + day_n).style.left = "110px";
                    break;
            case 5: document.getElementById("angle_" + day_n).style.left = "265px";
                    break;
        }
        
        
        for(var i = 1; i <= day_max +1; i++)
	{
		if(i == day_n)
		{
			if(expand_state[i-1][column_id-1] == 0)
			{
                                for(var j = 0; j<=4; j++)
                                {
                                    expand_state[i-1][j] = 0;
                                }
    
                                expand_state[i-1][column_id-1] = 1;
				document.getElementById("expansion_pre_" + i).style.height = "400px";
                                //scroll(0, 10 + 260*i);
                                //alert("hola");
                                $.ajax({
                                  type: "GET",
                                  dataType : "json",
                                  url: "json_detail",
                                  data: { place_id: id },
                                  success: function(data) {
                                      //alert("prueba2: " + data[0].latitude);
                                      document.getElementById("place_title_" + day_n).innerHTML = data[0].name;
                                      document.getElementById("place_img_" + day_n).src = data[0].photo_url1;
                                      document.getElementById("content_div_" + day_n).innerHTML = "<p><strong>" + data[0].name + "</strong> - " + data[0].reviews + "</p>";
                                      document.getElementById("address_" + day_n).innerHTML = data[0].address;
                                      document.getElementById("website_" + day_n).innerHTML = "<a href=" + data[0].website + ">" + data[0].website +  "</a>";
                                      document.getElementById("phone_" + day_n).innerHTML = data[0].telephone;
                                      //document.getElementById("im_map_" + day_n).src = "//maps.googleapis.com/maps/api/staticmap?center=" + data[0].latitude + "," + data[0].longitude + "&zoom=16&size=192x189&key=AIzaSyDYPvbfjDGq8iKqYPjd2w58GEjAQzdY87s&maptype=roadmap&markers=color:black%7C" + data[0].latitude + "," + data[0].longitude +"&sensor=false";
                                      document.getElementById("im_map_" + day_n).src = "http://maps.googleapis.com/maps/api/staticmap?center=" + data[0].latitude + "," + data[0].longitude + "&zoom=15&size=182x179&markers=color:black%7C" + data[0].latitude + "," + data[0].longitude + "&sensor=false";
                                      }
                                
                                    
                                  //alert( "Data Saved: " + msg );
                                });
			}
			else
			{
                            if(expand_state[i-1][column_id-1]==1)
                            {
                                expand_state[i-1][column_id-1] = 0;
				document.getElementById("expansion_pre_" + i).style.height = "0px";
                            }
				
			}
		}
		else
		{
			document.getElementById("expansion_pre_" + i).style.height = "0px";
			expand_state[i-1][column_id-1] = 0;
		}
	
	
		
	}
	
	if(expand_state[day_n-1][column_id] == 0)
	{
		//expand_state[day_n-1] = 1;
		//document.getElementById("expansion_pre_" + day_n).style.height = "400px";
	}
	else
	{
		//expand_state[day_n-1] = 0;
		//document.getElementById("expansion_pre_" + day_n).style.height = "0px";
	}
	
}

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
				//e.preventDefault();
                //$("div#options").toggle();
				//$(".deploy").toggleClass("up");
            });
			
			$("div#options").mouseup(function() {
				return false
			});
			$(document).mouseup(function(e) {
				if($(e.target).parent("a.deploy").length==0) {
					//$(".deploy").removeClass("up");
					//$("div#options").hide();
				}
			});			
			
        });			
		
		
		
/*background image rotator*/

$(document).ready(function() {
    
    if(document.getElementById("slideshow"))
    {
                $('#slideshow').cycle({
                fx: 'fade',
                pause:   1, 
                speed: 1800,
                timeout:  3500 
        });			
    }
});
	
/*jquery calendar calling*/
$(function() {
$( "#datepicker" ).datepicker({ dateFormat: 'dd-mm-yy',
    beforeShow: function (textbox, instance) {   
                instance.dpDiv.css({
                    marginTop: (-textbox.offsetHeight) + 30 + 'px',
                    marginLeft: textbox.offsetWidth + 'px'
                });
            }

});
$( "#datepicker2" ).datepicker({ dateFormat: 'dd-mm-yy',
    beforeShow: function (textbox, instance) {   
                instance.dpDiv.css({
                    marginTop: (-textbox.offsetHeight) + 30 + 'px',
                    marginLeft: textbox.offsetWidth + 155 + 'px'
                });
            }

});

$( "#datepicker3" ).datepicker({ dateFormat: 'dd-mm-yy',
    beforeShow: function (textbox, instance) {   
                instance.dpDiv.css({
                    marginTop: (-textbox.offsetHeight) - 228 + 'px',
                    marginLeft: textbox.offsetWidth + 198 + 'px'
                });
            }

});
$( "#datepicker4" ).datepicker({ dateFormat: 'dd-mm-yy',
    beforeShow: function (textbox, instance) {   
                instance.dpDiv.css({
                    marginTop: (-textbox.offsetHeight) - 228 + 'px',
                    marginLeft: textbox.offsetWidth + 338 + 'px'
                });
            }

});

});



/*header stick top calling*/
 $(window).load(function(){
     if(document.getElementById("header"))
     {
         //$("#header").sticky({ topSpacing: 0 });
     }      
});
	
/*placeholder on IE */
    $(function(){
      //$(':input[placeholder]').placeholder();
    });
	
/*scroll itinerary*/
$(function() {
  // initialize scrollable
  //$(".scrollable").scrollable();
});


function select_city_list_index() {
    document.getElementById("city_list").style.display = "block";
}

function city_select_ele(city_id, city_name) {
    document.getElementById("city_list").style.display = "none";
    $("#city").val(city_name);
    $("#city_id").val(city_id);
}

function traveler_list_show() {
    document.getElementById("traveler_list").style.display = "block";
}

function budget_city_list_index() {
    document.getElementById("budget_list").style.display = "block";
}

function budget_select_ele(budget_id, budget_name) {
    document.getElementById("budget_list").style.display = "none";
    $("#budget").val(budget_name);
    $("#budget_id").val(budget_id);
}