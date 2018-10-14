import pyexcel
from collections import OrderedDict
#
data = [
    OrderedDict({
        "Name" : "Quan",
        "Age" : 22,
        "City": "Hanoi"
    }),
    OrderedDict(){
        "Name" : "Khanh",
        "Age" : 22,
        "City": "Vinh"
    },
    OrderedDict(){
        "Name" : "Nam",
        "Age" : 23
    },
]
pyexcel.save_as(records=data, dest_file_name="samle.xlsx")