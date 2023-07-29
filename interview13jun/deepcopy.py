
"""Requirement
list
dict
tuple
nested
[]
"""
class DeepCopy:
    def __init__(self, obj):
        self.obj = obj
        return self.deep_copy(self.obj)

    def copy_list(self, obj):
        return obj[:]
    
    def copy_tuple(self, obj):
        return tuple(self.deep_copy(list(obj)))
    
    def copy_dict(self, obj):
        return obj.copy()
    
    def deep_copy(self, obj):
        if isinstance(obj, list):
            n_obj = self.copy_list(obj)
            for i in range(len(obj)):
                n_obj[i] = self.deep_copy(obj[i])
        elif isinstance(obj, dict):
            n_obj = self.copy_dict(obj)
            for k, v in obj.items():
                n_obj[k] = self.deep_copy(v)
        elif isinstance(obj, tuple):
            n_obj = self.copy_tuple(obj)
        else:
            return obj

        return n_obj
    




    







