$(function(context) {
    return function()
    {

        $(".smolpic").hover(function(){
            $("#largeimage").attr("src",this.src);
        })




    }
 }(DMP_CONTEXT.get()))
