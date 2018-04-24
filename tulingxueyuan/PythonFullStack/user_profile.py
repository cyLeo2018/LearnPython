def build_profile(first, last, **kwargs):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k,v in kwargs.items():
        profile[k] = v
    return profile

print(build_profile('chen','yang',age=28, high='175cm', weigth='140kg'))