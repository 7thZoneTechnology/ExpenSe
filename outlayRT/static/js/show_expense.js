

$(document).ready(function() {

    $('#show_exp').click(function(){
    	begin = $(this).attr("begin");
  		user = $(this).attr("username");
    	begin = parseInt(begin);	
     	$.get('./which_expenses', {beginning: begin, username: user}, function(data){
               $('#current_expenses').html(data);
        });
    });

});


