
def introspection_info(obj):
    attribute = dir(obj)
    type_ = type(obj).__name__
    module = obj.__class__.__module__
    method = [method for method in attribute if callable(getattr(obj, method))]
    res = {'atteibutes': attribute, 'type': type_,
           'module': module, 'method': method}
    return res


number_info = introspection_info(44)
print(number_info)

number_info = introspection_info('My object')
print(number_info)

