/*global $*/

$(document).ready(function(){
    $(".actionables").click(function(){
        var catid, button, state;
        catid = $(this).attr("data-catid");
        button = $(this).attr("id");
        state = $(this).attr("state");
        
        $.get('/trash_category/', {category_id: catid, type: button, action: state}, function(data){
            if (button == "trash") {
                $('#trash_count').html(" "+data);
                if (state == "do") {
                    $('#trash_glyph').hide();
                } else {
                    $('#trash_glyph').show();
                }
            } else {
                $('#love_count').html(" "+data);;
                if (state == "do") {
                    $('#love_glyph').hide();
                } else {
                    $('#love_glyph').show();
                }
            }
        });
        
        if (state == "do") {
            $(this).attr("state", "undo");
        } else {
            $(this).attr("state", "do");
        }
    });
});