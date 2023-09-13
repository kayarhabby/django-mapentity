import secrets

from django.core.cache import cache


class TokenManager:
    @classmethod
    def generate_token(self):
        token = secrets.token_urlsafe(32)

        # store the token in cache
        cache.set(token, True)
        return token

    @classmethod
    def verify_token(self, token):
        print("IN VERIFY TOKEN")
        return True
        #print(f"{token} is 1234 ? {bool(token=='1234')}")
        #return bool(token == '1234')
        return bool(cache.get(token))

    @classmethod
    def delete_token(self, token):
        # verify if token is in cache
        if cache.get(token):
            cache.delete(token)
            return True
        else:
            return False
