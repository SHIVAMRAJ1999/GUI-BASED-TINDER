import mysql.connector
class DBhelper:
    def __init__(self):
        try:
            self._connection=mysql.connector.connect(host='127.0.0.1',user='root',password='',database='tinderb3')
            self._cursor=self._connection.cursor()
            print("Connected to database")
        except:
            print("Could not connect to database")
    def search(self,key1,value1,key2,value2,table):
        self._cursor.execute(''' 
                             SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'
                             '''.format(table,key1,value1,key2,value2))
        data=self._cursor.fetchall()
        print(data)
        return data
    def searchOne(self,key1,value1,table,type):
        self._cursor.execute(''' 
                             SELECT * FROM `{}` WHERE `{}` {} '{}'
                             '''.format(table,key1,type,value1))
        data=self._cursor.fetchall()
        return data
    def insert(self,insertDict,table):
        
        colValue=''
        dataValue=''
        '''INSERT INTO `user` (`user_id','name`,`email`,`passwprd`,'gender`,`age`,`city`) VALUES('a','b','c','d'..)'''
        for i in insertDict:
            colValue=colValue+'`'+i+'`,'
            dataValue=dataValue+"'"+insertDict[i]+"',"
        colValue=colValue[:-1]
        dataValue=dataValue[:-1]
        print(colValue,dataValue)
            
        try:
            query="INSERT INTO `{}` ({}) VALUES({})".format(table,colValue,dataValue)
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0
    def update(self,insertDict,table):
        
        k=[]
        v=[]
        for i,j in insertDict.items():
            k.append(i)
            v.append(j)
        print(k,v)
        '''INSERT INTO `user` (`user_id','name`,`email`,`passwprd`,'gender`,`age`,`city`) VALUES('a','b','c','d'..)'''
        id_name=k[0]
        id_data=v[0]
        
        try:
            for l in range(1,len(k)):
                i=k[l]
                j=v[l]
                query="UPDATE `{}` SET `{}`='{}' WHERE `{}`='{}'".format(table,i,j,id_name,id_data)
                self._cursor.execute(query)
                self._connection.commit()
                
            return 1
        except:
            return 0
    def delete(self,key1,value1,key2,value2,table):
        try:
            self._cursor.execute(''' 
                                 DELETE FROM `{}` WHERE (`{}`='{}') AND (`{}`='{}')
                                 '''.format(table,key1,value1,key2,value2))
            self._connection.commit()
                
            return 1
        except:
            return 0
