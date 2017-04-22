from make_db_file import storeDbase, loadDbase

db = loadDbase()
db['sue']['pay'] = 10086
db['tom']['name'] = 'Tom Nikolas'
storeDbase(db)
