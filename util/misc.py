def get_random_string(length=12, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
        """
        Returns a random string of length characters from the set of a-z, A-Z, 0-9
        for use as a salt.

        The default length of 12 with the a-z, A-Z, 0-9 character set returns
        a 71-bit salt. log_2((26+26+10)^12) =~ 71 bits
        """
        import random
        try:
            random = random.SystemRandom()
        except NotImplementedError:
            pass
        return ''.join([random.choice(allowed_chars) for i in range(length)])
