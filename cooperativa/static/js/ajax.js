templates$(document).ready(function(){
    $("#Bus").submit(function(e){
        e.preventDefault();
        $.ajax({
            url:$(this).attr('action'),
            type:$(this).attr('method'),
            data:$(this) .serialize(),

            success: function(json){
                console.log(json)
            }
        })
    })

})