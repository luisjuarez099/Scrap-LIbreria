import scrap_sotano
import mysql_sotano

def run():
    scrap_sotano.scrap_pg()
    mysql_sotano.mysql_up()


if __name__=='__main__':
    run()