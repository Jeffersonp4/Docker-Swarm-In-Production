import psycopg2 as bd
from psycopg2 import pool
import pyodbc
from connection_variables import EncapsulatedConnection
from logging import log
import sys

class Conexion:
    _DATABASE = None
    _USERNAME = None
    _PASSWORD = None
    _DB_PORT = None
    _HOST = None
    _MIN_CON = 1
    _MAX_CON = 5
    _Pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._Pool is None:
            try:
                cls._Pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host= cls._HOST,
                                                      user= cls._USERNAME,
                                                      password= cls._PASSWORD,
                                                      port= cls._DB_PORT,
                                                      database= cls._DATABASE)

                print(f'Creacion del pool exitosa: {cls._Pool}')
                return cls._Pool
            except Exception as e:
                print(f'Ocurrio un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._Pool

    @classmethod
    def obtenerConexion(cls):
        conex = cls.obtenerPool().getconn()
        print(f'Conexion obtenida del pool: {conex}')
        return conex

    @classmethod
    def liberarConexion(cls, Conexion):
        cls.obtenerPool().putconn(Conexion)
        print(f'Regresamos la conexion al pool: {Conexion}')

    @classmethod
    def closeConexion(cls):
        cls.obtenerPool().closeall()



if __name__ == '__main__':
    conex1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conex1)
    conex2 = Conexion.obtenerPool()

