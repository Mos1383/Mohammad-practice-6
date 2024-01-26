class RoseDictionary:
    def __init__(self):
        self.data = {}

    def get_item(self, key, raise_error=True, default=None, error_msg=None):
        if key in self.data:
            return self.data[key]
        else:
            if raise_error:
                if error_msg:
                    raise KeyError(error_msg)
                else:
                    raise KeyError('error_msg')
            else:
                if default is not None:
                    return default
                else:
                    if error_msg:
                        return error_msg
                    else:
                        return 'Value was not found and no default value/message was specified.'
d = RoseDictionary()
print(d.get_item("key", raise_error=True, default="Default Value", error_msg="Custom error massage"))