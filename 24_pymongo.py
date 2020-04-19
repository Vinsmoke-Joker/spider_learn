from pymongo import MongoClient

# 实例化client，建立链接
client = MongoClient(host='192.168.159.128',port=27017)
collection = client['test']['t251']
# 插入一条数据
collection.insert({'_id':10010,'name':'xiaowang','age':'18'})

# 插入多条数据
data_list = [{'name':'test{}'.format(i) for i in range(10)}]
collection.insert_many(data_list)

# 查询一条记录
t = collection.find_one({'_id':10010,'name':'xiaowang','age':'18'})
print(t)
# 查询多条记录
t = collection.find({'name':'xiaowang'})
print(t)
a = 10
