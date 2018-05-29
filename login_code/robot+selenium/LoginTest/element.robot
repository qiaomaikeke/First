*** Keywords ***
打开浏览器
    Open Browser    ${url}    Chrome

输入用户名
    Input Text    name = username_field    ${username}

输入密码
    Input Password    name = password_field    ${password}

点击登陆
    Click Button    name=login_button

FORJ
    :FOR    ${j}    IN RANGE    2
    \    LOG    arg=${arg};j=${j}
