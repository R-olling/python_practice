# 邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）
# 如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"
# email_id = input("请输入邮箱：")
# if (email_id.count("@") == 1) and (email_id.count(".") >= 1):
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")
email_id = input("请输入邮箱：")
if (email_id.count("@") == 1) and ("." in email_id):
    print("邮箱格式正确")
else:
    print("邮箱格式错误")