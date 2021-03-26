$(".email").on('click', function(){

    var btnID = $(this).attr('id')
    $(this).fadeOut("fast", function(){
        $(this).siblings(".done").show()
    })

    $.ajax({
        data:{
            user_id: btnID
        },
        type:'POST',
        url:'/testAjax'
    })
    // alert(btnID)
})


$(document).ready( function () {
    $('#myTable').DataTable(
        {
            "lengthChange":false, paging:false, info:false
        }
    );


    oTable = $('#myTable').DataTable();   //pay attention to capital D, which is mandatory to retrieve "api" datatables' object, as @Lionel said
$('#myInputTextField').keyup(function(){
      oTable.search($(this).val()).draw() ;
})
} );