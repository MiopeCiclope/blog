$(document).ready(function(){
    $('#trash').click(function(){
        var catid;
        catid = $(this).attr("data-catid");
        $.get('/trash_category/', {category_id: catid}, function(data){
           $('#trash_count').html("  "+data);
        });
    });
});   

$(document).ready(function(){
    $('#love').click(function(){
        var catid;
        catid = $(this).attr("data-catid");
        $.get('/love_category/', {category_id: catid}, function(data){
           $('#love_count').html("  "+data);
        });
    });
});   