*** Keywords ***
链接数据库
    Connect To Database Using Custom Params    pymysql    database="datalogin",user="root",password="root",host="127.0.0.1",port=3306

查询数据库
    ${b}    Query    select * from error_pw

断开连接
    Disconnect From Database

表的行数
    ${row}    Row Count    select *from
