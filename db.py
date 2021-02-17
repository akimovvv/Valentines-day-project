import sqlite3

conn = sqlite3.connect("wish_service.db")
cursor = conn.cursor()

def inserting_user(user, recipient):
    cursor.execute("""INSERT INTO user(phone) SELECT (?) WHERE NOT EXISTS(SELECT phone FROM user WHERE phone = (?));""", (user.phone, user.phone))
    cursor.execute("""INSERT INTO user(phone) SELECT (?) WHERE NOT EXISTS(SELECT phone FROM user WHERE phone = (?));""",(recipient, recipient))
    conn.commit()

def find_sender_id(phone):
    cursor.execute("""SELECT id FROM user WHERE phone = (?)""", (phone,))
    a = cursor.fetchone()
    return a[0]

def find_recipient_id(recipient):
    cursor.execute("""SELECT id FROM user WHERE phone = (?)""", (recipient,))
    a = cursor.fetchone()
    return a[0]


def inserting_wish(wish):
    cursor.execute("""INSERT INTO wish(text, sender_id, recipient_id) SELECT (?), (SELECT id FROM user WHERE id = (?) AND max > cur), (?);""", (wish.text, wish.sender_id, wish.recipient_id,))
    cursor.execute("""UPDATE user SET cur = cur + 1 WHERE id = (?);""", (wish.sender_id,))
    conn.commit()

def find_phone(phone):
    cursor.execute("""INSERT INTO user(phone) SELECT (?) WHERE NOT EXISTS (SELECT phone FROM user WHERE phone = (?))""",(phone, phone,))
    cursor.execute("""SELECT id FROM user WHERE phone = (?);""", (phone, ))
    a = cursor.fetchone()
    return a[0]

def check_box(phone):
    cursor.execute("""SELECT COUNT(*) FROM wish WHERE recipient_id = (?)""", (phone,))
    a = cursor.fetchone()
    return a[0]

def show_text(phone):
    cursor.execute("""SELECT CASE WHEN (SELECT COUNT(*) FROM wish t WHERE t.sender_id = (?) and t.recipient_id = w.sender_id) = 0 THEN "Аноним" ELSE u.phone END sender, w.text phone FROM wish w JOIN user u on w.sender_id = u.id WHERE w.recipient_id = (?);""", (phone, phone,))
    print(cursor.fetchall())

def close_conn():
    conn.close()