import logging
import sqlalchemy as db
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


def crear_database():
    logging.debug(f"Abriendo conexión a base de datos")
    dbEngine = db.engine.create_engine(os.environ.get('DATABASE'))
    metadata_obj = db.MetaData()

    logging.debug(f"Generando tablas")
    usuarios = db.Table(
        'usuarios',
        metadata_obj,
        db.Column('usuario_id', db.Integer, primary_key=True),
        db.Column('usuario_nombre', db.Text),
        db.Column('usuario_clave', db.Text),
        db.UniqueConstraint('usuario_id', 'usuario_nombre', 'usuario_clave', name='uix_01'),
    )

    logging.info(f"Creando DB desde cero")
    metadata_obj.drop_all(dbEngine)
    metadata_obj.create_all(dbEngine)
    logging.info(f"DB Creada")

if __name__ == '__main__':
    pregunta = "Advertencia, correr este código reseteará la base de datos. ¿Estás seguro? Y/N"
    yes = {'yes', 'y', 'si', 's'}
    no = {'no', 'n'}

    done = False
    print(pregunta)
    while not done:
        choice = input().lower()
        if choice in yes:
            crear_database()
            done = True
        elif choice in no:
            logging.info(f"Cerrando el programa")
            done = True
        else:
            print("Responder Y/N.")