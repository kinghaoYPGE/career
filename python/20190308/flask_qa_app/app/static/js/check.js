// 校验两次密码输入是否一致
$('#confirm_password').blur(function () {
    if ($(this).val() != $('#password').val()){
        $('#submit-button').attr('disabled',"true");
        alert('两次密码输入不一致');
    }else{
        $('#submit-button').removeAttr('disabled');
    }
});

// 校验用户是否已存在
$('#name').blur(function () {
    var name = $("#name").val();
    if (!name) {
        return;
    }
    post_url = '/ajax/user/username_check';
    $.post(post_url, {"username": name}, function (data) {
        if (data) {
            alert(data.info);
        }
    });
});

// 校验邮箱是否已存在
$('#email').blur(function () {
    var email = $("#email").val();
    if(!email){
        return;
    }
    post_url = '/ajax/user/email_check';
    $.post(post_url, {"email": email}, function(data){
            if(data){
                alert(data.info);
            }
        });
});