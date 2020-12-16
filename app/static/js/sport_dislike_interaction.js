$(document).on('click', '#click-dislike-btn', function(event) {
    $.ajax({
    	url : '/sports_dislike',
    	type : "post",
    	contentType: 'application/json;charset=UTF-8',
    	dataType: "json",
    	data : JSON.stringify({'postid' : $(this).data('postid')}),
    	success : function(data) {
    		console.log(data);
    	},
    	error : function(xhr) {
    		console.log(xhr);
    	}
    });
    event.preventDefault();
});
