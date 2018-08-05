class EmpMiddleware:
    def process_request(self, request):
        group_name = None
        user_group_list = request.user.groups.all()
        if user_group_list:
            request.group_name = user_group_list[0]
        else:
            request.group_name = group_name
        print "Middleware successfully executed"






