
import sqlite3

def getAll():
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from PHONG'
    cursor.execute(query)

    result = cursor.fetchall()
    return result
    cursor.close

def getAllhoa():
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from HOADON'
    cursor.execute(query)

    result = cursor.fetchall()
    return result
    cursor.close

def getAllCus():
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from cus'
    cursor.execute(query)

    result = cursor.fetchall()
    return result
    cursor.close

def getAllElectri():
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from hoa_don_dien'
    cursor.execute(query)

    result = cursor.fetchall()
    return result
    cursor.close

def getAllWater():
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from hoa_don_nuoc'
    cursor.execute(query)

    result = cursor.fetchall()
    return result
    cursor.close

def getAllAccount():
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from account'
    cursor.execute(query)

    result = cursor.fetchall()
    return result
    cursor.close

def updateRoom(id,name,status):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    print(status)
    query = 'update phong set name = ?,Status = ? where ID=?'
    re =(name,status,id,)
    cursor.execute(query,re)
    sqliteConnection.commit()
    
    cursor.close

def findByid(id):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    
    query = 'select* from phong where ID=?'
    cursor.execute(query,(id,))
    
    result = cursor.fetchall()
    return result
    cursor.close

def findAllStatus(status):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()

    query = 'select* from phong where Status=?'
    cursor.execute(query,(status,))
    
    result = cursor.fetchall()
    return result
    cursor.close