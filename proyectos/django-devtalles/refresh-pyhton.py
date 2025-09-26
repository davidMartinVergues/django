


# HOF 

# def require_auth(func):
#     def wrapper(user2:str, test:str):
#         if user2.lower() == "admin":
#             return func(user2, test)
#         else:
#             return "access denid"
#     return wrapper

# def admin_dashboard(user, test):
#     return f"welcome {user} - {test}"

# aut_service = require_auth(admin_dashboard)

# print(aut_service('admin', 'test'))
# print(aut_service('guess','test'))

# decorators


def require_auth_to_decorator(func):
    def wrapper(user2:str, test:str):
        if user2.lower() == "admin":
            return func(user2, test)
        else:
            return "access denid"
    return wrapper

@require_auth_to_decorator
def admin_dashboard_to_decorator(user, test):
    return f"welcome {user} - {test}"

# aut_service = require_auth(admin_dashboard)

print(admin_dashboard_to_decorator('admin', 'test'))
print(admin_dashboard_to_decorator('guess','test'))