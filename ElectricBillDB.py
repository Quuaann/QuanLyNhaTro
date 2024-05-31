import sqlite3

def updateWaterBill(id,name,nu,sum):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    query = 'update hoa_don_nuoc set id_phong = ?,Number = ?, Tong = ? where ID=?'
    re =(name,nu,sum,id,)
    cursor.execute(query,re)
    sqliteConnection.commit()
    
    cursor.close

def addWaterBill(id,name,nu,sum):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    query = 'insert into hoa_don_nuoc values (?,?,?,?)'
    re =(id,name,nu,sum,)
    cursor.execute(query,re)
    sqliteConnection.commit()
    
    cursor.close

def findByidWater(id):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    
    query = 'select* from hoa_don_nuoc where ID=?'
    cursor.execute(query,(id,))
    
    result = cursor.fetchall()
    return result
    cursor.close

def deleteWater(id):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    
    query = 'delete from hoa_don_nuoc where ID=?'
    cursor.execute(query,(id,))
    sqliteConnection.commit()
    
    result = cursor.fetchall()
    
    cursor.close

def updateElecBill(id,name,nu,sum):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    query = 'update hoa_don_dien set id_phong = ?,Number = ?, Tong = ? where ID=?'
    re =(name,nu,sum,id,)
    cursor.execute(query,re)
    sqliteConnection.commit()
    
    cursor.close

def addElecBill(id,name,nu,sum):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    query = 'insert into hoa_don_dien values (?,?,?,?)'
    re =(id,name,nu,sum,)
    cursor.execute(query,re)
    sqliteConnection.commit()
    
    cursor.close

def findByid(id):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    
    query = 'select* from hoa_don_dien where ID=?'
    cursor.execute(query,(id,))
    
    result = cursor.fetchall()
    return result
    cursor.close

def delete(id):
    sqliteConnection = sqlite3.connect('QLNhaTro.db')
    cursor = sqliteConnection.cursor()
    
    query = 'delete from hoa_don_dien where ID=?'
    cursor.execute(query,(id,))
    sqliteConnection.commit()
    
    result = cursor.fetchall()

    cursor.close