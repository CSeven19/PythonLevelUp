# -*- encoding: UTF-8 -*-
import json


class Student:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age


def convert_to_dict(obj):
    '''把Object对象转换成Dict对象'''
    dict = {}
    dict.update(obj.__dict__)
    return dict


def convert_to_dicts(objs):
    '''把对象列表转换为字典列表'''
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict对象
        dict = {}
        dict.update(o.__dict__)
        obj_arr.append(dict)
    return obj_arr


# 类似java反射机制
def class_to_dict(obj):
    '''把对象(支持单个对象、list、set)转换成字典'''
    is_list = obj.__class__
    is_set = obj.__class__
    if is_list == [].__class__ or is_set == set().__class__:
        obj_arr = []
        for o in obj:
            # 把Object对象转换成Dict对象
            dict = {}
            dict.update(o.__dict__)
            obj_arr.append(dict)
        return obj_arr
    else:
        dict = {}
        dict.update(obj.__dict__)
        return dict

if __name__ == '__main__':
    stu = Student('zhangsan', 20)
    print('-----------')
    print(convert_to_dict(stu))
    print('-----------')
    print(convert_to_dicts([stu, stu]))
    print('-----------')
    print(class_to_dict(stu))
    print('-----------')
    print(class_to_dict([stu, stu]))
    stua = Student('zhangsan', 20)
    stub = Student('lisi', 10)
    stu_set = set()
    stu_set.add(stua)
    stu_set.add(stub)
    print(class_to_dict(stu_set))
    dict_stu = class_to_dict(stu_set)

    # json保存，读取
    file = open('1.json', 'w', encoding='utf-8')
    json_stu = json.dumps(dict_stu, file)
    file = open('1.json', 'r', 'utf-8')
    print(json.loads(file))
