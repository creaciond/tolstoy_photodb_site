from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship


db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "Authors"

    id_author = db.Column("idAuthor", db.Integer, primary_key=True)
    author_name = db.Column("authorName", db.Text)


class MuseumDescription(db.Model):
    __tablename__ = "MuseumAnnotations"
    __table_args__ = (PrimaryKeyConstraint("idPhoto"),)

    id_photo = db.Column("idPhoto", db.Integer, ForeignKey("PhotoDescriptions.idPhoto"))
    id_identif = db.Column("idIdentif", db.Text)
    id_inv = db.Column("idInv", db.Text)
    original_date = db.Column("originalDate", db.Text)
    original_author = db.Column("originalAuthor", db.Text)
    original_location = db.Column("originalLocation", db.Text)


class Location(db.Model):
    __tablename__ = "Locations"

    id_location = db.Column("idLocation", db.Integer, primary_key=True)
    location_name = db.Column("locationName", db.Text)


class PhotoRubric(db.Model):
    __tablename__ = "PhotoRubrics"
    __table_args__ = (PrimaryKeyConstraint("idPhoto", "idRubric"),)

    id_photo = db.Column("idPhoto", db.Integer, ForeignKey("PhotoDescriptions.idPhoto"))
    id_rubric = db.Column("idRubric", db.Integer, ForeignKey("Rubrics.idRubric"))


class Rubric(db.Model):
    __tablename__ = "Rubrics"
    __table_args__ = (PrimaryKeyConstraint("idRubric", "rubricName"),)

    id_rubric = db.Column("idRubric", db.Integer, primary_key=True)
    rubric_name = db.Column("rubricName", db.Text)


class Files(db.Model):
    __tablename__ = "PhotoFiles"
    __table_args__ = (PrimaryKeyConstraint("idPhoto"),)

    id_photo = db.Column("idPhoto", db.Integer, ForeignKey("PhotoDescriptions.idPhoto"))
    fullsize_file = db.Column("fullsizeFile", db.Text)
    miniature_file = db.Column("miniatureFile", db.Text)


class Photo(db.Model):
    __tablename__ = "PhotoDescriptions"

    id_photo = db.Column("idPhoto", db.Integer, primary_key=True)
    title = db.Column("photoName", db.Text)

    year = db.Column("year", db.Integer)
    photo_description = db.Column("photoDescription", db.Text)

    museum_comments = db.relationship("MuseumDescription")

    files = db.relationship("Files")

    # location
    id_location = db.Column("idLocation", db.Integer, ForeignKey("Locations.idLocation"))
    location = db.relationship("Location")

    # author
    id_author = db.Column("idAuthor", db.Integer, ForeignKey("Authors.idAuthor"))
    author = db.relationship("Author")

    # rubrics
    rubrics = db.relationship("Rubric", secondary="PhotoRubrics", lazy="dynamic")