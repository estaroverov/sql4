import mysql.connector as msql

# Функция вывода результата запроса

def print_query_result(result):
    for row in result:
        print(row)
    print()
    return


connector = msql.connect(user='root', password='',
                              host='localhost',
                              database='students')

cursor = connector.cursor()
query = "SELECT COUNT(*) FROM likes  \
    INNER JOIN media ON  likes.media_id = media.id \
    INNER JOIN profiles ON media.user_id = profiles.user_id \
    WHERE profiles.birthday>'2011-01-01';"

cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

query = "SELECT COUNT(*) FROM likes  \
    INNER JOIN profiles ON  likes.user_id = profiles.user_id \
    WHERE profiles.gender='m'\
    UNION \
    SELECT COUNT(*) FROM likes  \
    INNER JOIN profiles ON  likes.user_id = profiles.user_id \
    WHERE profiles.gender='f';"

cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

query = "SELECT * FROM users WHERE NOT users.id IN (SELECT DISTINCT from_user_id FROM messages);"

cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)

query = "SELECT from_user_id, to_user_id, COUNT(to_user_id) AS c \
FROM messages WHERE to_user_id IN \
(SELECT target_user_id FROM friend_requests WHERE status='approved'\
UNION SELECT initiator_user_id FROM friend_requests WHERE status='approved') \
AND from_user_id in (SELECT target_user_id FROM friend_requests WHERE status='approved'\
UNION SELECT initiator_user_id FROM friend_requests WHERE status='approved') \
GROUP BY from_user_id, to_user_id \
ORDER BY c DESC;"

cursor.execute(query)
result = cursor.fetchall()
print_query_result(result)