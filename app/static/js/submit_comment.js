$(document).on('click', '#input-submit-comment', function(event) {
    $.ajax({
    	url : '/add_comment',
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
