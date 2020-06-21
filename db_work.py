def search_by_place(place, cursor):
    cursor.execute(r"SELECT idPhoto, strDesc, strOrigPlace, dateCreated "
                   r"FROM photosSourceDesc AS pSD "
                   r"WHERE pSD.strOrigPlace LIKE '%{}%'".format(place))
    return cursor.fetchall()


def search_by_date(date_type, date, cursor):
    if date_type == "notBefore":
        cursor.execute("SELECT idPhoto, strDesc, strOrigPlace, dateCreated "
                       "FROM photosSourceDesc AS pSD "
                       "WHERE pSD.dateCreated > {}".format(date))
    elif date_type == "notAfter":
        cursor.execute("SELECT idPhoto, strDesc, strOrigPlace, dateCreated "
                       "FROM photosSourceDesc AS pSD "
                       "WHERE pSD.dateCreated < {}".format(date))
    elif date_type == "exact":
        cursor.execute("SELECT idPhoto, strDesc, strOrigPlace, dateCreated "
                       "FROM photosSourceDesc AS pSD "
                       "WHERE pSD.dateCreated = {}".format(date))
    return cursor.fetchall()


def search_by_title(title, cursor):
    cursor.execute("SELECT idPhoto, strDesc, strOrigPlace, dateCreated "
                   "FROM photosSourceDesc AS pSD "
                   "WHERE pSD.strDesc LIKE '%{}%'".format(title))
    return cursor.fetchall()


def search_by_rubric(category, cursor):
    statement = "SELECT pSD.idPhoto, pSD.strDesc, pSD.strOrigPlace, pSD.dateCreated FROM photosSourceDesc AS pSD " \
                "JOIN photosPublicationStmt AS pPS ON pSD.idPhoto = pPS.idPhoto WHERE pPS.strCategory LIKE '%{}%'".format(category)
    cursor.execute(statement)
    return cursor.fetchall()