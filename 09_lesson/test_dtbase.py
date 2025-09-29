from sqlalchemy import create_engine,text

db_connection_string ="postgresql://postgres:Shcherbachka93@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM public.student"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['user_id'] == 42568
    assert row1['level'] == "Pre-Intermediate"

    connection.close()

def test_insert():
    connection = db.connect()
    sql = text("INSERT INTO public.student(user_id,level) VALUES (42358,'Beginner')")
    connection.execute(sql)
    result = connection.execute( text( "SELECT * FROM public.student where user_id = 42358" ) )
    rows = result.mappings().all()
    row= rows[0]
    assert row['user_id'] == 42358
    assert row['level'] == "Beginner"
    sql_del = text( "Delete from public.student where user_id = 42358" )
    connection.execute( sql_del )
    connection.close()

def test_update():
    connection = db.connect()
    sql = text("INSERT INTO public.student(user_id,level) VALUES (42359,'Beginner')")
    connection.execute(sql)
    sql_up = text( "UPDATE  public.student SET level = 'Elementary' WHERE user_id = 42359" )
    connection.execute( sql_up )
    result = connection.execute( text( "SELECT * FROM public.student where user_id = 42359" ) )
    rows = result.mappings().all()
    row= rows[0]
    assert row['user_id'] == 42359
    assert row['level'] == "Elementary"
    sql_del = text( "Delete from public.student where user_id = 42359" )
    connection.execute( sql_del )
    connection.close()


def test_delete():
    connection = db.connect()
    sql = text( "INSERT INTO public.student(user_id,level) VALUES (42350,'Beginner')" )
    connection.execute( sql )
    sql_del = text( "Delete from public.student where user_id = 42350" )
    connection.execute( sql_del )
    result = connection.execute( text( "SELECT * FROM public.student where user_id = 42350" ) )
    rows = result.mappings().all()

    assert len(rows) == 0
    connection.close()
