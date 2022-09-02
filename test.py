
def dict_parser(arg, obj):
    args = arg.split(', {')
    arg_str = '{' + args[1]
    arg_dict = json.loads(arg_Str)
    if isinstance(arg_dict, dict):
        for k ,v in arg_dict.items():
            setattr(obj, k.strip('"'), v.strip('"'))
    else:
        pass
