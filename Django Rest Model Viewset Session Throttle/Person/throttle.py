from rest_framework.throttling import UserRateThrottle

class AdminThrottle(UserRateThrottle):
    scope = 'admin'